# Deep-dive по компаниям (батч S–Z) — due diligence + стратегическая ценность для ASRP, 2026-07-21

Продолжение серии [company-deepdive-2026-07-21-aa.md](company-deepdive-2026-07-21-aa.md) (A–C), [company-deepdive-2026-07-21-ab.md](company-deepdive-2026-07-21-ab.md) (D–G), [company-deepdive-2026-07-21-ac.md](company-deepdive-2026-07-21-ac.md) (H–M) и [company-deepdive-2026-07-21-ad.md](company-deepdive-2026-07-21-ad.md) (N–S), в том же **объединённом формате**: для каждой компании одновременно личный DD (для трудоустройства Михаила Капустина) + оценка двойной выгоды для ASRP по 4 осям. Охват — 13 компаний из вакансий djinni.co (бренды на S–Z, плюс `softo.it` и кирилличное «Маркетинг-Партнер»).

**Заказчик:** Михаил Капустин, CTO и сооснователь ASRP (Advanced Scientific Research Projects) — холдинг в neuroscience / AI / consciousness research / quantum computing / биомед / образовании (Arcanum12th), зарегистрирован в Казахстане и США.
**Roadmap ASRP:** (a) LLM-агенты / multi-agent, (b) GFS forecasting-платформа, (c) Arcanum12th образовательная платформа, (d) GMS consciousness-платформа.
**Шкала осей:** L / M / H / VH. **Вердикт двойной выгоды:** Высокая / Средняя / Низкая — бар для «Высокая» = реальное пересечение с deep-tech/AI-agent/education/neuroscience/quantum-роадмапом ASRP (не просто «легитимный работодатель»). iGaming / gambling / crypto-grey вертикали = сильный негативный halo для neuroscience/education-миссии ASRP.

> **Методологическая оговорка (калибровка уверенности).** Встроенные поисковые тулы снова недоступны (WebSearch + web-reader MCP = HTTP 429; WebFetch нет). Весь ресёрч — **прямые fetch'и первичных источников через `curl`** (браузерный UA): официальные сайты, DOU-профили (`jobs.dou.ua/companies/<slug>` + `/reviews/`), UK Companies House (`find-and-update.company-information.service.gov.uk`), WHOIS (`whois.nic.io`), Wikipedia, GitHub API (`api.github.com/orgs/<org>/repos`), djinni-профили (`djinni.co/jobs/company-<slug>/`). Поисковые агрегаторы **Brave Search** и **Yahoo Search** (оба отдали 200 в этом батче) использовались как fallback для сниппетов Crunchbase/ZoomInfo/Clutch/Glassdoor/LinkedIn/D&B/Latka/RocketReach/ContactOut — сами эти сайты ботами блочатся 403. **REACHABLE:** tektelic.com, uvik.net, universium.io/.co, uasoftdev.com, visarsoft.de, volia-software.com, xpower.eu, zultys.com, marketing-partner.ua, djinni (все 13 slug'ов, кроме redirect-вариантов), DOU (tektelic, uasoftdev, universium, uvik-software, visarsoft, volia-software), api.github.com (TektelicCommunications, Uvik-Software, visarsoft), UK Companies House (trafficlabel → 05696710), en.wikipedia.org (Zultys), whois.nic.io (tridenx.io). **BLOCKED/403 (только через сниппеты):** crunchbase org, glassdoor, clutch, linkedin, softo.it (Cloudflare JS-challenge). **DOU-профиля нет (404):** sweeptech-igaming-solutions, tridenx, xpower (+ все slug-варианты), softo-it/softo, marketing-partner — эти работодатели рекрутят на djinni без verified DOU-страницы. **Что верифицировано надёжно:** продуктовое позиционирование и вертикаль (по оф. сайту/djinni-мете), класс/размер/дата-регистрации (DOU + Companies House), ownership/фаундеры (Companies House officers, Wikipedia, GitHub org), юр. юрисдикция (Companies House, WHOIS), подтверждение реального тех-стека через публичные GitHub-org'ы (TEKTELIC, Uvik). **Что НЕ удалось проверить точно:** суммы раундов/выручка частных компаний (Crunchbase блочит, Latka/RocketReach — неаудированные агрегаторы), рейтинги Glassdoor/Clutch (403 — только сниппеты). **Spot-check 5 ключевых заявлений выполнен прямым curl — все 5 подтверждены, галлюцинаций не обнаружено:** (1) Traffic Label Ltd → Companies House 05696710, Incorporated 3 Feb 2006, Active, SIC 73110 + 62020; (2) TridenX → WHOIS tridenx.io creation 2026-03-20, registrant org «Triden Solution LLC» (GE), Squarespace; (3) TEKTELIC → GitHub org: все публичные репо = LoRa/hardware-crypto (ecc608, helium-crypto-rs, gateway-rs, lora-packet), AI/LLM-артефактов нет; (4) Uvik Software → GitHub org «Senior Python & AI engineers… Django · FastAPI · React. Est. 2015», Estonia; (5) Zultys → Wikipedia: founded by Iain Milnes 2001, Chapter 11 ND Cal, активы куплены Pivot VoIP за $2.65M (окт. 2006). **Одна коррекция вердикта:** агент дал Zultys «Средняя» при осях L/L/M/L и собственном выводе «почти нулевое пересечение с deep-tech roadmap» — по бару паритета (как Playtech/N-iX-services в батче ad: сильный личный работодатель без roadmap-overlap) это **Низкая** двойной выгоды; в карточке вердикт исправлен. Ничего не выдумано; провалы помечены «не нашлось».

---

## Сводная таблица (батч S–Z)

| # | Компания | Тип | Двойная выгода ASRP | Главный вывод одной строкой |
|---|---|---|:--:|---|
| 1 | softo.it | Unclear (fintech/iGaming-бренд-оболочка) | **Низкая** | Opaque FX/crypto-брокерский бренд под Cloudflare (нет верифицируемого юрлица, серая ниша Asia/MENA) — репутационный риск, нулевой roadmap-overlap. |
| 2 | SweepTech iGaming Solutions | Product (iGaming, early-stage) | **Низкая** | CS2 skin-gambling startup (Gibraltar, 2025, ребрендинг→JAMTech, сайт не резолвится) — прямой негативный halo для neuroscience/education CTO. |
| 3 | TEKTELIC Communications | Product (LoRaWAN/IoT hardware) | **Средняя** | Calgary LoRaWAN-product (450+ клиентов, Kyiv R&D ~40) с вертикалью Digital Medicine — **стенд-аут батча:** единственный реальный biomed/sensor overlap для GMS-оси ASRP. |
| 4 | Traffic Label Limited | Product/service (iGaming media + casino operator) | **Низкая** | UK media-агентство + casino-operator (20 лет, Companies House 2006, SIC 73110+62020, ~75 чел.) — легитимный, но gambling halo. |
| 5 | TridenX | Outsourcing/staffing (crypto-FinTech, маскировка под «AI») | **Низкая** | Анонимная грузинская LLC (домен 2026-03, crypto-staffing) — молодая, opaque, красные флаги по всей линии. |
| 6 | Uasoftdev | Outsourcing/outstaffing | **Низкая** | Молодой UA staff-aug (≤20, бренд с 2025, bootstrap) — generic body-shop без deep-tech IP и сети. |
| 7 | Universium | Outsourcing/AI-first studio | **Средняя** | AI-first boutique (LLM, PhD-фаундеры) с тактическим tech-transfer M, но DOU-жалобы на ghosting/no-show — red flags по оперзрелости. |
| 8 | Uvik Software | Outsourcing (Python/AI boutique) | **Средняя** | Качественный Python/AI-бутик (Tallinn+Черновцы, 50+, 2015, GitHub-evidenced) — лучший «безопасный» tech-transfer на LLM/GFS-ось ASRP. |
| 9 | Visarsoft | Outsourcing (AI-native, DACH) | **Средняя** | AI-native немецкий подряд (Мюнхен/Львів, реальные CV/ML-вакансии, miltech-кейс) — тактический ML/CV-transfer + доступ к DACH-рынку. |
| 10 | Volia Software | Outsourcing/services (US) | **Низкая** | US services-vendor (Houston, 2003, 81–200) с маркетинговым «AI»-слоем, но без deep-tech R&D; **не путать** с telecom Volia. |
| 11 | Xpower | Product (нишевый dealer-ERP, BE) | **Низкая** | Бельгийский dealer-management ERP XDMS (с 1993) + HyperCharge spin-off (UA) — надёжный работодатель, нулевой roadmap-overlap. |
| 12 | Zultys | Product (UCaaS/VoIP) | **Низкая** | US UCaaS-product (SIP/MX, voice-LLM «AI Receptionist», ~$18.9M ARR) — сильный личный работодатель, но маргинальный overlap → Низкая двойной выгоды (исправлено). |
| 13 | Маркетинг-Партнер | Marketing agency + gambling/crypto product | **Низкая** | Киевское рекламное агентство (2004, ЄДРПОУ 32956490) + gambling/crypto-линейка через Прагу — не engineering-работодатель, нулевая ASRP-ценность. |

