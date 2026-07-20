# djinni-automation

Пайплайн поиска работы на [djinni.co](https://djinni.co): Playwright-скрапер вакансий + Claude для анализа релевантности против вашего GitHub-профиля и генерации сопроводительных писем.

## Установка

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/playwright install chromium
export ANTHROPIC_API_KEY=sk-ant-...   # https://platform.claude.com
```

Опционально: `export GITHUB_TOKEN=ghp_...` — поднимает rate-limit GitHub API при сборке профиля. \
**Обязательно** для профиля `asrp` — `asrp.memory` приватный, токен должен иметь к нему доступ.

## Два профиля матчинга

Одна и та же база вакансий (`data/jobs.json`) оценивается через два независимых объектива:

| Профиль | Источник профиля | Вопрос |
|---|---|---|
| `personal` (по умолчанию) | GitHub-репо `Kapustin2000/Kapustin2000` (CV-дерево: experience/, projects/, publications/, skills/) + остальные публичные репо | Стоит ли мне откликнуться на эту вакансию? |
| `asrp` | Приватный `AdvancedScientificResearchProjects/asrp.memory` (README, index, cluster maps, партнёрский реестр) | Что эта вакансия говорит о компании-нанимателе: лид на партнёрство, возможность аутсорса для ASRP, или конкурентная разведка? |

## Пайплайн

```bash
# 1. Построить профили из GitHub
.venv/bin/python cli.py identity                    # → data/identity.md (личный)
.venv/bin/python cli.py identity --profile asrp     # → data/identity_asrp.md (ASRP)

# 2. Скрапить вакансии → data/jobs.json
.venv/bin/python cli.py scrape --pages 5 --keyword PHP
#    любые фильтры: настройте их на djinni в браузере и скопируйте query-строку из URL
.venv/bin/python cli.py scrape --query "primary_keyword=Fullstack&exp_level=3y"

# 3. Оценить вакансии против каждого профиля (0–10)
.venv/bin/python cli.py match                       # → data/matches.json
.venv/bin/python cli.py match --profile asrp        # → data/matches_asrp.json

# 4. Ранжированная таблица
.venv/bin/python cli.py top --min-score 6
.venv/bin/python cli.py top --profile asrp --min-score 4

# 5. Сопроводительное письмо (только для личного профиля) → data/letters/<job_id>.md
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
| `djinni/identity.py` | Для `personal` — GitHub API читает всё CV-дерево `Kapustin2000/Kapustin2000` + остальные репо. Для `asrp` — читает курируемый список файлов из приватного `asrp.memory` (README/index/cluster maps/партнёрский реестр), пропуская `sources/` (субмодули — «холодное хранилище»), `investigations/` (черновики) и `maps/entities/` (147 файлов, избыточно). Claude синтезирует профиль в Markdown |
| `djinni/matcher.py` | Каждая вакансия оценивается Claude со structured output. Для `personal` — score/вердикт/совпадения/пробелы/«хук» для письма. Для `asrp` — score/категории (`partnership_lead`, `outsourcing_opportunity`, `competitor_intel`)/сигналы/предлагаемое действие. Профиль кэшируется через prompt caching — платите за него ~1 раз на всю пачку |
| `djinni/cover_letter.py` | Письмо 120–180 слов, опирается на профиль + анализ матчера, стримится в терминал |

Оценки инкрементальны: уже оценённые вакансии пропускаются, можно спокойно догонять базу после каждого скрапа.

## Заметки

- Модель: `claude-opus-4-8` (см. `djinni/config.py`).
- Скрапер парсит текущую верстку djinni (селекторы `.job-item`, `.job-item__position` и т.д.) — если djinni поменяет верстку, чинить в `_parse_job_card`.
- Будьте вежливы к djinni: не скрапьте сотни страниц в цикле.
