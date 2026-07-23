# Seeking Alpha — Senior Python AI Engineer (LLM/Multi-Agent Systems)

**Tier B.** Легитимная известная компания, но C1 требование + нюансы, требующие внимания перед откликом.

## Вакансия

- **Ссылка:** https://djinni.co/jobs/807385-senior-python-ai-engineer-llm-multi-agent-sys/
- **Требуемый опыт:** 5 лет, английский **C1**
- **Локация:** Remote, IL/PL/UA/PT

## Due diligence компании

- **Реальность:** crowd-sourced финансовая платформа — новости, аналитика акций, Quant Ratings/Factor Grades, платные подписки. Основана 2004, David Jackson (ex-Morgan Stanley), HQ Ra'anana, Израиль. ~170 сотрудников (Wikipedia). UA-офис в Киеве, 21-80 человек, **не резидент Diia City** (минус для UA-найма — налоговые/юридические последствия).
- **Финансирование:** Series B $7M (2009, DAG Ventures + Benchmark + Accel), контент-партнёрство с Nasdaq. Текущая выручка/captable не раскрываются.
- **Тип:** 🟢 Product company.
- **⚠️ Важный технический нюанс — стек компании реально Ruby/Rails + Go + Objective-C (iOS), НЕ Python как основа.** GitHub-организация (149 публичных репо, spot-checked): форк `vellum-client-ruby` (Vellum.ai — LLMOps) от июня 2025 и оригинальный `git-log-mcp` (FastMCP-сервер) от февраля 2026 — показывают, что LLM/MCP-работа реальна, но встроена в Ruby-экосистему, не Python-first. Вакансия называется "Python AI Engineer" — возможно это отдельная новая инициатива/команда, а не основной стек компании. **Уточнить на скрининге, действительно ли роль Python-центричная или Python — это добавочный слой поверх Ruby-инфраструктуры.**
- **Отзывы о найме:** на DOU всего **1 отзыв** (март 2025) — негативный (тестовое задание → шаблонный отказ без обратной связи).
- **Red flags:** (1) Wikipedia-секция "Alleged use by stock manipulators" — короткие продавцы использовали псевдонимы (исследование Columbia Law School); сама компания не признана виновной, после этого ужесточила политику модерации; (2) не Diia City; (3) слишком маленькая выборка отзывов для надёжной оценки культуры.
- Источники: [company-deepdive-2026-07-21-ad.md](../../data/company-deepdive-2026-07-21-ad.md), [asrp-strategic-value-2026-07-20.md](../../data/asrp-strategic-value-2026-07-20.md)

## ASRP-релевантность (контекст)

Вердикт «Средняя» — реальный прикладной LLM/MCP-стек (форк vellum-client-ruby, git-log-mcp) + сильный global-fintech halo, частично переносимо на GFS-forecasting. Deep-tech/neuro/quantum интереса за компанией нет — это финтех-медиа, не deep-tech.

## Личный контекст — весь релевантный материал

### Опыт

- **Co-Founder & CTO, ASRP** — Global Forecasting System (GFS), LangChain-based forecasting.
- **AI Platform Engineer, Osnova** (Leipzig) — Python/FastAPI production опыт.

### Проекты и публикации — что реально подходит (и что подавать осторожно)

- **[Building an App Store Review Analysis Pipeline with Python NLP & Data Visualization](https://kapustinomm.hashnode.dev/building-an-app-store-review-analysis-pipeline-with-python-nlp-and-data-visualization)** — **лучший аргумент из всей публикационной базы для этой конкретной вакансии.** Модульный Python pipeline (FastAPI → RSS fetcher → text cleaning → VADER sentiment с гибридной формулой `0.6*text_sentiment + 0.4*star_rating` → TF-IDF keyword/issue extraction → insights engine с severity scoring). Явный архитектурный выбор в статье: "детерминированный модульный pipeline вместо end-to-end AI-агента... deterministic design ensures consistent, auditable results... essential for research-level reliability" — это ПОЧТИ дословно то, чем занимается Seeking Alpha с Quant Ratings (превращение текста/данных в структурированный, тестируемый, auditable сигнал).
- **Global Forecasting System (GFS)** — LangChain production форecasting-платформа. **⚠️ Осторожность:** GFS технически про анализ снов и коллективного бессознательного (см. [My First AI & Blockchain Hackathon](https://habr.com/en/articles/947040/)) — для серьёзной fintech-аудитории Seeking Alpha **лучше не углубляться в детали про сны**, упоминать GFS абстрактно ("forecasting platform aggregating multi-source signals for social/economic/geopolitical events") или вообще не упоминать, полагаясь на App Store Review Analysis статью как основной аргумент.
- [My Personal Exam: MVP LLM Agent on Google ADK](https://habr.com/en/articles/942696/) (7.8k views) — multi-agent координация, релевантно для "Multi-Agent Systems" части названия вакансии.

### Навыки

- Python/FastAPI, NLP (TF-IDF, sentiment analysis) — прямое совпадение с App Store Review Analysis опытом
- LangChain/LangGraph (3 года)
- **Ruby/Rails — НЕ в профиле.** Если реальный стек компании Ruby-based (см. red flag выше), это существенный gap, не задокументированный нигде.

### Честные разрывы/пробелы

- **C1 английский** — требует самопроверки, как и для CodeTiburon/Metamindz.
- **Возможный Python vs Ruby mismatch** — см. due diligence выше, реальный стек компании (GitHub) заметно более Ruby-ориентирован, чем предполагает название вакансии.
- Multi-agent orchestration — есть опыт (Cogit/GFS/AI_ORG), но не в контексте именно finance/investment-данных за пределами App Store Review Analysis статьи (которая не про финансы, а про app-store отзывы, хоть и той же методологической школы).

## Открытые вопросы к скринингу

1. **Первый вопрос:** насколько роль Python-центрична на практике, учитывая, что основной стек компании по GitHub — Ruby/Rails? Это новая инициатива или ошибка в описании вакансии?
2. Проверить реальный уровень английского (C1) до вложения времени в подготовку.
3. Учитывая единственный, негативный отзыв о найме (тестовое → шаблонный отказ) — уточнить процесс интервью заранее, не полагаться только на общие ожидания.
4. Не резидент Diia City — уточнить, как это влияет на налоговую/юридическую структуру для украинских кандидатов конкретно.
