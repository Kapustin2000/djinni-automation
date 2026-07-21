# Deep-dive по компаниям (батч N–S) — due diligence + стратегическая ценность для ASRP, 2026-07-21

Продолжение серии [company-deepdive-2026-07-21-aa.md](company-deepdive-2026-07-21-aa.md) (A–C), [company-deepdive-2026-07-21-ab.md](company-deepdive-2026-07-21-ab.md) (D–G) и [company-deepdive-2026-07-21-ac.md](company-deepdive-2026-07-21-ac.md) (H–M), в том же **объединённом формате**: для каждой компании одновременно личный DD (для трудоустройства Михаила Капустина) + оценка двойной выгоды для ASRP по 4 осям. Охват — 13 компаний из вакансий djinni.co (бренды на N–S).

**Заказчик:** Михаил Капустин, CTO и сооснователь ASRP (Advanced Scientific Research Projects) — холдинг в neuroscience / AI / consciousness research / quantum computing / биомед / образовании (Arcanum12th), зарегистрирован в Казахстане и США.
**Roadmap ASRP:** (a) LLM-агенты / multi-agent, (b) GFS forecasting-платформа, (c) Arcanum12th образовательная платформа, (d) GMS consciousness-платформа.
**Шкала осей:** L / M / H / VH. **Вердикт двойной выгоды:** Высокая / Средняя / Низкая — бар для «Высокая» = реальное пересечение с deep-tech/AI-agent/education/neuroscience-роадмапом ASRP (не просто «легитимный работодатель»).

> **Методологическая оговорка (калибровка уверенности).** Встроенные поисковые тулы снова недоступны (WebSearch + web-reader MCP = HTTP 429; WebFetch нет). Весь ресёрч — **прямые fetch'и первичных источников через `curl`** (браузерный UA): официальные сайты, DOU-профили (`jobs.dou.ua/companies/<slug>`), Wikipedia, GitHub API (`api.github.com`), Apple App Store lookup API, пресс-релизы/IR-сайты. **В этом батче Brave Search был нестабилен** — несколько раз отдал 429/captcha, поэтому агенты падали на оф. сайты + DOU + **Yahoo-агрегатор** (`search.yahoo.com/search?p=...`, отдаёт сниппеты Crunchbase/Clutch/Glassdoor/LinkedIn, сами эти сайты ботами блочатся 403). **REACHABLE:** n-ix.com, uk.wikipedia.org (N-iX), DOU (n-ix, new-wave-devs, newgmedia, newsoft, playtech, recruitgarden, s-pro, seeking-alpha, sigma-software, sharkscode, onetablet), nuxgame.com, onuhealth.com, itunes.apple.com (ONU/OWN rebrand), onetablet.co→yoursouschef.com, playtech.com + playtechpeople.com + investors.playtech.com, en.wikipedia.org (Playtech/Seeking Alpha), recruitgarden.com, s-pro.io + moneyhouse.ch, sigma.software, sharkscode.com, itukraine.org.ua, api.github.com (seekingalpha org), techcrunch.com. **BLOCKED/403:** crunchbase org-страницы, glassdoor, clutch, linkedin, finsmes.com (Cloudflare) — только через сниппеты. **DOU-слагов нет (404):** nuxgame, onu-health/own-health (stealth — нет company-профиля ни на DOU, ни на djinni). **Что верифицировано надёжно:** продуктовое позиционирование, класс/размер/дата-регистрации (DOU), ownership/фаундеры, AI/agent-заявления. **Что НЕ удалось проверить точно:** суммы раундов (Crunchbase блочит), рейтинги Glassdoor/kununu (403), точная глобальная headcount/выручка частных компаний. **Spot-check 5 ключевых заявлений выполнен прямым curl** (Sigma Software → NATO Innovation Challenge + NEAR AI confidential inference на sigma.software; Seeking Alpha → репозитории `git-log-mcp` + `vellum-client-ruby` на api.github.com; S-PRO → страница Optimisation Agent 200; Playtech → публичный LSE-профиль; ONU → Apple App Store API подтверждает rebrand Own Health→ONU) — **все 5 подтверждены, галлюцинаций не обнаружено.** Несколько брендов рекрутят на djinni без dedicated company-page (New Wave Devs, OneTablet, SharksCode, ONU Health) — помечено в карточках. Ничего не выдумано; провалы помечены «не нашлось».

---

## Сводная таблица (батч N–S)

| # | Компания | Тип | Двойная выгода ASRP | Главный вывод одной строкой |
|---|---|---|:--:|---|
| 1 | N-iX | Outsourcing vendor (product engineering) | **Средняя** | Top UA brand (2400+ eng, DOU 89/100) с реальной AI-agent-практикой (APEX, Palantir, Cursor) — лучший «безопасный» тех-трансфер в батче, но ядро = services. |
| 2 | New Wave Devs | Outsourcing/outstaffing | **Низкая** | Мелкий (~50 чел.) US-UA outstaffing без собственного R&D; djinni company-page не подтверждён. |
| 3 | NewGMedia | Product (iGaming holding) | **Низкая** | iGaming-холдинг 250–300 чел. + affiliate + собственный recruitment; репутационный mismatch для ASRP. |
| 4 | Newsoft | Outsourcing boutique (Lviv) | **Низкая** | Львовский бутик 50+ с растущей AI-практикой (Nomic AI-кейс), но staff-aug без пересечения с deep-tech. |
| 5 | NuxGame | Product (iGaming B2B) | **Низкая** | B2B iGaming-платформа (Curaçao, 2018, bootstrapped); отрицательный halo, нулевая синергия с roadmap. |
| 6 | ONU Health / OWN Health | Product (healthtech, early-stage) | **Средняя** | **Стенд-аут батча:** собственный AI Health Engine (RAG, биомаркеры) — прямой overlap с biomed + LLM-agent осями ASRP, но stealth/ранняя стадия/риск. |
| 7 | OneTablet | Product (restaurant SaaS, US) | **Низкая** | NYC-product «Sous Chef» (delivery-агрегатор) с киевским дев-офисом; vertical не пересекается с ASRP. |
| 8 | Playtech | Product (iGaming, LSE: PTEC) | **Низкая** | Flagship iGaming-вендор (€764M rev 2025, 7400 чел., Kyiv R&D 750) — сильный работодатель, но отрицательный halo для neuroscience-CTO. |
| 9 | RecruitGarden | Recruitment agency | **Низкая** | Киевское IT-кадровое агентство ≤20 чел. (2020); только потенциальный канал найма, без инженерной роли. |
| 10 | S-PRO | Outsourcing (CH, Sigma-style) | **Средняя** | Редкая для аутсорса **реальная** agent/RAG/LLM-практика (deployed Optimisation Agent для Multiplex, AI-Native SDLC); частичный перенос на LLM-ось ASRP. |
| 11 | Seeking Alpha | Product (fintech-data, US/IL) | **Средняя** | Global fintech-data brand (Benchmark/Accel, ~170 чел.) с прикладной LLM/MCP-инженерией — лучший halo + частичный перенос на GFS. |
| 12 | SharksCode | Product (iGaming B2B) | **Низкая** | UA iGaming-B2B вендор (Diia City, DOU 91/100) с AI/RAG-практикой для своих нужд; vertical = mismatch. |
| 13 | Sigma Software | Outsourcing (Sigma Group, SE) | **Средняя** | Top UA engineering brand (1500+, DOU 91/100) с публичными agentic-AI-работами (финал NATO Innovation Challenge, NEAR AI confidential inference) — реальный tech-трансфер. |

