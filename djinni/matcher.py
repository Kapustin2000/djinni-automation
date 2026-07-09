"""Score scraped jobs against the identity profile with Claude.

The identity profile goes into the system prompt with a cache breakpoint, so
scoring N jobs pays for the profile tokens roughly once.
"""

from __future__ import annotations

import json

import anthropic
from pydantic import BaseModel, Field
from rich.console import Console
from rich.table import Table

from .config import CLAUDE_MODEL, IDENTITY_FILE, JOBS_FILE, MATCHES_FILE


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


SYSTEM_TEMPLATE = """\
You are a pragmatic job-search assistant. You know the candidate through the \
identity profile below. For each job posting you receive, judge honestly how \
well the candidate fits. Do not inflate scores: a 7+ means the candidate could \
pass this screening today. Missing hard requirements (years of experience, \
core stack mismatch) must lower the score.

CANDIDATE IDENTITY PROFILE:

{identity}"""


def _load_jobs() -> list[dict]:
    if not JOBS_FILE.exists():
        raise SystemExit("Нет data/jobs.json — сначала запустите: python cli.py scrape")
    return json.loads(JOBS_FILE.read_text())


def match_jobs(min_score_to_show: int = 0, limit: int | None = None) -> list[dict]:
    if not IDENTITY_FILE.exists():
        raise SystemExit("Нет data/identity.md — сначала запустите: python cli.py identity")
    identity = IDENTITY_FILE.read_text()
    jobs = _load_jobs()
    if limit:
        jobs = jobs[:limit]

    existing: dict[str, dict] = {}
    if MATCHES_FILE.exists():
        existing = {m["job_id"]: m for m in json.loads(MATCHES_FILE.read_text())}

    client = anthropic.Anthropic()
    system = [{
        "type": "text",
        "text": SYSTEM_TEMPLATE.format(identity=identity),
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
            output_format=JobMatch,
        )
        result = response.parsed_output
        if result is None:
            print("  не удалось распарсить ответ, пропускаю")
            continue
        existing[job["id"]] = {"job_id": job["id"], **result.model_dump()}
        MATCHES_FILE.write_text(
            json.dumps(list(existing.values()), ensure_ascii=False, indent=2)
        )

    return show_top(min_score=min_score_to_show)


def show_top(min_score: int = 0) -> list[dict]:
    if not MATCHES_FILE.exists():
        raise SystemExit("Нет data/matches.json — сначала запустите: python cli.py match")
    matches = json.loads(MATCHES_FILE.read_text())
    jobs = {j["id"]: j for j in _load_jobs()}
    ranked = sorted(matches, key=lambda m: m["score"], reverse=True)
    ranked = [m for m in ranked if m["score"] >= min_score]

    table = Table(title="Вакансии по релевантности")
    table.add_column("Score", justify="right")
    table.add_column("ID")
    table.add_column("Вакансия")
    table.add_column("Компания")
    table.add_column("Вердикт", max_width=60)
    for m in ranked:
        job = jobs.get(m["job_id"], {})
        table.add_row(
            str(m["score"]), m["job_id"],
            job.get("title", "?"), job.get("company", "?"), m["verdict"],
        )
    Console().print(table)
    return ranked
