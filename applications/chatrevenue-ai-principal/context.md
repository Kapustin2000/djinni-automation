# ChatRevenue.ai — Principal Backend Engineer (Python/AI)

**Tier S.** Единственная вакансия сессии, явно называющая LangChain + LangGraph + LangSmith в требованиях.

## Вакансия

- **Ссылка:** https://djinni.co/jobs/824065-principal-backend-engineer-python-ai/
- **Требуемый опыт:** 5 лет, английский B2
- **Локация:** Remote, весь мир
- **Продукт:** agentic post-CRM — «post-CRM sales automation», LLM workflows поверх коммуникаций (email/calendar/Zoom/Slack) → граф бизнес-отношений
- **Стек (из вакансии):** LangChain, LangGraph, LangSmith, RAG/embeddings/vector search, knowledge graphs (NetworkX), Python/FastAPI, PostgreSQL, K8s, Azure, Kafka/Event Hub
- Есть вторая вакансия той же компании (Senior AI Engineer, IC-уровень, B2, 5 лет) — [chatrevenue-ai-senior/](../chatrevenue-ai-senior/context.md), не откликаться на обе одновременно

## Due diligence компании

- **Фаундеры подтверждены через LinkedIn:** Ratmir Timashev (со-основатель Veeam, exit ~$5B) и Vlad Voskresensky (со-основатель Revenue Grid, ~600k enterprise-клиентов). LinkedIn Воскресенского прямо указывает ChatRevenue.ai как текущее место; RocketReach подтверждает.
- **Стадия:** stealth-mode, до ~20 человек. DOU.ua: «Відгуків поки що немає». Glassdoor-профиля нет вообще.
- **Финансирование:** раунд не раскрыт (фаундер-бэкинг) — но у Тимашева после Veeam нет проблем с капиталом.
- **Тип:** 🟢 Product company.
- **Red flags:** не найдено (компания слишком молода для следа на Glassdoor/Reddit/Blind).
- **Отзывы о найме:** не найдено ни одного (ни позитивного, ни негативного) — честная "не нашлось", не путать с отсутствием проблем.
- Источники: [company-due-diligence-2026-07-20.md](../../data/company-due-diligence-2026-07-20.md), [interview-experience-2026-07-20.md](../../data/interview-experience-2026-07-20.md), [asrp-strategic-value-2026-07-20.md](../../data/asrp-strategic-value-2026-07-20.md)

## ASRP-релевантность (контекст, не для личного отклика)

Вердикт «Средняя» двойная выгода: единственная из AI-продуктовых компаний с явно названным LangChain+LangGraph+LangSmith стеком — готовая референс-реализация мейнстрим-агентного стека, но новизны для ASRP немного (сеть Тимашева/Воскресенского — enterprise-IT/SalesTech, не deep-tech). Halo сильный в enterprise-IT через имя Тимашева.

## Личный контекст — весь релевантный материал

### Опыт (реальные названия, для внутреннего использования)

- **Co-Founder & CTO, ASRP** (Apr 2023 – Present) — Cogit: Python агент-authoring сервис (генерация агента из текстового описания за ~1 минуту) → NestJS/PostgreSQL backend (RLS для tenant isolation) → агенты на Gemini/Claude, деплой в web chat/email/Outlook. Топ-контрибьютор ~45% в обоих ключевых репо.
- **AI Platform Engineer, Osnova** (Leipzig, Germany, Oct 2025 – Mar 2026) — Python/FastAPI backend для dynamic agents, tool registries, tenant-safe execution, email workflows, scheduling. Прямая параллель с "communications → agent workflow" продуктом ChatRevenue.ai.
- **Sr. AI/ML Engineer, Woolf** (San Francisco, Apr 2025 – Sep 2025) — LLM-агент для образовательной оценки на Google ADK/Vertex AI.
- Python специфично — 3 года (2023-наст.), не 5 лет как в требовании — но domain-опыт (агенты, LLM workflows) содержательно перекрывает разрыв в годах.

