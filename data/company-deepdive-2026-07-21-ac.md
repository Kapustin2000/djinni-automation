# Deep-dive по компаниям (батч H–M) — due diligence + стратегическая ценность для ASRP, 2026-07-21

Продолжение серии [company-deepdive-2026-07-21-aa.md](company-deepdive-2026-07-21-aa.md) (батч A–C) и [company-deepdive-2026-07-21-ab.md](company-deepdive-2026-07-21-ab.md) (батч D–G), в том же **объединённом формате**: для каждой компании одновременно личный DD (для трудоустройства Михаила Капустина) + оценка двойной выгоды для ASRP по 4 осям. Охват — 13 компаний из вакансий djinni.co (бренды на H–M).

**Заказчик:** Михаил Капустин, CTO и сооснователь ASRP (Advanced Scientific Research Projects) — холдинг в neuroscience / AI / consciousness research / quantum computing / биомед / образовании (Arcanum12th), зарегистрирован в Казахстане и США.
**Roadmap ASRP:** (a) LLM-агенты / multi-agent, (b) GFS forecasting-платформа, (c) Arcanum12th образовательная платформа, (d) GMS consciousness-платформа.
**Шкала осей:** L / M / H / VH. **Вердикт двойной выгоды:** Высокая / Средняя / Низкая — бар для «Высокая» = реальное пересечение с deep-tech/AI-agent/education/neuroscience-роадмапом ASRP (не просто «легитимный работодатель»).

> **Методологическая оговорка (важно для калибровки уверенности).** Встроенные поисковые инструменты снова недоступны (WebSearch + web-reader MCP = HTTP 429; WebFetch отсутствует). Поэтому весь ресёрч — **прямые fetch'и первичных источников через `curl`** (браузерный UA): официальные сайты, DOU-профили (`jobs.dou.ua/companies/<slug>`), Brave Search (отдаёт агрегированные сниппеты Crunchbase / ZoomInfo / startuphub.ai / LinkedIn / Wikipedia — сами crunchbase/zoominfo-страницы ботами блочатся, но их факты видны через сниппеты Brave). **REACHABLE в этом батче:** hiretop.com, halo-lab.com, itsmartflex.com, itexpert.com.ua, insulalabs.co, kyrrex.com, lionhires.com, brainrocket.com, luxonpro.com, mmdsmart.com, hyperone.com, DOU (множество слагов). **BLOCKED / пусто:** finsmes.com (в этот раз 403 Cloudflare — «Just a moment»), DuckDuckGo (CAPTCHA «bots use DuckDuckGo too»), Bing RSS (мусорная выдача на малоизвестные бренды), Glassdoor/LinkedIn/Clutch (403), `diversetechtalents.com` и `innotechfy.com` (connection failed / DNS, HTTP 000 — при этом обе присутствуют на DOU). Что надёжно верифицировано: продуктовое позиционирование (офиц. сайты), класс/размер/дата-регистрации (DOU), ownership/фаундеры (Brave→Crunchbase/сnipпеты + about-us страниц), связь LionHires↔BrainRocket (локальный `data/jobs.json`, где LionHires назван «exclusive recruitment partner» клиента в Fintech/iGaming/Marketing). Что **не** удалось проверить: точные суммы финансирования (Crunchbase-числа блочат бота напрямую), отзывы сотрудников (Glassdoor/Kununu 403), точные глобальные headcount/выручка. **Два бренда не идентифицированы однозначно как djinni-работодатели:** «International Maritime University» и «ITExpert» — подробнее в карточках. Ничего не выдумано; провалы помечены «не нашлось».

---

## Сводная таблица (батч H–M)

