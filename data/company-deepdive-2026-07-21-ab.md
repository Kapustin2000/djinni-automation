# Deep-dive по компаниям (батч D–G) — due diligence + стратегическая ценность для ASRP, 2026-07-21

Продолжение серии [company-deepdive-2026-07-21-aa.md](company-deepdive-2026-07-21-aa.md) (батч A–C) и [company-due-diligence-2026-07-20.md](company-due-diligence-2026-07-20.md), в том же **объединённом формате**: для каждой компании одновременно личный DD (для трудоустройства Михаила Капустина) + оценка двойной выгоды для ASRP по 4 осям. Охват — 13 компаний из вакансий djinni.co (бренды на D–G).

**Заказчик:** Михаил Капустин, CTO и сооснователь ASRP (Advanced Scientific Research Projects) — холдинг в neuroscience / AI / consciousness research / quantum computing / биомед / образовании (Arcanum12th), зарегистрирован в Казахстане и США.
**Roadmap ASRP:** (a) LLM-агенты / multi-agent, (b) GFS forecasting-платформа, (c) Arcanum12th образовательная платформа, (d) GMS consciousness-платформа.
**Шкала осей:** L / M / H / VH. **Вердикт двойной выгоды:** Высокая / Средняя / Низкая — бар для «Высокая» = реальное пересечение с deep-tech/AI-agent/education/neuroscience-роадмапом ASRP (не просто «легитимный работодатель»).

> **Методологическая оговорка (важно для калибровки уверенности).** Встроенные поисковые инструменты снова недоступны: WebSearch и web-reader MCP возвращают HTTP 429 «insufficient balance» (подтверждено перепроверкой 2026-07-21 — `web_search_prime` отдаёт `MCP error -429: insufficient balance`); WebFetch в этом окружении отсутствует. Поэтому весь ресёрч — **прямые fetch'и первичных источников через `curl`** (браузерный UA): официальные сайты, Wikipedia, prnewswire/finsmes/tech.eu/techcrunch, wellfound/tracxn, **UK Companies House**, **французская SIRENE** (`recherche-entreprises.api.gouv.fr`), **jobs.dou.ua**. Ключевые факты этого батча дополнительно прошли spot-check куратором: Datagrok (homepage подтверждает научный профиль: Enterprise Data Science / Cheminformatics / Macromolecules / Academia), GlobalLogic (DOU рейтинг **63/100**, 1500 спеціалістів, Diia City), GR8 Tech (DOU упоминает «Parimatch», 200–800 спец., Cyprus/Moldova/Poland), GoReel (whois: Creation 2025-06-29). Что надёжно верифицировано: продуктовое позиционирование (офиц. сайты), ownership/acquisition (Wikipedia, finsmes), регистрации/юрлица (Companies House, SIRENE), классификация и размер (DOU). Что **не** удалось проверить: отзывы сотрудников (Glassdoor/Clutch/Wellfound блокируют ботов — 403), кипрский реестр, точные глобальный headcount/выручка для GlobalLogic (corporate-сайт блочит бота — 302/empty). Ничего не выдумано; провалы помечены «не нашлось».

---

## Подробно по компаниям

### Datagrok
**Due diligence (личное):**
- Что делают / вертикаль: Web-based data-analytics платформа для научных данных — cheminformatics, macromolecules, enterprise data science, academia. Работает в браузере с датасетами 10M+ строк; 40+ коннекторов к БД, 20+ файловых форматов, 30+ форматов молекулярных структур, плагин-архитектура (R/Python/Julia/MATLAB/TF.js). Есть бесплатная лицензия для академии; заказчики — «топовые учёные по всему миру».
- Тип: Product company (Tech Product per DOU). Сильный deep-tech/scientific профиль, не аутсорс.
- Финансирование/размер/выручка: Юрлицо «Datagrok, Inc» (США, info@datagrok.ai). На DOU — «до 20 спеціалістів», киевский офис; зарегистрирована на DOU 03.01.2020. Глобальный размер и funding — не нашлось (finsmes/prnewswire пусто, tracxn 404).
- Отзывы сотрудников/культура: отзывов на DOU нет (только вакансия Engineering Manager, удалённо); публично pro-Ukraine. Рейтингов не нашлось.
- Red flags: Конкретных нет. Часто предполагаемая связь с ChemAxon/Certara (химическая компания, купленная Certara в октябре 2024) **из fetched-источников не подтверждена**. Команда маленькая.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: VH — knowledge graphs, научные data pipelines, in-browser ML (R/Python/Julia/TF.js), плагин-экосистема напрямую переносимы на LLM-agent/RAG/KG-infra роадмап ASRP + bio-med вертикаль.
2. Сеть/инвесторы: L–M — владельцы/инвесторы не идентифицированы (частная, без публичных раундов); доступа к neurotech/quantum-сети не видно.
3. Halo: M–H — работа в научной data-platform для топовых исследователей усиливает CTO-репутацию в deep-tech / научном сообществе.
4. Партнёрский потенциал: M–H — платформа может стать фундаментом ASRP bio-med/KG-инструментария; потенциальный лицензиат/партнёр по академ-каналам.
- **Вердикт двойной выгоды:** Высокая — единственная в батче с реальным пересечением с deep-tech + KG + bio-med роадмапом ASRP.

**Источники:** https://datagrok.ai/ (200), https://datagrok.ai/help (200, wiki), https://github.com/datagrok-ai/public/raw/master/README.md (200, raw), https://jobs.dou.ua/companies/datagrok/ (200), https://en.wikipedia.org/wiki/ChemAxon (200 — acquisition by Certara Oct 2024; связь с Datagrok не подтверждена).