**Итог батча:** 4 из 13 — Средняя (TEKTELIC, Universium, Uvik Software, Visarsoft); 9 — Низкая; Высоких нет. Батч резко перекошен в негативную сторону: **5 из 13 (SweepTech, softo.it, Traffic Label, TridenX, Маркетинг-Партнер) — iGaming/gambling/crypto-grey вертикали**, все с Низкой двойной выгоды и прямым репутационным минусом для CTO нейро/AI/образовательного холдинга; **3 из 13 (Uasoftdev, Volia Software, Xpower)** — мелкий/средний generic services без deep-tech R&D. Положительное ядро — **кластер UA AI-флаворированных бутиков с реальным переносимым стеком**: Uvik Software (Python/AI, лучший «безопасный» tech-transfer), Universium (AI-first/LLM, но red flags), Visarsoft (CV/ML + DACH). **Единственный стенд-аут двойной выгоды — TEKTELIC** (H партнёрский потенциал): вертикаль Digital Medicine + носимые LoRaWAN-сенсоры + hardware-экспертиза напрямую прилегают к biomed- и GMS-consciousness-осям ASRP (сенсорный/физиологический мониторинг) — при том что LLM/agent-roадмап TEKTELIC не закрывает (GitHub: только LoRa/hardware-crypto). Это самый интересный стратегический кандидат батча, но на hardware/sensor-стороне, а не на LLM-стороне. Среди низкорисковых работодателей с наибольшим tech-transfer — **Uvik Software** (Python/AI, GitHub-подтверждённая идентичность, позитивная культура).

---

## Подробно по компаниям

### softo.it
**Due diligence (личное):**
- Что делают / вертикаль: По профилю на Djinni — fintech «продуктовая компания»: найм SMM, Influencer Marketing Manager (рынки Asia/MENA), Retention Manager (email/push через SendGrid/Mailchimp/OneSignal/Firebase), Full Stack Developer (Python+JS). Совокупность признаков (рынки Азии/MENA, online brokers/crypto/iGaming, retention-маркетинг, продвижение через инфлюенсеров) характерна для оффшорного ритейл-FX/crypto-брокера. Веб-сайт softo.it — под Cloudflare JS-challenge, контент для curl недоступен.
- Тип: Unclear — бренд-оболочка в FX/crypto-брокеридже без прозрачного юридического лица.
- Финансирование/размер/выручка: «не нашлось». На Djinni зарегистрирован с 2026 (новый профиль). В UK Companies House точного совпадения по «SOFTO.IT» нет (только побочные SOFTOART, SOFTO LIMITED). DOU-профиля нет.
- Отзывы сотрудников/культура (Glassdoor/DOU/kununu): «не нашлось» — нет DOU-профиля (404), Glassdoor/kununu не обнаружены.
- Red flags: (1) непрозрачная юрисдикция/владелец; (2) Cloudflare блокирует аудит сайта; (3) вся активность — retention/SMM/инфлюенсеры для Азии в нише brokers/crypto/iGaming = типичный профиль серого оффшорного оператора; (4) на рынке труда <1 года.

**ASRP-ценность (4 оси):**
1. Тех-трансфер (agent orchestration/RAG/knowledge graphs/LLM infra, переносимо ли на roadmap ASRP): **L** — единственная инженерная вакансия (full-stack Python+JS) закрывает retention-маркетинг, не AI-agent/LLM-infra; переносить нечего.
2. Сеть/инвесторы (кто за компанией, интерес к deep-tech/neurotech/quantum/consciousness): **L** — публичных инвесторов/deep-tech партнёров нет, beneficial owner скрыт.
3. Halo (усилит ли репутацию Михаила как CTO ASRP): **L (негативно)** — ассоциация CTO нейро/образовательного холдинга с серой fintech/iGaming-оболочкой скорее повредит репутации.
4. Партнёрский потенциал (клиент/партнёр ASRP): **L** — брокерские продукты не клиенты ASRP; партнёрство = репутационный риск.
- **Вердикт двойной выгоды:** Низкая — opaque fintech/iGaming-бренд без верифицируемого юрлица и с репутационным риском; для roadmap ASRP пользы нет.

**Источники:** `https://djinni.co/jobs/company-softo-it/` (200 — «На сайте с 2026», industry=fintech, 4 вакансии SMM/Influencer/Retention/Full-Stack), `https://softo.it/` (200, но Cloudflare JS-challenge — контент недоступен), `https://jobs.dou.ua/companies/softo-it/` и `/companies/softo/` (404 — DOU-профиля нет), `https://find-and-update.company-information.service.gov.uk/search/companies?q=softo` (200 — точного совпадения нет), Brave/Yahoo search по «softo.it» (точного совпадения для бренда нет).

---

### SweepTech iGaming Solutions (в 2025 ребрендинг → JAMTech iGaming Solutions)
**Due diligence (личное):**
- Что делают / вертикаль: B2C iGaming-стартап — собственная SaaS Game & Entertainment Platform на стыке CS2 skin-gambling и онлайн-казино; строят in-house крипто-платёжный процессинг, anti-fraud, CRM/retention, аналитику игроков. Вертикаль — чистый гемблинг/гейминг.
- Тип: Product company (собственная платформа, не аутсорс), раннее-stage стартап.
- Финансирование/размер/выручка: Позиционируют себя как «well-funded iGaming startup». Точный раунд/инвесторы/выручка не нашлись (CB Insights: основана 2025, Gibraltar, без цифр финансирования). Размер команды малый (RocketReach показывает единичных сотрудников: Artem Trofymenko — Compliance Adviser, Bohdan Khudo — QA); на Djinni ~6–10 открытых вакансий (Data Analyst, Payments Eng, CRM Manager, Anti-Fraud, PixiJS Front-end) — активно нанимают в Киеве удалённо.
- Отзывы сотрудников/культура (Glassdoor/DOU/kununu): «не нашлось». Профиль на DOU — 404. Glassdoor-страницы нет. Перки из вакансий: 29 дней отпуска + оплачиваемые sick leave, 200 EUR/год на курсы, корпоративное оборудование.
- Red flags: (1) CS2 skin-gambling — высокорисковый регуляторный сегмент (Valve неоднократно преследовал skin-gambling-сайты); (2) ребрендинг SweepTech→JAMTech через <1 год — нет устоявшегося бренда; (3) юрлицо в Gibraltar (оффшорная гемблинг-юрисдикция) при найме в Украине удалённо — вопросы по трудовой защите; (4) собственный сайт не работает на момент проверки (jamtech.gg — DNS failure, sweeptech.io/jamtech.co — пустые/паркованные); (5) нет публичных отзывов — культуру валидировать невозможно.

