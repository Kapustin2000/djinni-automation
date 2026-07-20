# Стратегическая ценность 10 работодателей для ASRP — веб-ресерч, 2026-07-20

**Заказчик:** Михаил Капустин, CTO и сооснователь ASRP (Advanced Scientific Research Projects) — холдинг в neuroscience / AI / consciousness research / quantum computing / биомед / образовании (Arcanum12th), зарегистрирован в Казахстане и США.
**Roadmap ASRP:** (a) LLM-агенты / multi-agent, (b) GFS forecasting-платформа, (c) Arcanum12th образовательная платформа, (d) GMS consciousness-платформа.
**Вопрос:** если Михаил устроится в компанию X — какую *стратегическую* (не зарплатную) ценность это создаст для ASRP по 4 осям: тех-трансфер, доступ к инвесторам/сети, credibility-halo, прямое партнёрство.

> **Методологическая оговорка (важно для калибровки уверенности).** В этой сессии встроенные поисковые инструменты (WebSearch + web-reader MCP) были недоступны (HTTP 429 «insufficient balance»). Все 4 ресерч-агента переключились на прямые fetch’и первичных источников: sitemaps фондов (lsvp.com, khoslaventures.com, airstreet.com и др.), сайты компаний, тексты вакансий (Ashby / Djinni), страницы кейсов вендоров (sigma.software, n-ix.com), Wikipedia. Поэтому портфельные компании фондов и клиенты вендоров верифицированы надёжно; а то, что публично не светится (напр. внутренний LLM-стек Nova Digital, сам факт multi-agent-наработки Seeking Alpha, размер раунда ChatRevenue) — помечено как **inferred / не подтверждено**. Ничего не выдумано.

---

## Сводная матрица двойной выгоды

| # | Компания | Тех-трансфер | Сеть/инвесторы | Halo | Партнёрство | **Двойная выгода** |
|---|---|:--:|:--:|:--:|:--:|:--:|
| 1 | ChatRevenue.ai | M | M | M-H | L-M | **Средняя** |
| 2 | DualEntry | L | **VH** | **H** | L | **Высокая**¹ |
| 3 | Nova Digital | M | L-M | M | L-M | **Низкая** |
| 4 | Interloom | **VH** | **H** | H | M | **Высокая** |
| 5 | Empat | M | L-M | M | **H** | **Средняя** |
| 6 | CodeTiburon | M-H | L | L-M | **H** | **Средняя** |
| 7 | 6037 | L | M | M | M | **Низкая** |
| 8 | Sigma Software | **H** | **H** | M | **H** | **Высокая** |
| 9 | Seeking Alpha | M-H | M | M-H | **H** | **Средняя** |
| 10 | N-iX | **H** | **H** | M | **H** | **Высокая** |

¹ DualEntry — ценность **сконцентрирована на фандрейзинг-оси** (cap table = Lightspeed + Khosla + GV), а не разнесена по нескольким; подробнее ниже.

---

## Подробно по компаниям

### 1. ChatRevenue.ai
*Stealth-стартап, агentic «post-CRM» для продаж. Сооснователи подтверждены на Djinni: Ratmir Timashev (Veeam, ~$5B exit) и Vlad Voskresensky (Revenue Grid). Размер раунда публично не раскрыт — бэксвитит Тимашев.*