| # | Компания | Тип | Двойная выгода ASRP | Главный вывод одной строкой |
|---|---|---|:--:|---|
| 1 | HIRETOP | Staffing intermediary (senior eng recruitment) | **Низкая** | Бутиковый рекрутинг senior-инженеров (7 чел.); для CTO — не роль, для ASRP — лишь потенциальный канал найма. |
| 2 | Halo Lab | Outsourcing (digital/design studio) | **Низкая–Средняя** | Сильный UX-бренд (Dribbble Top-1); единственная реальная ценность — delivery UX под Arcanum12th/GMS. |
| 3 | Hunt.IT Recruitment (= Diverse Tech Talents) | Recruitment agency | **Низкая** | Мелкое киевское рекрутинговое агентство (≤20 чел.); нулевое пересечение с deep-tech. |
| 4 | Hyperone | Product company (cloud IaaS, PL) | **Низкая** | Польский cloud/IaaS (37k серверов, Terraform/K8s) — полезная инфра-дисциплина, но без agent/AI-пересечения. |
| 5 | IT SmartFlex | Product company (telecom BSS/OSS) | **Средняя** | **Стенд-аут батча:** продукт «AI Assistants» (knowledge bases, «Ask HR», call-center) + telecom-grade масштаб — реальный tech-трансфер на agent-роадмап ASRP. |
| 6 | ITExpert | Unclear (мелкий IT-сервис / не идент.) | **Низкая** | itexpert.com.ua = компьютерная помощь физлицам (Київ/Одеса); как djinni-tech-работодатель не подтверждён. |
| 7 | Innotechfy (TBC) | Outsourcing vendor (входить у North South Tech Group) | **Низкая** | Свежий (DOU 08.07.2025) микро-консалтинг ≤20 чел.; generic-стек, тонкий AI-слой. |
| 8 | InsulaLabs | Outsourcing (outstaffing, UA) | **Низкая** | UA-outstaffing 81–200 чел., 90% в Україні; потенційний staff-aug, але без стратегії. |
| 9 | International Maritime University | Unclear (морской вуз? / не идент.) | **Низкая** | Не вдалося підтвердити як djinni-роботодавця; найближчий реальний об'єкт — UMIP (Панама), не tech-компанія. |
| 10 | Kyrrex | Product company (crypto exchange) | **Низкая** | Регульована crypto-fiat біржа (2018, Мальта/Панама); фінтех-інфра без agent/neuro + репутаційне змішання для CTO-neuroscience. |
| 11 | LionHires / BrainRocket | Recruitment + outsourcing vendor | **Низкая** | BrainRocket (1300+ чел., Fintech/**iGaming**/Marketing) + LionHires як її рекрутинг-рука; iGaming-концентрація — мismatch для ASRP. |
| 12 | Luxonpro (Lux-on) | Outsourcing (product-dev studio) | **Низкая** | Бутикова студія в iGaming/Fintech/Dating; репутаційний мismatch + малий масштаб. |
| 13 | MMD Smart | Product company (CPaaS/messaging) | **Низкая** | Enterprise-месседжинг (MessageWhiz), IL/BG, 81–200; корисна інфра-дисципліна, але без AI/neuro-перетину. |

**Итог батча:** 9 из 13 — Низкая; 1 Средняя (IT SmartFlex — единственный с реальным AI-agent-продуктом); 1 Низкая–Средняя (Halo Lab — только UX-delivery); 2 не идентифицированы однозначно (ITExpert, International Maritime University). Батч H–M перегружен рекрутингом, аутстаффингом, crypto и iGaming — индустриями, которые почти не пересекаются с deep-tech/нейро/education-миссией ASRP.

---

## Подробно по компаниям

### HIRETOP
**Due diligence (личное):**
- Что делают / вертика: Senior-only remote engineering agency — помогают product-компаниям нанимать и **удерживать** senior remote-инженеров из 40+ стран; кураторские шорт-листы за 2 рабочих дня под стандартные стеки. Слоган: «engineers who stay».
- Тип: Staffing intermediary / recruitment agency (не product, не outsourcing разработки).
- Финансирование/размер/выручка: **7 человек** в трёх офисах (Tallinn, Valencia, Kyiv); основана в **2020** фаундером Andrew Ryzhenko (CEO). Заявляют **94% one-year retention** и «half our placements still on the same team three years later». Выручка/финансирование — не нашлось (bootstrapped, частная).
- Отзывы сотрудников/культура: не нашлось (7 человек, нет DOU/Glassdoor-следа).
- Red flags: Конкретных нет. Бутиковый рекрутинг с упором на retention — внятная ниша; но это не инженерная роль.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — рекрутинговый бизнес, собственной R&D/agent-инфры нет; «системы удержания инженеров» — это HR-процесс, а не тех-актив.
2. Сеть/инвесторы: L — частная, фаундер-backed, 7 человек; выхода на deep-tech/neuro/quantum-сеть нет.
3. Halo: L — работа в рекрутинговом бутике не усиливает CTO-brand ASRP.
4. Партнёрский потенциал: L — теоретически ASRP может использовать их как **канал найма senior-инженеров** (узкая ниша, retention-фокус), но это не партнёрство и не клиент.
- **Вердикт двойной выгоды:** Низкая — бутиковый рекрутинг без тех/R&D-пересечения; единственная ценность — возможный канал найма, не стратегическая.

