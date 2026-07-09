# djinni-automation

Пайплайн поиска работы на [djinni.co](https://djinni.co): Playwright-скрапер вакансий + Claude для анализа релевантности против вашего GitHub-профиля и генерации сопроводительных писем.

## Установка

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/playwright install chromium
export ANTHROPIC_API_KEY=sk-ant-...   # https://platform.claude.com
```

Опционально: `export GITHUB_TOKEN=ghp_...` — поднимает rate-limit GitHub API при сборке профиля.

## Пайплайн

```bash
# 1. Построить профиль из GitHub (Kapustin2000) → data/identity.md
.venv/bin/python cli.py identity

# 2. Скрапить вакансии → data/jobs.json
.venv/bin/python cli.py scrape --pages 5 --keyword PHP
#    любые фильтры: настройте их на djinni в браузере и скопируйте query-строку из URL
.venv/bin/python cli.py scrape --query "primary_keyword=Fullstack&exp_level=3y"

# 3. Оценить вакансии против профиля (0–10) → data/matches.json
.venv/bin/python cli.py match

# 4. Ранжированная таблица
.venv/bin/python cli.py top --min-score 6

# 5. Сопроводительное письмо → data/letters/<job_id>.md
.venv/bin/python cli.py letter 836003
.venv/bin/python cli.py letter 836003 --language Ukrainian
```

## Авторизованный скрапинг (опционально)

Публичный листинг работает без логина. Чтобы скрапить под своим аккаунтом (персональная лента, точные зарплаты):

```bash
.venv/bin/python cli.py login   # откроется браузер, залогиньтесь, нажмите Enter
```

Сессия сохраняется в `data/djinni_state.json` и дальше используется автоматически.

## Как это устроено

| Модуль | Что делает |
|---|---|
| `djinni/scraper.py` | Playwright открывает `/jobs/?page=N`; полные описания вакансий лежат прямо в листинге (`.js-original-text`), поэтому 1 страница = ~15 полных вакансий без захода в каждую |
| `djinni/identity.py` | GitHub API (профиль, репозитории, языки, README) → Claude синтезирует `data/identity.md` |
| `djinni/matcher.py` | Каждая вакансия оценивается Claude со structured output (score, вердикт, совпадения, пробелы, «хук» для письма). Профиль кэшируется через prompt caching — платите за него ~1 раз на всю пачку |
| `djinni/cover_letter.py` | Письмо 120–180 слов, опирается на профиль + анализ матчера, стримится в терминал |

Оценки инкрементальны: уже оценённые вакансии пропускаются, можно спокойно догонять базу после каждого скрапа.

## Заметки

- Модель: `claude-opus-4-8` (см. `djinni/config.py`).
- Скрапер парсит текущую верстку djinni (селекторы `.job-item`, `.job-item__position` и т.д.) — если djinni поменяет верстку, чинить в `_parse_job_card`.
- Будьте вежливы к djinni: не скрапьте сотни страниц в цикле.