- **1. Тех-трансфер — средний.** Единственная из трёх AI-продуктовых, где в вакансии **явно назван стек LangChain + LangGraph + LangSmith** + RAG/embeddings/vector search + knowledge graphs (NetworkX), Python/FastAPI, PostgreSQL, K8s, Azure, Kafka/Event Hub. Это **готовая референс-реализация** мейнстрим-стека для copilot+autopilot — полезна как проверенная отправная точка для in-house ASRP-платформы, но новизны мало. Пайплайн «коммуникации (email/calendar/Zoom/Slack) → граф бизнес-отношений» переиспользуем для Arcanum12th (захват взаимодействий в структуру знаний).
- **2. Сеть/инвесторы — средняя.** Именованных VC-фондов нет (финансирует фаундер). Сеть Тимашева/Воскресенского — это enterprise-software/SalesTech/Revenue Grid (~600k клиентов), **не deep-tech**. Полезна для B2B-коммерции, не для нейро/quantum-фандрейзинга.
- **3. Halo — средняя-высокая.** Имя Тимашева (Veeam $5B) — сильное в enterprise-IT, но это **не** deep-tech/научное имя; в deep-tech-комнатах почти не работает.
- **4. Партнёрство — низкое-среднее.** SalesTech-продукт, нет прямого оверлапа с продуктов ASRP; смежность только через «агentic workflow» как паттерн.
- **Вердикт: СРЕДНЯЯ** — даёт проверенный LangGraph-референс + halo сильного серийного фаундера, но без deep-tech-инвесторов и без продуктового перекрытия.

### 2. DualEntry
*AI-native ERP/бухгалтерия, NYC, осн. 2024. $90M Series A (10/2025) от **Lightspeed + Khosla + GV (+ Contrary, Vesey)**, пост-мани $415M, всего ~$100M. Фаундеры Benedict Dohmen & Santiago Nestares (масштабировали прошлую компанию до ~$100M ARR).*

- **1. Тех-трансфер — низкий.** Стек принципиально **homegrown** (ни один агент-фреймворк не назван), Postgres-as-default («use Postgres until it breaks»), Python/FastAPI, AWS, Snowflake/dbt. Нет knowledge graph, нет MCP, нет self-hosting (API-only к foundation-моделям). Реально переносимое: **дисциплина production-эвалов для LLM на структурированных финансовых данных** (релевантно GFS forecasting — структурированный, аудитный домен) и прагматичный single-store default. Не «копать» на multi-agent/KG-идеи.
- **2. Сеть/инвесторы — очень высокая (лучшее в выборке).** Cap table = **Lightspeed + Khosla + GV + Contrary + Vesey одновременно**. Из ресерча: Lightspeed держит Neuralink, Science Corp, Anthropic/xAI/Mistral/Thinking Machines Lab, Ultima Genomics/Xaira/Neko Health, Helion; Khosla — Synchron, Science Corp, OpenAI, longevity-скам (Loyal/Rubedo/Moonwalk/Cellino). Это **прямой тёплый путь к топ-3 deep-tech/нейро/longevity фондам планеты** — для фандрейзинга ASRP это, возможно, самый ценный актив во всём списке.
- **3. Halo — высокая.** «Principal/Senior AI Engineer в компании Lightspeed/Khosla/GV за $415M» — сильная строка в резюме CTO при разговоре с любым фондом.
- **4. Партнёрство — низкое.** Бухгалтерский ERP, нулевой оверлап с продуктами ASRP.
- **Вердикт: ВЫСОКАЯ** — но **ценность почти полностью на фандрейзинг-оси** (investor-access + halo); это «single-axis high», не разнесённый по осям. Отдельное предупреждение из прошлого due diligence: культура Glassdoor 2.7/5 («brutal», «worked into the ground») — стратегически irrelevant, но критично для личной реализации.

### 3. Nova Digital
*IT-ядро группы NOVA (Nova Poshta), 10+ лет, ~1000+ инженеров, 10M+ MAU, high-load (~30k tx/сек у группы).*

