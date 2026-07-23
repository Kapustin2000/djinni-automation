# N-iX — AI Application Engineer

**Tier A.** Использование Claude Code/Codex как ежедневного инструмента — прямое совпадение с текущей практикой.

## Вакансия

- **Ссылка:** https://djinni.co/jobs/827680-ai-application-engineer/
- **Требуемый опыт:** 7 лет (общий стаж закрыт — 10+ лет)
- **Требования:** Claude Code/Codex/ChatGPT/Vercel как ежедневный инструмент — буквально описание вашей практики, не абстрактный "AI experience"

## Due diligence компании

- **Масштаб:** ~2400+ инженеров (сайт/uk-Wikipedia), на DOU "понад 1500 спеціалістів", 10 стран (UA, PL, US, MT, SE, BG, RO, CO, IN, UK). Юр. HQ — Валлетта, Мальта; операционно — Львів. Основана в августе 2002 как NovelliX. Tracxn — unfunded company (founder-owned, без VC/PE).
- **Репутация (2026-07-21):** DOU **89/100** (3-е место среди 1500+ в «Найкращі ІТ-роботодавці 2025»), Best Inspiring Workplace in Europe 2024 (#1), 2026 (#4), Global Top 100 (#36).
- **Тип:** 🟡 Outsourcing vendor / product engineering services.
- **Agent-практика:** APEX-фреймворк (production Agentic AI), партнёрство с **Palantir** (первый UA-партнёр, Foundry-команда) и **Cursor** (AI-Augmented Team), AWS Premier Tier + AI Services Competency, Microsoft AI Cloud Partner.
- **Процесс собеседования:** 2-3 раунда обычно (скрининг → техническое 1-2ч с tech lead → финальный клиентский созвон). Встречаются крайности: марафон 5 вакансий/5 рекрутеров/13 месяцев без оффера; отдельная вакансия с 7 этапами ~8 часов (HR подтвердила — «требование клиента»).
- **Сложность интервью:** Glassdoor 3.13/5, «умеренная», большой разброс качества по конкретному интервьюеру.
- **Red flags:** массовый гостинг после техинтервью (жалобы 2022-2026), один отозванный устный оффер (Senior PM, 2020), lowball после успешного техинтервью (Scala, 2016), нескоординированность рекрутеров (5 разных сорсеров с нуля на одного кандидата). Существенных red flags как работодателя в целом — не найдено, это точечные исторические кейсы.
- **Скорость процесса:** от 4 дней до 3 недель по Glassdoor; на DOU за последние 2 года часто 1.5+ месяца.
- Источники: [company-due-diligence-asrp-remaining] н/д (N-iX был в основной due-diligence-2026-07-21 через dd_ad батч), [interview-experience-2026-07-20.md](../../data/interview-experience-2026-07-20.md), [asrp-strategic-value-2026-07-20.md](../../data/asrp-strategic-value-2026-07-20.md)

## ASRP-релевантность (контекст)

Вердикт «Средняя» — глубочайший agent-stack-overlap в выборке (LangChain/LangGraph/CrewAI, RAG, LLMOps guardrails), плюс named deep-tech/life-science клиенты (**Beyond Limits** — Caltech/NASA-JPL spinoff, cognitive AI; Fluke — научные приборы; Weinmann Emergency, Think Research, Brighter — health-tech). Halo высокий, но ядро остаётся engineering-services вендором без собственной deep-tech-повестки.

## Личный контекст — весь релевантный материал

### Опыт

- **Co-Founder & CTO, ASRP** — Cogit, топ-контрибьютор ~45%, heavily agent-assisted development (Claude Code как основной инструмент разработки самого Cogit, не только фичи продукта).
- **AI Platform Engineer, Osnova** (Leipzig) — Python/FastAPI, tool registries, agent factories.
- **Realtime Communications Engineer, WireBee** (Ohio, США) — voice-AI для inbound carrier calls, деплой в продакшн для реальных пользователей (не демо), детерминированный backend + non-hallucinating agent design — релевантно для "AI Application Engineer" фокуса на прикладной инженерии, не research.

### Проекты

- **Cogit** — построен с активным использованием agent-assisted coding практик.
- **AI Voice Agent** (WireBee-клиент) — non-hallucinating by construction, декомпозиция монолитного агента на multi-agent систему.
- **Cloud PBX Integration** (WireBee-клиент) — крупнейший проект контракта, self-healing reconciliation.

### Публикации — прямая параллель (прочитаны целиком)

- **[Google ADK and "Startup Technical Guide: AI Agents"](https://habr.com/en/articles/953592/)** (5.3k views, окт 2025) — **самое прямое попадание в требования вакансии.** Разбор security-раздела гайда Google: defense-in-depth, prompt-injection защита, "least-privilege tool restrictions", Secure AI Framework (SAIF) — практически дословно совпадает с "LLMOps guardrails (prompt-injection/RBAC/content filtering)" из вакансии N-iX. Также разбирает AgentOps (4-слойное тестирование: component/trajectory/outcome/system monitoring) — релевантно для APEX-фреймворка N-iX.
- **[Building AI Agent Infrastructure](https://habr.com/en/articles/960154/)** (10k+ views, окт 2025) — Filesystem Registry → Package Manager → AgentOps/MCP&A2A, реальный клиентский кейс — прямо релевантна тому, как N-iX описывает APEX-фреймворк как production agent factory.
- [How to Integrate Google ADK with a Custom Interface](https://habr.com/en/articles/933804/) (10.4k views) — production-ready implementation guide (adk web → api_server → Vertex AI Agent Engine deployment), показывает опыт end-to-end интеграции agent framework, не только прототипирования.
- [My Personal Exam: MVP LLM Agent on Google ADK](https://habr.com/en/articles/942696/) (7.8k views) — конкретные паттерны валидации/reviewer-агента перед выдачей ответа — релевантно для "content filtering" части LLMOps guardrails.

### Навыки

- Claude Code/Codex как ежедневный инструмент — прямое, буквальное совпадение с требованием вакансии
- LangGraph — 3 года
- LLMOps-смежные темы (prompt-injection defense, RBAC, content filtering) — частично через опыт non-hallucinating agent design (WireBee voice-AI проект)

### Честные разрывы/пробелы

- Ни одного явного разрыва по стеку не выявлено — самое близкое совпадение требований к практике во всей подборке.
- K8s — не упоминается явно в требованиях этой конкретной вакансии, вероятно не критично.

## Открытые вопросы к скринингу

1. Уточнить, к какому именно клиентскому проекту привязана роль — учитывая outstaff-модель N-iX, финальный клиентский созвон часто решающий.
2. Спросить про реальную длительность процесса для этой конкретной роли, учитывая широкий разброс (4 дня — 3 недели по старым данным, 1.5+ месяца по недавним отзывам).
3. Уточнить формат оплаты фидбека/скорость между этапами заранее, учитывая задокументированные случаи гостинга.