**Источники:** https://hiretop.com (200), https://hiretop.com/about (200 — Andrew Ryzhenko, 2020, 7 ppl Tallinn/Valencia/Kyiv, 94% retention).

---

### Halo Lab
**Due diligence (личное):**
- Что делают / вертика: Full-service digital agency — UI/UX design, брендинг, website/web-app full-cycle development, Quality Assurance, SEO & marketing. «Immersive user experience»; работают с зарубежными онлайн-продуктами.
- Тип: Outsourcing vendor (design/development studio). Не product, не recruitment.
- Финансирование/размер/выручка: На сайте — **150+ professionals, 10+ лет, 600+ проектов, $150k задоначено Украине**; на DOU — «81...200 спеціалістів». Офисы: Київ, Харків, Львів, Одеса, Луцьк, Полтава, Хмельницький, Чернівці + Estonia, Germany, Latvia, Poland, Portugal, Spain. Заявляют Top-3 Web Design Agencies 2022, Top-1 Trending Team на Dribbble. Финансирование/выручка — не нашлось (bootstrapped студия).
- Отзывы сотрудников/культура: на DOU **29 відгуків** (сводный числовой рейтинг через curl не извлечён — подгружается JS); заявляют «DOU rated … one of the best places to work». Удалёнка, гибкий график.
- Red flags: Конкретных нет. Это в первую очередь **дизайн-студия** (Dribbble/Behance-ориентированная) — инженерный AI-слой тонкий.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — web/design-разработка; собственного agent/RAG/KG-стека публично нет. Переносима только дисциплина фронтенд/UX-сборки.
2. Сеть/инвесторы: L — bootstrapped студия, без deep-tech VC.
3. Halo: L–M — сильна в design-сообществе (Dribbble Top-1), но это **не** deep-tech/научное имя; для CTO-neuroscience почти не работает.
4. Партнёрский потенциал: M — **наиболее конкретная ценность**: могут быть UX/delivery-партнёром под продуктовые платформы ASRP — особенно **Arcanum12th (образовательная платформа)** и GMS, где UX/визуализация критичны. Аналог Empat из батча 07-20, но без AI-native-экспертизы.
- **Вердикт двойной выгоды:** Низкая–Средняя — ценность почти полностью на партнёрской оси (UX-delivery для education/consciousness-платформ); без тех-трансфера, инвестор-сети и deep-tech-halo.

**Источники:** https://www.halo-lab.com (200), https://jobs.dou.ua/companies/halo-lab/ (200 — 81...200 спец., 150+ prof, 10+ yrs, 600+ projects), https://jobs.dou.ua/companies/halo-lab/reviews/ (200 — 29 відгуків).

---

### Hunt.IT Recruitment (= Diverse Tech Talents)
**Due diligence (личное):**
- Что делают / вертика: IT recruitment / talent acquisition. На djinni бренд «Hunt.IT Recruitment»; сайт huntit.io — маркетинговая воронка на GoHighLevel/LeadConnector (без серверного текста-описания). На DOU профиль под слагом `huntit` соответствует компании **«Diverse Tech Talents»** (www.diversetechtalents.com).
- Тип: Recruitment agency / staffing intermediary.
- Финансирование/размер/выручка: на DOU — **до 20 спеціалістів**, Київ. Сайт diversetechtalents.com при проверке **недоступен** (HTTP 000 — connection failed; повторно тоже). Выручка/финансирование — не нашлось.
- Отзывы сотрудников/культура: не нашлось.
- Red flags: Расхождение бренда (Hunt.IT / Huntit / Diverse Tech Talents) и недоступный основной домен — низкая прозрачность для работодателя; очень маленькая команда (≤20).

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — рекрутинг; R&D отсутствует.
2. Сеть/инвесторы: L — мелкое киевское агентство без deep-tech-сети.
3. Halo: L — рекрутинговый бренд не усиливает научный CTO-профиль.
4. Партнёрский потенциал: L — теоретический канал найма, не партнёр/клиент.
- **Вердикт двойной выгоды:** Низкая — классическое рекрутинговое агентство без какого-либо пересечения с deep-tech/нейро/education-миссией ASRP.

**Источники:** https://huntit.io (200 — GoHighLevel SPA, title «Huntit», без описания), https://jobs.dou.ua/companies/huntit/ (200 → компания «Diverse Tech Talents», ≤20 спец., Київ, diversetechtalents.com), https://diversetechtalents.com (000 — недоступен).

