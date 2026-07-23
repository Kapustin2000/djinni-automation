# Sigma Software — Forward AI Deployment Engineer (FDE)

**Tier A.** Деплой автономных агентов — прямое совпадение с Cogit/AI_ORG-опытом.

## Вакансия

- **Ссылка:** https://djinni.co/jobs/826500-forward-ai-deployment-engineer-fde/
- **Требуемый опыт:** 4 года, английский B2
- **Требования:** "agent factories, tool registries, multi-tenant runtime" — почти дословное описание архитектуры Cogit/AI_ORG

## Due diligence компании

- **Структура:** украинское плечо шведской Sigma Group / Danir AB, ~1500+ специалистов (DOU), основана 2002. Офисы в UA (много городов), PL, BG, RO, UZ + US/Sweden/LatAm.
- **Репутация (2026-07-21):** DOU **91/100** (Топ-50 UA, 63 голоса): компенсация 85%, условия 95%, карьера 89%, проект 92%, культура 88%, соцответственность 96%.
- **Тип:** 🟡 Outsourcing / technology consulting vendor (крупный).
- **Реальная agent-практика (не маркетинг):** «AI Compass» — productized методология (agentic SDLC, AI guardrails по ISO 42001/EU AI Act). Финал **NATO Innovation Challenge** с Agentic AI Concept (23.04.2026). Партнёрство с **NEAR AI** по confidential inference (20.04.2026). Живой кейс: для *Knowledge as a Service, Inc.* построили agentic AI SDLC на **Claude Code + Claude Cowork** (команда 4 человека — ~100 фич/мес).
- **Клиенты (научные/life-science):** AstraZeneca ×2 (COPD-исследования + systems integration), Siemens Healthineers (CT-мониторинг в Azure), CGM/CompuGroup Medical, и клиент с "multimodal naturalistic data for scientific research in social-behavioral-cognitive area" — прямой нейро/когнитивный оверлап (релевантно для ASRP-контекста, не для личного отклика).
- **Процесс собеседования:** официально 3 этапа (Technical → Secondary с Hiring/HR Manager → опциональный Client's interview), но реальные отзывы регулярно называют 4-6 раундов. Сложность Glassdoor 3.1/5 «moderate». Второй этап (Department Manager) часто сложнее первого — поведенческие вопросы, до 2.5 часов.
- **Известные вопросы:** классический DP/Knapsack на HackerRank («7 minutes left in the interview»), live coding на некоторых позициях, GraphQL/Redux (frontend), DevOps yes/no-опросник (GCP/AWS/Azure/Terraform/K8s/Docker).
- **Red flags:** ghosting — самая частая жалоба; тестовое 8+ часов без фидбека (компания официально извинилась публично на DOU); отказ после 5-6 раундов с формулировкой «нет бюджета», вакансия переоткрыта через 1-2 дня.
- **Скорость:** ~2 недели в простых случаях, до 4-5 недель с клиентскими интервью.
- Источники: [interview-experience-2026-07-20.md](../../data/interview-experience-2026-07-20.md), [asrp-strategic-value-2026-07-20.md](../../data/asrp-strategic-value-2026-07-20.md)

## ASRP-релевантность (контекст)

Вердикт «Высокая» — тех-трансфер (реальные agentic AI разработки + партнёрство NEAR AI) + клиент-сеть (AstraZeneca/Siemens/cognitive-research клиент — «родная» ASRP-смежность) + партнёрский канал (Sigma может покупать ASRP agent-tooling для FDE-практики).

## Личный контекст — весь релевантный материал

### Опыт

- **Co-Founder & CTO, ASRP** — Cogit: agent factories и tool registries для multi-tenant SaaS. "Agent factories, tool registries, multi-tenant runtime" из вакансии — это буквально описание того, что уже построено.
- **AI Platform Engineer, Osnova** (Leipzig) — tenant-safe execution layer для dynamic agents в multi-client workflows — тот же паттерн, который FDE-роль требует для работы с разными клиентами Sigma.
- **Realtime Communications Engineer, WireBee** (Ohio) — deployed voice-AI agent реальным пользователям, non-hallucinating design — демонстрирует опыт именно "forward deployment" (агент работает в реальных условиях у конечного пользователя/клиента), не только в лабораторных условиях.

### Проекты

- **Cogit** — factory pattern, спуская scoped агентов против shared tool registry, multi-tenant с первого дня.
- **AI Voice Agent** (WireBee-клиент) — прямая параллель c "agent deployed at client site" паттерном FDE-роли.
- **Cloud PBX Integration** (WireBee-клиент) — self-healing reconciliation при клиентском деплое, демонстрация надёжности агентской/интеграционной системы в проде у клиента.

### Публикации (прочитаны целиком)

- **[Building AI Agent Infrastructure](https://habr.com/en/articles/960154/)** (10k+ views, соавтор Kyryl Zmiienko) — factory/registry design тема прямо пересекается с "agent factories, tool registries" из вакансии; реальный клиентский кейс, не гипотетика.
- **[Google ADK and "Startup Technical Guide: AI Agents"](https://habr.com/en/articles/953592/)** (5.3k views) — разбор AgentOps (4-слойное тестирование) и security guardrails (defense-in-depth, Secure AI Framework) — прямая параллель с AI Compass практикой Sigma (guardrails по ISO 42001/EU AI Act).
- [My Personal Exam: MVP LLM Agent on Google ADK](https://habr.com/en/articles/942696/) (7.8k views) — практический опыт multi-agent координации (SequentialAgent/ParallelAgent/AgentTool) — релевантно для "multi-tenant runtime" части роли.

### Навыки

- LangGraph/multi-agent design — 3 года
- Docker, Terraform, CI/CD — 3-5 лет
- Production voice-AI deployment (WireBee) — дисциплина "агенты работают под реальными пользователями, не демо"

### Честные разрывы/пробелы

- **Kubernetes** — вакансия косвенно предполагает DevOps-опросник (GCP/AWS/Azure/Terraform/K8s/Docker) на техническом этапе по отзывам кандидатов. Нет реальной глубины K8s — см. общее правило. Стоит явно сказать на этапе, если вопрос всплывёт, а не пытаться закрыть общими словами.
- 4 года требуемого опыта — закрыто с запасом (10+ лет общего стажа).

## Открытые вопросы к скринингу

1. Насколько роль ориентирована на конкретных клиентов (как AstraZeneca/Siemens) vs внутреннюю AI Compass практику?
2. Учитывая реальные отзывы про 4-6 раундов вместо заявленных 3-х — уточнить ожидаемое количество этапов заранее, чтобы спланировать время.
3. Как распределяется рабочая нагрузка между Sigma-internal AI Compass разработкой и client-facing deployment?