### Проекты — прямое совпадение по архитектуре

- **Cogit** — ключевой аргумент: агенты читают/пишут в общий контекст/граф, не изолированные промпты; ровно то же самое, что ChatRevenue.ai описывает как "коммуникации → граф бизнес-отношений".
- **Global Forecasting System (GFS)** — LangChain/LangGraph production опыт помимо Cogit.
- **AI CV Matcher** (Woolf) — NLP + LLM для структурированного анализа документов, релевантно для RAG/embeddings части стека.

### Публикации (прочитаны целиком)

- **[Docling in Working with Texts, Languages, and Knowledge](https://habr.com/en/articles/935584/)** (13.9k views, авг 2025) — **прямое попадание в "knowledge graphs (NetworkX)" требование вакансии.** Документ как граф узлов (`DocItem`: `label`/`text`/`links`), parent-child + semantic ("related-to", "supports") + alignment links, LangChain-агент запрашивает граф через MRKL вместо чтения всего текста. Конкретный пример: превращение научной статьи в queryable knowledge graph — тот же паттерн, что нужен для "коммуникации → граф бизнес-отношений".
- **[Building AI Agent Infrastructure](https://habr.com/en/articles/960154/)** (10k+ views, окт 2025) — Filesystem Registry → Package Manager → AgentOps/MCP&A2A — архитектурная параллель для LangGraph/orchestration части, включая реальный код `ToolRegistry`.
- [Google ADK and "Startup Technical Guide: AI Agents"](https://habr.com/en/articles/953592/) (5.3k views) — разбирает эволюцию **RAG → GraphRAG → Agentic RAG** — прямая параллель с "RAG/embeddings/vector search, knowledge graphs" из требований вакансии.
- [Building a Resume Matcher with tRPC, NLP, and Vertex AI](https://habr.com/en/articles/943306/) (24k+ reads) — структурированный JSON-output паттерн (score/strengths/suggestions) — демонстрирует опыт получения предсказуемой структуры из LLM, не свободного текста.
- [My Personal Exam: MVP LLM Agent on Google ADK](https://habr.com/en/articles/942696/) (7.8k views) — конкретные паттерны координации агентов (SequentialAgent/ParallelAgent/AgentTool), философия "агент должен реально доводить задачу до конца".

### Навыки — прямое совпадение

- LangChain/LangGraph — 3 года, production (ASRP)
- Python/FastAPI — Osnova (production, multi-tenant)
- Knowledge graphs / NetworkX-смежное — через Docling-статью и Cogit context layer
- Kafka — НЕ в профиле явно (см. разрывы)
- K8s — см. разрывы (общий паттерн для нескольких вакансий, не только этой)

### Честные разрывы/пробелы

- **Python — 3 года vs требуемые 5.** Компенсируется content-опытом (агенты, LLM workflows — именно то, что ищут), но формально годы не совпадают. Не скрывать при прямом вопросе.
- **Kafka/Event Hub** — не встречается в профиле ни разу. Если это критичная часть стека (а не просто одна из систем в инфраструктуре), стоит явно спросить на скрининге, насколько глубоко нужно.
- **Kubernetes** — публичный профиль показывает 2021-2023, реальной сегодняшней глубины нет. Вакансия называет K8s в стеке — уточнить формат использования (deploy-only vs administer).
- **"Principal"-уровень** — по объёму лет может читаться overqualified-по-годам/underqualified-по-Python-специфично; это стоит обсуждать прямо, не через письмо.

## Открытые вопросы к скринингу

1. Насколько критичен опыт именно с Kafka/Event Hub — можно ли закрыть эквивалентным опытом с очередями (Redis, что есть в профиле)?
2. Как выглядит K8s-часть роли — администрирование кластера или просто деплой поверх готовой инфры?
3. Что означает "Principal" здесь конкретно — архитектурная ответственность, people-management, или оба?
4. Стоит ли откликаться на обе вакансии (Principal + Senior) или выбрать одну сразу?
