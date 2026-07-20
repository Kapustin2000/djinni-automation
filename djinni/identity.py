"""Build identity profiles from GitHub, used by the matcher to score jobs.

Two profiles:
  - "personal": the candidate's own CV repo (github.com/<user>/<user>, a curated
    tree of experience/projects/publications/skills) + their other public repos.
  - "asrp": ASRP's private knowledge-base repo (asrp.memory), read as a company
    capability/interest profile so jobs can be scored as business signals
    (partnership leads, outsourcing opportunities, competitor intel) rather than
    as a personal job application.

Both go through Claude to synthesize a structured Markdown profile that the
matcher and cover-letter generator use as source of truth.
"""

from __future__ import annotations

import base64
import json
import os
import ssl
import urllib.request

import anthropic
import certifi

from .config import (
    ASRP_GITHUB_OWNER,
    ASRP_MEMORY_REPO,
    CLAUDE_MODEL,
    GITHUB_USERNAME,
    identity_file,
)

GITHUB_API = "https://api.github.com"
TEXT_EXTENSIONS = (".md", ".yaml", ".yml")
_SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())

# Curated entry points into asrp.memory's "brain" layer (per its own README
# navigation: index -> maps/home -> cluster maps), skipping investigations/
# (process snapshots, not canon), docs/ (historical, not current-state),
# maps/entities/ (147 generated pages, too much for a static profile) and the
# sources/ submodules (cold storage, fetched on demand, not part of the brain).
ASRP_ALLOW_PATHS = [
    "README.md",
    "index.md",
    "_taxonomy.md",
    "memory-policy.md",
    "maps/home.md",
    "maps/clusters/commerce.md",
    "maps/clusters/consciousness.md",
    "maps/clusters/education.md",
    "maps/clusters/media.md",
    "maps/clusters/rnd.md",
    "maps/clusters/science.md",
    "materials/partnerships-registry.md",
    "materials/identifiers.md",
    "materials/channels.md",
    "Projects/cogit-agent-stack/index.md",
    "Projects/osnova-attractor/index.md",
]


def _gh(path: str):
    req = urllib.request.Request(f"{GITHUB_API}{path}")
    req.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30, context=_SSL_CONTEXT) as resp:
            return json.load(resp)
    except Exception:
        return None


def _repo_default_branch(owner: str, repo: str) -> str:
    data = _gh(f"/repos/{owner}/{repo}") or {}
    return data.get("default_branch", "main")


def _fetch_blob(owner: str, repo: str, sha: str) -> str | None:
    data = _gh(f"/repos/{owner}/{repo}/git/blobs/{sha}")
    if not data or data.get("encoding") != "base64":
        return None
    try:
        return base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    except Exception:
        return None


def collect_repo_text_tree(
    owner: str,
    repo: str,
    allow_paths: list[str] | None = None,
    max_file_chars: int = 20000,
    max_total_chars: int = 250000,
) -> list[dict]:
    """Fetch text file contents from a repo's tree.

    With `allow_paths`, fetches exactly those paths (a curated allowlist).
    Without it, fetches every blob with a .md/.yaml/.yml extension. Submodules
    (type != "blob") are never descended into, so cold-storage submodules like
    asrp.memory's sources/ are naturally excluded.
    """
    branch = _repo_default_branch(owner, repo)
    tree_resp = _gh(f"/repos/{owner}/{repo}/git/trees/{branch}?recursive=true") or {}
    entries = tree_resp.get("tree", [])

    wanted = set(allow_paths) if allow_paths is not None else None
    files: list[dict] = []
    total = 0
    for entry in entries:
        if entry.get("type") != "blob":
            continue
        path = entry["path"]
        if wanted is not None:
            if path not in wanted:
                continue
        elif not path.endswith(TEXT_EXTENSIONS):
            continue
        content = _fetch_blob(owner, repo, entry["sha"])
        if not content:
            continue
        content = content[:max_file_chars]
        files.append({"path": path, "content": content})
        total += len(content)
        if total >= max_total_chars:
            break
    return files


def collect_personal_data(username: str = GITHUB_USERNAME) -> dict:
    profile = _gh(f"/users/{username}") or {}

    curated_files = collect_repo_text_tree(username, username)

    repos = _gh(f"/users/{username}/repos?sort=updated&per_page=50") or []
    repo_summaries = []
    for repo in repos:
        if repo.get("fork") or repo["name"] == username:
            continue
        summary = {
            "name": repo["name"],
            "description": repo.get("description"),
            "language": repo.get("language"),
            "topics": repo.get("topics", []),
            "pushed_at": repo.get("pushed_at"),
            "stars": repo.get("stargazers_count"),
        }
        langs = _gh(f"/repos/{username}/{repo['name']}/languages")
        if langs:
            summary["languages"] = langs
        readme = _gh(f"/repos/{username}/{repo['name']}/readme")
        if readme and readme.get("content"):
            text = base64.b64decode(readme["content"]).decode("utf-8", errors="replace")
            summary["readme"] = text[:4000]
        repo_summaries.append(summary)

    return {
        "profile": {
            "name": profile.get("name"),
            "bio": profile.get("bio"),
            "company": profile.get("company"),
            "location": profile.get("location"),
            "blog": profile.get("blog"),
            "public_repos": profile.get("public_repos"),
            "created_at": profile.get("created_at"),
        },
        "curated_profile_repo_files": curated_files,
        "other_public_repos": repo_summaries,
    }


