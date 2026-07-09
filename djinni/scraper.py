"""Playwright-based scraper for djinni.co job listings.

The public listing at /jobs/ contains full job descriptions inline
(`.js-original-text`), so one listing page yields ~15 complete jobs.
Authenticated scraping (personalized feed, salary filters) reuses a saved
Playwright storage state produced by `python cli.py login`.
"""

from __future__ import annotations

import json
import re
from urllib.parse import urlencode

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

from .config import DJINNI_BASE, JOBS_FILE, STORAGE_STATE_FILE

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)


def login() -> None:
    """Open a visible browser so the user can log in; persist the session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent=USER_AGENT)
        page = context.new_page()
        page.goto(f"{DJINNI_BASE}/login")
        print("Залогиньтесь в открывшемся окне браузера.")
        print("Когда окажетесь на своём дашборде, вернитесь сюда и нажмите Enter...")
        input()
        context.storage_state(path=str(STORAGE_STATE_FILE))
        browser.close()
    print(f"Сессия сохранена в {STORAGE_STATE_FILE}")


def _parse_job_card(card) -> dict | None:
    job_id_attr = card.get("id", "")
    m = re.match(r"job-item-(\d+)", job_id_attr)
    if not m:
        return None
    job_id = m.group(1)

    link = card.select_one("a.job_item__header-link")
    title = card.select_one(".job-item__position")
    company = card.select_one("span.small.text-gray-800")
    salary = card.select_one('span[data-bs-toggle="tooltip"][title*="Salary"]')

    # meta line: "Full Remote · Countries of Europe or Ukraine · 4 years · English - B1 · Fintech"
    meta_block = card.select_one("div.fw-medium.d-flex")
    meta = (
        [s.get_text(strip=True) for s in meta_block.select("span.text-nowrap")]
        if meta_block
        else []
    )

    tags = [b.get_text(strip=True) for b in card.select(".job-item__tags .badge")]

    desc_el = card.select_one(f"#job-description-{job_id} .js-original-text")
    if desc_el is None:
        desc_el = card.select_one(f"#job-description-{job_id}")
    description = desc_el.get_text("\n", strip=True) if desc_el else ""

    return {
        "id": job_id,
        "url": f"{DJINNI_BASE}{link['href']}" if link else None,
        "title": title.get_text(strip=True) if title else None,
        "company": company.get_text(strip=True) if company else None,
        "salary": salary.get_text(strip=True) if salary else None,
        "meta": meta,
        "tags": tags,
        "description": description,
    }


def parse_listing_html(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    jobs = []
    for card in soup.select("div.job-item[id^=job-item-]"):
        job = _parse_job_card(card)
        if job:
            jobs.append(job)
    return jobs


def scrape(pages: int = 3, keyword: str | None = None, query: str | None = None) -> list[dict]:
    """Scrape N listing pages. `keyword` maps to djinni's primary_keyword filter;
    `query` is a raw query string (e.g. "primary_keyword=PHP&exp_level=5y") for
    anything more exotic — copy it from the djinni URL after setting filters in
    the browser."""
    use_auth = STORAGE_STATE_FILE.exists()
    scraped: list[dict] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=USER_AGENT,
            storage_state=str(STORAGE_STATE_FILE) if use_auth else None,
        )
        page = context.new_page()

        for page_no in range(1, pages + 1):
            params: dict[str, str] = {}
            if keyword:
                params["primary_keyword"] = keyword
            if page_no > 1:
                params["page"] = str(page_no)
            url = f"{DJINNI_BASE}/jobs/"
            qs = urlencode(params)
            if query:
                qs = f"{query}&{qs}" if qs else query
            if qs:
                url = f"{url}?{qs}"

            page.goto(url, wait_until="domcontentloaded")
            page.wait_for_selector(".job-item", timeout=15000)
            found = parse_listing_html(page.content())
            if not found:
                break
            scraped.extend(found)
            print(f"  страница {page_no}: {len(found)} вакансий")

        browser.close()

    # merge with what we already have, newest wins
    existing: dict[str, dict] = {}
    if JOBS_FILE.exists():
        existing = {j["id"]: j for j in json.loads(JOBS_FILE.read_text())}
    for job in scraped:
        existing[job["id"]] = job
    JOBS_FILE.write_text(json.dumps(list(existing.values()), ensure_ascii=False, indent=2))
    print(f"Всего в базе: {len(existing)} вакансий → {JOBS_FILE}")
    return scraped
