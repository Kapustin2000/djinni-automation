# Nova Digital — Python AI Lead

**Tier S.** Максимальная структурная стабильность в подборке — подтверждённая часть группы NOVA/Nova Poshta.

## Вакансия

- **Ссылка:** https://djinni.co/jobs/838005-python-ai-lead/
- **Требуемый опыт:** 5 лет, английский B1
- **Локация:** Remote, Ukraine
- **Продукт:** LLM & Agents платформа, 50M+ запросов/день (по словам CEO Андрея Чепиги в интервью DOU, авг. 2025) — highload инфраструктура национального масштаба
- ⚠️ **"Lead" неоднозначен** — не задокументировано, people-management это или tech lead. В вашем CV роль в AI_ORG описана как IC + "shaping platform", не formal people management — если Lead здесь означает управление людьми, это не задокументированный у вас опыт.

## Due diligence компании

- **Связь с Nova Poshta полностью подтверждена:** LinkedIn буквально "nova-poshta-digital-company", член IT Ukraine Association, упоминается в Interfax-Украина (продукт RouteStripe, −30% логистических затрат). Часть группы NOVA (Nova Poshta, NovaPay, Nova Global, Supernova Airlines) — 32M клиентов, 30 000 операций/сек.
- **Тип:** 🟢 Product company (in-house).
- **Вердикт due diligence:** НАДЁЖНО — самый структурно стабильный работодатель во всей подборке сессии.
- **Процесс собеседования (детально, DOU 20 отзывов прочитано напрямую):** 3-4 этапа для технических ролей, до 5 для senior/lead: рекрутер (Viber/Signal) → скрининг → техническое с руководителем департамента/тимлидом → интервью с ПМ (culture-fit) → для senior — доп. встречи с Product Owner/Delivery Manager/BA Lead → security check → оффер. Консенсус — "дружелюбная беседа, не допрос", без LeetCode/алгоритмов.
- **⚠️ Главный red flag сессии:** **отозванный ПОДПИСАННЫЙ оффер** (кейс PM, апрель 2024: "получил и подписал джоб-оффер, отказал другим компаниям… через несколько дней дискриминационно отказали"). Также встречается гостинг (2 месяца без фидбека) и изменение требований вакансии после прохождения этапов.
- **Скорость для успешных кандидатов:** быстро, ~1.5 недели/3 этапа, "фидбек почти мгновенный".
- Источники: [company-due-diligence-2026-07-20.md](../../data/company-due-diligence-2026-07-20.md), [interview-experience-2026-07-20.md](../../data/interview-experience-2026-07-20.md)

## ASRP-релевантность (контекст)

Вердикт «Низкая» — LLM/agent-наработки Nova Digital не подтверждены публично (на сайте novadigital.com ни одного упоминания GenAI — inferred только из вакансии). High-load инженерия переносима как дисциплина масштабной инфры, но deep-tech VC-сети за компанией нет.

## Личный контекст — весь релевантный материал

### Опыт

- **Co-Founder & CTO, ASRP** — Cogit архитектура и release ownership, топ-контрибьютор ~45%. Это единственная роль, где формально был какой-то management-компонент (co-founder), но не people-management в классическом смысле (нет отчётов о размере команды под прямым управлением).
- **AI Platform Engineer, Osnova** (Leipzig) — Python/FastAPI backend для multi-tenant agent SaaS.
- **Team Lead, MOB.325** (Ukraine, 2021-2023) — формальный "Team Lead" титул в прошлом, единственная строчка в CV, которая может подтвердить people-management опыт, если потребуется на скрининге.

### Проекты

- **Cogit** — прямая параллель по масштабу мышления ("agent systems don't get to be fragile"), хотя абсолютный объём трафика Cogit не задокументирован количественно (в отличие от заявленных 50M+ req/day у Nova Digital).
- **Global Forecasting System (GFS)** — LangChain production опыт.

### Публикации (прочитаны целиком)

- **[Building AI Agent Infrastructure](https://habr.com/en/articles/960154/)** (10k+ views) — три пути эволюции: Filesystem Registry (MVP) → Package Manager (MLP) → AgentOps (Enterprise, "microservice-like scalability") — прямая параллель с "агенты не должны быть хрупкими при 50M+ запросов/день".
- [Google ADK and "Startup Technical Guide: AI Agents"](https://habr.com/en/articles/953592/) (5.3k views) — AgentOps-раздел: "most agents fail in production not because of bad models, but because nobody does the tedious operational work" — прямо в тему highload-требований роли.
- [How to Run LLMs Locally with LM Studio](https://habr.com/en/articles/1005054/) (38.6k views, самая читаемая статья!) — если разговор коснётся инфраструктурной экономии/приватности при таком масштабе запросов, это релевантный опыт.

### Навыки

- LangChain/LangGraph, Python/FastAPI — прямое совпадение
- B1 английский — не проблема, требование ниже, чем у большинства других вакансий Tier S/A

### Честные разрывы/пробелы

- **Формат "Lead"** — главный неопределённый пункт, не пробел как таковой, а вопрос без ответа. Есть один формальный Team Lead в CV (MOB.325), но не в AI/agent контексте.
- Kubernetes — не релевантно для этой роли явно (в вакансии не упоминается), но если highload-инфраструктура подразумевает K8s — та же честная оговорка, что и везде: нет реальной глубины.

## Открытые вопросы к скринингу

1. **Первый и главный вопрос:** что означает "Lead" здесь — people-management, tech lead (архитектурная ответственность без прямых отчётов), или оба?
2. Как распределяется LLM/agent нагрузка при 50M+ запросов/день — какая часть системы уже agent-based, а какая классический ML/rule-based?
3. Учитывая red flag с отозванным подписанным оффером — **не отказываться от других активных процессов до фактического получения и подтверждения контракта на руках**, даже после устного/письменного оффера здесь.