- **1. Тех-трансфер — средний.** High-load инженерия национального масштаба (TMS Prolog, RouteStripe, NovaDoc, SOC-as-a-Service) — переносима как **дисциплина масштабной инфры** для любой ASRP-платформы под миллионы транзакций. Но **LLM/agent-наработки не подтверждены публично** (на сайте novadigital.com нет ни одного упоминания GenAI/LLM — это inferred из вакансии «Python AI Lead»). Глубину агент-стека нельзя считать доказанной.
- **2. Сеть/инвесторы — низкая-средняя.** Капитал группы Nova Poshta (украинская логистика), deep-tech-VC нет.
- **3. Halo — средняя.** Сильна внутри украинского IT / high-load-систем, слаба в международных deep-tech-комнатах.
- **4. Партнёрство — низкое-среднее.** Возможна как **инфра-референс / high-load delivery-партнёр**, но не как покупатель продуктов ASRP.
- **Вердикт: НИЗКАЯ** — стабильная инженерная школа + UA-halo, но без deep-tech-инвесторов и без продуктовой синергии; плюс задокументированный риск отзыва оффера снижает и практическую ценность.

### 4. Interloom Technologies GmbH
*Мюнхен/Берлин, «tacit knowledge / context graph для AI-агентов». $16.5M seed (€14.2M, 03/2026) от **DN Capital + Bek Ventures + Air Street Capital**, всего ~$20M. Клиенты Zurich/VW/Commerzbank/JLL.*

- **1. Тех-трансфер — очень высокая (богатейшая находка).** Их ядро — **3-слойный Context Graph (Source → Canonical → Projection)**: сырые данные остаются на месте, canonical-слой с entity resolution и типизированными рёбрами выводится один раз, projection-слой кормит и людей, и агентов. Поверх — **MemoryRank** (ранжирование по исходам, «без opaque vector stores»), **dual-harness агенты** (Field Agent = узкие права/аудит vs Assistant = sandboxed CLI/exploration), **Procedures** (assembly-line из людей/агентов/детерминированных скриптов), **Agentic Org Chart** (агенты со скоупами/эскалациями). Self-host моделей на GPU, multi-cloud K8s, Go/Terraform, homegrown eval (LLM-as-judge). **Gartner-репорт (G00846665, 02/2026)** позиционирует context graphs как «новую обязательную инфру для agentic систем» (>50% к 2028). Всё это **напрямую ложится** на ASRP-роадмап: KG + multi-agent (GMS consciousness / Arcanum12th) и precedent-retrieval (GFS forecasting).
- **2. Сеть/инвесторы — высокая.** **Air Street Capital** (Nathan Benaich, *State of AI Report*) — AI-first специалист с TechBio-рукавом (Exscientia, Recursion, Profluent, Enveda, LabGenius) + frontier-AI-infra (ElevenLabs, Lambda, poolside, Ndea) = **лучший европейский вход для ASRP** в AI-фандрейзинг. DN Capital и Bek — generalist/enterprise, малорелевантны, но Air Street перекрывает.
- **3. Halo — высокая.** VC-backed EU-стартап с enterprise-трекшн (VW/Commerzbank/Zurich), категориеобразующий продукт с Gartner-покрытием — даёт научную/инфра-кредибилити, а не просто «enterprise SaaS».
- **4. Партнёрство — среднее.** Прямым покупателем продуктов ASRP не станет (бэк-офис enterprise), но реальный кандидат на **совместную разработку agent/knowledge-инфра**.
- **Вердикт: ВЫСОКАЯ** — единственная компания, где сильны **все четыре оси одновременно**: лучший тех-трансфер + релевантный frontier-AI фонд + категорийный halo + партнёрский потенциал.

### 5. Empat
*Украинская AI-native студия, 10+ лет, 300+ проектов, 23 рынка, AI Center of Excellence, сертифицированы на Claude/OpenAI/Copilot. Логотипы Porsche, Panasonic, Transparency International, CBRE — верифицированы на сайте. 6 Y Combinator-alumni и 19 Forbes 30u30 в клиентской базе.*