def collect_asrp_data() -> dict:
    files = collect_repo_text_tree(
        ASRP_GITHUB_OWNER, ASRP_MEMORY_REPO, allow_paths=ASRP_ALLOW_PATHS
    )
    if not files:
        raise SystemExit(
            f"Не удалось прочитать {ASRP_GITHUB_OWNER}/{ASRP_MEMORY_REPO} — "
            "репозиторий приватный, установите GITHUB_TOKEN с доступом к нему."
        )
    return {"org": ASRP_GITHUB_OWNER, "repo": ASRP_MEMORY_REPO, "files": files}


PERSONAL_SYNTHESIS_PROMPT = """\
Below is raw data from a developer's GitHub account: their curated CV repo \
(profile, experience, projects, publications, skills — the source of truth) \
plus their other public repos (supplementary evidence). Synthesize it into a \
professional identity profile in Markdown that will be used to (a) score job \
postings for relevance and (b) write cover letters.

Structure it as:
# Identity: <name>
## Summary — 3-4 sentences, who this person is professionally
## Core skills — bullet list, concrete technologies with evidence from the data
## Notable projects — per project: what it is, tech stack, what it demonstrates
## Strengths to emphasize — angles that make this candidate stand out
## Likely target roles — job titles this profile realistically matches

Be honest and evidence-based: only claim skills visible in the data. Note the \
approximate depth (e.g. "multiple substantial projects" vs "one experiment").

GitHub data:
"""

ASRP_SYNTHESIS_PROMPT = """\
Below is raw data from ASRP's (Advanced Scientific Research Projects) private \
knowledge-base repo: README, navigation index, entity taxonomy, memory policy, \
and its 6 topic-cluster maps (R&D, education, commerce, consciousness, media, \
science), plus its partnerships registry and a couple of internal project pages.

Synthesize it into a company profile in Markdown that will be used to score \
job postings scraped from a job board — NOT to judge candidates, but to judge \
whether the posting is a useful business signal for ASRP. Structure it as:

# ASRP Company Profile
## Summary — 3-4 sentences: what ASRP is, its structure, its stage
## Focus areas — one bullet per cluster (R&D, education, commerce, \
consciousness/science, media), concrete enough to pattern-match against a job \
posting's domain
## Partnership & business-development signals — what kind of hiring company \
(by industry/domain) would be a good partnership or client lead for ASRP, and \
why, grounded in the actual clusters/partnerships data
## Outsourcing capabilities — what concrete kinds of project work ASRP's team \
could realistically pitch to do as a subcontractor/vendor, based on its actual \
demonstrated skills/projects (not aspirational)
## Competitive landscape — niches where a hiring company operating in the same \
space would be useful competitive intelligence
## Not relevant — the kind of ordinary job posting that is just noise for this \
lens (e.g. generic roles with no connection to any of the above)

Be honest and evidence-based: only claim focus areas/capabilities visible in \
the data. Do not invent partnerships or deals not present in the source.

ASRP knowledge-base data:
"""


def _synthesize(prompt: str, data: dict) -> str:
    client = anthropic.Anthropic()
    with client.messages.stream(
        model=CLAUDE_MODEL,
        max_tokens=16000,
        thinking={"type": "adaptive"},
        messages=[{
            "role": "user",
            "content": prompt + json.dumps(data, ensure_ascii=False, indent=1),
        }],
    ) as stream:
        response = stream.get_final_message()
    return next(b.text for b in response.content if b.type == "text")


def build_identity(profile: str = "personal", username: str | None = None) -> str:
    out_file = identity_file(profile)

    if profile == "asrp":
        print(f"Собираю данные {ASRP_GITHUB_OWNER}/{ASRP_MEMORY_REPO}...")
        data = collect_asrp_data()
        print(f"  {len(data['files'])} файлов из канона знаний")
        prompt = ASRP_SYNTHESIS_PROMPT
    else:
        username = username or GITHUB_USERNAME
        print(f"Собираю данные GitHub для {username}...")
        data = collect_personal_data(username)
        print(
            f"  профиль + {len(data['curated_profile_repo_files'])} файлов CV-репо "
            f"+ {len(data['other_public_repos'])} других репозиториев"
        )
        prompt = PERSONAL_SYNTHESIS_PROMPT

    print("Синтезирую профиль через Claude...")
    identity = _synthesize(prompt, data)
    out_file.write_text(identity)
    print(f"Профиль сохранён → {out_file}")
    return identity
