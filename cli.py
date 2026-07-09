#!/usr/bin/env python3
"""djinni-automation CLI.

Pipeline:
  python cli.py identity                 # 1. GitHub -> data/identity.md
  python cli.py scrape --keyword PHP     # 2. djinni -> data/jobs.json
  python cli.py match                    # 3. score jobs -> data/matches.json
  python cli.py top --min-score 6        #    ranked table
  python cli.py letter <job_id>          # 4. cover letter -> data/letters/<id>.md

Optional:
  python cli.py login                    # save djinni session for authed scraping
"""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Djinni job-search automation")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("login", help="Залогиниться на djinni и сохранить сессию")

    p_scrape = sub.add_parser("scrape", help="Скрапить листинг вакансий")
    p_scrape.add_argument("--pages", type=int, default=3)
    p_scrape.add_argument("--keyword", help="primary_keyword фильтр (Python, PHP, Fullstack...)")
    p_scrape.add_argument("--query", help="сырая query-строка из URL djinni с фильтрами")

    p_identity = sub.add_parser("identity", help="Построить профиль из GitHub")
    p_identity.add_argument("--username", default=None)

    p_match = sub.add_parser("match", help="Оценить вакансии против профиля")
    p_match.add_argument("--limit", type=int, help="оценить только первые N вакансий")
    p_match.add_argument("--min-score", type=int, default=0)

    p_top = sub.add_parser("top", help="Показать ранжированный список")
    p_top.add_argument("--min-score", type=int, default=0)

    p_letter = sub.add_parser("letter", help="Сгенерировать сопроводительное письмо")
    p_letter.add_argument("job_id")
    p_letter.add_argument("--language", default="English", help="English / Ukrainian / Russian")

    args = parser.parse_args()

    if args.command == "login":
        from djinni.scraper import login
        login()
    elif args.command == "scrape":
        from djinni.scraper import scrape
        scrape(pages=args.pages, keyword=args.keyword, query=args.query)
    elif args.command == "identity":
        from djinni.identity import build_identity
        from djinni.config import GITHUB_USERNAME
        build_identity(args.username or GITHUB_USERNAME)
    elif args.command == "match":
        from djinni.matcher import match_jobs
        match_jobs(min_score_to_show=args.min_score, limit=args.limit)
    elif args.command == "top":
        from djinni.matcher import show_top
        show_top(min_score=args.min_score)
    elif args.command == "letter":
        from djinni.cover_letter import generate_letter
        generate_letter(args.job_id, language=args.language)


if __name__ == "__main__":
    main()