- **1. Тех-трансфер — средний.** AI-native с реальными практиками (AI Agents Development, AI-Accelerated Dev, AI Agent Blueprint Workshop) и современным тулчейном (Gemini/Claude/ChatGPT/DeepSeek/Cursor/Codex). Но это студия — **широта вместо глубины**: увидите много паттернов, но без глубокой собственной R&D-инфры.
- **2. Сеть/инвесторы — низкая-средняя.** Внешних VC нет (bootstrapped). Сеть — через клиентов (blue-chip + YC-alumni/founders).
- **3. Halo — средняя.** Blue-chip-логотипы + топ-работодатель UA 2024; halo «натирается» через ассоциацию с Porsche/Panasonic/CBRE, а не через собственное имя.
- **4. Партнёрство — высокая (самое конкретное).** **Верифицированный delivery-партнёр для сборки продуктов ASRP** — особенно Arcanum12th (образовательная платформа). У них есть продуктовизованные форматы: «Fast Fixed-Scope MVP» ($30k / 6–12 нед), «AI Agent Blueprint Workshop», «CTO-as-a-Service», PoC за 2–4 нед. Это прямая коммерческая готовность.
- **Вердикт: СРЕДНЯЯ** — уникальна тем, что даёт **осязаемое партнёрство** (могут собрать Arcanum12th) + AI-native-экспозицию + blue-chip-halo; минус — нет инвестор-сети и нет глубокой R&D.

### 6. CodeTiburon
*Харьковский аутсорс с 2009, полностью ребрендирован под «Agentic AI Systems» (Agentic AI, RAG/Knowledge & Document Automation, AI-Native SE).*

- **1. Тех-трансфер — средняя-высокая.** Верифицированный кейс **«Building Production Infrastructure for an AI Agent Engineering Platform»** (распределённый бэкенд, eval-пайплайны, workflow-оркестрация, API-дизайн, observability, CI/CD quality gates, cloud-native) — **почти точное совпадение со стеком роли** (Python + K8s + LLM + Agents + Knowledge Graphs) и с потребностью ASRP в agent-инфре.
- **2. Сеть/инвесторы — низкая.** Малый аутсорс, без известных инвесторов.
- **3. Halo — низкая-средняя.** 16 лет на рынке, но низкопрофильный бренд, без founder-fame и без marquee-наград.
- **4. Партнёрство — высокая.** Верифицированная способность строить agent-platform-инфру = могут быть **staff-aug / инженерным расширением** под KG+agent-билд ASRP.
- **Вердикт: СРЕДНЯЯ** — сильный тех+партнёрский фит, но тонкий halo и отсутствие инвестор-сети ограничивают «двойную» составляющую.

### 7. 6037
*Venture partnership внутри экосистемы Genesis (один из крупнейших product-IT-холдингов Украины). Модель: acquire majority stake → accelerate → spin-off. Consumer B2C SaaS, Kyiv/Lviv, ~30 открытых ролей.*

- **1. Тех-трансфер — низкий.** Consumer-B2C-SaaS roll-up + маркетинг-машина («Creative Factory»); deep agent/AI-R&D не продукт.
- **2. Сеть/инвесторы — средняя.** **Экосистема Genesis** = украинский product-IT-капитал + дистрибуция; useful для UA-коммерции, но не для deep-tech-VC.
- **3. Halo — средняя.** Genesis-бренд работает в украинском IT и consumer-SaaS; для frontier-deep-tech — **опосредованно** (коммерция/дистрибуция, не наука).
- **4. Партнёрство — средняя.** Возможный **consumer-distribution / venture-маршрут** для consumer-продукта ASRP (в первую очередь образование/Arcanum12th) — модель acquire-and-scale + Genesis-дистрибуция могут дать B2C-масштаб; могут выкупить majority-stake в спин-оффе. Для consciousness/forecasting — не фит.
- **Вердикт: НИЗКАЯ** (средняя по Genesis-сети) — ценность только в consumer-дистрибуции; тех-трансфер и frontier-выравнивание слабые.

### 8. Sigma Software
*Украинское плечо шведской Sigma Group / Danir AB, ~2000 чел. Productized AI-практика «AI Compass».*