---

### Hyperone
**Due diligence (личное):**
- Что делают / вертика: Польский **cloud/IaaS-провайдер** (HyperOne Platforma) — «sprawny dostęp do zasobów teleinformatycznych» (доступ к IT/теле-ресурсам без capex). Модели биллинга по использованию, управление из браузера/API/SDK/CLI, интеграции с **Packer, Terraform, Docker-Machine**. Заявляют **37 350 развёрнутых облачных серверов**; есть «Early adopters program», сообщество.
- Тип: Product company (cloud infrastructure, IaaS). Польский рынок.
- Финансирование/размер/выручка: не нашлось (страницы /about и Wikipedia 404; корпоративные цифры публично не светятся). По косвенным признакам — средний региональный cloud-провайдер.
- Отзывы сотрудников/культура: не нашлось.
- Red flags: Конкретных нет. **Дизамбигуация:** есть отдельный бренд «Hyperone» — египетская сеть гипермаркетов (Mansour Group, ритейл) — это **другая** компания, не нанимающая IT-инженеров через djinni; совпадение названия.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L–M — cloud-native инженерия (Terraform/K8s/IaaS, multi-region scaling, biling) переносима как **дисциплина масштабной инфры** под любую ASRP-платформу; но agent/AI/KG-пересечения нет.
2. Сеть/инвесторы: L — польский regional-cloud, без deep-tech/neuro/quantum-VC.
3. Halo: L–M — легитимный EU cloud, но не научное/инфлюентное имя.
4. Партнёрский потенциал: L — мог бы быть инфра-провайдером ASRP, но стратегического партнёрства не просматривается.
- **Вердикт двойной выгоды:** Низкая — солидная cloud-инженерия для личного DD, но без пересечения с agent/нейро/education-роадмапом ASRP.

**Источники:** https://hyperone.com (200 → https://www.hyperone.com/, польск. cloud, 37350 серверов, Terraform/Docker-Machine/Packer), https://www.hyperone.com/about (404), https://en.wikipedia.org/wiki/Hyperone (404 — нет статьи).

---

### IT SmartFlex
**Due diligence (личное):**
- Что делают / вертика: **Telecom BSS/OSS product vendor** — линейка продуктов для телеком-операторов на микро-сервисной платформе SmartFlex Core: SmartFlex CRM (со встроенной телефонией), SmartFlex USSD, **MyVodafone** (моб. приложение для абонентов Vodafone), OBM/Telescope (массовые/триггерные сообщения через SMS/RCS/email/Viber, telescope.ua), **AI Assistants** (интеллектуальные ассистенты для enterprise — call-center automation, «Ask HR», с учётом информбезопасности, внутренней инфры и баз знаний), BeKind (благотворительная платформа, bekind.ua).
- Тип: Product company (Tech Product per DOU). Не аутсорс — собственные продукты; работает с/для Vodafone (сильный сигнал).
- Финансирование/размер/выручка: на DOU — **200...800 спеціалістів**, Київ (itsmartflex.com). Финансирование/выручка — не нашлось.
- Отзывы сотрудников/культура: на DOU профиль есть, отзывы подгружаются JS — числовой рейтинг через curl не извлечён.
- Red flags: Конкретных нет. Продуктовая компания с реальными telecom-клиентами (Vodafone) и собственным AI-направлением.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: M–H (**лучшее в батче**) — продукт **AI Assistants** (knowledge bases + enterprise-infosec + call-center/«Ask HR») — это **готовый паттерн enterprise-агента над базой знаний**, напрямую релевантный оси (a) LLM-агенты и платформам Arcanum12th/GMS ASRP. Плюс telecom-grade микро-сервисная платформа и high-load/надёжность.
2. Сеть/инвесторы: L–M — украинская product-компания с отношением Vodafone; deep-tech/neuro/quantum-VC нет, но enterprise-телеком-сеть реальна.
3. Halo: M — продуктовая компания с marquee-клиентом (Vodafone) и собственным AI-продуктом — moderate credibility для CTO.
4. Партнёрский потенциал: M — их AI Assistants-стек и опыт enterprise-KG/infosec могут быть переиспользованы/интегрированы с ASRP; потенциальный тех-партнёр по agent-инфре (а не покупатель продуктов ASRP).
- **Вердикт двойной выгоды:** Средняя — единственная в батче, где реальный AI-agent-продукт (knowledge bases, enterprise-ассистенты) + telecom-grade масштаб дают осязаемый tech-трансфер на agent-роадмап ASRP; минус — нет deep-tech-инвесторов и нейро-пересечения.

