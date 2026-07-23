# Interloom Technologies GmbH — AI/ML Engineer

**Tier S · Приоритет №1.** Единственная вакансия сессии физически в Берлине.

## Вакансия

- **Ссылка:** https://djinni.co/jobs/835087-ai-ml-engineer/
- **Требуемый опыт:** 2 года (самый низкий барьер в Tier S/A)
- **Локация:** Remote, весь мир (но компания физически в Мюнхен/Берлин/Лондон)
- **Зарплата:** $$$$ (точная вилка не зафиксирована в сыром скрапе, не открывалась полная вакансия повторно)
- **Продукт:** tacit knowledge / context graph для AI-агентов — 3-слойный Context Graph (Source→Canonical→Projection), MemoryRank (ранжирование по исходам, без opaque vector stores), dual-harness агенты (Field Agent vs sandboxed Assistant), Procedures, Agentic Org Chart. Self-host моделей на GPU, multi-cloud K8s, Go/Terraform.

## Due diligence компании

- **Финансирование:** seed €14.2M / $16.5M (март 2026, DN Capital + Bek Ventures + Air Street Capital), до этого $3M от Air Street в 2024 (day-1 round). Суммарно ~$20M. Раунд закрыт ~4 месяца назад на момент ресёрча — деньги свежие, найм на них.
- **Клиенты:** Zurich Insurance, JLL, Fiege, Commerzbank, Volkswagen — для seed-стадии очень сильный enterprise-трекшн.
- **Тип:** 🟢 Product company, прямой работодатель.
- **Отзывы сотрудников:** не найдено (компания молодая и маленькая, ~20 человек).
- **Red flags:** Единственный сигнал — фрагмент Reddit-комментария в r/cscareerquestionsEU: *"Interviewed with them last year, felt red flags from the hiring..."* — содержание НЕ верифицировано (Reddit блокирует прямой фетч). Не реконструировать, что именно имелось в виду.
- **Gartner:** контекст-графы позиционируются как обязательная инфраструктура для agentic систем к 2028 (>50%) — подтверждает, что продукт не хайп.
- Источники: [company-due-diligence-2026-07-20.md](../../data/company-due-diligence-2026-07-20.md), [asrp-strategic-value-2026-07-20.md](../../data/asrp-strategic-value-2026-07-20.md), [interview-experience-2026-07-20.md](../../data/interview-experience-2026-07-20.md)

## ASRP-релевантность (для контекста, не для личного отклика)

Interloom — лидер по совокупности всех 4 осей ASRP-ценности: лучший тех-трансфер (context graph + multi-agent архитектура напрямую ложится на roadmap ASRP), сеть (Air Street Capital — лучший AI-first + TechBio вход в Европе), halo (категориеобразующий VC-backed стартап с Gartner-покрытием), партнёрство (кандидат на совместную разработку agent/knowledge-инфры). См. [asrp-strategic-value-2026-07-20.md](../../data/asrp-strategic-value-2026-07-20.md) для полного разбора — это отдельная, business-development линия, не смешивать с личным откликом.

## Личный контекст — весь релевантный материал

### Опыт (реальные названия, для внутреннего использования)

- **Lead Engineer, ASRP** (в CV/письмах — без "Co-Founder/CTO", см. правило в [_profile-reference.md](../_profile-reference.md)) (Apr 2023 – Present) — собственные продукты ASRP: Arcanum Landing Engine, GFS и др. (Cogit/AI_ORG сюда НЕ входят — см. ниже).
- **Cogit + AI_ORG — клиентский engagement с Osnova** (Leipzig, Germany, Oct 2025 – Mar 2026), выполнялся через ASRP как исполнителя, но продукт принадлежит Osnova. Cogit — customer-facing agent-operations слой (NestJS + React + PostgreSQL, row-level security), агенты на Gemini + Claude через web chat/email/Outlook. AI_ORG — Python/FastAPI backend для dynamic agents, tool registries, tenant-safe execution. Топ-контрибьютор (~45%) в обоих ключевых репо, владел release-процессом staging→production. Прямая параллель с multi-tenant runtime Interloom.
- **Sr. AI/ML Engineer, Woolf** (San Francisco, Apr 2025 – Sep 2025) — LLM-агент для образовательной оценки, Google ADK/Vertex AI.
- **Realtime Communications Engineer, WireBee** (Ohio, Nov 2025 – Jul 2026) — real-time телефония, Redis, WebSocket, Jambonz — НЕ прямая параллель с Interloom, но показывает опыт production-систем под реальной нагрузкой.

