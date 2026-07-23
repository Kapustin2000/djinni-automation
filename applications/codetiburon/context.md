# CodeTiburon — Founding AI Platform Architect (Python + K8s)

**Tier A, но с реальным разрывом.** Верифицированный кейс "Building Production Infrastructure for an AI Agent Engineering Platform" — архитектурно близко к тому, что вы строили. **Но вакансия прямо требует K8s, а реального опыта K8s нет.**

## Вакансия

- **Ссылка:** https://djinni.co/jobs/835471-founding-ai-platform-architect-python-and-kub/
- **Требуемый опыт:** 7 лет, английский **C1**
- **Требования:** Python + Kubernetes как основа архитектуры — K8s явно акцентирован, не побочная деталь

## ⚠️ Ключевой личный разрыв — не смягчать

**K8s: реального опыта нет.** Публичный skills-профиль формально показывает "Kubernetes 2 yrs, 2021-2023" (через MOB.325/LAB325), но по факту глубины, достаточной для роли "Founding AI Platform Architect", где K8s — основа архитектуры, — нет. Это не «не в последнем окне», это честно «не умею на уровне, который нужен архитектору». Решить до отклика: либо (а) не откликаться на эту конкретную вакансию, либо (б) откликаться с явным честным дисклеймером в первом же сообщении, чтобы не терять время на нескольких раундах интервью, если K8s — hard requirement.

## Due diligence компании

- **Реальность:** харьковская аутсорс-компания с 2009 года — 17 лет, точно не однодневка. Clutch-профиль с позитивными клиентскими отзывами ("organized, good at estimates, not the cheapest"). После начала полномасштабной войны ребрендировалась в "European AI-native engineering company".
- **Тип:** 🟡 Outsourcing vendor.
- **Верифицированный кейс:** "Building Production Infrastructure for an AI Agent Engineering Platform" (eval-пайплайны, workflow-оркестрация, observability, CI/CD quality gates) — близкое совпадение со стеком роли (Python+K8s+LLM+Agents+Knowledge Graphs).
- **Отзывы сотрудников:** все 10 отзывов на DOU (2019-2022) позитивные, но о работе внутри, не о собеседованиях. Интервью-опыт кандидатов **не найден вообще** — ни этапы, ни сложность, ни red flags, ни скорость процесса. Glassdoor заблокирован Cloudflare.
- **Нюанс роли:** "Founding" внутри 17-летней стабильной компании — новое продуктовое направление внутри устойчивого бизнеса, мягче риск, чем founding в чистом стартапе, но и upside (equity) вероятно скромнее. Стоит спросить прямо на скрининге.
- Источники: [company-due-diligence-2026-07-20.md](../../data/company-due-diligence-2026-07-20.md), [interview-experience-2026-07-20.md](../../data/interview-experience-2026-07-20.md)

## ASRP-релевантность (контекст)

Вердикт «Средняя-высокая» тех-трансфер (верифицированный agent-platform-инфра кейс), но низкая сеть/halo. Партнёрство — потенциальный staff-aug/инженерное расширение под KG+agent-билд ASRP.

## Личный контекст — весь релевантный материал

### Опыт

- **Co-Founder & CTO, ASRP** — Cogit, релиз-пайплайн staging→production, топ-контрибьютор ~45%.
- **AI Platform Engineer, Osnova** (Leipzig) — tool registries, tenant-safe execution — архитектурная часть роли совпадает хорошо.

### Проекты

- **Cogit** — eval-driven итерация, tool-registry design, multi-tenant safety — именно то, что нужно "Founding AI Platform Architect" на архитектурном уровне.

### Публикации (прочитаны целиком)

- **[Building AI Agent Infrastructure](https://habr.com/en/articles/960154/)** (10k+ views) — прямая параллель с verified кейсом CodeTiburon ("eval pipelines, workflow orchestration, observability, CI/CD quality gates") — статья разбирает ровно этот путь эволюции от MVP к enterprise-зрелой agent-инфраструктуре (Filesystem Registry → Package Manager → AgentOps).
- [Google ADK and "Startup Technical Guide: AI Agents"](https://habr.com/en/articles/953592/) (5.3k views) — раздел AgentOps описывает именно eval-пайплайны (4-слойное тестирование: component/trajectory/outcome/system monitoring) — прямая параллель с "eval pipelines" в описании кейса CodeTiburon.

### Навыки

- Python/FastAPI, agent factories, tool registries — совпадение
- **K8s — честно нет.** Terraform/Docker/CI-CD есть, но это не то же самое, что архитектура на Kubernetes.
- **C1 английский** — отдельный вопрос для честной самооценки, требование высокое (как и у Metamindz/Seeking Alpha).

### Честные разрывы/пробелы

1. **Kubernetes — нет реального опыта.** Главный блокер этой конкретной вакансии.
2. **C1 английский** — требует отдельной самопроверки перед серьёзной подготовкой.
3. Оба разрыва одновременно — вероятно, самая рискованная вакансия Tier A по совокупности требований.

## Открытые вопросы к скринингу

1. **Первым вопросом:** насколько K8s — это hands-on администрирование кластеров архитектором, или архитектурные решения поверх managed K8s (EKS/GKE), которые не требуют глубокого operational опыта?
2. Что конкретно означает "Founding" в контексте 17-летней компании — реальный equity upside или просто новое название для нового direction?
3. Проверить свой английский уровень объективно (тест/самооценка) до вложения времени в подготовку — общая рекомендация для C1-вакансий.