---

### Delasport
**Due diligence (личное):**
- Что делают / вертика: B2B-провайдер iGaming-софта — собственный Sportsbook, Casino/PAM, Odds Feed, Trading Services, Managed Services; 30+ лицензий (UK Gambling Commission, Malta, Ontario, Denmark, Sweden, Netherlands, South Africa). Платформа «полностью owns IP».
- Тип: Product company (внутренний продукт, не аутсорс). Международная, R&D в Киеве с 2022 (Podil).
- Финансирование/размер/выручка: 300+ сотрудников (сайт + DOU); основана 2010. На DOU — «81...200 спеціалістів», Kyiv. CEO Oren Cohen Shwartz (Израиль), CTO Georgi Stalev (Болгария). Funding — не нашлось. Гипотеза о Nasdaq Stockholm (ticker DELA) **опровергнута** — публичных листингов нет; похоже на private/bootstrapped. В UK Companies House отсутствует.
- Отзывы сотрудников/культура: DOU-страница есть, отзывов на DOU не нашлось; на careers — внутренние testimonials (позитивные, но маркетинг). Glassdoor/Kununu — не нашлось (403/отсутствует).
- Red flags: Индустрия gambling/iGaming — репутационный/этический риск для CTO neuroscience/consciousness-холдинга ASRP; украинский R&D строит ePayment/wallet/bonus-движок (регуляторно-нагруженный домен).

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L–M — солидный modern stack (Java 21, Spring Boot 3, Kafka, MongoDB, GCP, K8s, microservices), но это transactional/betting-инфра, а не LLM-agents/KG/forecasting; переносимость минимальная.
2. Сеть/инвесторы: L — инвесторы не идентифицированы; к deep-tech/neurotech/quantum сетям доступа нет.
3. Halo: L — iGaming не усиливает академический CTO-brand ASRP, скорее разбалансирует (gambling vs neuroscience/education).
4. Партнёрский потенциал: L — ASRP не клиент и не партнёр для betting-platform.
- **Вердикт двойной выгоды:** Низкая — легитимный product-работодатель с сильной инженерией в Киеве, но индустрия и стек почти не пересекаются с deep-tech-миссией ASRP.

**Источники:** https://www.delasport.com (200), https://www.delasport.com/about-us/ (200), https://www.delasport.com/careers/ (200), https://www.delasport.com/news/ (200), https://jobs.dou.ua/companies/delasport/ (200), https://find-and-update.company-information.service.gov.uk/search/companies?q=delasport (200, no results), https://www.finsmes.com/?s=delasport (200, no results).

---

### Devcom
**Due diligence (личное):**
- Что делают / вертика: Software development outsourcing — custom software, mobile/web, QA, UI/UX, cloud-migration (AWS/Azure/GCP), Salesforce, BI. Активно продаёт AI/LLM/ChatGPT/Agent/Agentic-AI и Web3/NFT/DeFi как услуги. Индустрии: Healthcare, Construction, Energy, Home Improvement, Fintech, Logistics, Retail.
- Тип: Outsourcing vendor (классический). Не product, не staffing-intermediary.
- Финансирование/размер/выручка: 200+ инженеров (сайт); на DOU — «81...200 спеціалістів». Основана 2000 (25+ лет). HQ Port Orange, FL, USA + дев-офис во Львове. CEO Dima Semensky. Не VC-backed, private. Выручка не нашлась.
- Отзывы сотрудников/культура: 7 отзывов на DOU (последний 31.10.2025, System Administrator, позитивный); сами они заявляют «DOU rated DevCom as one of the 15 best places to work» (без даты/числа). Сводного численного рейтинга однозначно не идентифицировано.
- Red flags: Конкретных нет. «Agentic AI / ChatGPT Development / NFT / DeFi» как услуги — маркетинговый breadth, не глубокая deep-tech-экспертиза.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — generic outsourcing без собственной deep-tech IP; AI/Web3 как billable service, не как research.
2. Сеть/инвесторы: L — частная аутсорс-контора (FL); выходов на neurotech/quantum/consciousness-сеть нет.
3. Halo: L — CTO-роль в outsourcing-вендоре не усиливает scientific-brand ASRP, скорее снижает alt-профиль.
4. Партнёрский потенциал: L–M — мог бы поставлять инженеров на некритичные работы, но стратегического партнёрства не просматривается.
- **Вердикт двойной выгоды:** Низкая — легитимный 25-летний аутсорсер со следом во Львове, но нулевое пересечение с deep-tech-роадмапом ASRP; разве что как «запасной работодатель».

**Источники:** https://devcom.com (200), https://devcom.com/about/ (404 — SPA), https://devcom.com/career/ (200), https://jobs.dou.ua/companies/dev-com/ (200), https://jobs.dou.ua/companies/dev-com/reviews/ (200), https://en.wikipedia.org/wiki/DevCom (404).

---

