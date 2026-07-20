"""Score scraped jobs against an identity profile with Claude.

Two profiles, see djinni/identity.py:
  - "personal": is this a job the candidate should apply to?
  - "asrp": is this posting a business signal for ASRP as a company (a
    partnership lead, an outsourcing opportunity, or competitor intel)?

The identity profile goes into the system prompt with a cache breakpoint, so
scoring N jobs pays for the profile tokens roughly once.
"""

from __future__ import annotations

import json

import anthropic
from pydantic import BaseModel, Field
from rich.console import Console
from rich.table import Table

from .config import CLAUDE_MODEL, JOBS_FILE, identity_file, matches_file


class JobMatch(BaseModel):
    score: int = Field(description="Relevance 0-10: 0 = wrong profession, 10 = perfect fit")
    verdict: str = Field(description="One sentence: apply / maybe / skip, and why")
    matching_points: list[str] = Field(
        description="Candidate's concrete experience matching this job's requirements"
    )
    gaps: list[str] = Field(description="Requirements the candidate does not clearly meet")
    hook: str = Field(
        description="The single strongest angle to lead a cover letter with, or empty if score < 5"
    )


class CompanyMatch(BaseModel):
    score: int = Field(
        description="0-10 relevance to ASRP as a company: 0 = irrelevant noise, 10 = urgent lead to act on"
    )
    categories: list[str] = Field(
        description="Any of: partnership_lead, outsourcing_opportunity, competitor_intel — empty if not relevant"
    )
    verdict: str = Field(description="One sentence: what this posting signals and why it matters (or doesn't)")
    signals: list[str] = Field(
        description="Concrete facts from the posting that justify the categories/score"
    )
    suggested_action: str = Field(
        description="Concrete next step (e.g. 'reach out to <company> re: partnership'), empty if score < 4"
    )


PERSONAL_SYSTEM_TEMPLATE = """\
You are a pragmatic job-search assistant. You know the candidate through the \
identity profile below. For each job posting you receive, judge honestly how \
well the candidate fits. Do not inflate scores: a 7+ means the candidate could \
pass this screening today. Missing hard requirements (years of experience, \
core stack mismatch) must lower the score.

CANDIDATE IDENTITY PROFILE:

{identity}"""

ASRP_SYSTEM_TEMPLATE = """\
You are a business-development scout for ASRP (Advanced Scientific Research \
Projects), a research/education/consciousness-science/commerce holding. You \
know ASRP through the company profile below. Each job posting you receive was \
scraped from a job board (djinni.co) — score it NOT as a job for an individual \
candidate, but as a signal about the COMPANY that posted it:

- partnership_lead: does the hiring company operate in a space ASRP could \
partner with, sell to, or collaborate with?
- outsourcing_opportunity: does the posting describe project work ASRP's team \
could realistically pitch to do as a subcontractor/vendor, given ASRP's actual \
demonstrated capabilities in the profile?
- competitor_intel: does the hiring company operate in the same niche as ASRP, \
making this useful competitive intelligence?

A posting can match multiple categories or none. Do not inflate scores: most \
individual job postings are irrelevant noise (score 0-2) for a company like \
ASRP — reserve 6+ for a posting with a clear, concrete signal grounded in the \
profile, not a vague industry-buzzword overlap.

ASRP COMPANY PROFILE:

{identity}"""

PROFILE_CONFIG = {
    "personal": {
        "schema": JobMatch,
        "system_template": PERSONAL_SYSTEM_TEMPLATE,
        "table_title": "Вакансии по релевантности (личный профиль)",
    },
    "asrp": {
        "schema": CompanyMatch,
        "system_template": ASRP_SYSTEM_TEMPLATE,
        "table_title": "Вакансии как бизнес-сигналы для ASRP",
    },
}


def _load_jobs() -> list[dict]:
    if not JOBS_FILE.exists():
        raise SystemExit("Нет data/jobs.json — сначала запустите: python cli.py scrape")
    return json.loads(JOBS_FILE.read_text())


def match_jobs(profile: str = "personal", min_score_to_show: int = 0, limit: int | None = None) -> list[dict]:
    cfg = PROFILE_CONFIG[profile]
    id_file = identity_file(profile)
    m_file = matches_file(profile)

    if not id_file.exists():
        raise SystemExit(f"Нет {id_file} — сначала запустите: python cli.py identity --profile {profile}")
    identity = id_file.read_text()
    jobs = _load_jobs()
    if limit:
        jobs = jobs[:limit]

    existing: dict[str, dict] = {}
    if m_file.exists():
        existing = {m["job_id"]: m for m in json.loads(m_file.read_text())}

    client = anthropic.Anthropic()
    system = [{
        "type": "text",
        "text": cfg["system_template"].format(identity=identity),
        "cache_control": {"type": "ephemeral"},
    }]

    for i, job in enumerate(jobs, 1):
        if job["id"] in existing:
            continue
        job_text = (
            f"Title: {job['title']}\nCompany: {job['company']}\n"
            f"Salary band: {job.get('salary')}\nMeta: {' | '.join(job.get('meta', []))}\n"
            f"Tags: {', '.join(job.get('tags', []))}\n\n{job['description'][:6000]}"
        )
        print(f"[{i}/{len(jobs)}] {job['title']} — {job['company']}")
        response = client.messages.parse(
            model=CLAUDE_MODEL,
            max_tokens=2000,
            system=system,
            messages=[{"role": "user", "content": f"Job posting:\n\n{job_text}"}],
            output_format=cfg["schema"],
        )
        result = response.parsed_output
        if result is None:
            print("  не удалось распарсить ответ, пропускаю")
            continue
        existing[job["id"]] = {"job_id": job["id"], **result.model_dump()}
        m_file.write_text(json.dumps(list(existing.values()), ensure_ascii=False, indent=2))

    return show_top(profile=profile, min_score=min_score_to_show)


def show_top(profile: str = "personal", min_score: int = 0) -> list[dict]:
    cfg = PROFILE_CONFIG[profile]
    m_file = matches_file(profile)
    if not m_file.exists():
        raise SystemExit(f"Нет {m_file} — сначала запустите: python cli.py match --profile {profile}")
    matches = json.loads(m_file.read_text())
    jobs = {j["id"]: j for j in _load_jobs()}
    ranked = sorted(matches, key=lambda m: m["score"], reverse=True)
    ranked = [m for m in ranked if m["score"] >= min_score]

    table = Table(title=cfg["table_title"])
    table.add_column("Score", justify="right")
    table.add_column("ID")
    table.add_column("Вакансия")
    table.add_column("Компания")
    if profile == "asrp":
        table.add_column("Категории")
    table.add_column("Вердикт", max_width=60)
    for m in ranked:
        job = jobs.get(m["job_id"], {})
        row = [str(m["score"]), m["job_id"], job.get("title", "?"), job.get("company", "?")]
        if profile == "asrp":
            row.append(", ".join(m.get("categories", [])))
        row.append(m["verdict"])
        table.add_row(*row)
    Console().print(table)
    return ranked