- **1. Тех-трансфер — высокая.** Зрелая продуктовизованная AI-практика: AI Compass (agentic SDLC, AI guardrails по ISO 42001/EU AI Act), AI-Powered SDLC с «persistent engineering memory», Data Engineering for AI «под copilots и agentic workflows». **Живой кейс:** для *Knowledge as a Service, Inc.* построили agentic AI SDLC на **Claude Code + Claude Cowork** (команда из 4 — ~100 фич/мес). Роль FDE («agent factories, tool registries, multi-tenant runtime») подтверждает реальный агент-деплой.
- **2. Сеть/инвесторы — высокая.** Именованные **научные/life-science клиенты**: **AstraZeneca ×2** (patient recruitment для COPD-исследований + systems integration), **Siemens Healthineers** (миграция CT-мониторинга в Azure), **CGM/CompuGroup Medical**, фарм-закупка (HIPAA/ISO), и — ключевое — **клиент с «multimodal naturalistic data for scientific research in social-behavioral-cognitive area»** (прямой нейро/когнитивный оверлап с ASRP).
- **3. Halo — средняя.** Крупный уважаемый вендор (Global Outsourcing 100), но не frontier-имя.
- **4. Партнёрство — высокая.** Канал в **фарма R&D + med devices + research-data** + правдоподобный co-sell/delivery-партнёр; сама Sigma может быть покупателем ASRP agent-tooling для своей FDE-практики и research-клиентов.
- **Вердикт: ВЫСОКАЯ** — сильны тех-трансфер + клиент-сеть (AstraZeneca/Siemens/cognitive-research) + партнёрский канал; особенно ценен cognitive-research-клиент как «родная» ASRP-смежность.

### 9. Seeking Alpha
*Финансовая платформа / крупнейшее инвест-сообщество, ~20M MAU, осн. 2004 David Jackson (ex-Morgan Stanley analyst). Peer-reviewed: статьи SA предсказывают доходность акций. Quant ratings = существующий ML на масштабе.*

- **1. Тех-трансфер — средняя-высокая.** LLM/multi-agent-наработка для инвестиционного контента **не верифицирована публично** (SA блокирует `/page/*`, поиск лежал) — это inferred из вакансии «Senior Python AI Engineer (LLM/Multi-Agent Systems)». Но у них уже есть ML на масштабе (Quant ratings) — это сильный baseline для forecasting-экспертизы.
- **2. Сеть/инвесторы — средняя.** David Jackson (ex-Morgan Stanley), 20M-аудитория = **финансовая/инвесторская сеть**. Релевантна для фандрейзинга в finance-комнатах, но **не** для deep-tech/нейро/quantum.
- **3. Halo — средняя-высокая.** Узнаваемый fintech-бренд, peer-валидированный, миллионы пользователей — силён в finance/investor-кругах, слаб в deep-tech-research.
- **4. Партнёрство — высокая.** Самый высокий потолок как клиента: **GFS forecasting-платформа** может получить **marquee design-partner** в SA (их Quant-рейтинги + корпус авторов = естественный тестбед для forecasting/agent-продукта). Контингентно — зависит от того, строит ли SA это in-house.
- **Вердикт: СРЕДНЯЯ** — синергия с GFS (forecasting) + fintech-halo + потенциальный marquee-клиент; но тех-трансфер контингентен (inferred), а deep-tech-сеть тонка.

### 10. N-iX
*~2000+ чел, крупный UA/EU-аутсорс, Fortune 500. AI под брендом «Pragmatic AI Software Engineering» + программа **APEX** (07/2026).*