### Dillo
**Due diligence (личное):**
- Что делают / вертика: IT staff augmentation + software outsourcing + «AI Agents» как сервис. Позиционирование: «senior engineers, low flat margin, 100% pricing transparency», «24–48h to first candidate CVs», «~35% below US hiring cost», «9 days request to signed offer». 21 анонимизированный case study (SaaS, FinTech, Healthcare, Banking, eCommerce, InsurTech, Manufacturing, Energy).
- Тип: Staffing intermediary / staff-augmentation agency (с outsourcing-рукавом). Не product company. Заявлен AI-Agents-сервис, но отдельные страницы `/ai-agents`, `/staff-augmentation`, `/why-dillo`, `/about`, `/get-in-touch` возвращают **404** — навигация ведёт на несуществующие страницы (частично сломанный WordPress на Apache/Ubuntu).
- Финансирование/размер/выручка: HQ Austin, TX (самозаявление). Founders/команда/выручка — не нашлось. На DOU страницы нет (404 для `/dillo/` и `/dillo-tech/`). Не на UK Companies House (US-юрлицо).
- Отзывы сотрудников/культура: не нашлось (нет DOU; Glassdoor/Kununu заблокированы).
- Red flags: (а) навигация сайта частично битая (404 на ключевые разделы) при заявленных «real US HQ» и «21 case study»; (б) основатели и юрлицо не раскрыты; (в) blog активный (последний пост 15.06.2026: AI-native SDLC, Claude Code, Angular→React) — контент реальный и компетентный, но это типичный thought-leadership рекрутерского агентства.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — собственной deep-tech IP нет; blog охватывает AI-SDLC на хорошем уровне, но это контент-маркетинг, не research-transfer.
2. Сеть/инвесторы: L — неизвестные основатели, no VC signal, нет выхода на neurotech/quantum-сеть.
3. Halo: L — ассоциация со staffing intermediary не усиливает CTO-репутацию ASRP.
4. Партнёрский потенциал: L–M — мог бы быть каналом найма senior-инженеров на ASRP-проекты (прозрачная модель маржи — плюс), но стратегического партнёрства нет.
- **Вердикт двойной выгоды:** Низкая — для CTO это скорее vendor найма, чем работодатель или стратегический партнёр; пересечения с deep-tech-роадмапом ASRP нет.

**Источники:** https://dillo.tech (200), https://dillo.tech/blog/ (200), https://dillo.tech/case-studies/ (200), https://dillo.tech/ai-agents/ (404), https://dillo.tech/staff-augmentation/ (404), https://dillo.tech/about/ (404), https://jobs.dou.ua/companies/dillo/ (404), https://jobs.dou.ua/companies/dillo-tech/ (404). Отброшенные омонимы: dillo.com (Texas auto insurance), dillo.ai (перевод жестового языка).

---

### Elevate Core
**Due diligence (личное):**
- Что делают / вертика: **не нашлось** — ни одного работающего сайта идентифицировать не удалось. `elevatecore.com` → 302-редирект на маркетплейс доменов `atom.com/name/ElevateCore` (домен выставлен на продажу); `elevatecore.org` → заглушка «Coming Soon»; `elevate-core.tech` → парковка Reg.ru («Домен не привязан к хостингу»); `.net`/`.ai`/`.dev`/`.io` — не резолвятся или пустые.
- Тип: unclear. В UK Companies House есть два свежих неродственных микрошелла: **ELEVATECORE LTD** (№16505212, инк. 09.06.2025, SIC 85590/85600 — Other education/Educational support services, 35a Kincaid Road, London SE15, **confirmation statement overdue**) и **ELEVATECORE SERVICES LIMITED** (№16003004, инк. 07.10.2024, SIC 63110/70229 — Data processing/Management consultancy, 89 The Avenue, Seaham SR7). Оба — типичные «картонные» UK-оболочки; ни сайт, ни сотрудники, ни продукт к ним не привязаны.
- Финансирование/размер/выручка: не нашлось.
- Отзывы сотрудников/культура: не нашлось (ни DOU, ни Wellfound, ни Glassdoor — ничего не проиндексировано).
- Red flags: Ни одного верифицируемого следа деятельности; домен выставлен на продажу; совпадение имён с UK-шеллами не доказывает, что это тот же бизнес. Либо компания настолько ранняя/непубличная, что не оставила цифрового следа, либо название в списке djinni не соответствует реальному юрлицу.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — продукт не подтверждён, нечего переносить.
2. Сеть/инвесторы: L — не идентифицированы.
3. Halo: L — никакой репутационной массы.
4. Партнёрский потенциал: L.
- **Вердикт двойной выгоды:** Низкая — нет верифицируемого контрагента, DD невозможно завершить.

**Источники:** https://elevatecore.com (302 → atom.com/name/ElevateCore — домен на продажу), https://elevatecore.org (200, заглушка «Coming Soon»), https://elevate-core.tech (200, парковка Reg.ru), https://find-and-update.company-information.service.gov.uk/company/16505212 (ELEVATECORE LTD, UK, инк. 2025-06-09), https://find-and-update.company-information.service.gov.uk/company/16003004 (ELEVATECORE SERVICES LIMITED, UK, инк. 2024-10-07).

---