**Итог батча:** 5 из 13 — Средняя (N-iX, ONU Health, S-PRO, Seeking Alpha, Sigma Software); 8 — Низкая. Батч содержит мощный **iGaming-кластер** (NewGMedia, NuxGame, Playtech, SharksCode — все Низкая, с отрицательным halo для neuroscience-миссии ASRP) и сильный **UA-outsourcing-кластер с подлинной AI-agent-практикой** (N-iX, S-PRO, Sigma Software) — это «безопасные» варианты тех-трансфера. **Единственный стенд-аут двойной выгоды — ONU Health** (VH tech-transfer: собственный AI Health Engine / RAG / multimodal biomarker orchestration прямо ложится на LLM-agent roadmap ASRP и частично на biomed), но это ранний stealth-стартап без подтверждённого финансирования (rebrand OWN→ONU через 5 мес, /shop 404, Tilda-сайт) — высокий upside при высоком риске. Среди низкорисковых работодателей лучший halo + частичный GFS-перенос даёт **Seeking Alpha** (global fintech-data + GitHub-evidenced LLM/MCP-инженерия).

---

## Подробно по компаниям

### N-iX
**Due diligence (личное):**
- Что делают / вертика: Международная IT-компания (product engineering / outsourcing) — разработка ПО, AI-консалтинг («Pragmatic AI Software Engineering»), cloud, data engineering, embedded/IoT, game dev (N-iX Games), cybersecurity, SAP. Клиенты — Fortune 500 (Lebara, AVL, Fluke, GoGo, Currencycloud, Mitek).
- Тип: Outsourcing vendor / product engineering services (приватная founder-owned).
- Финансирование/размер/выручка: ~2400+ инженеров (сайт/uk-Wikipedia), на DOU «понад 1500 спеціалістів»; 10 стран (UA, PL, US, MT, SE, BG, RO, CO, IN, UK). Юр. HQ — Валлетта, Мальта; операционно — Львів. Основана в августе 2002 как NovelliX (Andriy Pavliv / Dmytro Kosarev / Werner Richard Krainer); первый клиент — Novell (2003). Tracxn — **unfunded company** (без VC/PE раундов; founder-owned). Рост +331% за 2016–2019, Inc. 5000 US 2023 (№356 среди software).
- Отзывы сотрудников/культура: DOU **89/100**, 3-е место среди 1500+ в «Найкращі ІТ-роботодавці 2025»; 66 отзывов (регистрация с 28.10.2009, Diia City). Best Inspiring Workplace in Europe 2024 (#1), 2026 (#4), Global Top 100 (#36). Единичные жалобы на бюрократию и middle-management.
- Red flags: исторический иск NIX (Харків) за схожесть названий — незначимо. После 2022 релокация 600+ инженеров (риск снижен хабами в Колумбии 2023, Румынии и Индии 2025). Существенных red flags как работодателя не найдено.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: **H** — выделенные практики AI Agent Development (APEX-фреймворк для production Agentic AI), Computer Vision, GenAI, RAG; партнёрство с **Palantir** (первый UA-партнёр, Foundry-команда), **Cursor** (AI-Augmented Team), AWS Premier Tier + AI-компетенция, Microsoft AI Cloud Partner, Snowflake — стек напрямую переносим на roadmap ASRP (LLM-агенты, multi-agent).
2. Сеть/инвесторы: **M** — enterprise-клиенты Fortune 500 + platform-vendors (AWS/Microsoft/Google/SAP/Snowflake/Palantir/Cursor); собственного deep-tech/neuro/quantum-портфеля нет, фундаментальных consciousness/neuro R&D не нашлось.
3. Halo: **H** — один из самых узнаваемых UA IT-брендов (Forbes Ukraine Top 10 IT 2025, Inspiring Workplaces Europe #1, Forrester/Everest PEAK Matrix); кейс в резюме CTO ASRP = сильный сигнал top-tier global engineering at scale.
4. Партнёрский потенциал: **M** — как outsourcing-вендор скорее исполнитель/расширитель команды ASRP, чем клиент; AI-практика + enterprise-портфель = реферальный канал к большим клиентам; Palantir/Cursor открывают двери в deep-tech-экосистему.
- **Вердикт двойной выгоды:** Средняя — сильное пересечение по AI-agent-стеку (APEX, Palantir Foundry, Cursor) и высокий halo для Михаила как CTO, но ядро N-iX остаётся engineering-services-вендором без собственной deep-tech/neuro/quantum-повестки; полезен как канал и бренд, а не как стратегический синергет.

**Источники:** https://www.n-ix.com/ (200 — 2400+ engineers, 10 countries, 2002–2026), https://uk.wikipedia.org/wiki/N-iX (200 — основатели NovelliX→N-iX, офисы, партнёрства), https://jobs.dou.ua/companies/n-ix/ (200 — «понад 1500 спеціалістів», рейтинг 89/100, 66 отзывов, Diia City), Yahoo-сниппет Tracxn/Crunchbase (founder Andrew Pavliv, unfunded).

---

### New Wave Devs
**Due diligence (личное):**
- Что делают / вертика: UA outstaffing / staff augmentation — веттят и поставляют mid/senior удалённых разработчиков (RoR, React, Next.js, JS, Rust) в команды клиентов «за 48 часов»; закрывают рекрутмент/HR в web/mobile + UI/UX.
- Тип: Outsourcing/outstaffing vendor (позиционируется как «outstaffing company»), НЕ product.
- Финансирование/размер/выручка: 21–80 спец. по DOU (сайт — «50+ specialists, clients in 6 countries»); DOU-регистрация 14.11.2019; клиентские кейсы с ноября 2021 (Venn, Норвегия). Внешнего финансирования нет — bootstrap. Юрлицо в США — Sheridan, Wyoming (registered-agent адрес, не офис). Команда: CEO/Founder Roman Oliinychenko, CTO Alex Sergienko, BDM Angelina Oliinychenko.
- Отзывы сотрудников/культура: страница отзывов на DOU есть, численный рейтинг не парсится; сниппеты позитивны в части обучения («1.5 года в NWD, переключился RoR→Erlang/Elixir — компания поддержала»). Glassdoor/kununu не найдено.
- Red flags: (1) прямой djinni company-profile **не подтверждён** — `djinni.co/jobs/company-new_wave_devs/` редиректит на дефолтный `/jobs/` (работодатель подтверждён только на DOU); (2) «американское присутствие» = Sheridan WY (агент, не офис); (3) маркетинговое «10+ years in IT» расходится с реальной регистрацией (DOU 2019, клиенты с 2021); (4) модель bench + outstaff — собственного продукта/IP нет; (5) малый размер (~50) и типичные outstaff-риски (простой между проектами, маржа, зависимость от нескольких клиентов).

**ASRP-ценность (4 оси):**
1. Тех-трансфер: **L** — стек RoR/React/JS/Rust и bodyshop-модель; собственных AI/agent/RAG-активов нет, переносить нечего.
2. Сеть/инвесторы: **L** — bootstrap, инвесторов нет; клиенты — SaaS-скейлапы (Venn, Productmine, Bequant, Mrsool, POM Safe), к deep-tech отношения не имеют.
3. Halo: **L** — работа в/с outstaff-вендором размывает CTO/deep-tech позиционирование, а не усиливает.
4. Партнёрский потенциал: **L** — они поставляют разработчиков, а не покупают AI/neuro/quantum-платформы; покупательского спроса на roadmap ASRP нет.
- **Вердикт двойной выгоды:** Низкая — чистый outstaffing без тех/R&D/партнёрского пересечения с deep-tech roadmap ASRP; ценность для Михаила разве что как «запасной» доход/бенч.

**Источники:** https://newwavedevs.com/ (200 — «Hire Remote Developers in 48 Hours», стек, команда, клиенты), https://jobs.dou.ua/companies/new-wave-devs/ (200 — outstaffing, Kyiv + Sheridan USA, 21–80 спец., 14.11.2019), https://jobs.dou.ua/companies/new-wave-devs/reviews/ (200), `djinni.co/jobs/company-new_wave_devs/` → редирект на /jobs/ (djinni-профиль НЕ подтверждён).

---

### NewGMedia
**Due diligence (личное):**
- Что делают / вертика: Холдинг в iGaming-вертикали (сама называет себя «Gambling Company»/«award-winning iGaming product»); помимо основного игорного продукта управляет affiliate-сетью, собственной платформой и рекрутинговым агентством. 500 000+ игроков (milestone 2021).
- Тип: Product company (iGaming) + смежные бизнес-юниты (affiliate, platform, recruitment). Не аутсорс, но и не deep-tech.
- Финансирование/размер/выручка: 250–300+ сотрудников (DOU: 200…800), офисы в 27–38 странах (Київ, Львів, Кишинёв, Лимассол, Рига, ЮАР). Основана 2016. Финансирование/инвесторы/выручка — не нашлось (выглядит как bootstrap/private holding). **Не резидент Diia City.**
- Отзывы сотрудников/культура: DOU — 26 отзывов, явного числового рейтинга нет. Сигнал смешанный и перекошенный: большинство — короткие восторженные отзывы от кандидатов, которых трудоустраивало собственное рекрутинг-подразделение NewGMedia (паттерн «наняли → попросили отзыв»). Есть жалобы: пассивная агрессия рекрутера на скрининге, опоздания рекрутера на собеседование. Один развёрнутый позитив внутреннего PM (7 мес в продукте) — сильная продуктовая команда, открытая коммуникация.
- Red flags: (1) вертикаль — онлайн-гэмблинг/iGaming; для neuroscience/education-бренда ASRP это репутационная несовместимость; (2) структура размазана по классическим iGaming-юрисдикциям (Кипр, Молдова, Латвия); (3) не Diia City (нет льгот для UA-сотрудников); (4) нераскрытые фаундеры/инвесторы/fin-структура; (5) перекос DOU-отзывов в сторону «самообслуживания» собственным рекрутингом.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: **L** — стек вокруг iGaming-продукта и affiliate-движка (Java/QA), публичных следов AI/agent/RAG нет; на roadmap ASRP не переносимо.
2. Сеть/инвесторы: **L** — инвесторы/cap table не раскрываются, контактов с deep-tech/neuro/quantum нет; окружение — исключительно gambling/affiliate.
3. Halo: **L** — ассоциация с gambling-холдингом скорее ослабит CTO-нарратив ASRP, чем усилит.
4. Партнёрский потенциал: **L** — потребностей в LLM-агентах/GFS/consciousness у iGaming-холдинга не просматривается; клиентом не является.
- **Вердикт двойной выгоды:** Низкая — легитимный iGaming product-холдинг, но нулевое пересечение с deep-tech/AI-agent/education/neuro roadmap ASRP и репутационный минус.

**Источники:** https://jobs.dou.ua/companies/newgmedia/ (200 — 200…800, 250+ в 38 странах, офисы, не Diia City, iGaming+affiliate+platform+recruitment), https://jobs.dou.ua/companies/newgmedia/reviews/ (200 — 26 отзывов), https://newgmedia.net/about-us/ (200 — «started 2016», «award-winning Gambling Company», 300+ в 27 странах, timeline), https://newgmedia.net/ (200 — business-юниты).

---

### Newsoft
**Due diligence (личное):**
- Что делают / вертика: Львовская бутиковая software-dev (custom web/mobile + IT staff augmentation + AI Discovery/Solution Design); клиенты в США и UK в вертикалях healthcare/fitness, e-commerce, sport, cybersecurity, transportation, AI.
- Тип: Outsourcing vendor / staff-augmentation boutique (US-registered «NEWSOFT, INC», офис — Львів).
- Финансирование/размер/выручка: ~50+ человек (40+ инженеров, 21–80 по DOU); основана 2019 (5-летие в 2024, +50% рост в 2023); bootstrapped, выручка не публикуется. 30+ завершённых проектов, 10 текущих клиентов. Фаундеры Volodymyr Tkach (CEO) и Oleh Roshka.
- Отзывы сотрудников/культура: **15 отзывов на DOU** — преимущественно позитивные (дружелюбная атмосфера, сильные коллеги, качественный онбординг, офис с йогой/теннисом в центре Львова); встречается негатив — жалоба на отсутствие фидбека после интервью (Head of People публично извинился). Clutch: Top Shopify/Wellness & Healthcare/E-Commerce/Mobile App Developers Lviv (2019–2026), 5.0 satisfaction (self-reported).
- Red flags: (1) идентификация подтверждена — именно djinni-работодатель «Newsoft» (Lviv, newsoft-ns.com, DOU slug `newsoft`), а не один из десятков одноимённых; (2) мелкий бутик без внешних инвестиций, классическая body-shop модель; (3) «американская» инк.-оболочка при офисе во Львове — типовая схема; (4) один негативный HR-кейс.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: **M** — растущая AI-практика (нанимают ML Ops & Infrastructure Engineer и Senior AI/ML Engineer для USA/NL, кейс с Nomic AI — LLM/embeddings infra, услуга «AI Solution Design»), но это клиентский сервис, не собственный продукт; часть RAG/ML-infra навыков переносима, но с roadmap ASRP (consciousness/quantum/Arcanum12th) не пересекается.
2. Сеть/инвесторы: **L** — два UA-фаундера-бутстраппера, без VC/deep-tech интересов.
3. Halo: **L** — уважаемый львовский бутик с Clutch-наградами, но как работодатель senior/CTO не добавляет стратегического halo.
4. Партнёрский потенциал: **L–M** — потенциально dev-партнёр/staff-aug для инженерных задач ASRP, но без стратегического совпадения по продукту/deep-tech.
- **Вердикт двойной выгоды:** Низкая — легитимный, культурно приятный львовский аутсорсер с растущей AI-практикой, но классический staff-aug без пересечения с deep-tech/Arcanum/consciousness roadmap ASRP; для Михаила-инженера — нормальный вариант, стратегической двойной выгоды нет.

**Источники:** https://jobs.dou.ua/companies/newsoft/ (200 — 21–80 спец., Львів, активные вакансии ML Ops/AI-ML), https://jobs.dou.ua/companies/newsoft/reviews/ (200 — 15 отзывов), https://www.newsoft-ns.com/ + /about (200 — фаундеры Tkach/Roshka, основана 2019, Львів Zelena 149, 50+ team, Clutch awards, Nomic AI testimonial). Brave Search 429 — данные с оф. сайта и DOU.

---

### NuxGame
**Due diligence (личное):**
- Что делают / вертика: B2B-вендор iGaming-софта (с 2018) — turnkey-платформа для онлайн-казино и спортсбук, crypto/sweepstakes casino, game aggregator (17.5K+ игр от 140+ провайдеров, 180+ валют), betting API, affiliate/agent systems, AML/KYC, юр. консалтинг для операторов. 100+ клиентов, ~99% uptime.
- Тип: Product company (B2B SaaS / платформенный вендор для iGaming-операторов).
- Финансирование/размер/выручка: Bootstrapped — $0 внешнего раунда (Crunchbase). Выручка ~$8M (RocketReach/ZoomInfo, неаудировано). Headcount: 64–74 (ZoomInfo/ContactOut), 51–200 (LinkedIn), «200+ специалистов» (сайт) — заметное расхождение. +144% YoY клиентской базы 2024, +59% объёма ставок.
- Отзывы сотрудников/культура: Glassdoor ~15 отзывов, смесь негатива («ambitions, greed, inconsistency») и позитива («QA Is Valued and Collaborative»). DOU-профиля нет (404). Djinni-профиль активный (PHP/Laravel, Senior DevOps/AWS, удалёнка по Европе).
- Red flags: (1) вертикаль iGaming — прямой репутационный конфликт с ASRP; (2) юр. место — Curaçao (reg. 153051, Korporaalweg 10, Willemstad), оффшорная гемблинг-юрисдикция; (3) sweepstakes casino под регуляторным давлением в США (декабрь 2025); (4) нет внешнего финансирования/VC-DD; (5) расхождение headcount сайта vs внешних в ~3 раза.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: **M** — real-time high-load обработка ставок, anti-fraud, API-интеграции, game aggregation, 24/7 back-office, но никакой работы с LLM/агентами/RAG/KG/neurotech — переносится только «боевой» инженерный опыт (микросервисы, реалтайм, платежи), а не AI-deep-tech-стек.
2. Сеть/инвесторы: **L** — bootstrapped ($0), нет VC; сеть = iGaming-операторы, платёжки, game-студии (Yggdrasil, TaDa, AffPapa, Cellxpert), нулевое пересечение с neurotech/quantum/AI-research.
3. Halo: **L (отрицательно)** — CTO-позиция в iGaming/Curaçao-компании повредит halo ASRP (нейронаука/consciousness/этика); «casino platform» для академических партнёров — антипаттерн.
4. Партнёрский потенциал: **L** — roadmap ASRP не имеет функционального пересечения с потребностями iGaming-операторов.
- **Вердикт двойной выгоды:** Низкая — вертикаль iGaming фундаментально несовместима с миссией ASRP, даёт отрицательный halo и нулевую синергию; тех-трансфер ограничивается generic backend без AI-компоненты.

**Источники:** https://nuxgame.com/ (200), https://nuxgame.com/about-us/ (200 — основан 2018, «200+ specialists», 100+ клиентов, leadership Daniel Heywood CEO / Yanina Kaplya COO / Denis Kosinsky CMO / Bar Konson CPO / Dmitriy Volkov CBDO, награды AffPapa/EiGE/SBC/SiGMA/EGR), https://nuxgame.com/privacy-policy/ (200 — Curaçao reg. 153051), LinkedIn-сниппет (Yahoo) — 51–200, Willemstad, 2018, Daniel Heywood (Nicosia), https://djinni.co/jobs/company-nuxgame/ (200 — активные вакансии), https://jobs.dou.ua/companies/nuxgame/ (404 — DOU-профиля нет), Crunchbase-сниппет (Yahoo) — $0 raised.

---

### ONU Health (ранее OWN Health)
**Due diligence (личное):**
- Что делают / вертика: Healthtech-стартап в preventive/digital health — единое mobile-приложение (AI Health Engine + ONU Score), подписка ONU Pro для интерпретации биомаркеров, собственный wearable ONU Bracelet ($99). Позиционирование «catch risks early, before symptoms show up» (сравнивают с Function Health, Superpower, Bevel). Интеграции с Apple Health, Whoop, Garmin.
- Тип: Product company / early-stage digital-health startup (свой app + AI + hardware).
- Финансирование/размер/выручка: не нашлось (нет прессы, Crunchbase 403, news-страница пуста: «Press coverage will appear here as it's published»). Маленькая команда: Andrey Ilskiy (Founder/CEO, NY), Dr. Sebastian Ebert (Head of Medical), Dr. Kirill Rudinsky (Head of Research), Vitalii Lyubimov (Head of Engineering), Mustafa Varol (Head of AI). App Store: ONU 2 отзыва (5.0), Own Health 1 отзыв (5.0) — база на уровне waitlist. Юрлицо **ONU Health Inc.**, Delaware C-Corp (Imprint обновлён 16.01.2026), офисы NY (220 E 23rd St) и Berlin (Chausseestrasse 37). **Rebrand OWН→ONU подтверждён через Apple App Store API** (Developer ID 1868488000): «Own Health» v1.0 — 16.09.2025 → «ONU: All-In-One Health App» v1.0 — 14.02.2026, текущая 1.1.7 от 15.06.2026.
- Отзывы сотрудников/культура: не нашлось. На djinni.co и dou.ua company-профиля нет (slug-вариации = 404; djinni company-filter: «Такої компанії не існує») — stealth-рекрутинг. Восточноевропейские фамилии Head of Engineering/Research объясняют найм через djinni (вероятно через agency/прямые вакансии без company-профиля).
- Red flags: (1) очень ранняя стадия — ни одного пресс-релиза/фандинг-анонса/покрытия за 11 мес работы; (2) ребрендинг через 5 мес после запуска (OWN→ONU) — возможен trademark-конфликт, развод с инвестором или смена позиционирования; (3) /shop возвращает 404 — браслет фактически не продаётся; (4) сайт на Tilda (low-investment web для healthtech с медицинской претензией); (5) stealth-рекрутинг без публичного профиля работодателя; (6) на TechCrunch/tech.eu отсутствует (3 фейковых matchа по подстроке «ONU»).

**ASRP-ценность (4 оси):**
1. Тех-трансфер: **VH** — собственный AI Health Engine (заявленные 3B+ параметров, trained на 147M medical resources / 42M anonymised patient profiles), RAG по medical knowledge с human-in-the-loop review, персонализированный action-planning поверх мультимодальных сигналов (wearables + labs + sleep) — практически 1:1 к ASRP LLM-agent/GFS-платформе и частично к biomed-роадмапу.
2. Сеть/инвесторы: **L** — инвесторы не раскрыты, press-coverage отсутствует, очевидного deep-tech/neuro/quantum спонсора нет; сеть сводится к основателю Andrey Ilskiy.
3. Halo: **M** — Head of Engineering/CTO-track в AI-healthtech с заявленной медицинской нагрузкой даёт релевантный halo в biomed/AI-агентах, но при нулевой узнаваемости и отсутствии институциональных маркеров качества передача репутации ограничена.
4. Партнёрский потенциал: **M** — реальное пересечение по биомед-вертикали (biomarkers, HRV, stress, biological age — темы, релевантные neuroscience-роадмапу ASRP), но ONU в consumer-wellness, не в clinical research; партнёрство скорее технологическое (LLM-инфра, RAG), чем коммерческое.
- **Вердикт двойной выгоды:** Средняя — тех-трансфер VH (AI Health Engine / RAG / multimodal biomarker orchestration прямо ложится на ASRP LLM-agent roadmap и частично на biomed), но network L, halo M, партнёрство M, а лично для DD это ранний stealth-стартап без подтверждённого финансирования и стабильного бренда — высокий upside при высоком риске.

**Источники:** https://onuhealth.com/ + /about-us + /imprint + /ai-engine + /careers + /press (200 — позиционирование, команда, ONU Health Inc. Delaware C-Corp, NY/Berlin, CEO Andrey Ilskiy), /shop (404), https://itunes.apple.com/lookup?id=1868488000&entity=software (200, JSON — 2 app: «Own Health» v1.0.2 + «ONU: All-In-One Health App» v1.1.7, seller ONU Health Inc.), https://jobs.dou.ua/companies/onu-health/ и slug-вариации (404), djinni company-filter «Такої компанії не існує» (stealth).

---

### OneTablet
**Due diligence (личное):**
- Что делают / вертика: US-based (HQ New York City) product company; продукт **Sous Chef** — SaaS «operating system for off-premise restaurant operations»: агрегация заказов Uber Eats / DoorDash / Grubhub / Caviar / Wonder в одной консоли, управление меню/ценами/prep-таймингами, AI-инсайты («Ask your delivery data anything», first-party ordering через ChatGPT). UA дев-офис в Киеве (≤20 по DOU).
- Тип: Product company (remote-first SaaS; Tech Product по DOU).
- Финансирование/размер/выручка: ≤20 спец. (DOU); регистрация на DOU 07.04.2020; **не резидент Diia City**. Финансирование/инвесторы/выручка — не нашлось (Crunchbase/Tracxn/Wellfound блочат/нет профиля, founder/CEO публично не назван).
- Отзывы сотрудников/культура: «Відгуків поки що немає» на DOU; Glassdoor не идентифицирован.
- Red flags: непубличность фаундеров/инвесторов; очень маленькая команда при 5+ годах работы; не Diia City (юр./налог. незащищённость для UA-найма в 2026); активных вакансий на DOU/djinni в момент проверки не найдено (профиль djinni.co отсутствует — `onetablet`, `one-tablet`, `sous-chef`, `yoursouschef` — все 404); бренд «OneTablet» на djinni подтверждён только через DOU `onetablet`, не прямой djinni-ссылкой.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: **M** — есть прикладные LLM-интеграции (NL-запросы к delivery-данным, ChatGPT-first-party ordering), но это product-AI в restaurant vertical, а не deep agent/RAG-инфра; перенос опыта ограничен.
2. Сеть/инвесторы: **L** — фаундеры/инвесторы не раскрыты, vertical = restaurant tech.
3. Halo: **L** — узкий B2B-SaaS в фуд-техе, не добавляет веса как CTO neuro/AI-холдинга («US product company, Kyiv dev team» — нейтрально-позитивный факт в резюме).
4. Партнёрский потенциал: **L** — ресторан-tech не целевой рынок для LLM-агентов / GFS / Arcanum12th / GMS.
- **Вердикт двойной выгоды:** Низкая — легитимный US product company с украинским дев-офисом, но vertical (restaurant delivery SaaS) не пересекается с deep-tech/neuro/AI-agent/education направлениями ASRP; тех-трансфер ограничен прикладным LLM-опытом.

**Источники:** https://jobs.dou.ua/companies/onetablet/ (200 — ≤20 спец., Kyiv, 07.04.2020, не Diia City, «operating system for modern restaurants»), https://onetablet.co/ (301→yoursouschef.com 200 — Sous Chef, AI-powered restaurant management, интеграции Uber Eats/DoorDash/Grubhub), https://onetablet.co/about-us (200 — HQ NYC, партнёрства Profit Cookers/Star Micronics), https://www.restaurantnews.com/...profit-cookers-onetablet... (200 — пресс-релиз 04.02.2026), https://djinni.co/companies/onetablet/ (404 — профиль на djinni не найден).

---

### Playtech
**Due diligence (личное):**
- Что делают / вертика: Крупнейший в мире B2B-разработчик ПО для онлайн-гемблинга (онлайн-казино, live-casino, спортбеттинг, покер, бинго, лотереи, ритейл-беттинг) — платформа, контент и услуги для 180+ лицензиатов (William Hill, Ladbrokes, Bet365, Snai/Sisal и др.).
- Тип: Product company (горизонтальный B2B для операторов), публичная — **LSE: PTEC**, FTSE 250, premium listing на Main Market.
- Финансирование/размер/выручка: основана 1999 (Teddy Sagi, Тарту, Эстония). HQ — Douglas, Isle of Man (UK Gambling Commission license #38516); операционно — Лондон. ~7400 сотрудников в 20 странах. **FY2025** (отчёт 26.03.2026, investors.playtech.com): revenue €764M, Adjusted EBITDA €197M, net cash €29M, рост выручки в США/Канаде +61%; reported net income €1,484M (включая gain от продажи Snaitech). 2025 — завершена продажа B2C-юнита Snaitech, переход к «pure-play B2B». CEO — Mor Weizer, Chairman — Brian Mattingley. UA R&D «PTS UA Services LLC» открыт в Киеве в августе 2011 (Gulliver BC), 750 специалистов; команд в Киеве — BetBuddy, IMS, Live, Casino, Bingo, Sports, Quickspin, Rarestone. Львовского офиса на оф. сайте нет (только Kyiv).
- Отзывы сотрудников/культура: DOU **85/100** (150 голосов): компенсація 84%, умови 91%, кар'єра 80%, проєкт 83%, культура 83%, соцвідп. 89%. Вакансии: AI Project/Governance & Operations Manager, Fullstack/Scala/DevOps/Front-End Game Dev.
- Red flags: (1) вертикаль iGaming — прямая репутационная несовместимость с ASRP; (2) регуляторные штрафы: £3.5M от UK Gambling Commission за «serious systemic failings» в соц.ответственности/AML (PTES, 2020); (3) основатель Teddy Sagi — фигура с противоречивой репутацией (израильская судимость в 1990-х; divested, но ассоциация сохраняется); (4) зависимость от регулирования гемблинга в 40+ юрисдикций; (5) operating loss €128M 2025 (net income раздут разовой продажей Snaitech).

**ASRP-ценность (4 оси):**
1. Тех-трансфер: **L** — узкая ML-экспертиза (BetBuddy — responsible-gambling analytics, интеграция Featureshouse для fraud, IMS data platform, вакансия AI Governance), но это доменно-специфичная аналитика в гемблинге, а не LLM-агенты/RAG/KG; прямого переноса на roadmap ASRP нет.
2. Сеть/инвесторы: **L** — публичный LSE/FTSE 250, институциональные инвесторы из iGaming/consumer-tech; ни у одного направления ASRP нет естественного перетекания интересов.
3. Halo: **L (негативно)** — Playtech = flagship iGaming-вендор; для CTO neuroscience/consciousness-холдинга ассоциация с гемблингом скорее ослабит личный halo и создаст friction с академическими/медицинскими партнёрами ASRP.
4. Партнёрский потенциал: **L** — монопрофильный регулируемый B2B-гемблинг; никаких смежных vertical, куда ASRP мог бы зайти как поставщик.
- **Вердикт двойной выгоды:** Низкая — сильный легитимный работодатель с крепкой инженерной культурой в Киеве (плюс для личного дохода), но iGaming-домен даёт нулевое пересечение с roadmap ASRP и репутационный минус.

**Источники:** https://en.wikipedia.org/wiki/Playtech (200), https://www.playtech.com/ + /about-us + /locations (200), https://www.playtechpeople.com/country/ukraine/ (200 — только Kyiv R&D с 2011, 750 спец., Lviv нет), https://jobs.dou.ua/companies/playtech/ (200 — 85/100, 200–800 спец., Kyiv), https://www.investors.playtech.com/ (200 — FY2025 revenue €764M, Adj EBITDA €197M, продажа Snaitech, pure-play B2B).

---

### RecruitGarden
**Due diligence (личное):**
- Что делают / вертика: UA кадровое агентство (recruiting/staffing), специализация — IT-рекрутинг (подбор full-time office/remote IT-специалистов для клиентских компаний), услуги RPO и employer brand. Слоган: «Probably the best recruitment agency in Ukraine».
- Тип: Recruitment agency (посредник), не product, не outsourcing.
- Финансирование/размер/выручка: bootstrapped/private, до 20 сотрудников по DOU; выручка/финансирование — не нашлось. Основатель — Marina (CEO).
- Отзывы сотрудников/культура: Clutch — 14 отзывов («хорошее соотношение цена/качество» у клиентов); Glassdoor-профиль есть, численный рейтинг не открылся (Cloudflare); на DOU отзывов сотрудников мало (агентство <20 чел.).
- Red flags: не резидент Diia City; кадровое агентство — Михаилу как senior-инженеру/CTO там инженерной роли нет (разве что внутренние tools). Публичного tech-стека нет.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: **L** — технической инфраструктуры нет, recruiting-сервис.
2. Сеть/инвесторы: **L** — частное bootstrapped-агентство без institutional backing и без связи с deep-tech.
3. Halo: **L** — работа в кадровом агентстве не добавляет CTO-авторитета в neuroscience/AI-среде.
4. Партнёрский потенциал: **L–M** — теоретически канал найма IT-талантов для ASRP, но как клиент/партнёр по deep-tech — нет.
- **Вердикт двойной выгоды:** Низкая — типичное UA рекрутинговое агентство без тех/deep-tech пересечения с roadmap ASRP; полезно только как потенциальный источник найма.

**Источники:** https://recruitgarden.com/ (200 — описание, теглайн, «Founded in 2020»), https://jobs.dou.ua/companies/recruitgarden/ (200 — до 20 спец., Київ, 16.04.2020, «Recruiting Agency», не Diia City), Yahoo-сниппеты (djinni presence, LinkedIn 2556 followers, Clutch 14 reviews, Crunchbase-профиль, CEO Marina).

---

### S-PRO
**Due diligence (личное):**
- Что делают / вертика: Custom software development и IT-консалтинг; ключевые вертикали — Fintech, Healthcare, Manufacturing, Energy; услуг-стек: AI/ML, web, blockchain, mobile, UI/UX, cloud, data. Швейцарский холдинг (S-PRO AG, Zug) с R&D-хабами в Украине/Польше и офисами в US, NL, DE, AM.
- Тип: Outsourcing vendor / product engineering studio (300+ проектов с 2014, 72% клиентов — Европа, в основном CH/DE).
- Финансирование/размер/выручка: Bootstrapped (Crunchbase без раундов). 250+ специалистов (LinkedIn/сайт), DOU 200–800. Юрлицо S-PRO AG, Zug (CHE-415.465.002.21); дополнительно S-PRO Ventures AG (Zürich, Löwenstrasse 45 — тот же офис, вероятно venture-arm). Точная выручка не раскрывается. CEO — Igor Izraylevych.
- Отзывы сотрудников/культура: Glassdoor **4.1/5**, 90% рекомендуют друзьям; Clutch **4.9/5** (46 отзывов); on-site schema.org aggregateRating 4.9 (117 отзывов). DOU-профиль активен с 12.02.2016.
- Red flags: S-PRO НЕ резидент Diia City. Сайт marketing-heavy; часть «продуктов» (Optimisation Agent, RegRadar, Aura for Excel) подаются как S-PRO-продукты, но бизнес-модель — time&materials/staff augmentation; продуктового revenue engine публично не видно. M&A/стратегических инвесторов не найдено.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: **H** — реальная (не маркетинговая) AI-практика: AI-Native SDLC (CSS-визуализация RAG-архитектуры с Claude в IDE), «GenAI & Agentic AI prototyping» (Claude Code + Mobbin + Figma), задеплоенный продукт **Optimisation Agent by S-PRO** (20M+ кино-билетов/год для Multiplex — крупнейшей сети UA), AI-кейсы для compliance, VC-платформ, маркетинга. 50+ AI/Data проектов за 3 года. Стек переносим на roadmap ASRP (LLM-агенты, multi-agent, RAG).
2. Сеть/инвесторы: **L–M** — bootstrapped outsourcing, клиенты в fintech/healthcare; S-PRO Ventures AG существует, но публичного портфолио в neurotech/quantum/consciousness нет; основная сеть — швейцарско-немецкий mid-market enterprise.
3. Halo: **M** — бренд уважаемый (Clutch 4.9, Glassdoor 4.1, швейцарская инкорпорация), но outsourcing-вендор не даёт halo в research/deep-tech сообществе; усиливает operational AI-delivery credentials, но не научную репутацию.
4. Партнёрский потенциал: **M** — потенциальный исполнитель для прототипирования/масштабирования Arcanum12th/GMS, но собственная клиентура не пересекается с neuro/quantum/consciousness; партнёрство скорее «как вендор», чем стратегический союзник.
- **Вердикт двойной выгоды:** Средняя — подлинная agent/RAG/LLM-экспертиза (редкая для аутсорсинга), что делает роль полезной для тех-трансфера в LLM-ось ASRP, но клиентская база/инвестиционный профиль не пересекаются с neuro/quantum/consciousness roadmap; основная ценность — senior/CTO-track в сильной AI-delivery команде + опциональный вендор для прототипов.

**Источники:** https://s-pro.io (200 — positioning, Optimisation Agent/RegRadar/AI-Native SDLC, CEO Igor Izraylevych, 250+ engineers), https://s-pro.io/landing/optimisation-agent/ (200 — deployed AI-agent, 20M+ билетов/год для Multiplex), https://s-pro.io/prototypes-services-with-genai (200 — GenAI & Agentic AI prototyping, aggregateRating 4.9), https://s-pro.io/landing/ai-native-sdlc/ (200 — RAG visualization + Claude в IDE), https://jobs.dou.ua/companies/s-pro/ (200 — 200–800, Киев/Лодзь/Цюрих, 12.02.2016, не Diia City), Yahoo-сниппеты (LinkedIn/Clutch/Glassdoor/Crunchbase), moneyhouse.ch (200 — S-PRO AG Zug + S-PRO Ventures AG Zürich).

---

### Seeking Alpha
**Due diligence (личное):**
- Что делают / вертика: Crowd-sourced финансовая платформа — новости, аналитика акций, crowdsourced статьи от независимых авторов (buy-side contributors), количественные рейтинги (Quant Ratings, Factor Grades) и платные подписки SA Premium/Pro; монетизация = подписка + реклама.
- Тип: Product company — легитимный глобальный финтех-дата/финансовый-паблишинг бренд.
- Финансирование/размер/выручка: ~170 сотрудников (Wikipedia); UA-офис в Киеве 21–80 (DOU), регистрация на DOU 18.12.2020, **не резидент Diia City**. **Series B $7M (2009, лидер DAG Ventures + Benchmark + Accel; контент-партнёрство с Nasdaq).** Текущая выручка/captable публично не раскрываются; слух об инвестиции Surveyor Capital/Point72 в первичных источниках подтвердить не удалось (не нашлось). Основатель David Jackson (ex-Morgan Stanley).
- Отзывы сотрудников/культура: на DOU всего **1 отзыв** (март 2025) — негативный опыт кандидата («сдали тестовое, прислали шаблонный отказ без обратки»). Glassdoor напрямую 403; большая выборка недоступна.
- Red flags: (1) Wikipedia-секция «Alleged use by stock manipulators» — корот-селлеры использовали псевдонимы (исследование Columbia Law School, Mitts); судимой ответственности у SA нет, после этого ужесточили политику псевдонимов/редактуры; (2) не Diia City (минус для UA-найма); (3) слишком мало публичных отзывов сотрудников для надёжной оценки культуры.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: **M–H** — стек Ruby/Rails + Go + Objective-C (iOS), Nix/devenv, Elasticsearch; форк `vellum-client-ruby` (Vellum.ai — LLMOps) от 2025-06-08 и оригинальный `git-log-mcp` (FastMCP-сервер) от 2026-02-13 — значит, активно строят LLM-пайплайны поверх финансового текста и экспериментируют с MCP/agent-тулингом, что прямо переносимо на GFS-forecasting/knowledge-work ASRP. Не front-office multi-agent-оркестрация, но серьёзная прикладная LLM-инженерия.
2. Сеть/инвесторы: **M** — старые бэкеры Benchmark, Accel, DAG Ventures; стронг VC-педигри, но это consumer-finance медиа-поверхность, явных интересов в neuro/quantum/consciousness нет.
3. Halo: **H** — глобально узнаваемый финтех-дата-бренд с дистрибуцией через Nasdaq, CNBC, MarketWatch, MSN, TheStreet; senior/CTO-роль даёт публичную рыночную видимость и credibility в fintech-data.
4. Партнёрский потенциал: **M** — buy-side contributors и Quant Ratings — естественный потребитель LLM-аналитики/forecasting-инструментов; но это контент-бизнес с собственной ML-командой, внешний deep-tech-заказ маловероятен.
- **Вердикт двойной выгоды:** Средняя — реальный прикладной LLM/MCP-стек + сильный global-fintech halo усиливают личную позицию Михаила и частично переносимы на GFS, но прямого моста в neuro/quantum/consciousness roadmap ASRP нет (это финтех-дата, не deep-tech).

**Источники:** https://en.wikipedia.org/wiki/Seeking_Alpha (200 — основана 2004, David Jackson, HQ Ra'anana IL, ~170 employees, Series B $7M 2009 DAG/Benchmark/Accel, stock-manipulation section), https://jobs.dou.ua/companies/seeking-alpha/ (200 — Київ, 21–80, Tech Product, не Diia City, 18.12.2020), /reviews/ (200 — 1 отзыв), https://techcrunch.com/2009/12/02/seeking-alpha-funding-nasdaq/ (200 — Series B $7M), https://api.github.com/orgs/seekingalpha (200 — 149 public repos; форк vellum-client-ruby 2025-06-08 + оригинальный git-log-mcp FastMCP 2026-02-13 — **spot-checked, confirmed**). Surveyor Capital/Point72 / выручка / свежие Glassdoor-рейтинги — не подтвердилось из первичных источников.

---

### SharksCode
**Due diligence (личное):**
- Что делают / вертика: UA лицензированная IT-компания (ТОВ «ШАРКСКОД», ЄДРПОУ 44423600); разрабатывает высокотехнологичные B2B-платформы — **основная вертикаль iGaming** (казино/betting-инфраструктура), плюс CRM/enterprise, AI/LLM-инструменты, HR/Legal/Marketing.
- Тип: Product company (собственные B2B-платформы для iGaming), не классический аутсорс; между product shop и white-label platform vendor.
- Финансирование/размер/выручка: DOU 200–800 спец.; Datanyze/LinkedIn 250–500; рейтинг DOU проголосовали лишь 23 сотрудника (реальный размер, вероятно, 150–300). Финансирование — не нашлось (Crunchbase 403). **Резидент Diia City.** Участник IT Ukraine Association, в июне 2026 вошли в AI Committee. Директор-бенефициар Hryshchenko Pavlo Oleksandrovych.
- Отзывы сотрудников/культура: DOU **91/100** (23 голоса): компенсація 89%, умови 95%, кар'єра 89%, проєкт 94%, культура 89%, соцвідп. 92%. 23 текстовых отзыва (в основном позитивные — рекрутер Олена, HR Олександра, work-life balance). Glassdoor — не нашлось.
- Red flags: (1) **главный бизнес — iGaming-инфраструктура** (этический/репутационный риск для нейро-/научного CTO); (2) молодое юрлицо — зарегистрировано в ЕДР 26.03.2024 (на DOU с 21.10.2024), хотя IT Ukraine указывает «Заснована в 2021» (расхождение); (3) директор-бенефициар публично минимально светится; (4) завышенный диапазон «200–800» vs ~23 голосов; (5) employer brand на djinni.co отсутствует (профиль `/companies/sharkscode/` 404); рекрутинг идёт в основном через DOU.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: **M** — реальная практика LLM-агентов (статья на DOU «Як ми впровадили AI-агента у HR: архітектура, RAG і автоматизація онбордингу» 10.03.2026; «Як змінилася роль QA-інженера з приходом ШІ» 15.06.2026) и членство в AI Committee IT Ukraine, но стек заточен под iGaming/high-load B2B, а не под research-grade AI.
2. Сеть/инвесторы: **L** — частный UA iGaming-вендор без VC, без deep-tech/neuro/quantum сети; CEO публично не светится.
3. Halo: **L** — ассоциация с iGaming размывает научно-технологический образ; AI Committee даёт минимальный отблеск, не компенсируя вертикаль.
4. Партнёрский потенциал: **L** — потенциальный покупатель generic LLM-агентов/RAG для внутренних нужд (HR, support, QA), но roadmap ASRP с iGaming-продуктом не пересекается.
- **Вердикт двойной выгоды:** Низкая — легитимный, быстрорастущий UA product-employer с неплохой культурой (DOU 91/100) и живой AI/RAG-практикой для собственных нужд, но корневая вертикаль iGaming и отсутствие пересечения с neuro/quantum/consciousness/education roadmap ASRP делают двойную пользу минимальной; интерес возможен только как площадка для Михаила-инженера, не как стратегическое партнёрство.

**Источники:** https://sharkscode.com/ (200 — iGaming-сектор), https://jobs.dou.ua/companies/sharkscode/ (200 — 91/100, 200–800 спец., Diia City, 21.10.2024), /reviews/ (200 — 23 отзыва), https://itukraine.org.ua/en/member/sharkscode (200 — участник IT Ukraine, «Заснована в 2021», специализации CRM/AI/HR/Legal/Marketing/Media, фокус iGaming; AI Committee 09.06.2026), Yahoo-сниппет youcontrol.com.ua (ЄДРПОУ 44423600, директор Hryshchenko Pavlo Oleksandrovych), Crunchbase/LinkedIn-сниппеты (Yahoo), https://djinni.co/companies/sharkscode/ (404 — профиль на djinni отсутствует).

---

### Sigma Software
**Due diligence (личное):**
- Что делают / вертика: Кастомная разработка и engineering-консалтинг (outsourcing / technology consulting), часть шведской Sigma Group (владелец — Danir AB); ключевые вертикали — Automotive, Aviation, Defense, AdTech, Healthcare, Finance & Banking, Logistics, Manufacturing, Embedded & IoT.
- Тип: Outsourcing / technology consulting vendor (крупный).
- Финансирование/размер/выручка: ~1500+ специалистов (DOU); основана 2002 (JSON-LD + футер «2002–2026»); часть Sigma AB / Sigma Group (Швеция, Malmö, материнская Sigma AB основана 1986, владелец группы — Danir AB). Офисы: UA (Київ, Львів, Харків, Дніпро, Одеса, Вінниця, Івано-Франківськ, Луцьк, Моршин, Полтава, Суми, Тернопіль, Черкаси, Чернівці), PL (Варшава/Краків/Познань), BG (Бургас), RO (Бухарест), UZ (Ташкент) + US/Sweden/LatAm. Самостоятельное финансирование/раунды не применимы (часть давно существующей шведской группы).
- Отзывы сотрудников/культура: DOU **91/100** (Топ-50, 63 голоса): компенсація 85%, умови 95%, кар'єра 89%, проєкт 92%, культура 88%, соцвідп. 96%. Сильная репутация топ-tier UA-работодателя; на сайте продвигаются AI-инициативы (AI Compass, **финал NATO Innovation Challenge с Agentic AI Concept 23.04.2026**, **партнёрство с NEAR AI по confidential inference 20.04.2026** — оба подтверждены на sigma.software).
- Red flags: публичных red flags нет; обычные для крупного аутсорсинга риски — зависимость от клиентских заказов, смена CEO (новость «Sigma Software зміниться СЕО»), ограниченная product-составляющая.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: **H** — реальные Agentic AI-разработки (финал NATO Innovation Challenge с agentic AI concept) и партнёрство с NEAR AI по confidential-inference-инфраструктуре для enterprise/government; AI Compass — собственная методология AI-трансформации; RAG/LLM/SDLC AI-пилоты — напрямую переносимы на multi-agent/LLM-agent дорожку ASRP.
2. Сеть/инвесторы: **M** — за компанией крупная шведская Sigma Group / Danir AB (стабильный институциональный бэкер), но фокус группы — enterprise/government/industrial, а не neurotech/quantum/consciousness-research.
3. Halo: **H** — топ-UA engineering brand (Топ-50 DOU, 1500+ инженеров, международные офисы, NATO/NEAR AI партнёрства); senior/CTO-роль добавляет очевидный брендовый вес.
4. Партнёрский потенциал: **M** — как development partner для ASRP-платформ возможен (у Sigma есть AI Compass как услуга), но стратегического интереса к neuro/consciousness/quantum нет; партнёрство реалистично только в LLM-agent инженерном слое.
- **Вердикт двойной выгоды:** Средняя — для Михаила сильный легитимный работодатель топ-уровня с реальной agentic-AI экспертизой (прямое пересечение с AI-agent осью ASRP), но strategic depth по neuro/quantum/consciousness отсутствует, а партнёрский потенциал ограничен engineering-услугами.

**Источники:** https://sigma.software/ (200 — основана 2002, Sigma Group/Danir AB ownership, вертикали, AI Compass, NATO Innovation Challenge Agentic AI finals 23.04.2026, NEAR AI confidential inference partnership 20.04.2026 — **spot-checked, confirmed**), https://jobs.dou.ua/companies/sigma-software/ (200 — 1500+ спец., 91/100, Топ-50, 63 голоса, города), https://en.wikipedia.org/wiki/Sigma_AB (200, редирект с Sigma_Software — подтверждает связь с Sigma AB, Malmö, 1986, owner Danir AB), https://sigma.software/about (200).

---

## Кросс-батчевые выводы (A–S, 52 компании)

Этот батч (N–S) повторяет паттерн серий aa/ab/ac: **iGaming-кластер даёт стабильно отрицательную двойную выгоду** (здесь NewGMedia, NuxGame, Playtech, SharksCode — все Низкая), **рекрутинг/аутстафф — стабильно Низкая** (New Wave Devs, RecruitGarden). Новое в этом батче — **два подлинно релевантных тех-кластера**, которых в aa–ac было мало:

1. **UA-outsourcing с публичной agentic-AI-практикой** (N-iX, S-PRO, Sigma Software — все Средняя, H на tech-transfer). Это «безопасные» варианты: низкий риск работодателя + реальный перенос LLM-agent/RAG-стека на roadmap ASRP. Из всей серии это наиболее надёжная категория для тех-трансфера без компромисса по halo.
2. **Прикладной LLM/MCP в продуктовой финтех-дате** (Seeking Alpha — Средняя, H halo + GitHub-evidenced LLM/MCP-инженерия) — лучший в серии global-halo при частичном переносе на GFS.
3. **Единственный «стенд-аут» прямой двойной выгоды — ONU Health** (Средняя, но VH tech-transfer): собственный AI Health Engine / RAG / multimodal biomarker orchestration = прямое пересечение с LLM-agent roadmap + biomed ASRP. Риск раннего stealth-стартапа высокий, но такого плотного тех-overlap в серии ещё не было (ближайший аналог — **Bswan AI** из батча aa по AI-нативности, но ONU — это ещё и biomed-вертикаль ASRP).

**Рекомендация для Михаила:** если приоритет = низкий риск + AI-agent тех-трансфер → **Sigma Software / N-iX / S-PRO** (в порядке halo→scale). Если приоритет = максимальное пересечение с biomed/neuro roadmap ASRP и готовность к стартап-риску → **ONU Health** (Head of Engineering/CTO-track, прямой RAG/agent-перенос). Если приоритет = global fintech halo + GFS-перенос → **Seeking Alpha**. iGaming-четвёрку (NewGMedia/NuxGame/Playtech/SharksCode) и рекрутинг-пару — **исключить** из стратегического шорт-листа ASRP (только как бытовой income, с пониманием репутационного mismatch).