**ASRP-ценность (4 оси):**
1. Тех-трансфер (agent orchestration/RAG/knowledge graphs/LLM infra, переносимо ли на roadmap ASRP): **L** — стек узко-гемблинговый (крипто-платежи, anti-fraud, PixiJS-игровой фронт, CRM/retention); AI-работа сводится к BI (LTV/cohort/retention, A/B), не к LLM-агентам/RAG/KG. На roadmap ASRP не переносимо.
2. Сеть/инвесторы (кто за компанией, интерес к deep-tech/neurotech/quantum/consciousness): **L** — инвесторы не раскрыты («well-funded» без имён); Gibraltar-гемблинг-инвесторы не пересекаются с deep-tech/AI/нейро/квантовой экосистемой.
3. Halo (усилит ли репутацию Михаила как CTO ASRP): **L (негативно)** — связка CTO нейро/AI/education-холдинга с CS2 skin-gambling брендом противоречит миссии Arcanum12th и нейро-направлению.
4. Партнёрский потенциал (клиент/партнёр ASRP): **L** — платформа не потребляет ни нейро-, ни квантовые, ни education-продукты; AI-задачи закрываются стандартной BI/Python-аналитикой без внешних партнёров.
- **Вердикт двойной выгоды:** Низкая — чистый iGaming/skin-gambling стартап без пересечения с deep-tech/AI-agent/education/нейро roadmap ASRP, плюс прямой репутационный негатив для CTO ASRP.

**Источники:** `https://djinni.co/jobs/company-sweeptech-igaming-solutions/` (200 — meta «trusted, next-gen gambling platforms», ~10 вакансий со стеком Node.js/Web3, PixiJS, Payments, Data Analyst SQL/BigQuery/Python), Yahoo-сниппеты: cbinsights.com/company/jamtech-igaming-solutions (founded 2025, Gibraltar), gi.linkedin.com/company/jamtech-igaming-solutions (ребрендинг SweepTech→JAMTech, «skin gaming and entertainment»), rocketreach.co/jamtech-igaming-solutions (имена сотрудников), `https://jobs.dou.ua/companies/sweeptech-igaming-solutions/` (404), `https://jamtech.gg` (DNS failure), `https://jamtech.co`/`https://sweeptech.io` (200, но контент пустой/паркованный).

---

### TEKTELIC Communications
**Due diligence (личное):**
- Что делают / вертикаль: Канадская продуктовая компания (Calgary, с 2009), лидер LoRaWAN® IoT — разрабатывает и продаёт gateway'и (линейка KONA: Macro/Mega/Enterprise/Micro/Photon/Strand/Mobile), сенсоры, network-сервер и end-to-end решения для Smart Buildings/Facility Management, Asset/Personnel Tracking, Smart Metering и **Digital Medicine / Medical IoT**. 450+ заказчиков по миру; Kyiv R&D-офис (~40 чел.).
- Тип: Product company (tech product, NAICS 517 — Telecommunications). На DOU — «Tech Product».
- Финансирование/размер/выручка: ~119 сотрудников (ContactOut), 81–200 (DOU). **Открытых данных о раундах финансирования не нашлось** — crunchbase/parsers.vc/wellfound/prnewswire ничего не подтверждают (wellfound 403, parsers.vc 404). Похоже на самоокупаемую приватную компанию без VC.
- Отзывы сотрудников/культура (Glassdoor/DOU/kununu): DOU — 2 отзыва, оба очень положительные (Marketing Manager ~4 года; Lead Gen Team Lead). Плюсы: дружный киевский офис ~40 людей, Well-being-программа ($250/год на спорт/психолога/масаж), гибкий график, поездки в Calgary, открытость к AI-инструментам. Glassdoor/kununu — не найдено.
- Red flags: **Не є резидентом Diia City** (DOU) — для личной занятости в Украине это классический налоговый формат. Открытых фин. цифр нет. Иных red flags не найдено.