### Friendly Technologies
**Due diligence (личное):**
- Что делают / вертика: B2B-вендор **carrier-grade платформы управления устройствами и IoT** (TR-069, TR-369/USP, LwM2M, OMA-DM, MQTT, CoAP), Wi-Fi-менеджмент для телекомов (Wi-Fi Management+, Friendly AI Assistant™ для автоматического разрешения проблем), embedded-клиенты для IoT-устройств, Smart Home. Клиенты — Jio, Orange, Bharti Airtel, Claro, Telcel, Windstream, Vodacom, Safaricom, Tata Play, Nordnet, Aussie Broadband, Coca-Cola, AGL и др. (500+ per сайту).
- Тип: Product company — собственная платформа, лицензии, партнёрская сеть. Не аутсорс.
- Финансирование/размер/выручка: частная, внешних раундов не раскрывает. Основатель/CEO — Ilan Migdal. Сайт заявляет «tens of millions of devices on a single platform» и «500+ customers». Точный headcount/выручка — не нашлось (Crunchbase/Glassdoor/Tracxn — 403/404). Frost & Sullivan Customer Value Leadership Award 2015. Действует с 2007.
- Отзывы сотрудников/культура: не нашлось (Glassdoor заблокирован; на DOU не присутствуют).
- Red flags: Существенных по самой компании не найдено. В прошлом — публичный отчёт Check Point о критических уязвимостях в TR-069 ACS-реализациях (Friendly упомянута как «нашла их у конкурентов», репутационно нейтрально). География: HQ New York (Friendly Technologies Inc.), R&D — Израиль (команда: Migdal, Greenberg, Braunstein, Kimchi и др.), офисы в Колумбии, Бразилии, Украине.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: M — есть «Friendly AI Assistant» (LLM/ML для диагностики Wi-Fi), Kubernetes-based orchestration, работа с большими потоками телеметрии; релевантно roadmap-оси AI-агентов ASRP, но доменно далеко (telecom device management, не KG/RAG в смысле ASRP).
2. Сеть/инвесторы: M — телеком-заказчики уровня Jio/Orange/Airtel; интереса к neurotech/quantum/consciousness не прослеживается.
3. Halo: M — узнаваемый нишевый лидер в TR-069/IoT Device Management (Frost&Sullivan), но не «deep-tech brand» в смысле ASRP.
4. Партнёрский потенциал: M — потенциальный канал для ASRP-платформ в telco/edtech; текущих пересечений нет.
- **Вердикт двойной выгоды:** Средняя — зрелая продукт-компания с реальной AI/ML/edge-инфраструктурой, но пересечение с roadmap ASRP (LLM-agents/education/neuro) только частичное.

**Источники:** https://www.friendly-tech.com/ (200), https://www.friendly-tech.com/about-us/ (200, команда, история с 2007), https://www.friendly-tech.com/contact/ (200, HQ New York, офисы LATAM/Бразилия/Украина), https://friendly-tech.com/page-sitemap.xml (200, логотипы клиентов).

---

### FuturiX Solutions
**Due diligence (личное):**
- Что делают / вертика: Аутсорс/IT-услуги — web/mobile development, blockchain (DeFi, dApp, smart contracts, crypto exchanges, payment systems, AML), DevOps (CI/CD), QA, IT-консалтинг. Портфолио: Change DEX (агрегатор свопов), QZL (смарт-контракт-аудит), Axoire (crypto wallet), ChangeBIT (AML), CryptoGalaxy, BotMart, LIMETTE (interior e-commerce), Scruffy (pet grooming marketplace), Conexus.
- Тип: Outsourcing vendor — клиентский цикл «idea → delivery», удалённые вакансии, явное позиционирование как сервис. Не продукт.
- Финансирование/размер/выручка: внешних инвестиций не нашлось. Сайт заявляет «5+ Years Of Expertise». Команда компактная (3 руководителя на сайте). Юрлицо: **FUTURIX IT CONSULTING LTD** (UK Companies House №15719593, инк. 14.05.2024, Farnham GU10, SIC 62020 — IT consultancy); **confirmation statement overdue** (должен был быть подан 27.05.2026).
- Отзывы сотрудников/культура: не нашлось (Glassdoor/DOU/Kununu — 0; на DOU не зарегистрированы).
- Руководство: CEO Mykhailo Zhmaitsev, CSO Valerii Borshchev, COO Viktor Zhernokleiev (украинские имена) → типичный украинский удалённый аутсорс с UK-оболочкой.
- Red flags: UK-шелл с просроченным confirmation statement; «5+ years» при юрлице 2024; бизнес-модель крипто-тяжёлая (DeFi/AML/DEX) — корреляция с regulated/high-risk сегментом; отсутствие верифицируемых отзывов и публичных клиентов с именами.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — стек React/Next/Nest/.NET/blockchain-generic; ничего собственного в LLM-agents/RAG/KG.
2. Сеть/инвесторы: L — публичных инвесторов/институтов нет.
3. Halo: L — body-shop без репутации в deep-tech.
4. Партнёрский потенциал: L — мог бы быть sub-contractor по веб-разработке, но не клиент/партнёр уровня ASRP.
- **Вердикт двойной выгоды:** Низкая — аутсорс без стратегической массы, репутационных точек касания с roadmap ASRP нет.

**Источники:** https://futurix.solutions/ (200), https://futurix.solutions/about-us (200, руководство), https://futurix.solutions/portfolio (200, кейсы), https://futurix.solutions/career (200, вакансии), https://find-and-update.company-information.service.gov.uk/company/15719593 (FUTURIX IT CONSULTING LTD, UK, инк. 2024-05-14, **confirmation overdue**).

---