- **1. Тех-трансфер — высокая.** Глубочайший agent-stack-overlap в выборке: AI-agent-dev с **LangChain/LangGraph/CrewAI** явно названы, RAG, fine-tuning, LLMOps-guardrails (prompt-injection, RBAC, content filtering), MLOps/quantization, open-source LLM-экспертиза, AWS **Premier Tier + AI Services Competency**, партнёрство с **Palantir**. 200+ AI/ML/data инженеров. Роль «AI Application Engineer» (Claude Code/Codex/ChatGPT как ежедневные инструменты) — точное описание практики ASRP.
- **2. Сеть/инвесторы — высокая.** Именованные **научные/life-science/deep-tech клиенты**: **Beyond Limits** (Caltech/NASA-JPL spinoff, cognitive AI с «space heritage» — прямой frontier-science оверлап), **Fluke** (научные измерительные приборы), **Weinmann Emergency** (мед-приборы), **Think Research** (clinical decision support), **Brighter** (health-tech), неназванный **clinical-trials**-клиент. Явный GTM в **pharma & biotech + medtech**.
- **3. Halo — средняя.** Крупный уважаемый вендор Fortune-500-уровня, но не frontier-имя.
- **4. Партнёрство — высокая.** Канал в medtech/научные приборы/pharma-biotech + co-delivery-партнёр; сама N-iX — правдоподобный покупатель более глубокого ASRP IP по агентам/сознанию-AI (deepest stack match).
- **Вердикт: ВЫСОКАЯ** — сильнейший вендор по tech-transfer (глубочайший агент-стек) + научная/deep-tech клиент-база (Beyond Limits/JPL — заметно для frontier-позиционирования ASRP) + партнёрский канал.

---

## Кросс-список: фонды за этими компаниями с deep-tech-аппетитом → цели фандрейзинга ASRP

| Фонд | За какой компанией | Deep-tech вердикт | Доказательство (портфель) |
|---|---|---|---|
| **Lightspeed Venture Partners** | DualEntry | **BROAD DEEP-TECH** | Neuralink, Science Corp, Anthropic/xAI/Mistral/Thinking Machines Lab, Ultima Genomics, Xaira, Neko Health, Guardant, Natera, Helion (fusion). Нет pure-play quantum. |
| **Khosla Ventures** | DualEntry | **BROAD DEEP-TECH** | Synchron (BCI), Science Corp, OpenAI/Cognition/Sakana/Symbolica, Loyal/Rubedo/Moonwalk/Cellino/eGenesis (longevity), Commonwealth Fusion/Varda. Нет pure-play quantum. |
| **Air Street Capital** | Interloom | **AI-first + TechBio** | Exscientia, Recursion, Profluent, Enveda, LabGenius (TechBio); ElevenLabs, Black Forest Labs, Lambda, Contextual, poolside, Ndea (frontier-AI). *State of AI Report* (Nathan Benaich). Нет neuro/BCI, нет quantum. |
| **GV (Google Ventures)** | DualEntry | **BROAD DEEP-TECH, life-sci core** | Flatiron, Verve Therapeutics, Metsera, One Medical (+ исторически 23andMe/Editas/Denali). Sole LP = Alphabet. |
| DN Capital | Interloom | LOW/NO | Consumer/marketplace/fintech (Shazam, OLX, Auto1, Remitly). |
| Bek Ventures | Interloom | LOW | Enterprise SaaS/security/fintech (UiPath, Payhawk, Picus, Upstash, Codasip, Photoneo). Нет neuro/quantum/longevity. |
| Contrary | DualEntry | LOW (research-only) | Anduril, Nomic, Orchard Robotics; *исследования* по anti-aging/cell-therapies, но портфельных ставок нет. |
| Vesey Ventures | DualEntry | LOW/NO | Fintech-only, $78M debut fund, ex-AMEX Ventures. |

**Целевой шорт-лист для ASRP (в порядке приоритета):**
1. **Lightspeed** — глубочайшее совпадение: 2× BCI (Neuralink, Science Corp), frontier-AI-россыпь, longevity/genomics-бенч, даже fusion. Главный пробел — нет pure-play quantum.
2. **Khosla Ventures** — фактически вровень; самый «bold science»-бренд, структурированные практики Frontier + Therapeutics + MedTech.
3. **Air Street Capital** — лучший AI-first-специалист и **лучший европейский вход**; TechBio-рукав + голос через *State of AI Report*.
4. **GV** — life sciences как заявленное ядро; надёжный бэкер биомед-стороны ASRP.