**ASRP-ценность (4 оси):**
1. Тех-трансфер (agent orchestration/RAG/knowledge graphs/LLM infra, переносимо ли на roadmap ASRP): **L** — стек LoRaWAN-firmware (Rust, C), gateway hardware, packet decoders; в `github.com/TektelicCommunications` 7 публичных репо — всё про IoT-радио и аппаратный crypto (ecc608, helium-crypto-rs, gateway-rs, lora-packet). LLM/agent/RAG/KG-артефактов нет — переносить на LLM-agent/GFS roadmap почти нечего (spot-check'ом подтверждено).
2. Сеть/инвесторы (кто за компанией, интерес к deep-tech/neurotech/quantum/consciousness): **L** — видимых раундов нет; партнёры AWS IoT Core for LoRaWAN, Blynk (smart-building, 2025-11), Helium network. Ссылок на neuro/quantum/VC-deep-tech не найдено.
3. Halo (усилит ли репутацию Михаила как CTO ASRP): **M** — признанный global LoRaWAN-бренд (450+ клиентов, линейка KONA, MWC-анонсы как SEAL wearable GPS) — добавит репутации в hardware/IoT, но не в AI/deep-tech.
4. Партнёрский потенциал (клиент/партнёр ASRP): **H** — реальный overlap по оси biomed-sensing / GMS: вертикаль «Digital Medicine» (носимые LoRaWAN-сенсоры, remote patient monitoring) и hardware-экспертиза напрямую релевантны сенсорной части ASRP (биомед/нейро-мониторинг, GMS). Возможен пилот по интеграции биометрических датчиков через LoRaWAN-инфру.
- **Вердикт двойной выгоды:** Средняя — прочная продуктовая компания с **единственным в батче реальным hardware/sensor overlap для biomed-оси ASRP** (Digital Medicine + носимые сенсоры → GMS), но не покрывает LLM/agent-roemap и не даёт deep-tech-сети; стенд-аут батча на sensor-стороне.

**Источники:** `https://tektelic.com/about-us/` (200 — LoRaWAN, Digital Medicine, Calgary, 2009), `https://tektelic.com/products/` (200 — линейка KONA), `https://jobs.dou.ua/companies/tektelic/` (200 — 81–200, Киев+Калгари, НЕ Diia City, Tech Product), `https://jobs.dou.ua/companies/tektelic/reviews/` (200 — 2 положительных отзыва, офис ~40), `https://djinni.co/jobs/company-tektelic-communications/` (200 — 450+ клиентов, 15+ лет, Well-being $250/год), `https://api.github.com/orgs/TektelicCommunications` + `/repos` (200 — 7 репо, всё LoRa/hardware-crypto, **AI/LLM нет**), Yahoo-сниппеты blynk.io/blog (партнёрство Blynk×TEKTELIC 2025), einnews pr_news 618563153 (носимый SEAL GPS на MWC), contactout.com/company/tektelic-5182104 (119 сотрудников, NAICS 517). НЕ НАЙДЕНО: Wikipedia (404), crunchbase, wellfound (403), цифры финансирования/выручки.

---

### Traffic Label Limited
**Due diligence (личное):**
- Что делают / вертикаль: UK-registered digital media / affiliate-маркетинг со специализацией на iGaming — «connect casino brands with the right audience» через SEO, PPC, analytics. По собственному заявлению также operates as a casino operator («managing affiliate programs and casino brands») — двойная роль: и affiliate, и оператор казино-брендов. Вертикаль — iGaming-маркетинг + casino operations.
- Тип: Product/service company (media-агентство + casino operator), не аутсорс-разработка и не staffing.
- Финансирование/размер/выручка: ~75 сотрудников (собственный сайт). Выручка/финансирование не нашлись — private UK-компания, abbreviated accounts. Incorporation: **3 февраля 2006** (≈20 лет), Company number **05696710**, SIC **73110 (Advertising) + 62020 (IT consultancy)** (spot-check'ом подтверждено: статус Active, регулярные CS01/AA filings — компания комплаентна).
- Отзывы сотрудников/культура (Glassdoor/DOU/kununu): Glassdoor — 5/5, но 1–2 отзыва (один из офиса в Киеве → подтверждает Kyiv-присутствие). Kununu — не нашлось. DOU — не нашлось. Выборка слишком мала для уверенного вывода о культуре.
- Red flags: (1) вертикаль — iGaming affiliate + казино-оператор (миссия расходится с ASRP); (2) активный Kyiv-найм при UK-юрисдикции — вопросы трудовых protections; (3) beneficial owners (PSC) — media-предприниматели без deep-tech-фона; (4) 7 исторических resignations officers при 10 current — для 20-летней компании норма, но признак нескольких restructuring-волн.

**ASRP-ценность (4 оси):**
1. Тех-трансфер (agent orchestration/RAG/knowledge graphs/LLM infra, переносимо ли на roadmap ASRP): **L** — стек SEO/PPC/analytics/WordPress-маркетинг-site; AI/ML/LLM-инфраструктуры нет, переносимых engineering-активов практически нет.
2. Сеть/инвесторы (кто за компанией, интерес к deep-tech/neurotech/quantum/consciousness): **L** — основатель Oded KEINAN (Director, английский резидент), Tobias MEHRING (Director, British) — media/marketing-предприниматели; PSC-структура без deep-tech syndicate; публичных сигналов интереса к neurotech/quantum/AI-agents нет.
3. Halo (усилит ли репутацию Михаила как CTO ASRP): **L (негативно)** — связка с casino-operator/affiliate-брендом прямо противоречит нейро/education-миссии ASRP и Arcanum12th.
4. Партнёрский потенциал (клиент/партнёр ASRP): **L** — casino-affiliate marketing не нуждается в LLM-агентах/RAG/GFS/нейро-инструментах ASRP; MarTech закрывается стандартными SEO/PPC-инструментами.
- **Вердикт двойной выгоды:** Низкая — 20-летний легитимный UK media/iGaming-affiliate + casino-operator без тех/стратегических пересечений с deep-tech roadmap ASRP, с прямым негативным halo для CTO нейро/образовательного холдинга.

**Источники:** `https://find-and-update.company-information.service.gov.uk/company/05696710` (200 — Company 05696710, «Level One, 86 Queens Road, Buckhurst Hill, England, IG9 5BS», Active, SIC 73110+62020, Incorporated 3 Feb 2006), `/company/05696710/officers` (200 — 10 current / 7 resignations; Oded KEINAN Director appointed 3 Feb 2006, Tobias Jonathan MEHRING Director appointed 13 Oct 2017, Rebecca KEINAN Secretary), `/company/05696710/filing-history` (200 — регулярные CS01+AA), `https://www.trafficlabel.com/` (200 — «multi-channel media agency… 75 team members… started 2006… operates as a casino operator, managing affiliate programs and casino brands»), Glassdoor UK Overview (через Yahoo-сниппет, прямой 403 — «5/5, 1 review», страница «Reviews in Kyiv» → подтверждает Kyiv-офис).

---

### TridenX
**Due diligence (личное):**
- Что делают / вертикаль: На сайте tridenx.io и в вакансиях позиционируется как «engineering partnership» / IT-outsourcing — Product Strategy/Design, **AI/Intelligence Engineering (ML/LLM/data)**, Software Product Development, Digital Transformation, Cloud DevOps, Quality Engineering. Реально активный подряд — staffing для B2B **криптовалютных/FinTech-проектов**: на djinni открыты «Senior System Administrator (B2B-криптовалютный проект)» и «Senior Full-Stack Engineer (Crypto/FinTech)». Клиентов не раскрывает.
- Тип: По классу — **outsourcing/staffing vendor для crypto-FinTech**, замаскированный под «продуктовую компанию» (на djinni помечена как «Продуктова компанія», но размещает подряд на чужие продукты).
- Финансирование/размер/выручка: «не нашлось». Никаких цифр фонда/выручки/количества сотрудников в открытых источниках нет. LinkedIn-страницы компании не обнаружено.
- Отзывы сотрудников/культура (Glassdoor/DOU/kununu): «не нашлось» — DOU нет, Glassdoor нет, kununu нет. Единственное «свидетельство» — тексты самих вакансий на djinni.
- Red flags: **множественные.** (1) Домен `tridenx.io` зарегистрирован **2026-03-20** (~4 месяца назад, Squarespace Domains, spot-check'ом подтверждено) — крайне молодая структура; (2) WHOIS registrant organization: **«Triden Solution LLC»**, country **GE (Грузия)** — рассинхрон с «TridenX Solutions LLC» в маркетинге; (3) основной сайт — single-page Vite/React shell без контента в HTML, без blog/portfolio/team page; (4) на djinni только с 2026; (5) анонимные фаундеры, без LinkedIn-присутствия; (6) реальный подряд — крипто/B2B-инфраструктура (обменники?), что в украинском аутсорс-контексте часто сигнализирует о серых заказчиках.

**ASRP-ценность (4 оси):**
1. Тех-трансфер (agent orchestration/RAG/knowledge graphs/LLM infra, переносимо ли на roadmap ASRP): **L** — несмотря на обещания «AI Intelligence Engineering, ML/LLM», никаких публичных артефактов (open-source, case studies, техноблога) нет — маркетинговая декларация без подтверждения. Реальный стек в вакансиях — Linux L3/Ansible/Nginx/PostgreSQL для crypto-инфраструктуры; к roadmap ASRP не переносится.
2. Сеть/инвесторы (кто за компанией, интерес к deep-tech/neurotech/quantum/consciousness): **L** — инвесторов/советников/партнёров публично нет; грузинская LLC без раскрытия beneficial owners.
3. Halo (усилит ли репутацию Михаила как CTO ASRP): **L (отрицательный риск)** — ассоциация с молодой анонимной крипто-staffing-структурой скорее ослабит, чем усилит репутацию deep-tech/нейро-CTO.
4. Партнёрский потенциал (клиент/партнёр ASRP): **L** — клиенты крипто-FinTech (по вакансиям), заказчиков в биомед/AI/нейро/education нет; совпадений по вертикали не просматривается.
- **Вердикт двойной выгоды:** Низкая — молодая анонимная грузинская LLC с замаскированным под «AI» крипто-staffing'ом, без подтверждённой экспертизы или сети; для личной занятости и для ASRP-партнёрства интереса практически не несёт.

**Источники:** `https://tridenx.io/` (200 — single-page React/Vite shell, только `<title>TridenX Solutions LLC</title>`, в HTML пусто), `https://djinni.co/jobs/company-tridenx/` (200 — профиль «TridenX», на сайте с 2026, услуги + 2 вакансии Senior SysAdmin B2B-крипто и Senior Full-Stack Crypto/FinTech), `whois -h whois.nic.io tridenx.io` (creation 2026-03-20T07:39:53Z, registrant org «Triden Solution LLC», country GE, registrar Squarespace Domains), Yahoo-поиск «TridenX company» (brand уникален; другие Trident-компании — судостроение/металлы/Trident Gum/TriNetX healthcare/Trinetix — нерелевантны), Yahoo «"TridenX Solutions LLC" founder OR CEO site:linkedin.com» — ничего (LinkedIn-страницы нет). НЕ НАЙДЕНО: основатели, дата основания, размер, выручка, инвесторы, отзывы, portfolio/case study.

---

### Uasoftdev
**Due diligence (личное):**
- Что делают / вертикаль: Staff augmentation и dedicated development teams — placement senior-разработчиков (в основном украинцев, локация EU) в продуктовые команды малых и средних компаний UK/EU/US. Слоган «a vetted engineer in 60 hours».
- Тип: Outsourcing/staff-augmentation vendor (founder-led body-shop). На DOU основной бизнес — «Outstaffing».
- Финансирование/размер/выручка: ≤20 специалистов (DOU); сайт (бренд UASOFTDEV) опубликован 2026-01-20, на DOU зарегистрированы 31.03.2025 — молодой бренд. CEO Aleksey Pavlishen (13 лет B2B-sales, 5 лет в staff-aug), CTO Alexander Shutalyov. Финансирование/выручка «не нашлись» (bootstrapped).
- Отзывы сотрудников/культура (Glassdoor/DOU/kununu): На DOU 2 отзыва (контент не извлекается без JS). На Clutch — 10 verified client-отзывов (Yahoo-сниппет), профиль подтверждён; также листинги на GoodFirms и Krowdbase. Внутренней культуры Glassdoor/kununu нет.
- Red flags: Очень молодой бренд (сайт от 2026-01, DOU от 03-2025); **не резидент Diia City**; бутиковый масштаб (≤20 чел); публичной фин. информации нет. Серьёзных red flags не найдено, но и подтверждённой трек-записи глубже 1 года нет.

**ASRP-ценность (4 оси):**
1. Тех-трансфер (agent orchestration/RAG/knowledge graphs/LLM infra, переносимо ли на roadmap ASRP): **L** — стек широкий (Python/Django/FastAPI, Node, PHP, Java, Scala, .NET, React/Vue/Angular, Flutter/RN, AWS/Azure/GCP, K8s, Terraform, упоминания OpenAI и Anthropic Claude в schema.org), но это generic staff-aug — глубокой agent orchestration/RAG/KG-инфры в портфеле не видно.
2. Сеть/инвесторы (кто за компанией, интерес к deep-tech/neurotech/quantum/consciousness): **L** — bootstrapped founder-led shop, внешних инвесторов / deep-tech-связей не обнаружено.
3. Halo (усилит ли репутацию Михаила как CTO ASRP): **L** — нет публичной репутации в deep-tech/AI/neuro.
4. Партнёрский потенциал (клиент/партнёр ASRP): **L** — теоретически закрывают generic-инженерные дыры, но не клиенты и не технологические партнёры.
- **Вердикт двойной выгоды:** Низкая — типичный украинский staff-aug начального уровня без deep-tech IP и без стратегической сети.

**Источники:** `https://uasoftdev.com` (200 — schema.org JSON-LD: CEO Aleksey Pavlishen, CTO Alexander Shutalyov, услуги, tech-stack incl. OpenAI/Anthropic Claude, addressCountry UA), `https://jobs.dou.ua/companies/uasoftdev/` (200 — «до 20 спеціалістів», «Зареєстрована 31.03.2025», «Outstaffing», «Не є резидентом Diia City»), `https://djinni.co/jobs/company-uasoftdev/` (200 — активная найм-активность), Yahoo-сниппет clutch.co/profile/uasoftdev (10 verified reviews), GoodFirms/Krowdbase listings.

---

### Universium
**Due diligence (личное):**
- Что делают / вертикаль: AI-first product development studio — help founders «vet talent, build your app, and spin off a standalone team». Позиционируются как «Top-rated team to build your AI product», упор на LLM и deep learning, основатели с PhD. Услуги: founder-led engineering, contract-to-hire, design.
- Тип: Hybrid product-development/staff-aug studio с AI-фокусом (на DOU — «Startup»).
- Финансирование/размер/выручка: В собственном ответе на DOU заявляют: проект основан 2016 (первый домен universium.solutions), .co с 2019, US-регистрация с 2020. На DOU «до 20 спеціалістів», но в свежем djinni-posting (2026-07-03) сами пишут «30 members at the moment». Финансирование/выручка «не нашлись». Заявляют «Trusted by 50+ founders on Clutch» (self-claim, Clutch напрямую не читается — Cloudflare).
- Отзывы сотрудников/культура (Glassdoor/DOU/kununu): На DOU 3 отзыва, минимум 2 негативных: кандидат не дождался ответственного за интервью (no-show без warning); другой прошёл 3 этапа и потом месяц не получал фидбэка («завтра будет») — компания публично признала ошибку. Glassdoor/kununu нет.
- Red flags: Несоответствие масштаба (DOU «до 20» vs djinni «30 members»); неоднозначная юрисдикция (сайт 2016, но LinkedIn-публикации моложе 11 мес по комментарию на DOU); зафиксированы кейсы непрофессионального рекрутинга (no-show, ghosting) — concern по операционной зрелости; **не резидент Diia City**.

**ASRP-ценность (4 оси):**
1. Тех-трансфер (agent orchestration/RAG/knowledge graphs/LLM infra, переносимо ли на roadmap ASRP): **M** — реальный AI-first-фокус, стек (Python + TypeScript/React/Node/GCP, Playwright/Puppeteer, Jest; вакансия QA Automation с Python) и заявки на LLM + deep learning от людей с PhD — это ближе к roadmap ASRP (LLM-агенты), чем у обычного body-shop. Но портфолио публично не раскрыто, верифицировать глубину agent-инжиниринга не удалось.
2. Сеть/инвесторы (кто за компанией, интерес к deep-tech/neurotech/quantum/consciousness): **L** — заявка на 50+ основателей-клиентов = сеть в startup-SaaS, не в deep-tech/neuro/quantum; investor backing не обнаружен.
3. Halo (усилит ли репутацию Михаила как CTO ASRP): **L** — репутация подмочена конкретными негативными отзывами на DOU (ghosting/no-show); усилитель слабый.
4. Партнёрский потенциал (клиент/партнёр ASRP): **M** — могли бы быть полезным исполнителем для прототипирования LLM-фич ASRP / Arcanum12th при tight scope и short-batch engagement (contract-to-hire у них заточен); как клиент — нет.
- **Вердикт двойной выгоды:** Средняя — AI-first-позиционирование совпадает с roadmap ASRP по LLM, и возможен тактический контракт на разработку, но стратегической deep-tech сети/IP или halo нет, плюс red flags по операционной зрелости (ghosting).

**Источники:** `https://universium.io` и `https://www.universium.co` (200 — og-content «Top-rated team to build your AI product», «AI-first», «Founder-led», «Contract-to-hire», «Ph.D. degrees behind our backs, tap into LLM and deep learning», «Trusted by 50+ founders on Clutch»), `https://jobs.dou.ua/companies/universium/` (200 — «до 20 спеціалістов», «Зареєстрована 29.01.2019», «Startup», «Не є резидентом Diia City»), `https://jobs.dou.ua/companies/universium/reviews/` (200 — 3 отзыва; 2 негативных no-show/ghosting + официальный ответ компании с извинениями; комментарий о whois .co 2019 и US-регистрации с 2020), `https://djinni.co/jobs/company-universium/` (200 — JSON-LD вакансии «Exceptional QA Automation Engineer (Python)» от 2026-07-03: Python+TS+React+Node+GCP+Playwright; цитата «rapidly growing team (30 members at the moment)»).

---

### Uvik Software
**Due diligence (личное):**
- Что делают / вертикаль: Python-first staff augmentation — embed senior Python/AI-ML/Data/DevOps/full-stack инженеров в продуктовые команды клиентов US/UK/EU. Фокус: Django/Flask/FastAPI, Data Engineering, Data Analytics, прикладные AI/DS-задачи. Дев-офис в Черновцах.
- Тип: Outsourcing/staff-augmentation vendor (engineer-led, узкоспециализированный Python boutique).
- Финансирование/размер/выручка: Основана 2015, HQ Tallinn (Estonia) + коммерческий офис Ipswich (UK). 50+ специалистов (собств. копирайт), DOU — «21–80 спеціалістов». Основатели — ветераны из IBM, EPAM, Prezi. Финансирование/выручка «не нашлись» (bootstrap).
- Отзывы сотрудников/культура (Glassdoor/DOU/kununu): DOU — 7 отзывов, все позитивные: «хороший коллектив», «выдают новую технику (мак, монитор)», «удалённая работа налажена», «практически отсутствует бюрократия», «современный стек», «открыто дают фидбэк». TechBehemoths 5/5 (3 отзыва). Wikidata Q139900139 подтверждает профиль.
- Red flags: Узкий фокус (только Python-экосистема) — для одних плюс, для других ограничение; **не резидент Diia City** (юр. HQ в Эстонии); публичных данных о выручке/инвесторах нет. Серьёзных red flags нет.

**ASRP-ценность (4 оси):**
1. Тех-трансфер (agent orchestration/RAG/knowledge graphs/LLM infra, переносимо ли на roadmap ASRP): **M→H** — реальный Python/AI/ML-стек + Data Engineering прямо пересекается с LLM-agent- и GFS-forecasting-дорожкой ASRP (Django/FastAPI — типовой backend для LLM-сервисов; Data Eng. — для RAG/knowledge graphs). Живой GitHub-org `Uvik-Software` (spot-check'ом подтверждено: «Senior Python & AI engineers… Django · FastAPI · React. Est. 2015», Estonia) — подтверждение технической идентичности. Переносимо.
2. Сеть/инвесторы (кто за компанией, интерес к deep-tech/neurotech/quantum/consciousness): **L** — bootstrapped boutique без deep-tech/neuro/quantum-сети; клиенты в основном SaaS/product в US/UK.
3. Halo (усилит ли репутацию Михаила как CTO ASRP): **L** — хорошая репутация в Python-сообществе UA, но не deep-tech halo.
4. Партнёрский потенциал (клиент/партнёр ASRP): **M** — реалистичный исполнитель для Python/AI-компонент ASRP (LLM-оркестрация, RAG-pipeline, data-аналитика) — можно интегрировать быстрее, чем набирать in-house; как клиент — нейтрально.
- **Вердикт двойной выгоды:** Средняя — узкий, но качественный Python/AI-бутик с проверенной культурой и тех-пересечением с roadmap ASRP; тактически полезен как extension-команда, стратегической сети/IP не даёт.

**Источники:** `https://uvik.net` (200 — title «Hire Senior Python & AI Engineers | Uvik Software»), `https://uvik.net/about-us/` (200, Yahoo-сниппет — «engineer-led staff augmentation founded in 2015, HQ Tallinn Estonia, commercial office Ipswich UK», «founded by engineering veterans from IBM, EPAM, and Prezi»), `https://jobs.dou.ua/companies/uvik-software/` (200 — «21–80 спеціалістов», Черновцы, «инженерная команда 50+», Python/Django/Flask/FastAPI/Data/AI-DS, SaaS/data-платформы), `https://jobs.dou.ua/companies/uvik-software/reviews/` (200 — 7 позитивных отзывов), `https://api.github.com/orgs/Uvik-Software` (200 — location Estonia, blog uvik.net, «Senior Python & AI engineers… Django · FastAPI · React. Est. 2015», 3 публичных репо), `https://djinni.co/jobs/company-uvik-software/` и `company-uvik/` (200 — активная найм-активность).

---

### Visarsoft
**Due diligence (личное):**
- Что делают / вертикаль: Visarsoft GmbH (Мюнхен/Германия, с 2018) — позиционируется как «AI-native software engineering firm»: кастомная разработка веб-платформ, API, модернизация legacy, AI-driven продукты. На активных вакансиях Djinni — DevOps/observability (.NET/Azure/Datadog), Lead Backend Architect для финтех-платформы на 20M+ транзакций/мес (Node.js/PostgreSQL/GraphQL/RabbitMQ), Senior Computer Vision Engineer (Geospatial/Visual AI, miltech). Украинский офис во Львове, гибрид/remote.
- Тип: Outstaffing/service company (DOU прямо классифицирует как «Outstaffing»), но с собственной инженерной командой и заметным «AI-product»-уклоном на уровнях backend и CV.
- Финансирование/размер/выручка: DOU — «до 20 спеціалістів», Львів; зарегистрирована 17.02.2019; **не резидент Diia City**. Dun & Bradstreet имеет профиль на Visarsoft GmbH (Мюнхен), но конкретных цифр выручки/финансирования «не нашлось». Founder — Roman Prystatskyy (LinkedIn DE).
- Отзывы сотрудников/культура (Glassdoor/DOU/kununu): DOU — 6 отзывов (2022–2023), все позитивные: дружная атмосфера, помощь коллег, оплата курсов, уроки английского, тимирдинги, уютный офис во Львове. Минусов и негатива не нашлось. Glassdoor/kununu профиля нет.
- Red flags: Полные тёзки — `visarsoft.com` это **совершенно отдельное** индийское рекрутерское агентство (Bengaluru/Andhra Pradesh, +91 phone) — не путать. Сама Visarsoft GmbH небольшая (<20 чел. по DOU), значительная часть вакансий — контрактная работа на «international enterprise customer» (типичный outstaff). **Не резидент Diia City**. GitHub-след почти отсутствует (1 публичный repo `shared-core`, последний пуш 2022).

**ASRP-ценность (4 оси):**
1. Тех-трансфер (agent orchestration/RAG/knowledge graphs/LLM infra, переносимо ли на roadmap ASRP): **M** — «AI-native»-позиционирование и реальная CV-вакансия (DINOv2, CLIP, LightGlue, FAISS, cross-view geo-localisation, defence tech) подтверждает практический ML/CV-опыт в команде. Однако в открытом доступе нет следов собственных LLM-агентов, RAG- или KG-инфры — переносим скорее ML/CV-инженерный опыт, а не готовый стек под ASRP-roemap.
2. Сеть/инвесторы (кто за компанией, интерес к deep-tech/neurotech/quantum/consciousness): **L** — небольшая частная GmbH без публичных инвесторов, без признаков deep-tech/quantum/neuro-окружения; основатель один (Roman Prystatskyy).
3. Halo (усилит ли репутацию Михаила как CTO ASRP): **L** — узкая service-компания в Мюнхене без заметного бренда в deep-tech-сообществе.
4. Партнёрский потенциал (клиент/партнёр ASRP): **M** — может быть полезна как инженерный подрядчик/расширение команды для немецкоязычного рынка (Deutsch — преимущество в вакансиях), но не стратегический клиент.
- **Вердикт двойной выгоды:** Средняя — крепкий малый AI-native подрядчик с реальным CV/ML-конкретным опытом и доступом к DACH-рынку, но без стратегического deep-tech-перекрытия с roadmap ASRP.

**Источники:** `https://visarsoft.de` (200 — «AI-native software engineering firm», Germany since 2018), `https://visarsoft.com` (200 — **ВАЖНО: отдельное индийское рекрутерское агентство-тёзка**), `https://djinni.co/jobs/company-visarsoft/` (200 — 4 активные вакансии, sameAs=visarsoft.de), `https://jobs.dou.ua/companies/visarsoft/` (200 — до 20 спеціалістів, Львів, Outstaffing, зареєстрована 17.02.2019, не Diia City), `https://jobs.dou.ua/companies/visarsoft/reviews/` (200 — 6 позитивных отзывов 2022–2023), `https://api.github.com/orgs/visarsoft` (200 — Munich, Germany; blog=visarsoft.de; 1 public repo), Yahoo-сниппеты LinkedIn DE (founder Roman Prystatskyy), Dun & Bradstreet, ZoomInfo.

---

### Volia Software
**Due diligence (личное):**
- Что делают / вертикаль: US IT-services компания (custom software development, application integration, QA, IT consulting, App/system/network management). Сайт активно перепозиционируется на AI-тематику («AI-driven innovation», «AI-enhanced testing», «strategic AI implementation»). Финтех/healthcare/enterprise-клиенты. Киевский дев-центр + польский/восточно-европейский штат.
- Тип: Service company / outsourcing vendor (US-incorporated, украинский delivery). На DOU — «Service».
- Финансирование/размер/выручка: Founded 2003, ex-«Big 5» partners; HQ Houston, TX. DOU — 81–200 спеціалістів, Київ. Сайт/LinkedIn исторически заявляли «900/600+ professionals», но текущая цифра по DOU 81–200 — реалистичный размер. RocketReach (агрегатор) — $61.1M revenue, 34 employees (число явно неполное/устаревшее). Точных независимых цифр «не нашлось».
- Отзывы сотрудников/культура (Glassdoor/DOU/kununu): DOU — **0 отзывов**. Glassdoor — 4/5 (на 4–5 отзывов, агрегаторский сниппет, детали недоступны — glassdoor 403).
- Red flags: Существует крупная украинская telecom-компания «Volia» (volia.com, Киев, GPON/кабельное TV) — **другой бизнес**, не путать. Маркетинговый текст сайта («900 technology professionals») заметно расходится с актуальным размером по DOU (81–200) — признак недавнего сжатия или устаревшей «старой» цифры. Публичного GitHub-следа организации нет (`api.github.com/orgs/volia-software` → 404). Резидентство Diia City на DOU не указано.

**ASRP-ценность (4 оси):**
1. Тех-трансфер (agent orchestration/RAG/knowledge graphs/LLM infra, переносимо ли на roadmap ASRP): **L** — маркетинговый «AI-driven»-слой, но в открытом доступе нет признаков собственной agent orchestration/RAG/KG-инфры — это классический services-shop, перепродающий AI-услуги клиентам, без deep-tech R&D.
2. Сеть/инвесторы (кто за компанией, интерес к deep-tech/neurotech/quantum/consciousness): **L** — частная US-компания, основанная ex-Big-5 консультантами; investor-base не публична, neurotech/quantum/consciousness-окружения нет.
3. Halo (усилит ли репутацию Михаила как CTO ASRP): **L** — не усиливает репутацию в deep-tech-сообществе.
4. Партнёрский потенциал (клиент/партнёр ASRP): **L–M** — возможный канал для ASRP на enterprise-клиентов в США (Houston presence), но не стратегический technological partner.
- **Вердикт двойной выгоды:** Низкая — стабильный, но не deep-tech services vendor без реального перекрытия с roadmap ASRP (агенты/GFS/Arcanum12th/GMS).

**Источники:** `https://volia-software.com` (200 — US company, HQ Houston TX, founded 2003, AI-driven positioning), `https://jobs.dou.ua/companies/volia-software/` (200 — 81–200 спеціалістів, Київ, registered 11.02.2012, «Service»), `https://jobs.dou.ua/companies/volia-software/reviews/` (200 — 0 отзывов), `https://api.github.com/orgs/volia-software` (404 — нет публичного GitHub-следа), Yahoo-сниппеты LinkedIn (600+ employees claim), AeroLeads (telecom Volia — **не та**), Glassdoor (4/5, 4–5 reviews — агрегатор), RocketReach ($61.1M revenue / 34 employees), `https://volia.com` (403 — отдельный украинский telecom-бренд, к Volia Software отношения не имеет).

---

### Xpower
**Due diligence (личное):**
- Что делают / вертикаль: Xpower NV (Бельгия, Beervelde/Lochristi, Oost-Vlaanderen) — **Dealer Management Software (DMS)/ERP** для дилеров в вертикалях Truck & Bus, Cars, Recreational Vehicles, Construction Equipment, Material Handling, Agriculture & Garden. Флагман — **XDMS** (модульный ERP, CRM, workshop/warehouse management, BI, OEM interfaces). С 1993. Партнёры — европейские автомобильные/машинные бренды. Гипотеза «iGaming/energy» не подтвердилась.
- Тип: Product company (собственный нишевый ERP-продукт XDMS) + дочерний цифровой spin-off **HyperCharge** (no-code workflow automation платформа «HyperPortal», украинская dev-команда).
- Финансирование/размер/выручка: Crunchbase (Yahoo-сниппет) — Hypercharge acquired by Xpower; location Lochristi. Dun & Bradstreet имеет профиль Hypercharge. Конкретных цифр выручки Xpower NV «не нашлось». Украинский офис: текущие вакансии на Djinni — в Киеве. Точный размер украинской команды «не нашёлся».
- Отзывы сотрудников/культура (Glassdoor/DOU/kununu): На DOU профиль **отсутствует** (проверены слаги xpower, xpower-be, xpower-group, hypercharge — все 404). Glassdoor по украинскому офису не найдено. Культура «Euro product company with Ukrainian dev office» — типичная для бельгийских DMS-вендоров.
- Red flags: Имя «Xpower/Hypercharge» пересекается с посторонними компаниями: Hypercharge Networks Corp (EV charging, Canada, публичная) и XCharge Group (EV charging, 2015) — **другие бизнесы**, не путать. Украинский контур Xpower — это HyperCharge digital spin-off под бельгийским офисом (CEO Andy De Groote, Ghent area). Текущие Djinni-вакансии (UI/UX, Strapi backend, PM with marketing twist, industry tags «edutech/advertising») частично расходятся с классическим ERP-DMS-позиционированием — вероятно, относятся именно к HyperCharge-стороне.

**ASRP-ценность (4 оси):**
1. Тех-трансфер (agent orchestration/RAG/knowledge graphs/LLM infra, переносимо ли на roadmap ASRP): **L** — нише-вертикальный ERP/DMS и no-code workflow automation = enterprise automation, а не LLM-агенты/RAG/KG. Перекрытие с roadmap ASRP минимальное.
2. Сеть/инвесторы (кто за компанией, интерес к deep-tech/neurotech/quantum/consciousness): **L** — частная бельгийская компания (с 1993), European dealer-network; интереса к neurotech/quantum/consciousness нет.
3. Halo (усилит ли репутацию Михаила как CTO ASRP): **L** — не усиливает deep-tech-репутацию.
4. Партнёрский потенциал (клиент/партнёр ASRP): **L** — нишевый automotive/dealer-ERP-рынок далёк от доменов ASRP.
- **Вердикт двойной выгоды:** Низкая — зрелый нишевый бельгийский ERP-продукт с украинской dev-командой; надёжный работодатель, но стратегического перекрытия с ASRP-roemap нет.

**Источники:** `https://djinni.co/jobs/company-xpower/` (200 — meta «Xpower, based in Beervelde (Belgium), is the supplier of enterprise resource planning and dealer management systems»; sameAs=xpower.be), `https://www.xpower.eu` (200, после редиректа с xpower.be 301 — XDMS product, OEM interfaces, экспертиза с 1993, вертикали Truck/Bus/Cars/Agri/Construction), `https://api.github.com/orgs/hypercharge` (200 — GitHub-орг «hypercharge» создан 2013-04-05, 12 публичных репо, но без описания/локации), `https://jobs.dou.ua/companies/xpower/` и слаговые варианты (404 — профиль на DOU отсутствует), Yahoo-сниппеты Crunchbase (Hypercharge acquired by Xpower; Lochristi), LinkedIn (Andy De Groote CEO Xpower NV), Dun & Bradstreet, Facebook/Xpowerbe («HyperCharge digital spin-off within Xpower is located in Ukraine»).

---

### Zultys
**Due diligence (личное):**
- Что делают / вертикаль: Американская product company в Unified Communications / UCaaS — собственная IP-PBX-платформа MX, настольные SIP-телефоны (ZIP), контакт-центр (ICC), и новый продукт «AI Receptionist» (конверсационный LLM-агент для приёма входящих вызовов).
- Тип: Product company (UCaaS-вендор), собственная R&D-команда, гибрид premise/cloud.
- Финансирование/размер/выручка: Private. Основан Iain Milnes в 2001 в Sunnyvale, CA; в сент. 2006 — Chapter 11, в окт. 2006 активы куплены Pivot VoIP (Telrad Connegy) за **$2.65M** + долги (Wikipedia, spot-check'ом подтверждено). По агрегаторам Latka (2025) — ~$18.9M ARR, оценка ~$56.8M, ~172 сотрудника; Pitchbook — ~89 сотрудников. Точных независимых цифр выручки нет. CEO — Vladimir Movshovich; в команде VPs с восточно-европейскими фамилиями (Matsienak, Savchenko, Umyarov, Brodskiy) — консистентно с R&D-присутствием в Украине.
- Отзывы сотрудников/культура (Glassdoor/DOU/kununu): Glassdoor прямого доступа нет (403); агрегаторы и LinkedIn-страница Zultys Inc активны, но конкретный рейтинг/отзывы «не нашлись».
- Red flags: История банкротства 2006 (закрыта и перепродана) — исторический факт, не текущая проблема; после смены владельца компания работает >20 лет. Других красных флагов не найдено.

**ASRP-ценность (4 оси):**
1. Тех-трансфер (agent orchestration/RAG/knowledge graphs/LLM infra, переносимо ли на roadmap ASRP): **L** — стек AWS/Terraform/Kubernetes/Jenkins для UCaaS-платформы + продукт «AI Receptionist» (LLM-агент для звонков). Перенос на roadmap ASRP (multi-agent/RAG/GMS) маргинальный: опыт с enterprise-grade availability и LLM-voice применим, но глубокой науки нет.
2. Сеть/инвесторы (кто за компанией, интерес к deep-tech/neurotech/quantum/consciousness): **L** — private, backing Telrad-связанной группы, нет deep-tech/neuro/quantum-инвесторов.
3. Halo (усилит ли репутацию Михаила как CTO ASRP): **M** — узнаваемый бренд UCaaS с 20+ годами истории, активный «AI Receptionist» добавит строчку про voice-AI product, но не deep-tech halo.
4. Партнёрский потенциал (клиент/партнёр ASRP): **L** — UCaaS-клиенты это SMB/enterprise-телефоны, не пересекаются с ASRP-вертикалями.
- **Вердикт двойной выгоды:** Низкая — сильная product company с реальной AWS/voice-LLM-работой и стабильным доходом для Михаила как инженера, но **почти нулевое пересечение с deep-tech roadmap ASRP** (по бару паритета с Playtech/N-iX-services это Низкая двойной выгоды при высоком личном DD; вердикт агента «Средняя» скорректирован).

**Источники:** `https://www.zultys.com` (200 — продукты, AI Receptionist, executive team, founded 2006 post-Chapter 11), `https://en.wikipedia.org/wiki/Zultys` (200 — founded by Iain Milnes 2001, Chapter 11 Sept 2006 ND Cal, acquired by Pivot VoIP $2.65M Oct 2006), `https://www.zultys.com/about-us/` (200 — VP-состав, financially strong, HIPAA/HITECH compliance), `https://djinni.co/jobs/company-zultys/` (200 — DevOps AWS $5500–6000, sysadmin $1300–1800, telecom industry, UA remote), `https://www.zultys.com/careers/` (200 — открытые US-роли Inside Sales, Technical Support Engineer), Yahoo-сниппеты getlatka.com ($18.9M ARR, $56.8M, 172 emp), pitchbook.com (89 emp), crunchbase.com (founders Ian Milnes, Patrick Ferriter).

---

### Маркетинг-Партнер (Marketing-Partner)
**Due diligence (личное):**
- Что делают / вертикаль: ООО «Маркетинг-Партнер» (ЄДРПОУ 32956490, Київ, вул. Милютенка 29, керівник Ладик Л. М.), основан в 2004 — исторически рекламно/маркетинговое агентство (полиграфия, выставочные стенды, SEO/контекст, SMM, digital-агентство). Сайт marketing-partner.ua подтверждает это позиционирование. Сейчас на Djinni компания позиционируется как «международная продуктовая IT-компания» с офисом в Праге и продуктами «Sweepstakes US / Casino SA» (iGaming) и крипто-проектами (Media Buyer Crypto, Team Lead Media Buying Crypto). По сути — гибрид: классическое киевское маркетинг-агентство, открывшее продуктовую вертикаль в gambling/crypto через чешскую юрисдикцию.
- Тип: Смешанный — recruitment/marketing-services agency + продукт в gambling/crypto (iGaming Sweepstakes/Casino, Crypto Media Buying). Engineering-first работодателем не является: большинство ролей — SMM, Media Buyer, Influencer; engineering-вакансия одна (Backend Node.js/Nest.js, Прага, офис).
- Финансирование/размер/выручка: «не нашлось». На Djinni с 2024. UA-регистрация подтверждена; офис в Праге упоминается только в вакансиях.
- Отзывы сотрудников/культура (Glassdoor/DOU/kununu): «не нашлось». На newotzyv.ru/wk3.ru/spravker.ru есть страницы-каталоги, но конкретные рейтинги/отзывы публично не отображаются.
- Red flags: (1) головное юрлицо — старое рекламное агентство в Киеве, а продукты и найм — iGaming/Crypto через Прагу (типичная схема grey-market gambling); (2) почти все роли — маркетинг/медиабайинг в серых нишах; (3) по одной engineering-вакансии на Node.js — собственная R&D-команда минимальна.

**ASRP-ценность (4 оси):**
1. Тех-трансфер (agent orchestration/RAG/knowledge graphs/LLM infra, переносимо ли на roadmap ASRP): **L** — единственный backend-стек Node.js/Nest.js/PostgreSQL/Docker/K8s/AWS для gambling-продуктов; ничего общего с AI-агентами/RAG/quantum/neuro.
2. Сеть/инвесторы (кто за компанией, интерес к deep-tech/neurotech/quantum/consciousness): **L** — частное UA-ООО, публичных deep-tech-инвесторов нет.
3. Halo (усилит ли репутацию Михаила как CTO ASRP): **L (негативно)** — ассоциация с iGaming/Crypto-Media-Buying ослабляет академический/deep-tech-профиль CTO ASRP.
4. Партнёрский потенциал (клиент/партнёр ASRP): **L** — как канал к gambling/crypto-клиентам не релевантен roadmap ASRP; как продукт — тоже.
- **Вердикт двойной выгоды:** Низкая — для Михаила как инженера это маркетинговое агентство с серой gambling-продуктовой линейкой; для ASRP ценности по всем четырём осям практически нет.

**Источники:** `https://djinni.co/jobs/company-marketing-partner/` (200 — «На сайте с 2024», описание миссии 2004, 4 вакансии в gambling/crypto), `https://marketing-partner.ua/` (200 — подтверждает рекламное агентство, полиграфия, интернет-маркетинг с 2004), Yahoo-сниппет ukraine.com.ua/egrpou/32956490 (ООО МАРКЕТИНГ-ПАРТНЕР, Київ, керівник Ладик Л. М.), Yahoo-поиск «"Маркетинг-Партнер" Київ» (Yandex Maps, locator.biz, wk3.ru, spravker.ru классифицируют как «рекламное/диджитал агентство»).

---

## Сноска по охвату серии

Этот батч (S–Z + `softo.it` + «Маркетинг-Партнер») закрывает 13 оставшихся брендов из списка вакансий djinni.co. Серия `company-deepdive-2026-07-21-{aa,ab,ac,ad,ae}` теперь покрывает полный алфавитный набор (aa: A–C, ab: D–G, ac: H–M, ad: N–S, ae: S–Z + хвост). Сводный кросс-батч-ранкинг — в [final-ranking-2026-07-20.md](final-ranking-2026-07-20.md) (будет требовать обновления после батчей ae). Самые сильные кандидаты двойной выгоды по всем пяти батчам остаются на AI-agent/neurotech-пересечении: **ONU Health** (батч ad, VH tech-transfer, biomed+LLM), **TEKTELIC** (этот батч, H partnership, biomed-sensor+hardware), **Uvik Software / S-PRO / Sigma Software / N-iX / Seeking Alpha** (UA-outsourcing с реальной AI-agent-практикой, M–H tech-transfer, низкий личный риск). iGaming/crypto-grey-кластер (≈9 брендов по всем батчам, incl. SweepTech, Traffic Label, softo.it, TridenX, Маркетинг-Партнер, NewGMedia, NuxGame, Playtech, SharksCode) стабильно даёт Низкую двойную выгоду и отрицательный halo для neuroscience/education-миссии ASRP.