**Источники:** https://itsmartflex.com (200 — SmartFlex Core/CRM/USSD, MyVodafone, OBM/Telescope, AI Assistants, BeKind), https://jobs.dou.ua/companies/it-smartflex/ (200 — 200...800 спец., Київ, itsmartflex.com).

---

### ITExpert
**Due diligence (личное):**
- Что делают / вертика: **Не идентифицировано однозначно.** Найденный itexpert.com.ua — небольшой WordPress-сайт «IT послуги для бізнесу та приватних осіб… Професійна комп'ютерна допомога» (Київ, Одеса) — т.е. **мелкий потребительский/business IT-сервис** (компьютерная помощь, не разработка). Домен itexpert.com редиректит на **cyberitex.com** (CyberITEX — «Cybersecurity & Managed IT Solutions») — отдельная компания. На DOU под ожидаемыми слагами (itexpert, it-expert и др.) профиля **нет**.
- Тип: Unclear — либо мелкий IT-сервис (itexpert.com.ua), либо MSP/кибербез (CyberITEX), но ни один вариант не подтверждён как бренд djinni-вакансии.
- Финансирование/размер/выручка: не нашлось / не применимо.
- Отзывы сотрудников/культура: не нашлось.
- Red flags: Невозможность однозначно сопоставить бренд «ITExpert» с реальным tech-работодателем; найденный .ua-сайт — это компьютерная помощь физлицам, что не вяжется с djinni-инженерной вакансией.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — идентификация не подтверждена; даже если CyberITEX (MSP/кибербез) — это эксплуатация/managed-сервисы, не agent/AI/neuro.
2. Сеть/инвесторы: L — не идентифицировано.
3. Halo: L — не идентифицировано.
4. Партнёрский потенциал: L — не идентифицировано.
- **Вердикт двойной выгоды:** Низкая — бренд не подтверждён как tech-работодатель; найденные кандидаты (мелкий IT-сервис / MSP) не имеют пересечения с ASRP.

**Источники:** https://itexpert.com.ua (200 — WP-сайт «IT послуги», комп'ютерна допомога, Київ/Одеса), https://itexpert.com (200 → редирект на cyberitex.com), DOU-пробы слагов itexpert/it-expert/itexperts = 404.

---

### Innotechfy (TBC)
**Due diligence (личное):**
- Что делают / вертика: «Global IT consulting and software engineering company», входит в **North South Tech Group** (консорциум IT-компаний: North South Tech, TeepCore, Kode Resources и др.). Домены: Fintech, Healthcare, E-commerce, Real Estate, enterprise SaaS. Capability: custom web/mobile, legacy rebuild, MVP, **AI-Powered Analytics & Dashboards**, healthcare/medical-device integration, fintech-платформы/API.
- Тип: Outsourcing vendor (Service per DOU). Малый, свежий.
- Финансирование/размер/выручка: на DOU — **до 20 спеціалістів**, **зарегистрирована 08.07.2025** (очень свежая). Стек: React, Angular, .NET, Node.js, Python, Swift, Kotlin, C#, PostgreSQL, MongoDB, RabbitMQ. Выручка/финансирование — не нашлось. Основной домен innotechfy.com — connection failed (000); innotechfy.co жив, но контент JS-рендерится (пусто в curl).
- Отзывы сотрудников/культура: не нашлось (нет следа).
- Red flags: Очень молодая (на DOU с июля 2025), ≤20 человек, недоступен основной домен — низкая публичная зрелость; «(TBC)» в задании корректно отражает неуверенность.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — generic-стек аутсорса; «AI-Powered Analytics & Dashboards» — маркетинговый breadth, не глубокая AI-R&D.
2. Сеть/инвесторы: L — входить у небольшой холдинг (North South Tech Group), без deep-tech/neuro-VC.
3. Halo: L — стартап-аутсорс без репутационного веса.
4. Партнёрский потенциал: L —太小/слишком свежая для стратегического партнёрства.
- **Вердикт двойной выгоды:** Низкая — свежий микро-аутсорс в общем холдинге; нет пересечения с deep-tech-миссией ASRP.

**Источники:** https://jobs.dou.ua/companies/innotechfy/ (200 — до 20 спец., Service, рег. 08.07.2025, part of North South Tech Group), Brave→https://northsouthtechgroup.com (консорциум IT-компаний), https://innotechfy.co (200, JS-пусто), https://innotechfy.com (000).

