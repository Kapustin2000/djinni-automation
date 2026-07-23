# Adaptiq — Principal DevOps Engineer (AWS)

**Tier C. Подтверждённый легитимный аутсорсер, но личный разрыв — "Principal"-уровень чистого DevOps.**

## Вакансия

- **Ссылка:** https://djinni.co/jobs/835490-principal-devops-engineer-aws/
- **Требуемый опыт:** 8 лет
- **Локация:** Remote, EU/UA
- **Продукт клиента:** AI-native cloud платформа для enterprise-клиентов в реальном времени
- ⚠️ У Adaptiq есть ещё несколько похожих вакансий под разных клиентов (Senior MLOps Platform Engineer $7500, Senior FullStack AI cybersecurity $8000, Senior DevOps Engineer $7500 — "платформа мониторинга для сложных hardware-систем, тот же клиент видел и в других Adaptiq-вакансиях") — паттерн один и тот же аутстафф-вендор укомплектовывает несколько параллельных клиентских проектов.

## Due diligence компании

- **Реальность:** израильский R&D staff-augmentation вендор — собирают и масштабируют удалённые продуктовые R&D-команды для израильских/глобальных tech-компаний. Вертикали клиентов: Cybersecurity, AdTech, Semiconductors, Automotive, Big Data, FinTech, AI, SaaS, Gaming, IoT, Transportation.
- **Тип:** 🟡 Outsourcing/staff-augmentation vendor (НЕ product).
- **Портфель клиентов (подтверждено):** proteanTecs (semiconductors), SQReam (GPU data), Melingo (NLP), Harmonya/TechSee/Zenity (AI & AI-agent security), Autotalks, Prisma Photonics, Duda, Bringg, Gett, Coro, Cynet, PlainID. 5 кейс-стади с конкретными цифрами (Bringg: 0→30+ спецов за 7 мес).
- **Основатели:** Oleg Shkuropat (COO), Anna Horiachkina (CDO), Michael Starr (CRO). Домен зарегистрирован 2020-11-06.
- **Red flags:** не найдено. Зрелый, легитимный вендор с прозрачным предложением (Discovery → Solution Design → Implementation → Evolution & Scaling).
- **Отзывы сотрудников:** не найдено напрямую (Glassdoor/Crunchbase 403), но на сайте подробный 4-шаговый процесс найма.
- Источники: [company-deepdive-2026-07-21-aa.md](../../data/company-deepdive-2026-07-21-aa.md), [asrp-strategic-value-2026-07-20.md](../../data/asrp-strategic-value-2026-07-20.md)

## ASRP-релевантность (контекст)

Вердикт «Средняя» — для личной роли это шаг в сторону от CTO (продают часы, не продукт), но доступ к израильской AI/cyber/semiconductor сети (proteanTecs, SQReam, Melingo, Harmonya/TechSee/Zenity) даёт реальную стратегическую ценность для ASRP — эти клиенты прямо релевантны LLM/agent-роадмапу.

## Личный контекст — весь релевантный материал

### Опыт

- **Co-Founder & CTO, ASRP** — Cogit, release-процесс staging→production, инфраструктурная дисциплина при multi-tenant архитектуре.
- **AI Platform Engineer, Osnova** (Leipzig) — Python/FastAPI, tenant-safe execution — инфраструктурная надёжность.
- **Realtime Communications Engineer, WireBee** — production infra для real-time телефонии (Redis, WebSocket) — демонстрация DevOps-дисциплины под реальной нагрузкой, хоть и не "чистый DevOps".

### Проекты

- **Cloud PBX Integration** (WireBee-клиент) — self-healing reconciliation, OAuth2-клиент с concurrency-safe token refresh — показывает инфраструктурную зрелость.
- **Cogit** — row-level security, tenant isolation — те же принципы изоляции/наблюдаемости, что нужны AWS/cyber-клиентам Adaptiq.

### Публикации

- Не специфично AI-heavy запрос (роль про DevOps/AWS, не про LLM) — публикации менее релевантны здесь, чем для AI-ролей. Если разговор коснётся AI-инфраструктуры — [Building AI Agent Infrastructure](https://habr.com/en/articles/960154/) как общий аргумент про production-grade инфраструктурное мышление.

### Навыки

- Docker, Terraform, CI/CD, AWS/GCP/Azure — 3-5 лет
- **Kubernetes — честно нет реального опыта** (см. [_profile-reference.md](../_profile-reference.md)) — не так критично для этой роли, как для CodeTiburon (где K8s — ядро архитектуры), но AWS-центричная "Principal" роль всё равно предполагает глубокую инфраструктурную экспертизу.

### Честные разрывы/пробелы

- **Главный барьер: "Principal"-уровень чистого DevOps на 8 лет.** DevOps в вашем профиле всегда шёл в связке с продуктовой разработкой (fullstack + DevOps), не отдельная многолетняя специализация такого уровня. Вероятный прямой вопрос на интервью: "сколько лет вы делали ТОЛЬКО DevOps?" — ответ честно меньше 8.
- Это тот же паттерн разрыва, что и у Metamindz UK Senior DevOps — стоит признать сходство и не пытаться закрыть его одинаково по-разному в разных письмах.

## Открытые вопросы к скринингу

1. Какой конкретно уровень "Principal" ожидается — архитектурная ответственность за AWS-инфраструктуру нескольких клиентских проектов, или именно многолетняя чистая DevOps-специализация?
2. Учитывая несколько похожих вакансий Adaptiq (MLOps, FullStack AI cybersecurity, DevOps) — уточнить, к какому именно клиенту привязана конкретно эта Principal-роль.
3. Честно взвесить: если "8 лет только DevOps" — это hard requirement, вероятно не стоит вкладывать время в подготовку.
