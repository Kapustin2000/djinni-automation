# DualEntry — Backend Engineer (до $20000)

**Tier C. Финансово реально, но культура настораживает.**

## Вакансия

- **Ссылка:** https://djinni.co/jobs/834780-backend-engineer/
- **Требуемый опыт:** 5 лет, английский C1
- **Зарплата:** до $20000/мес — аномально высокая для грейда, изначально казалась подозрительной (см. ниже — подтверждена).

## Due diligence компании

- **Финансирование подтверждено:** основана 2024 в Нью-Йорке (Benedict Dohmen, Santiago Nestares), вышла из stealth в октябре 2025 с **Series A $90M от Lightspeed, Khosla Ventures и GV (Google Ventures)** при оценке ~$415M; суммарно >$100M за 15 месяцев. Заявленный масштаб — $100B журнальных проводок через платформу.
- **⚠️ Проверяемый red flag по культуре:** Glassdoor — **2.7/5 по ~15-16 отзывам, лишь 41% рекомендуют**. Заголовки: «Talented team hindered by brutal culture, lack of ethics, and poor leadership», «Terrible culture and lack of leadership»; в текстах — «people are worked into the ground», микроменеджмент, WLB 2.5/5.
- **Тип:** 🟢 Product company (AI-native ERP).
- **Вердикт:** финансово НАДЁЖНО, по культуре НАСТОРАЖИВАЕТ — высокая зарплата, судя по всему, компенсация за режим "выгорание как норма".
- Источники: [PRNewswire о Series A](https://www.prnewswire.com/news-releases/dualentry-raises-a-90-million-series-a-from-lightspeed-venture-partners-khosla-ventures-and-gv-google-ventures-302573366.html), [Glassdoor reviews](https://www.glassdoor.com/Reviews/Dual-Entry-Reviews-E10128335.htm), [company-due-diligence-2026-07-20.md](../../data/company-due-diligence-2026-07-20.md)

## ASRP-релевантность (контекст, важно понимать отдельно от личного решения)

Вердикт «Высокая, но single-axis» — ценность полностью на фандрейзинг-оси. Cap table (**Lightspeed + Khosla + GV одновременно**) — лучший в выборке тёплый путь к топ-3 нейро/longevity-фондам планеты (Lightspeed держит Neuralink/Science Corp/Anthropic; Khosla — Synchron/OpenAI/longevity-портфель). Продукт (бухгалтерский ERP) — нулевой оверлап с ASRP. Это отдельное соображение для business-development, не должно перевешивать личное решение о культуре.

## Личный контекст — весь релевантный материал

### Опыт

- **Co-Founder & CTO, ASRP** — Cogit, multi-tenant backend с строгими требованиями к tenant isolation и auditability — релевантно для ERP/финансовых данных, где точность и аудируемость критичны.
- **Sr. AI/ML Engineer, Woolf** (San Francisco) — LLM-агент для образовательной оценки, Google ADK/Vertex AI — показывает опыт структурированного анализа документов через LLM.
- **Realtime Communications Engineer, WireBee** — деterministic, non-hallucinating voice-AI agent — прямая параллель с "AI не может галлюцинировать цифру" в бухгалтерском контексте.

### Проекты — прямая параллель

- **AI CV Matcher** (Woolf) — tRPC + NLP skill extraction + Vertex AI для структурированного анализа документов — дисциплина "держать LLM-вывод укоренённым в извлечённой, верифицируемой структуре, а не свободном тексте" — та же проблема, что и с бухгалтерскими данными.
- **AI Voice Agent** (WireBee-клиент) — детерминированный, backend владеет всеми решениями, агент только общается и докладывает — та же философия non-hallucination.

### Публикации (прочитаны целиком)

- **[Building a Resume Matcher with tRPC, NLP, and Vertex AI](https://habr.com/en/articles/943306/)** (24k+ reads — вторая по популярности статья!) — прямая иллюстрация структурированного document analysis с LLM: JSON-output с чёткими полями (score/strengths/suggestions), а не свободный текст.
- **[Building an App Store Review Analysis Pipeline](https://kapustinomm.hashnode.dev/building-an-app-store-review-analysis-pipeline-with-python-nlp-and-data-visualization)** — явный архитектурный выбор в статье: "детерминированный модульный pipeline вместо end-to-end AI-агента... deterministic design ensures consistent, auditable results" — ровно та философия, которая нужна для "AI не может галлюцинировать цифру" в бухгалтерских данных.
- [Google ADK and "Startup Technical Guide: AI Agents"](https://habr.com/en/articles/953592/) (5.3k views) — раздел про Grounding (RAG вместо fine-tuning для борьбы с галлюцинациями) — прямая теоретическая база для non-hallucination требований финансовой системы.

### Навыки

- Node/TS, Python/FastAPI, PHP/Laravel — полный backend диапазон
- Docker, Terraform, AWS/GCP/Azure, CI/CD
- LangGraph (3 года) — если AI трогает ledger/reconciliation где-либо в системе

### Честные разрывы/пробелы

- **C1 английский** — требует самопроверки.
- Формально требования по стеку закрыты хорошо — основной вопрос не технический, а личный (готовность к описанному режиму работы).

## Открытые вопросы / решение перед откликом

1. **Главный вопрос не техническому фиту, а себе:** готовы ли вы к режиму, описанному в Glassdoor (микроменеджмент, WLB 2.5/5, "worked into the ground")? Решить это заранее, чтобы не терять время, если ответ "нет".
2. Если откликаться — прямо спросить про work-life balance и реальную нагрузку на самом интервью, не полагаться на общие фразы рекрутера.
3. Есть ли equity компонент помимо базовой ставки — при таком раунде и оценке это может быть существенной частью пакета.