---

### InsulaLabs
**Due diligence (личное):**
- Что делают / вертика: **Украинская IT-компания, модель — outstaffing** («build skilled, talented teams… the main business model is outstaffing» — быстрое масштабирование команд клиентов за счёт доступа к специалистам). **90% сотрудников в Украине**, удалённый формат, фиксированный график в европейском часовом поясе, долгосрочное сотрудничество. Бренд-метафора — автоспорт/«race crew».
- Тип: Outsourcing vendor (Outstaffing per DOU). Не product.
- Финансирование/размер/выручка: на DOU — **81...200 спеціалістів**, **зарегистрирована 07.05.2025**. Сайт insulalabs.co (на insulalabs.com — Squarespace-заглушка «Insula Labs, LLC», контакт bosley@insulalabs.com). Выручка/финансирование — не нашлось. На момент проверки — «Currently no job openings» на собственном сайте (но активно на DOU/djinni).
- Отзывы сотрудников/культура: не нашлось (профиль свежий).
- Red flags: Свежая регистрация (май 2025) при уже 81–200 специалистах — быстрый наём/масштаб; стандартные для outstaffing замечания (модель «какого клиента получишь»).

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — outstaffing; собственная R&D/IP отсутствует (инженеры работают на клиентов).
2. Сеть/инвесторы: L — украинский outstaff, без deep-tech-сети.
3. Halo: L — outstaff-вендор не усиливает научный CTO-профиль.
4. Партнёрский потенциал: L–M — потенциальный **staff-aug** (инженерное расширение) под ASRP-билд, но без стратегического веса (как CodeTiburon из батча aa, но моложе/без верифицированного agent-кейса).
- **Вердикт двойной выгоды:** Низкая — свежий UA-outstaffing без собственного IP и без deep-tech-пересечения; разве что как запасной staff-aug.

**Источники:** https://jobs.dou.ua/companies/insulalabs/ (200 — 81...200 спец., Outstaffing, рег. 07.05.2025, 90% UA, insulalabs.co), https://www.insulalabs.co/about-us (200 — outstaffing-модель, racing-метафора), https://www.insulalabs.com (200 — Squarespace-заглушка).

---

### International Maritime University
**Due diligence (личное):**
- Что делают / вертика: **Не идентифицировано однозначно как djinni-работодатель.** В выдаче Brave под точной фразой «International Maritime University» — это **учебные заведения**: International Maritime University of Panama (UMIP — maritime college в Панама-Сити), и IAMU (International Association of Maritime Universities). Ни один не подтверждён как IT-работодатель, размещающий вакансии на djinni. На Wikipedia отдельной статьи «International Maritime University» нет (404).
- Тип: Unclear — вероятна образовательная институция (если это UMIP) или профильный вуз; не tech-компания.
- Финансирование/размер/выручка: не нашлось / не применимо.
- Отзывы сотрудников/культура: не нашлось.
- Red flags: Невозможность подтвердить, какой именно субъект прячется за брендом на djinni; ни один публичный «International Maritime University» не нанимает IT-инженеров через украинскую платформу в обычной практике.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — не идентифицировано; даже если образовательная институция — R&D-стек не виден.
2. Сеть/инвесторы: L — не идентифицировано.
3. Halo: L — не идентифицировано.
4. Партнёрский потенциал: L — единственный гипотетический оверлап — education-ось ASRP (Arcanum12th), но без подтверждённой tech-составляющей это спекулятивно.
- **Вердикт двойной выгоды:** Низкая — бренд не подтверждён как tech-работодатель; вероятная образовательная институция не даёт ни тех-трансфера, ни стратегического партнёрства для ASRP.

**Источники:** https://en.wikipedia.org/wiki/International_Maritime_University (404 — нет статьи), Brave Search → UMIP (en.wikipedia.org/wiki/International_Maritime_University_of_Panama) и IAMU (iamu-edu.org) как ближайшие совпадения; подтверждения как djinni-работодателя не найдено.

---