### GR8_TECH
**Due diligence (личное):**
- Что делают / вертика: B2B iGaming / sportsbook platform vendor (бренд «GR8 Tech»). Ставочное/казино-ПО как услуга для операторов. Преемник **Parimatch Tech** (по DOU: «25.01.2023 — Почала працювати компанія GR8 Tech, яка стала наступницею Parimatch Tech»). Вакансии на DOU: Head of Office Admin, Media Buyer, Senior Full-Stack .NET Engineer (with Node.js & Go), QA Engineer, Risk & Anti-Fraud Operations Specialist (Casino), Middle Information Security Access Specialist.
- Тип: Product company (Tech Product per DOU) — собственная платформа, не аутсорс.
- Финансирование/размер/выручка: на DOU — **200–800 специалистов**, офисы **Cyprus, Moldova, Poland**. Точная выручка/инвесторы — не нашлось (Crunchbase 403). Гипотеза о происхождении от EveryMatrix **опровергнута** — это spin-off Parimatch Tech. По DOU: «13.03.2023 — втратила до 70% виторгу через санкції проти Parimatch» и «31.03.2023 — реструктуризація і скорочення майже 50% команди».
- Отзывы сотрудников/культура: страница на DOU существует (200), но числовой рейтинг не отображается без JS; есть публичный след сокращения ~50% команды в 2023.
- Red flags: Тяжёлая репутационная нагрузка — Parimatch был **санкционирован Украиной (РНБО, 10.03.2023)** за continued Russia-links; GR8 Tech как «наследница» унаследовала ~70%-е падение выручки и масштабный layoff. Зрелый iGaming-сегмент с compliance-рисками по лицензированию (UK GC, MGA, Curaçao и т.п.).

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — стек .NET/Node.js/Go, real-time betting data, anti-fraud ML; для LLM-agent/RAG/KG roadmap ASRP перенесёмого почти ничего нет.
2. Сеть/инвесторы: L — связь с Parimatch Group; интереса к deep-tech/neuro/quantum/consciousness не прослеживается.
3. Halo: L (скорее негативный) — ассоциация с санкционным контекстом и iGaming разрушит, а не усилит репутацию CTO ASRP в neuroscience/education.
4. Партнёрский потенциал: L — iGaming-сегмент не клиент/партнёр ASRP-roadmap.
- **Вердикт двойной выгоды:** Низкая — стратегического пересечения с роадмапом ASRP нет, репутационный профиль по происхождению от Parimatch-санкций токсичен для образовательной/научной миссии ASRP.

**Источники:** https://jobs.dou.ua/companies/gr8-tech/ (200 — 200–800 спец., Cyprus/Moldova/Poland, статьи о реструктуризации и санкционном ударе), https://gr8.tech (403, «Website Unavailable»), https://en.wikipedia.org/wiki/EveryMatrix (200, контекст iGaming B2B), https://en.wikipedia.org/wiki/Parimatch (200 — санкции РНБО Украины 10.03.2023, подтверждение origin).

---

### GameInspire
**Due diligence (личное):**
- Что делают / вертика: B2B-платформа для операторов онлайн-казино (iGaming). Модули: Casino Games, Payments, Betting, KYC/Anti-Fraud, Affiliate Management, CRM, Bonus System, Reporting & Analytics. Лицензия Curaçao (Antillechain N.V.). Заявленные метрики: 6M+ MAU, 250+ подключённых казино, 3500+ игр в портфеле.
- Тип: Product company (Tech Product per DOU) — собственная B2B iGaming-платформа, не аутсорс. Гипотеза «game-dev студия» **не подтверждается** — это gambling-tech, а не видеоигры.
- Финансирование/размер/выручка: 81–200 специалистов (DOU); зарегистрирована на DOU 08.05.2025 (очень свежая). Выручка/финансирование — не нашлось. WHOIS домена закрыт через WithheldforPrivacy (Iceland) — бенефициар анонимен.
- Отзывы сотрудников/культура: рейтинг на DOU отсутствует (нет голосов). Glassdoor/kununu — не нашлось.
- Red flags: (1) вертикаль — онлайн-гемблинг, этически конфликтует с миссией ASRP; (2) /news, /vacancies, /careers на сайте возвращают 404 — работает только лендинг и форма «Request a Demo»; (3) анонимный владелец домена, офшорная лицензия Curaçao; (4) не резидент Diia City.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — стек iGaming (платежи, KYC, бонусная аналитика, реалтайм) почти не пересекается с agent orchestration / RAG / KG / LLM-infra роадмапом ASRP.
2. Сеть/инвесторы: L — анонимный владелец, публичных deep-tech/neurotech/quantum инвесторов нет.
3. Halo: L — гемблинг-вертикаль репутационно вредит CTO нейронаучного холдинга.
4. Партнёрский потенциал: L — оператор казино не клиент и не партнёр ASRP.
- **Вердикт двойной выгоды:** Низкая — вертикаль iGaming прямо конфликтует с deep-tech/education/сознание-роадмапом ASRP.

**Источники:** https://gameinspire.com (200 — лендинг; /news, /vacancies, /careers — 404), https://jobs.dou.ua/companies/gameinspire/ (200), https://find-and-update.company-information.service.gov.uk/search/companies?q=gameinspire (200, совпадений нет), WHOIS gameinspire.com — NameCheap + WithheldforPrivacy (Iceland).

---

### Genius Match
**Due diligence (личное):**
- Что делают / вертика: Tech-staffing / outstaffing — подбор и встраивание инженеров (Software, DevOps, Cloud, Security, Data, AI) для US tech-компаний. Подрядчик работает в командах клиента (встраиваемая модель), контракт с Genius Match. Запущен собственный AI-продукт **Geni** (geni.geniusmatch.com) — assessment-инструмент для скоринга кандидатов по skills/experience/cultural fit; продаётся и клиентам. Case studies: Regent Education (enterprise financial-aid software), EdTech-клиент.
- Тип: Staffing intermediary / outstaffing (per DOU — именно Outstaffing). Гипотезы «dating-app» и «AI recruiting startup» частично сходятся: есть AI-продукт для рекрутинга, но ядро бизнеса — body-shop / staff augmentation.
- Финансирование/размер/выручка: 21–80 специалистов (DOU); на сайте заявляют «15+ years», «operations in 20+ countries», «100% retention», «7+ years average tenure», ISO/SOC2 practices. Внешнее финансирование / выручка / инвесторы — не нашлось (Crunchbase 403). На DOU с 24.10.2024.
- Отзывы сотрудников/культура: рейтинг на DOU отсутствует; Glassdoor — не нашлось (403).
- Red flags: (1) это intermediary — вы не employee end-client'а, а контрактник Genius Match (важно для визы/статуса); (2) «15+ years» на сайте vs. регистрация на DOU в 2024 — несъёмка (возможно моложе, либо ребрендинг); (3) не резидент Diia City; (4) юрисдикция/офис публично не раскрыты (UK Companies House не находит «GENIUS MATCH LIMITED» — только диссолвнутые тёзки).