**⚠️ Quantum-провал.** Ни у одного из 8 фондов нет верифицируемой pure-play quantum-computing ставки в текущем портфеле (единственные «quantum»-хиты — QuantumScape = батареи). Если quantum computing — приоритетный угол ASRP, эти 8 фондов не естественный фит; нужны quantum-специализированные фонды/стратегические LP отдельно (это за рамками текущего ресерча — не выдумываю имена).

---

## Итоговый синтез (как читать)

- **Двойная выгода ВЫСОКАЯ — 4 компании, по разным причинам:**
  - **Interloom** — самая «диверсифицированная» выгода: сильны все 4 оси (лучший тех-трансфер + релевантный фонд Air Street + категорийный halo + партнёрство). Если выбирать одно место под стратегическую ценность для ASRP — это лидер.
  - **N-iX** и **Sigma Software** — лучший «enterprise-канал»: глубокий агент-стек + именованные научные/life-science/med-device клиенты (Beyond Limits/JPL у N-iX; AstraZeneca/Siemens Healthineers + cognitive-research у Sigma) = и tech-transfer, и партнёрский доступ к pharma/research-покупателям.
  - **DualEntry** — «single-axis high»: вся ценность в фандрейзинг-оси (cap table Lightspeed+Khosla+GV = лучший в выборке тёплый путь к нейро/longevity-фондам), но продукт далёк от ASRP и культура токсична.

- **Двойная выгода СРЕДНЯЯ — 4 компании:**
  - **Seeking Alpha** — потолок как клиента для GFS (forecasting), но контингентно; **Empat** — самое конкретное партнёрство (могут собрать Arcanum12th) без инвестор-сети; **ChatRevenue** — LangGraph-референс + halo Тимашева, без deep-tech-сети; **CodeTiburon** — тех+партнёрский фит, но тонкий halo.

- **Двойная выгода НИЗКАЯ — 2 компании:** **Nova Digital** (стабильная школа high-load, без deep-tech-инвесторов/синергии) и **6037** (только consumer-дистрибуция через Genesis).

**Стратегический вывод для CTO:** если приоритет — **фандрейзинг ASRP** → DualEntry даёт самый сильный разовый доступ к нейро/longevity-фондам; если приоритет — **построить тех ASRP** → Interloom (context-graph + multi-agent) и N-iX/Sigma (agent-стек + научные клиенты); если приоритет — **быстрый продукт/партнёрство** → Empat (собрать Arcanum12th) и Seeking Alpha (GFS design-partner).

---

### Источники (первичные, верифицированные в сессии)
**Фонды:** lsvp.com/company-sitemap.xml, khoslaventures.com/portfolio, gv.com/about, airstreet.com/portfolio (+ stateof.ai), dncapital.com/sitemap.xml, bekventures.com/sitemap-portfolio.xml, contrary.com/companies, vesey.vc.
**Тех-стек:** jobs.ashbyhq.com/dualentry/*, interloom.com/en/blog/* + /en/product/context/ + /en/careers/*, djinni.co вакансии ChatRevenue (820606, 824065, 806786).
**Вендоры:** sigma.software/services/ai-compass + /case-studies?industry=healthcare, n-ix.com/ai-agent-development-services/ + /clients/* + /news/n-ix-launches-apex-*.
**Halo/партнёрство:** en.wikipedia.org/wiki/Seeking_Alpha, novadigital.com, empat.tech (+ /industries, /cases), codetiburon.com, 6037.tech.
**Контекст due diligence:** data/company-due-diligence-2026-07-20.md, data/company-cards-glm-2026-07-20.md.