### Kyrrex
**Due diligence (личное):**
- Что делают / вертика: **Регулируемая crypto-fiat биржа** («one-stop-shop digital finance»): spot-трейдинг, Earn (стейкинг до 14% APY), crypto loans, affiliate, **Kyrrex Partners**; для институционалов — liquidity hub, OTC-платформа, кошелёк, crypto-merchant, banking, tokenization. Торг-комиссия 0.25% maker/taker; API для торговых ботов.
- Тип: Product company (Tech Product per DOU). Fintech/crypto.
- Финансирование/размер/выручка: **основана в 2018** фаундером **Viktor Kochetov** (CVO/co-founder — Mike Romanenko). На DOU — **81...200 спеціалістів**, «Основний бізнес: Tech Product», зарегистрирована 26.06.2020. Юрисдикция: заявлена Malta-registered; **услуги оказывает Fintech Operations Development S.A. (Панама)**; Crunchbase/ZoomInfo показывают разные HQ (Malta / Australia). Точная сумма финансирования — **не нашлось** (Crunchbase-числа ботами напрямую не отдаются).
- Отзывы сотрудников/культура: не нашлось (Glassdoor 403).
- Red flags: Мульти-юрисдикционная crypto-структура (Malta registration + Panamanian operating entity) — типичная для crypto, но требует осторожности; crypto-индустрия — репутационно смешанный контекст для CTO neuroscience/education-холдинга (аналог iGaming-замечания из батча ab).

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L–M — fintech/trading-инфра (matching engine, wallets, KYC/AML, high-concurrency) — солидный backend, но **не** agent/AI/KG/forecasting; переносимость минимальна для ASRP.
2. Сеть/инвесторы: L — crypto/fintech-сеть, без neurotech/quantum/consciousness-выходов.
3. Halo: L — crypto-биржа не усиливает академический/neuro CTO-brand ASRP (скорее разбалансирует).
4. Партнёрский потенциал: L — ASRP не клиент и не партнёр для crypto-exchange.
- **Вердикт двойной выгоды:** Низкая — легитимный crypto-product с сильным бэкендом, но индустрия и стек почти не пересекаются с deep-tech/нейро/education-миссией ASRP; плюс репутационное смешение.

**Источники:** https://kyrrex.com (200 → /global), https://kyrrex.com/about-us (200 — Viktor Kochetov 2018, Mike Romanenko CVO), https://jobs.dou.ua/companies/kyrrex/ (200 — 81...200 спец., Tech Product, рег. 26.06.2020), Brave→Crunchbase/startuphub.ai (Malta-based, основана 2018).

---

### LionHires / BrainRocket
**Due diligence (личное):**
- Что делают / вертика: **Связанные бренды.** **LionHires** — global recruitment/relocation-партнёр («connect top talent with international career opportunities»), работает эксклюзивно с международными tech-корпорациями, ведёт релокацию (страховка, бонусы, переезд). **BrainRocket** — собственно product-engineering компания: custom software development end-to-end в **Fintech, iGaming, Marketing** (+ design, delivery, business-solutions). Связь подтверждена локально: в `data/jobs.json` LionHires назван «exclusive recruitment partner» клиента, строящего product engineering в Fintech/iGaming/Marketing — это описание BrainRocket.
- Тип: LionHires = recruitment agency; BrainRocket = outsourcing/product-dev vendor (крупный).
- Финансирование/размер/выручка: BrainRocket — **1300+ сотрудников**, 7 стран (Spain, Serbia, Poland, Portugal, Armenia, Cyprus, Malta), **140+ solutions delivered**, **300+ открытых вакансий**. LionHires — размер не раскрывается. Финансирование/выручка — не нашлось (private). Ни та, ни другая нет на DOU.
- Отзывы сотрудников/культура: не нашлось напрямую (Glassdoor 403); на сайте — корпоративные testimonials.
- Red flags: **iGaming-концентрация** (как Delasport/GR8 Tech в батчах ab/aa) — репутационный/этический риск для CTO neuroscience/education-холдинга ASRP; агрессивный масштаб (300+ вакансий) типичен для iGaming/fintech body-shop.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L–M — продуктовая инженерия в fintech/iGaming (backend/frontend для scale), но не agent/AI/neuro; breadth без deep-tech-глубины.
2. Сеть/инвесторы: L — без deep-tech/neuro/quantum-VC; сеть в iGaming/fintech.
3. Halo: L — iGaming/fintech dev-shop не усиливает научный CTO-brand (скорее снижает alt-профиль, как Delasport).
4. Партнёрский потенциал: L — ASRP не клиент и не партнёр; iGaming-домен = mismatch.
- **Вердикт двойной выгоды:** Низкая — крупный легитимный вендор (BrainRocket) + его рекрутинг-рука (LionHires), но iGaming/fintech-фокус без пересечения с deep-tech/нейро/education-миссией ASRP.

