"""Generate a cover letter for a specific job, grounded in the identity profile
and the matcher's analysis (matching points + hook)."""

from __future__ import annotations

import json

import anthropic

from .config import CLAUDE_MODEL, IDENTITY_FILE, JOBS_FILE, LETTERS_DIR, MATCHES_FILE

PROMPT = """\
Write a cover letter for the job below, on behalf of the candidate described \
in the identity profile.

Rules:
- Language: {language}.
- 120-180 words. Djinni recruiters skim: short beats thorough.
- Lead with the hook (the candidate's strongest matching angle), not with \
"I am writing to apply".
- Reference 1-2 concrete projects/skills from the profile that map to this \
job's actual requirements. Never invent experience.
- If the match analysis lists gaps, do not draw attention to them, but do not \
lie about them either.
- Tone: direct, confident, human. No corporate filler, no flattery about the \
company unless the posting gives a concrete reason.
- End with a simple availability/next-step line.

CANDIDATE IDENTITY PROFILE:
{identity}

MATCH ANALYSIS (from a prior screening step):
{match}

JOB POSTING:
{job}

Output only the letter text, no preamble.
"""


def generate_letter(job_id: str, language: str = "English") -> str:
    if not IDENTITY_FILE.exists():
        raise SystemExit("Нет data/identity.md — сначала запустите: python cli.py identity")
    jobs = {j["id"]: j for j in json.loads(JOBS_FILE.read_text())}
    job = jobs.get(job_id)
    if not job:
        raise SystemExit(f"Вакансия {job_id} не найдена в data/jobs.json")

    match: dict = {}
    if MATCHES_FILE.exists():
        match = next(
            (m for m in json.loads(MATCHES_FILE.read_text()) if m["job_id"] == job_id),
            {},
        )

    job_text = (
        f"Title: {job['title']}\nCompany: {job['company']}\n"
        f"Meta: {' | '.join(job.get('meta', []))}\n\n{job['description'][:6000]}"
    )

    client = anthropic.Anthropic()
    with client.messages.stream(
        model=CLAUDE_MODEL,
        max_tokens=4000,
        thinking={"type": "adaptive"},
        messages=[{
            "role": "user",
            "content": PROMPT.format(
                language=language,
                identity=IDENTITY_FILE.read_text(),
                match=json.dumps(match, ensure_ascii=False, indent=1) if match else "(not scored yet)",
                job=job_text,
            ),
        }],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
        response = stream.get_final_message()
    print()

    letter = next(b.text for b in response.content if b.type == "text")
    out = LETTERS_DIR / f"{job_id}.md"
    out.write_text(f"# {job['title']} — {job['company']}\n{job['url']}\n\n---\n\n{letter}\n")
    print(f"\nСохранено → {out}")
    return letter