**ASRP-ценность (4 оси):**
1. Тех-трансфер: M — Geni (LLM-based candidate scoring, anti-fake-resume) — реальный, хоть и узкий, AI-agent/assessment-продукт; контент про «AI-orchestration layer» и AI-enabled SDLC показывает методическую зрелость. Но core business — staffing, не инженерия.
2. Сеть/инвесторы: L — CEO/CTO Shaun Poulton (США), сильные украинские лидеры (Igor Stadniuchuk, Nataliia Guseinova, Helen Prashchur) и Elizabeth Jenkins (ex-Edgewater Federal Solutions / ManpowerGroup / Experis — federal contracting). Deep-tech/neuro/quantum-инвесторов не видно.
3. Halo: L — CTO рекрутингового агентства ослабляет «deep-tech CTO»-позиционирование Михаила.
4. Партнёрский потенциал: M — реалистичный канал найма engineers (cloud/data/AI) для ASRP-роадмапа; как стратегический партнёр — слабо.
- **Вердикт двойной выгоды:** Средняя — полезен как hiring-канал для инженерных ролей ASRP, но не стратегическое пересечение с deep-tech-миссией.

**Источники:** https://geniusmatch.com (200 — /why-us, /leadership, /careers, /case-study, /blog, /contact), https://jobs.dou.ua/companies/genius-match/ (200, классификация Outstaffing), https://find-and-update.company-information.service.gov.uk/search/companies?q=genius+match (200, прямого совпадения нет), https://www.linkedin.com/company/genius-match (существует, LinkedIn 403 для бота).

---

### GlobalLogic
**Due diligence (личное):**
- Что делают / вертика: Digital engineering / R&D services — аутсорс продуктовой разработки и IT-сервисов для software + hardware. Клиенты в automotive, healthcare, media, finance, telecom. Сильная engineering-культура: встраиваемые системы, cloud, AI/ML-сервисы для enterprise.
- Тип: Outsourcing vendor / services MNC (крупнейший глобальный digital-engineering игрок под крылом Hitachi). Per DOU — Service. Не product company.
- Финансирование/размер/выручка: Subsidiary of **Hitachi (TSE:6501)**. Аквизишн Hitachi в 2021 — **US$9.6B enterprise value** (Wikipedia, со ссылкой на пресс-релиз) / $9.5B EV (finsmes, 31.03.2021) — крупнейшая M&A в истории Hitachi на тот момент. В Украине **1500+ специалистов**, офисы в Киеве, Харькове, Львове, Николаеве; с 2022 команда в Украине выросла на 1000+; «Україна — найбільший хаб талантів у Європі» (интервью с Юлией Штукатуровой, главой Ukraine, 08.2025). Глобальный headcount исторически ~30k+ (но точной свежей цифры из открытых источников в этом заходе не получено — corporate-сайт блочит бота).
- Отзывы сотрудников/культура: DOU рейтинг **63/100** (65 голосов). Срез: Компенсація 51%, Умови праці 77%, Кар'єра 52%, Проєкт 68%, Корп. культура 50%, Соц. відповідальність 79%. Резидент **Diia City**. На DOU с 23.09.2009. Glassdoor — 403.
- Red flags: (1) рейтинг на DOU ниже среднего для топ-аутсорсеров (63/100, культура 50%, компенсация 51% — типичная «зрелая сервис-корпорация»); (2) services-модель — для CTO стартап-холдинга это «наёмный manager», а не owner-CTO; (3) смена CEO — назначен новый President & CEO (per Wikipedia; имя куратором отдельно не верифицировалось); (4) интеграция с Hitachi идёт (Sept 2025 — Hitachi купила немецкую synvert и влила в GlobalLogic) — орг. турбулентность.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: M — есть AI/ML, cloud, embedded practices и R&D-инфраструктура; переносимо частично (LLM-infra, data-pipelines, edge/embedded), но kernel — services, не product IP; agent orchestration / RAG / KG придётся тянуть своим усилием.
2. Сеть/инвесторы: H — Hitachi parent имеет Lumada, Hitachi Cambridge Laboratory (quantum computing research), Hitachi AI; прямой доступ к одной из крупнейших deep-tech-конгломераций Японии.
3. Halo: H — GlobalLogic + Hitachi на CV = enterprise-grade репутация и credibility на глобальном B2B.
4. Партнёрский потенциал: H — реальный кандидат на engineering-партнёрство для построения платформ ASRP (LLM-агенты, GFS forecasting, Arcanum12th); Hitachi как потенциальный strategic backer в deep-tech.
- **Вердикт двойной выгоды:** Высокая — Hitachi-backed digital engineering leader с реальной deep-tech-крышей и сильным halo; лучшая пара «личное занятость + стратегия ASRP» батча.