**Источники:** https://lionhires.com (200 — global recruitment partner, relocation), https://brainrocket.com (200 — 1300+ ppl, 7 стран, 140+ solutions, Fintech/iGaming/Marketing), локальный data/jobs.json (LionHires = «exclusive recruitment partner» клиента в Fintech/iGaming/Marketing → BrainRocket), DOU brainrocket/lion-hires/lionhires = 404.

---

### Luxonpro (Lux-on)
**Due diligence (личное):**
- Что делают / вертика: Бутиковая **product development studio** (Product Development · Architecture · Growth) — дизайн и разработка «stable and intuitive digital platforms» from idea to launch + долгосрочная поддержка. Домены: **Dating & Social Platforms, iGaming Platforms, Fintech Products**.
- Тип: Outsourcing vendor (boutique product-dev studio). Не product-company-собственник, не recruitment.
- Финансирование/размер/выручка: «small team» (явно бутиковая, «you work directly with the people building your product»); конкретный headcount/выручка — не нашлось. На DOU нет.
- Отзывы сотрудников/культура: не нашлось.
- Red flags: Фокус на **iGaming и Dating** — репутационный mismatch для neuroscience/education-миссии ASRP (как Delasport/Luxonpro-соседи по батчу); малый масштаб.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L — бутиковая студия, без deep-tech/AI/neuro IP.
2. Сеть/инвесторы: L — частная студия без deep-tech-VC.
3. Halo: L — iGaming/dating-dev не усиливает научный CTO-brand.
4. Партнёрский потенциал: L — ASRP не клиент; iGaming/dating = mismatch.
- **Вердикт двойной выгоды:** Низкая — бутиковая студия в iGaming/Fintech/Dating без пересечения с deep-tech-роадмапом ASRP; разве что «запасной работодатель».

**Источники:** https://luxonpro.com (200 — Lux-on, Product Development/Architecture/Growth, iGaming/Fintech/Dating), DOU luxonpro/lux-on/luxon = 404.

---

### MMD Smart
**Due diligence (личное):**
- Что делают / вертика: **Enterprise CPaaS / месседжинг-компания** — флагман **MessageWhiz** («first conversion-based messaging platform for enterprises»), SMS OTP-аутентификация, Call Center Connect, Wholesale Messaging/Voice, Retail Voice. Позиционируются как партнёр для Tier-1 компаний worldwide по критическим коммуникациям.
- Тип: Product company (telecom/CPaaS/messaging). Не аутсорс.
- Финансирование/размер/выручка: на DOU — **81...200 спеціалістів**, зарегистрирована 05.10.2018. HQ: **Израиль** (Petah Tikva / Tel Aviv) + **Sofia, Bulgaria** (ZoomInfo/Crunchbase); key employee — Karen Krivaa; ~5 094 подписчиков на LinkedIn. Точная выручка/финансирование — не нашлось.
- Отзывы сотрудников/культура: не нашлось напрямую (Glassdoor 403).
- Red flags: Конкретных нет. Легитимный международный CPaaS-продукт с Tier-1-клиентами.

**ASRP-ценность (4 оси):**
1. Тех-трансфер: L–M — messaging/CPaaS-инфра (A2P SMS, voice, high-throughput delivery) + «conversion-based» (данные/ML-угол для оптимизации доставки); переносима как инфра-дисциплина, но без agent/AI/KG.
2. Сеть/инвесторы: L — израильский telecom/CPaaS, без neurotech/quantum-VC.
3. Halo: L–M — легитимный enterprise-месседжинг с Tier-1-клиентами; moderate credibility, но не научное имя.
4. Партнёрский потенциал: L — ASRP не клиент для CPaaS; стратегического партнёрства не видно.
- **Вердикт двойной выгоды:** Низкая — солидный telecom/CPaaS-продукт (полезная high-throughput-инженерия для личного DD), но без пересечения с agent/нейро/education-роадмапом ASRP.

**Источники:** https://mmdsmart.com (200 — MessageWhiz, SMS OTP, Call Center Connect, Wholesale Voice, CPaaS), https://jobs.dou.ua/companies/mmd-smart/ (200 — 81...200 спец., рег. 05.10.2018), Brave→ZoomInfo/Crunchbase/LinkedIn (HQ Israel Petah Tikva/Tel Aviv + Sofia Bulgaria, 51–200, Karen Krivaa, ~5094 LinkedIn followers).

---

*Серия батчей: aa (A–C), ab (D–G), **ac (H–M, этот файл)**. Следующий батч должен продолжить нумерацию (ad, …).*