### Проекты

- **Cogit + AI_ORG** (клиентский engagement, Osnova) — прямая архитектурная параллель: агенты читают/пишут в общий контекст, tenant isolation, dual-deployment (web/email/Outlook).
- **Arcanum Landing Engine** (собственный продукт ASRP) — 4-repo full-cycle AI система (OpenAI agent → GraphQL backend → Nuxt editor → Nuxt renderer), живая на arcanum12th.education. ⚠️ **Пока не упоминать в CV/письмах** — проект не готов/недостаточно прописан, добавим позже, когда будет нормальное описание кейса.
- **Global Forecasting System (GFS)** (собственный продукт ASRP) — LangChain-based, прототип на Theta EuroCon хакатоне.
- **AI CV Matcher** (клиентский engagement, Woolf) — tRPC + NLP + Vertex AI.

### Публикации — прямая тематическая параллель (статьи прочитаны целиком, не только README)

- **[Docling in Working with Texts, Languages, and Knowledge](https://habr.com/en/articles/935584/)** (13.9k views, авг 2025) — **вероятно САМАЯ сильная параллель из всех 11 статей**: разбирает граф-ориентированное представление знаний (документ как сеть узлов с `label`/`text`/`links`, parent-child + semantic + alignment links), LangChain-агент, который "спрашивает" граф через MRKL-подход вместо чтения всего текста подряд — концептуально то же самое, что 3-слойный Context Graph Interloom (Source→Canonical→Projection). Написана в контексте разработки ASRP.science (научный журнал нового поколения).
- **[Building AI Agent Infrastructure: Three Paths from Chaos to Scalable Systems](https://habr.com/en/articles/960154/)** (10k+ views, окт 2025, соавтор Kyryl Zmiienko) — основана на реальном клиентском кейсе (немецкий рынок, монорепо без tool registry). 3 пути: Filesystem Registry (код `ToolRegistry` на Python) → Package Manager (инструменты как независимые пакеты) → **AgentOps/MCP+A2A** (агенты как автономные сервисы через Model Context Protocol) — прямая параллель с MemoryRank/dual-harness агентами Interloom.
- [My Personal Exam: MVP LLM Agent on Google ADK](https://habr.com/en/articles/942696/) (7.8k views) — конкретные архитектурные паттерны: `SequentialAgent`/`ParallelAgent`, `AgentTool` (агент как инструмент для другого агента), reviewer-агент для валидации перед выдачей — релевантно для dual-harness (Field Agent vs sandboxed Assistant) паттерна Interloom.
- [Google ADK and "Startup Technical Guide: AI Agents"](https://habr.com/en/articles/953592/) (5.3k views) — разбор Grounding/GraphRAG/Agentic RAG для борьбы с галлюцинациями — релевантно, раз MemoryRank Interloom явно позиционируется как "без opaque vector stores".

### Навыки — прямое совпадение

- LangChain/LangGraph — 3 года, production
- Python/FastAPI — 1+ год, production multi-tenant backend
- Node.js/TypeScript — 5 лет
- Terraform, Docker, CI/CD — 3-5 лет (но НЕ Kubernetes — см. ниже)
- Multi-agent systems — 1 год hands-on, помимо теоретического понимания через AI_ORG/Cogit

### Честные разрывы/пробелы

- **Kubernetes:** публичный skills-профиль показывает "2021-2023", но реальной глубины нет — Interloom использует "multi-cloud K8s" в стеке, это потенциальный gap, если K8s-администрирование — часть роли (а не просто "продукт деплоится на K8s кем-то другим"). Уточнить на скрининге, насколько глубоко нужен именно K8s vs Go/Terraform (Go тоже не в профиле).
- **Go:** не упоминается нигде в профиле — Interloom использует Go для части инфраструктуры. Проверить, насколько это критично для роли AI/ML Engineer (может быть не в зоне ответственности).
- Требуемый опыт всего 2 года — по факту переквалифицирован, но это не проблема, наоборот низкий барьер входа.

## Открытые вопросы к скринингу

1. Насколько роль AI/ML Engineer предполагает Go/K8s-инфраструктуру vs фокус на модельном/агентном слое?
2. Реален ли гибрид/офис в Берлине или строго remote-first с редкими встречами?
3. Что имелось в виду под неверифицированным Reddit red-flag комментарием — стоит спросить прямо о процессе найма/культуре на скрининге.