**Источники:** https://en.wikipedia.org/wiki/GlobalLogic (200 — redirect на https://en.wikipedia.org/wiki/Hitachi#GlobalLogic, секция слита с марта 2025), https://jobs.dou.ua/companies/globallogic/ (200 — рейтинг 63/100, 1500+ в Украине, Diia City), https://www.finsmes.com/?s=globallogic (200 — Hitachi To Buy GlobalLogic for EV of USD$9.5B, 31.03.2021; покупки Sidero 2023, Fortech 2022, ECS Group 2020), https://www.globallogic.com (302/empty — бот-блок).

---

### GoReel
**Due diligence (личное):**
- Что делают / вертика: B2B/B2C SaaS — AI-генератор «вирусных» TikTok-слайдшоу из текстового промпта, с авто-постингом, трендовой музыкой и хештегами. **Не iGaming** (гипотеза опровергнута) — это маркетинг-API поверх TikTok.
- Тип: Микро-product-company / инди-SaaS. Хостится на Vercel, лендинг на Next.js, OG-изображения лежат на `app.goreel.ai`. Никаких признаков команды/юрлица/инвесторов.
- Финансирование/размер/выручка: не нашлось. Публичных раундов/пресс-релизов нет. Монетизация — подписка $17 / $47 / $97 в месяц (Starter/Pro/Scale) с прайсинга на сайте. Домен `goreel.ai` зарегистрирован **2025-06-29** через GoDaddy с приватностью Domains By Proxy (возраст ≈ 1 год).
- Отзывы сотрудников/культура: не нашлось (нет DOU; Wellfound/Glassdoor/Crunchbase — 403).
- Red flags: (1) маркетинговые клики «Trusted by over 700 businesses» и «10,000+ Happy Users» ничем не подкреплены — X-аккаунт `@goreelai` создан в июле 2025, 0 постов, 0 подписчиков, био «Coming Soon»; (2) полное отсутствие верифицируемого юрлица, фаундеров, адреса, условий поддержки (только «24/7 Email Support»); (3) X-handle в `twitter:creator` указан как `@goreel` (не `@goreelai`) — небрежность брендинга; (4) типичный паттерн «инди/агентство-валидационный» продукт.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — prompt→slides + scheduling — маркетинг-автоматизация, не agent orchestration / RAG / KG / LLM infra ASRP-roadmap.
2. Сеть/инвесторы: L — сетевой след нулевой, инвесторов/советников не идентифицируется.
3. Halo: L — не даёт ни нейротех- ни educational-репутации CTO ASRP.
4. Партнёрский потенциал: L — клиентская база TikTok-маркетологи e-commerce, не deep-tech.
- **Вердикт двойной выгоды:** Низкая — продукт не пересекается с roadmap ASRP ни по одной из 4 осей, репутация компании неидентифицируема.

**Источники:** https://goreel.ai (307 → https://www.goreel.ai/, 200 — лендинг с описанием/прайсингом; og:title «GoReel - AI-Powered TikTok Slideshow Generator», twitter:creator `@goreel`), https://x.com/goreelai (200 — «Coming Soon · Joined July 2025 · 0 posts · 0 followers»), whois goreel.ai: Creation 2025-06-29, Registrar GoDaddy, Registrant «Domains By Proxy, LLC», https://find-and-update.company-information.service.gov.uk/search/companies?q=goreel (no results). Отброшенные омонимы: go-reel.com / goreel.co / goreel.tech (пустые/заглушки, не относятся к продукту).

---

### Graz.tech
**Due diligence (личное):**
- Что делают / вертика: Омниканальный ритех/e-commerce-интегратор — платформы для торговых центров (Evomall), PaaS для e-grocery/ресторанов/ритейла, WMS+dark-store, loyalty, мобильные приложения; отдельная практика — Cust-Dev (custom dev + аутстафф) и внедрение Odoo ERP. Заявленные клиенты: Lotok, Будинок Іграшок, Post.ua, Post-Int.com, Umico, Qarrib, Citrus, Moyo.
- Тип: Outsourcing vendor / consulting-and-implementation shop. На сайте прямо: «Cust-Dev services… offering end-to-end development and **outsourcing specialists**» — продажа человекочасов, не продукт.
- Финансирование/размер/выручка: не нашлось. Юрлицо не идентифицируется однозначно: домен `graz.tech` создан **2022-03-13** (≈4 года) через GoDaddy; контакты — `Info@graz.tech`, +380 67 433 44 33 (Украина, Kyivstar), +33 6 43 88 34 19 (Франция), адрес 5 Rue Des Mulhouse, 68300 Saint-Louis (Франция, рядом с Базелем). В SIRENE по этому адресу/названию — 0; в UK Companies House единственное совпадение «GRAZ TECHNOLOGIES LTD» (07296437) — dissolved в 2014, не та.
- Отзывы сотрудников/культура: не нашлось. На DOU slug `/companies/graztech/` редиректит в 404 — профиля нет.
- Red flags: (1) нет страниц команды/основателей (`/team`, `/about-us`, `/cases` — все 404); (2) полное отсутствие соцсетей (LinkedIn/IG/FB/YT) на лендинге; (3) юрлицо/owner/размер команды не идентифицируются; (4) testimonials без ссылок; (5) украинский телефон при французском адресе — типичный паттерн «украинский фриланс-кооператив с EU-фасадом».

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L–M — инженерия на уровне ERP/WMS/CMS/e-commerce (Odoo, Dark Store, PUDO); для roadmap ASRP (LLM agents / GFS / Arcanum12th / GMS) почти не переносимо; RAG/KG нет.
2. Сеть/инвесторы: L — публичных инвесторов/советников нет; клиенты — украинский/закавказский mass-retail, не deep-tech.
3. Halo: L — ритейл-интегратор без brand recognition в deep-tech; не усиливает CTO-репутацию ASRP.
4. Партнёрский потенциал: L — клиентская база не пересекается с neurotech/quantum/consciousness/education; ASRP им как заказчику не нужен.
- **Вердикт двойной выгоды:** Низкая — сфера (омниканальный ритех + Odoo-аутстафф) лежит вне deep-tech-роадмапа ASRP, а корпоративная прозрачность недостаточна для серьёзного partner-DD.

