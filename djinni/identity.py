"""Build a professional identity profile from a GitHub account.

Collects public profile + repos + READMEs via the GitHub API, then asks Claude
to synthesize a structured profile (data/identity.md) that the matcher and
cover-letter generator use as the source of truth about the candidate.
"""

from __future__ import annotations

import base64
import json
import os
import urllib.request

import anthropic

from .config import CLAUDE_MODEL, GITHUB_USERNAME, IDENTITY_FILE

GITHUB_API = "https://api.github.com"


def _gh(path: str):
    req = urllib.request.Request(f"{GITHUB_API}{path}")
    req.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except Exception:
        return None


def collect_github_data(username: str = GITHUB_USERNAME) -> dict:
    profile = _gh(f"/users/{username}") or {}
    repos = _gh(f"/users/{username}/repos?sort=updated&per_page=50") or []

    repo_summaries = []
    for repo in repos:
        if repo.get("fork"):
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
        "repos": repo_summaries,
    }


SYNTHESIS_PROMPT = """\
Below is raw data from a developer's GitHub account (profile, repositories, \
languages, READMEs). Synthesize it into a professional identity profile in \
Markdown that will be used to (a) score job postings for relevance and \
(b) write cover letters.

Structure it as:
# Identity: <name>
## Summary — 3-4 sentences, who this person is professionally
## Core skills — bullet list, concrete technologies with evidence from repos
## Notable projects — per project: what it is, tech stack, what it demonstrates
## Strengths to emphasize — angles that make this candidate stand out
## Likely target roles — job titles this profile realistically matches

Be honest and evidence-based: only claim skills visible in the data. Note the \
approximate depth (e.g. "multiple substantial projects" vs "one experiment").

GitHub data:
"""


def build_identity(username: str = GITHUB_USERNAME) -> str:
    print(f"Собираю данные GitHub для {username}...")
    data = collect_github_data(username)
    print(f"  профиль + {len(data['repos'])} репозиториев")

    client = anthropic.Anthropic()
    print("Синтезирую профиль через Claude...")
    with client.messages.stream(
        model=CLAUDE_MODEL,
        max_tokens=16000,
        thinking={"type": "adaptive"},
        messages=[{
            "role": "user",
            "content": SYNTHESIS_PROMPT + json.dumps(data, ensure_ascii=False, indent=1),
        }],
    ) as stream:
        response = stream.get_final_message()

    identity = next(b.text for b in response.content if b.type == "text")
    IDENTITY_FILE.write_text(identity)
    print(f"Профиль сохранён → {IDENTITY_FILE}")
    return identity