**Источники:** https://graz.tech/ (200 — лендинг «Omnichannel Solutions», модули Evomall / Odoo integrator / Cust-Dev, продукты PaaS E-Grocery/Restaurants/Retail/Mall), https://graz.tech/ua/ (200), https://graz.tech/sitemap.xml (модульные страницы; /team, /cases, /about-us отсутствуют), whois graz.tech: Creation 2022-03-13, Registrar GoDaddy, https://jobs.dou.ua/companies/graztech/ (301→404), https://recherche-entreprises.api.gouv.fr/search?q=Graz.tech (total_results: 0), https://recherche-entreprises.api.gouv.fr/search?code_postal=68300&q=graz (total_results: 0), https://find-and-update.company-information.service.gov.uk/search/companies?q=graz+tech (единственное совпадение GRAZ TECHNOLOGIES LTD 07296437 — Dissolved 2014-02-25).

---

## Сводная таблица (батч D–G)

| Компания | Тип | Двойная выгода ASRP | Главный вывод одной строкой |
|---|---|---|---|
| **Datagrok** | Product (научная data-platform, cheminformatics) | 🟢 **Высокая** | Единственная в батче с реальным пересечением deep-tech + KG + bio-med (VH тех-трансфер); но команда ≤20 и владельцы непрозрачны. |
| **Delasport** | Product (iGaming/sportsbook) | 🔴 Низкая | Сильная инженерия в Киеве (Java/Kafka/K8s), но gambling-вертикаль и betting-stack почти не пересекаются с миссией ASRP. |
| **Devcom** | Outsourcing vendor | 🔴 Низкая | Легитимный 25-летний аутсорсер (Lviv/FL), нулевое пересечение с deep-tech-роадмапом; «запасной работодатель». |
| **Dillo** | Staffing intermediary | 🔴 Низкая | Staff-aug агентство (Austin) с битым сайтом и нераскрытыми основателями; для CTO — скорее канал найма, чем работодатель. |
| **Elevate Core** | Unclear / не идентифицирован | 🔴 Низкая | Реальный оператор не идентифицирован — домен на продаже, только UK-шеллы-омонимы; DD невозможен. |
| **Friendly Technologies** | Product (IoT device mgmt, TR-069) | 🟡 Средняя | Зрелый нишевый лидер (Jio/Orange/Airtel) с AI/edge-инфраструктурой, но доменно далеко от ASRP. |
| **FuturiX Solutions** | Outsourcing (UK shell, крипто-тяжёлый) | 🔴 Низкая | Body-shop с UK-оболочкой 2024 и просроченной отчётностью; репутационной массы нет. |
| **GR8_TECH** | Product (iGaming, наследник Parimatch) | 🔴 Низкая | iGaming без пересечения с роадмапом + токсичный санкционный фон (Parimatch, РНБО 2023). |
| **GameInspire** | Product (iGaming B2B) | 🔴 Низкая | Свежая (2025) iGaming-платформа (Curaçao, анонимный владелец); вертикаль конфликтует с миссией ASRP. |
| **Genius Match** | Staffing / outstaffing | 🟡 Средняя | Body-shop, но есть AI-продукт Geni; полезен как hiring-канал для ASRP, стратегического пересечения нет. |
| **GlobalLogic** | Outsourcing / services MNC (Hitachi) | 🟢 **Высокая** | Hitachi-backed ($9.6B) digital engineering leader — лучший halo + доступ к Hitachi deep-tech-конгломерации; services-модель не owner-CTO. |
| **GoReel** | Микро-product (TikTok AI SaaS) | 🔴 Низкая | Годовалый (2025) инди-SaaS без юрлица/фаундеров; нулевое пересечение с роадмапом ASRP. |
| **Graz.tech** | Outsourcing / retail-integrator | 🔴 Низкая | Омниканальный ритех + Odoo-аутстафф без идентифицируемого юрлица (UA-телефон + FR-адрес); вне deep-tech. |

**Итог батча:** 2 «Высокая» (**Datagrok** — лучший тех-трансфер/science-fit; **GlobalLogic** — лучший halo/сеть через Hitachi), 2 «Средняя» (**Friendly Technologies**, **Genius Match**), 9 «Низкая». Батч сильно перекошен в iGaming (Delasport, GR8_TECH, GameInspire) и generic-outsourcing (Devcom, FuturiX, Graz.tech) — обе ниши дают минимальную двойную выгоду для deep-tech/education-миссии ASRP. Единственные два имени, заслуживающие приоритетного движения: **Datagrok** (прямое совпадение с bio-med/KG-осью, маленькая но научная команда) и **GlobalLogic** (engineering-партнёрство + стратегическая дверь в Hitachi).

**Слепые зоны (общие для батча):** отзывы сотрудников (Glassdoor/Clutch/Wellfound блочат ботов — 403) — главный верификационный пробел; кипрский реестр недоступен из окружения (влияет на GR8_TECH, Delasport); точный глобальный headcount/выручка GlobalLogic не извлечены (corporate-сайт блочит бота). Всё, что помечено «не нашлось», действительно не нашлось в первичных источниках — ничего не выдумано.
