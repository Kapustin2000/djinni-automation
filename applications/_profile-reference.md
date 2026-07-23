# Профиль-референс для генерации CV/писем (внутренний, не отправлять как есть)

Источник фактов для всех `applications/<company>/`. Правила анонимизации применены единообразно во всех документах (CV, cover letter, hi-letter):

- **ASRP** — называется прямо (это реальный холдинг), но **титул НЕ "Co-Founder & CTO"** — использовать **"Lead Engineer — ASRP (independent AI research lab)"** (или близкий вариант без слов "co-founder"/"CTO"/"founder"). Причина: титул "Co-Founder & CTO" — частый триггер для рекрутеров/HR при найме на обычную IC/senior-роль — читается как "flight risk" (уйдёт обратно в свой стартап), "не будет слушаться" (привык быть боссом), overqualified/зарплатные ожидания не совпадут. Описание работы (что реально делал) не меняется — меняется только как называется позиция/роль в ASRP.
- **Прошлые клиентские/штатные роли, не под своим брендом** — называются **обобщённо**, без названия компании И без конкретного города (город сужает анонимность до одной легко гуглящейся компании — например, "German AI SaaS company in Leipzig" почти однозначно указывает на Osnova). В CV/cover letter/hi-letter — только страна/регион, без города:
  - "AI Platform Engineer" (Leipzig, Germany, Oct 2025 – Mar 2026) → **"a German AI SaaS company"** (не "in Leipzig")
  - "Realtime Communications Engineer" (Ohio, US, Nov 2025 – Jul 2026) → **"a US logistics-tech company"** (не "in Ohio")
  - "Sr. AI/ML Engineer" (San Francisco, US, Apr 2025 – Sep 2025) → **"a US-based EdTech company"** (было решено сначала называть Woolf прямо, затем скорректировано — тоже анонимно)
- **K8s/Kubernetes — НЕ заявлять как реальный навык.** Публичный skills-профиль показывает "Kubernetes 2 yrs, 2021–2023", но по факту реальной глубины нет — не использовать в cover letter/CV как то, что можно защитить на техническом интервью. Если вакансия требует K8s явно (CodeTiburon, отчасти Adaptiq) — честно писать "нет реального опыта", не смягчать до "не в последнем окне".
- **EU citizenship — упоминать явно и заметно** (не прятать внутри общей фразы про remote). Практически значимый плюс для любой EU-based компании — снимает вопрос визы/work permit с самого начала.
- **ASRP — не "текущая работа, которую брошу ради найма", а действующая исследовательская практика, которую я не планирую закрывать.** (Утверждено 2026-07-23.) Позиционировать в Summary как ongoing: R&D ASRP (agent-архитектуры, knowledge graphs) напрямую подпитывает качество delivery на клиентских engagement'ах — не "я работаю в ASRP, пока не найду что-то получше", а "у меня есть исследовательская база, которая делает мою работу на вас лучше". Формулировка-эталон (Interloom Summary): *"I lead engineering at ASRP, an independent AI research lab I run on an ongoing basis — its R&D on agent architectures and knowledge graphs directly feeds the quality of what I deliver on client work."*
- **Тип занятости — открыт к full-time, contract, freelance; не настроен именно на "устройство в штат".** (Утверждено 2026-07-23, ответ пользователя: *"я не уверен что я к кому-то иду работать в штат, скорее либо фриланс либо через существующие юр лица: KZ/US"*.) Во всех CV/cover letter добавлять явную фразу об открытости к разным форматам занятости, а не только full-time employee:
  - **CV Summary:** "...open to full-time, contract, or freelance engagements."
  - **CV Work Authorization:** "Open to full-time, contract, or freelance engagements — also able to contract directly through US- and Kazakhstan-based entities where useful." (заменяет старую формулировку "Also eligible to work in the US (via an American entity) and Kazakhstan (via a Kazakhstan-based entity)" — та же фактура, но явно про контракт/фриланс, не только "eligible to work").
  - **Cover letter, "Practical note" абзац:** добавлять отдельным предложением: "I'm open to full-time, contract, or freelance arrangements — whatever fits how you're structuring the hire."
  - Hi-letter — не перегружать этим (короткое первое сообщение), можно оставить только EU citizenship/location.

## Стандарт формата CV (утверждён 2026-07-22)

Единый современный tech-резюме формат для всех 35 заявок — не Europass, без фото/таблиц/CEFR-полосок.

- **Источник:** markdown (`cv.md`, для чтения/редактуры) + HTML (`cv.html`, реальный источник для рендера) в каждой папке application. Финальный файл на отправку — `cv.pdf`, рендерится из HTML.
- **GitHub-ссылка в контактах — короткая: `github.com/Kapustin2000/`** (профиль), не `github.com/Kapustin2000/Kapustin2000` (это репозиторий с тем же именем, что и юзернейм — выглядит избыточно в контактной строке). **Исключение:** глубокие ссылки на конкретные файлы/папки внутри репозитория (например, на список публикаций `.../tree/master/publications/technical-articles`) обязаны содержать полный путь `github.com/Kapustin2000/Kapustin2000/...` — иначе ссылка сломана (двойной слэш). Менять короткую форму только в контактной строке header'а, не в глубоких ссылках.
- **⚠️ Как рендерить (проверено, работает на этой машине):** LibreOffice не установлена — DOCX-путь из skill `docx` недоступен локально. Вместо этого — HTML+CSS → PDF через `weasyprint` (Python, уже установлен, но требует явного указания пути к homebrew-библиотекам):
  ```bash
  DYLD_FALLBACK_LIBRARY_PATH="$(brew --prefix)/lib" weasyprint cv.html cv.pdf
  ```
  Без этой переменной weasyprint падает с `OSError: cannot load library 'libgobject-2.0-0'` (pango/cairo стоят через brew, но не в стандартном dlopen-пути).
  Проверка результата: `pdfinfo cv.pdf | grep Pages` (должно быть 1, максимум 2), `pdftoppm -jpeg -r 130 cv.pdf page` → Read на `page-1.jpg` для визуальной проверки, `pdftotext -layout cv.pdf -` для проверки, что ATS-парсер извлечёт текст в правильном порядке.
- **Готовый HTML-шаблон:** [`applications/_cv-template.html`](_cv-template.html) — рабочий, провалидированный дизайн (использован для Interloom). Копировать и менять только контент (Summary/Skills/Experience/Projects/Publications) под конкретную роль, **не трогать CSS** без необходимости — уже подобраны отступы/шрифты под 1 страницу A4 для профиля такого объёма.
- **⚠️ Важный ATS-баг, который уже словили и исправили:** `letter-spacing` + `text-transform: uppercase` на заголовках секций (`h2.section`) ломает текстовое извлечение — pdftotext/ATS-парсеры читают "SUMMARY" как "S UMMARY" (лишний пробел после первой буквы). **Не использовать `letter-spacing` на текстовых элементах вообще** — только обычный bold + чуть увеличенный font-size для заголовков секций. Это специфика PDF text-layer рендеринга (letter-spacing превращает буквы в отдельно позиционированные глифы, которые парсер трактует как отдельные "слова").
- **Целевой объём:** 1 страница A4 при 10+ годах опыта — требует сжатия: не дублировать Projects отдельной секцией, если те же проекты уже описаны в Experience; секция Publications — максимум 2 самые релевantные статьи, не весь список 11.
- **Структура:** Header (имя, роль-тайтл под конкретную вакансию, город, контакты) → Summary (2-3 строки, тейлор под роль) → Skills (сгруппировано, порядок меняется под акцент роли: AI-heavy vs DevOps vs fullstack) → Experience (reverse-chronological, все реальные роли с анонимизацией по правилам выше) → Projects (2-4 самых релевантных под конкретную роль, не все 8 сразу) → Publications (**только если роль AI/agent-heavy** — не для чистых DevOps/backend ролей) → Education → Work authorization.
- **Publications для AI-heavy ролей — не ограничиваться 2 статьями.** Пул из 11 "безопасных" технических статей (см. каталог публикаций ниже) достаточно богат, чтобы показывать 3-4 самые релевантные под конкретную вакансию, а не всегда одни и те же 2. Ограничение — влезание в 1 страницу; если не влезает — сокращать описания каждой статьи до одной строки, а не резать список до 2.
- **Work authorization строка — всегда одна и та же, во всех CV:** "EU citizenship — no visa/work-permit sponsorship required in the EU. Berlin-based. Also eligible to work in the US (via American entity) and Kazakhstan (via Kazakhstan-based entity)."
- **ATS-совместимость:** обычный текст, стандартные заголовки, никаких колонок/иконок/полосок-рейтингов навыков.
- **⚠️ Даты для клиентских engagement'ов — НЕ показывать календарные диапазоны.** Osnova (окт 2025 – мар 2026), WireBee (ноя 2025 – июл 2026) и Woolf (апр 2025 – сен 2025) реально **пересекаются по времени друг с другом и с ASRP** (Apr 2023 – Present) — это client-engagements, которые велись параллельно с основной ролью в ASRP. Показывать точные даты рискует вызвать вопрос «почему вы работали в нескольких местах одновременно» до того, как есть возможность объяснить контекст (co-founder + консультационные/контрактные engagement'ы).
  - **Как оформлять в CV:** структурировать как "Selected Client Engagements" (или аналог) под основной записью ASRP, **без отдельных календарных дат** — только длительность («9 mos», «6 mos», «5 mos») без start/end, либо вообще без длительности, только roles + stack. ASRP показывать нормально как "Apr 2023 – Present" (это непрерывная, не вызывающая вопросов роль).
  - Старая таблица "Хронология опыта" ниже сохраняет полные даты для внутреннего использования (справочно, кто где когда работал) — **не копировать даты оттуда напрямую в генерируемый cv.md**.

## Стандарт тона hi-letter / cover-letter (утверждён 2026-07-22, откалибровано на примере Interloom)

**Разница в аудитории — ключевая.** Hi-letter читает *холодным* — обычно рекрутер/HR, часто нетехнический, без предварительного контекста, первым сообщением. Cover-letter читается вторым шагом, осознанно открытым (после того, как hi-letter уже зацепил) — там уместнее больше технической плотности. Не писать их одинаково.

### Правила для hi-letter (короткое первое сообщение)

1. **Не ссылаться на источник, которого читатель ещё не видел.** Фразы вида "Through ASRP, I built..." не работают в первом сообщении — читатель ещё не знает, что такое ASRP, и это не incorporated в предыдущий контекст (потому что предыдущего контекста для него нет). Открывать нужно с нуля, как будто это единственное, что человек увидит.
2. **Открывашка — живая мысль, не пересказ due diligence.** Не начинать с перечисления раунда финансирования/инвесторов/фактов о компании ("I've been following since the €14.2M seed round with Air Street, DN Capital...") — это звучит как отчёт, не как заинтересованность. Вместо этого — простое, естественное наблюдение о том, что компания делает и почему это интересно ("a proper knowledge base for agents feels like the next big challenge in AI"). Конкретные факты (раунд, инвесторы) остаются в `context.md` про запас — не в первом сообщении.
3. **Технический стек — переводить на простой язык, не перечислять акронимы подряд.** Рекрутер не оценит "NestJS + React + PostgreSQL with row-level security, plus a Python/FastAPI backend with tool registries and tenant-safe execution" — это звучит внушительно технически подкованному человеку, но HR не считает это как "то, чем занимается компания". Переводить в результат/функцию: "platforms where AI agents work across a company's email, chat, and other channels while keeping shared context and staying safely separated between different clients" — то же самое по сути, но понятно любому читателю.
4. **Показывать широту, не один проект.** Не ограничиваться одним client engagement — упоминать разные технологии/фреймворки (LangChain/LangGraph, Google ADK) и разные домены (Voice AI, agent platforms) одной фразой, чтобы показать разносторонний, не однобокий опыт.
5. **Публикации — упоминать casually, одной конкретной ссылкой, не статистикой охвата.** Формулировка вида "I also write a lot about AI — here's [one piece](ссылка), for instance, on..." звучит естественнее, чем накопительные цифры ("read over 20,000 times combined") — последнее читается как самореклама/маркетинг, а не как реальная реплика в разговоре. Выбирать САМУЮ релевантную для конкретной вакансии статью и давать одну ссылку, не список из двух-трёх заголовков.
6. **EU citizenship — короткой практичной фразой**, не отдельным блоком.
7. **Финал — открытое, не давящее приглашение** ("Happy to share more detail... whichever is more useful for you"), не переспрашивать конкретные архитектурные детали в первом сообщении.

### Правила для cover-letter (второй шаг, более развёрнуто)

- Можно и нужно называть конкретные технологии/архитектурные детали — читатель уже заинтересован и, вероятно, технический (или пересылает hiring manager'у).
- Можно ссылаться на конкретные факты due diligence (раунд, инвесторы), но по-прежнему не в первом же предложении — начинать тоже с естественного интереса, потом переходить к конкретике.
- Более уместно детально разбирать архитектурные параллели (Docling/Context Graph и т.п.) — здесь это ожидаемый уровень детализации.

**Итог:** одна и та же фактура (проекты/навыки/публикации) — но hi-letter и cover-letter не должны быть дублирующими друг друга текстами разной длины. Это два разных регистра для двух разных читателей на двух разных этапах воронки.

## Хронология опыта (реальная, для CV — с анонимизацией по правилам выше)

| Период | Роль | Компания (как писать) | Стек |
|---|---|---|---|
| 2025-11 – 2026-07 | Realtime Communications Engineer | a US logistics-tech company (client engagement) | TypeScript, Node.js, Redis, WebSocket, Jambonz, NetSapiens |
| 2025-10 – 2026-03 | AI Platform Engineer | a German AI SaaS company (Leipzig) | Python, FastAPI, React, PostgreSQL, Azure |
| 2025-04 – 2025-09 | Senior AI/ML Engineer | a US-based EdTech company (San Francisco) | Google ADK, Vertex AI, Gemini, TypeScript, Python |
| 2023-04 – Present | Co-Founder & CTO | **ASRP** (named directly) | Vue, Nuxt, LangChain/LangGraph, Docker, Node.js, PyTorch |
| 2021-07 – 2023-04 | Team Lead / Sr. Backend Dev (dual role, same group) | MOB.325 / LAB325 (Ukraine) | Node.js, GraphQL, Docker, K8s*, AWS, ClickHouse |
| 2020-08 – 2021-04 | Team Lead | Coelix (Tel Aviv, remote) | Laravel, Vue, PHP |
| 2021-03 – 2021-07 | Sr. Backend Dev | Provectus (San Francisco) | PHP, Laravel, Node.js |
| 2020-02 – 2020-07 | Full Stack Dev | Ephyros (Kyiv) | PHP, Laravel, Vue |
| 2018-09 – 2020-02 | Full Stack Dev | HYS Enterprise (Odesa) | WordPress, React |
| 2018-01 – 2018-09 | Full Stack Dev | Top Agent (Odesa) | PHP |
| 2017-07 – 2017-12 | Full Stack Dev | PHP-academy (Kyiv) | PHP |
| 2016-06 – 2016-11 | Backend Dev | SuperMediaAds | PHP |

*K8s listed publicly for 2021-2023 window — see caveat above, don't lean on this in interviews.

## Проекты (реальные, для CV Projects-секции)

**⚠️ Важная поправка (2026-07-22): Cogit и AI_ORG — ОБА принадлежат клиентскому engagement'у с Osnova (German AI SaaS company), НЕ собственные продукты ASRP.** Ранее в этом файле и в уже сгенерированных документах (interloom/cv.md и т.д.) Cogit ошибочно описывался как "продукт ASRP" — это неверно, нужно исправить везде, где уже написано. Правильная структура по факту (из [asrp-portfolio-public](https://github.com/AdvancedScientificResearchProjects/asrp-portfolio-public) и публичного профиля, таблица "By Company"):
- **Osnova (German AI SaaS company)** → Cogit SaaS (customer-facing agent-operations слой) + AI_ORG (backend платформа для dynamic agents) + ProOrder AI — это ОДИН client engagement с несколькими компонентами, работа выполнялась через/в рамках ASRP как исполнителя (contract), но продукт принадлежит Osnova.
- **ASRP (собственные продукты холдинга)** → Arcanum12th / Arcanum Landing Engine, ASRP Media, ASRP.science, Global Forecasting System (GFS), ASRP Ecosystem.
- **WireBee (US logistics-tech company)** → WireBee Phone Platform, AI Voice Agent, Cloud PBX Integration, Smart Queue.
- **Woolf (US-based EdTech company)** → AI CV Matcher.

Правильный список для CV:

- **Cogit + AI_ORG** (client engagement, German AI SaaS company — работа велась через ASRP как исполнителя, продукт принадлежит клиенту) — multi-tenant AI-organizations platform: Cogit — customer-facing agent-operations слой (NestJS+React+PostgreSQL, row-level security, agents on Gemini+Claude); AI_ORG — Python/FastAPI backend для dynamic agents, tool registries, tenant-safe execution. Top contributor (~45%) across both core repos, owned staging→production release flow.
- **Arcanum Landing Engine** (ASRP, собственный продукт) — full-cycle AI course-landing system, 4 repos (OpenAI agent, GraphQL backend, Nuxt editor, Nuxt renderer), live at arcanum12th.education, 14 courses/locales.
- **AI Voice Agent** (client engagement, US logistics-tech company) — conversational voice-AI for inbound carrier calls, 4-channel AI↔backend integration, non-hallucinating by construction.
- **Cloud PBX Integration** (client engagement, US logistics-tech company) — largest project of the engagement, self-healing reconciliation layer, SIP-Call-ID correlation.
- **Global Forecasting System (GFS)** (ASRP, собственный продукт) — LangChain-based forecasting platform, first prototype built at Theta EuroCon hackathon Berlin (Sep 2025).
- **AI CV Matcher** (client engagement, US-based EdTech company) — LLM-agent for educational assessment, Google ADK/Vertex AI.
- **Resume Matcher** (personal/published project) — tRPC + TypeScript + Google Vertex AI, PDF resume parsing + job matching.

**Как формулировать в CV/письмах, чтобы не звучало странно:** "Cogit"/"AI_ORG" — упоминать как "a multi-tenant AI-organizations platform I built for a German AI SaaS company" (не "at ASRP"). Роль в ASRP (Co-Founder & CTO) остаётся общим фреймингом карьеры, но конкретно Cogit/AI_ORG — заслуга внутри client engagement, не собственный продукт холдинга.

## Полный каталог публикаций (23 записи) — что можно использовать в job-заявках, что нет

Источник: [github.com/Kapustin2000/Kapustin2000/tree/master/publications](https://github.com/Kapustin2000/Kapustin2000/tree/master/publications). 11 технических статей (разобраны построчно ниже) + 6 popular science + 4 research publications + 1 academic paper + 1 media mention.

**⚠️ КЛЮЧЕВОЕ ПРАВИЛО.** Публикации делятся на две группы по применимости к обычным (не-ASRP) job-заявкам:

### ✅ Безопасно использовать в job-заявках (обычные tech-компании)

| Кластер | Публикации |
|---|---|
| **AI Agents & Infrastructure** | Google ADK Custom Interface · MVP LLM Agent on Google ADK · Google ADK Startup Guide · AI Agent Infrastructure |
| **Applied AI & NLP** | Docling in Working with Texts · Resume Matcher with tRPC · App Store Review Analysis |
| **Local & Voice AI** | How a Call Works in Programmable Telephony · LM Studio Local LLM Guide · Voice AI Systems Powered by Jambonz |
| **Software Market Research** | Software Development Tools in the Job Market (academic paper, 2018) |

Это ровно те же 11 технических статей, разобранные подробно ниже.

### 🚫 НЕ упоминать в обычных job-заявках (ASRP consciousness-research — другая аудитория)

| Кластер | Публикации |
|---|---|
| **GFS, Forecasting & Blockchain** | Banchenko Forecasting · GMS and GFS Right-Brain Technologies · Economics of Dreams · (AI & Blockchain Hackathon — искл., см. ниже) |
| **Lucid Dreaming & Consciousness** | AI and Lucid Dreaming · Pet Project to Research 2023/2024 · Dream Synchronization · Lucid Dreams and VR |
| **Neurotechnology & Future Interfaces** | Future Technologies · BCI in HR · Lucid Dreams and VR · GMS/GFS Right-Brain |
| **Health & Biofeedback Research** | Clinical Validation of the Inspira-X System |

**Почему:** эти публикации — реальная научная работа ASRP (анализ снов, коллективное бессознательное, BCI, лайт исследования дыхания), аутентичная миссии холдинга, но для обычного tech-рекрутера/hiring manager в SaaS/product-компании это прозвучит как минимум неожиданно, в худшем случае — как псевдонаука, подрывающая доверие к остальному резюме. Не использовать эти заголовки/ссылки/детали в CV, cover letter или hi-letter для стандартных вакансий (весь список из 22 обычных applications).

**⚠️ Особый случай — GFS (Global Forecasting System).** Уже упоминается в нескольких письмах (Seeking Alpha, DualEntry, 6037) как "a LangChain-based forecasting platform, first prototype built at a hackathon in Berlin". **Это упрощение — намеренно, не обман:** GFS по факту анализирует контент снов/коллективное бессознательное для форкастинга (см. Banchenko-Technology). Уровень абстракции "forecasting platform" — честный (это действительно forecasting-платформа на LangChain), просто не углубляться в источник сигнала (dream content), если не спросят прямо. **Не добавлять деталей про сны/коллективное бессознательное в письма для обычных компаний** — если на интервью спросят "как именно вы форкастите", тогда решать по ситуации, что и как раскрывать.

**Когда МОЖНО использовать consciousness-research кластеры:** только для ASRP-related контекста (бизнес-девелопмент, партнёрства, инвесторы, разговор с кем-то, кто уже знает про ASRP и её миссию) — не для личных job-заявок в это раздел `applications/`.

## Публикации — полный разбор (11 статей, прочитаны целиком, не только README-аннотации)

Для каждой — что внутри конкретно и для каких вакансий/тем это сильный аргумент.

### [Building AI Agent Infrastructure: Three Paths from Chaos to Scalable Systems](https://habr.com/en/articles/960154/) — 10k+ views (Habr/Medium, окт 2025)
Соавтор: Kyryl Zmiienko (Senior AI/ML Engineer, ASRP). **Основана на реальном клиентском кейсе** (немецкий рынок, клиент не назван в самой статье — уже анонимизировано автором) — большой монорепо инструментов для агентов без registry/версионирования. Разбирает 3 архитектурных пути:
1. **Filesystem Registry with Lazy Loading** — с примером кода `ToolRegistry` (Python, `importlib`), быстрое MVP-решение
2. **Package Manager & Modular Tool Ecosystem** — инструменты как независимые пакеты (`pdf-toolset`, `image-processing`) с собственным registry
3. **AgentOps Infrastructure (MCP & A2A)** — агенты как автономные сервисы, Model Context Protocol + Agent-to-Agent протокол, "microservice-like" зрелость
**Лучшая статья для:** Interloom (context/registry архитектура), N-iX/Sigma Software (agent factories, tool registries), любая вакансия про масштабирование agent-систем.

### [Docling in Working with Texts, Languages, and Knowledge](https://habr.com/en/articles/935584/) — 13.9k views (авг 2025)
Контекст: разработка **ASRP.science** (научный журнал нового поколения) — автоматизация парсинга академических документов. Разбирает **Docling** — граф-ориентированное представление знаний: документ становится сетью узлов (`DocItem`) с `label`, `text`, `links` — parent-child, semantic ("related-to", "supports", "contradicts"), alignment links. Пример кода: LangChain-агент, который запрашивает у Docling-документа структурированные метаданные через MRKL-подход (агент не читает весь текст, а "спрашивает" граф). Реальный пример метаданных из статьи ASRP про forecasting (DOI, authors, keywords).
**Лучшая статья для:** Interloom (**прямая параллель** с их Context Graph/Source→Canonical→Projection — знание как граф узлов, не как vector store), ChatRevenue.ai (knowledge graphs/NetworkX), Datagrok-типа компаний (не в личном списке, но для ASRP-контекста).

### [Google ADK and "Startup Technical Guide: AI Agents"](https://habr.com/en/articles/953592/) — 5.3k views (окт 2025)
Разбор 64-страничного гайда Google Cloud по AI-агентам, 5 инсайтов: (1) агенты — не чат-боты, а планирующие/действующие системы; (2) нужна полная инфраструктура, не только LLM; (3) **Grounding** — RAG → GraphRAG → Agentic RAG, чтобы бороться с галлюцинациями; (4) **AgentOps** — 4-слойное тестирование (component/trajectory/outcome/system monitoring), "vibe-testing" не работает в продакшне; (5) security — defense-in-depth, prompt-injection защита, Secure AI Framework.
**Лучшая статья для:** N-iX (LLMOps guardrails, prompt-injection defense — прямое совпадение с пунктом 5), Sigma Software (AI Compass, ISO 42001/EU AI Act — пункт 5), Interloom/DualEntry (non-hallucination — пункт 3), демонстрирует глубокое понимание production AI standards, не только "написал промпт".

### [My Personal Exam: How I Built an MVP LLM Agent on Google ADK](https://habr.com/en/articles/942696/) — 7.8k views (сен 2025)
Контекст: Woolf (EdTech, оценка знаний). Архитектурная эволюция от монолитного `LlmAgent` к модульной системе: `SequentialAgent`/`ParallelAgent` для координации этапов, `AgentTool` (агент как инструмент для другого агента), reviewer-агент для валидации перед выдачей ответа, `temperature=0` для детерминированных ответов в критичных местах, `output_key` для передачи данных между агентами без дублирования текста. **10 уроков** в конце (делегируй через агентов, планируй архитектуру с учётом токенов, добавляй feedback/валидацию и т.д.). Также рефлексия про эволюцию роли CTO (от чистого кода к найму/делегированию/бюджетам).
**Лучшая статья для:** любая multi-agent вакансия — самый детальный практический разбор архитектурных паттернов (не только философия, но конкретные классы ADK).

### [How to Integrate Google ADK with a Custom Interface](https://habr.com/en/articles/933804/) — 10.4k views (июл-авг 2025)
Технический tutorial: `adk web` → `adk api_server` (полный FastAPI сервер под капотом) → deployment через Vertex AI Agent Engine (`reasoning_engines.AdkApp`, `agent_engines.create`). Разбирает Agent Engine API (`create_session`, `stream_query`, `async_stream_query`), архитектуру "proxy backend" для production-интеграции (авторизация, фильтрация ответов, логирование, session state).
**Лучшая статья для:** роли, где важен полный production deployment cycle агента (Interloom, N-iX, Sigma FDE), демонстрирует, что опыт не ограничен experimentation, а доходит до реального deployment.

### [Building a Resume Matcher with tRPC, NLP, and Vertex AI](https://habr.com/en/articles/943306/) — 24k+ reads (сен 2025, **вторая по популярности статья**)
tRPC end-to-end typesafe API + PDF text extraction + базовый NLP (`natural` + `compromise` для tokenization/POS-tagging) для skill extraction + Gemini 1.5 Flash для структурированной оценки соответствия резюме/вакансии (JSON с `score`, `strengths`, `suggestions`). Честная рефлексия о лимитах: tRPC тесно связывает фронт с этой конкретной реализацией, нет built-in кэширования.
**Лучшая статья для:** DualEntry (структурированный анализ документов, LLM output укоренён в извлечённой структуре, не свободный текст), ChatRevenue.ai (structured JSON output pattern).

### [Building an App Store Review Analysis Pipeline with Python NLP & Data Visualization](https://kapustinomm.hashnode.dev/building-an-app-store-review-analysis-pipeline-with-python-nlp-and-data-visualization) (84 views, но контентно сильная — окт 2025)
Модульный (не monolithic-agent) pipeline: FastAPI → App Store RSS fetcher (без платного API) → text cleaning (ftfy, BeautifulSoup) → **VADER sentiment + гибридная формула `0.6*text_sentiment + 0.4*star_rating`** → TF-IDF keyword/issue extraction с категоризацией (Payment/Performance/Trust) → insights engine с severity scoring. Явный архитектурный выбор: **детерминированный модульный pipeline вместо end-to-end AI-агента** — "sacrifices reproducibility... deterministic design ensures consistent, auditable results... essential for research-level reliability".
**Лучшая статья для:** **Seeking Alpha** (Quant Ratings = превращение текста/данных в структурированный, тестируемый сигнал — практически тот же класс задачи) — сильнейший аргумент для этой конкретной вакансии, сильнее, чем GFS-хакатон (см. осторожность про GFS ниже).

### [My First AI & Blockchain Hackathon: Building the Global Forecasting System at Theta EuroCon in Berlin](https://habr.com/en/articles/947040/) — 5.3k views (сен 2025)
GFS — forecasting-система, анализирующая **сны и данные коллективного бессознательного**, сопоставляя их с новостями/котировками/DEFCON-уровнями (основана на "Banchenko-Technology", публикация 2024). Позиционируется как конкурент BlackRock Aladdin. Технически: web-интерфейс + Telegram-бот + AI-модель анализа снов + media search (проверка, "манифестируются" ли сны в реальных новостях) + "Kapustin Markers Algorithm" для паттерн-матчинга.
**⚠️ Осторожность:** тема снов/коллективного бессознательного — аутентична миссии ASRP (consciousness research), но может звучать неубедительно/псевдонаучно для консервативной корпоративной аудитории (особенно Seeking Alpha — серьёзный fintech). **Для внешних писем лучше упоминать GFS абстрактно** ("forecasting platform aggregating multi-source signals", "hackathon prototype for a forecasting system") **без деталей про сны**, если аудитория не готова к этому контексту. Для App Store Review Analysis статьи — совсем не нужно упоминать эту связь, она стоит сама по себе.

### [How to Run LLMs Locally with LM Studio: Complete Guide 2026](https://habr.com/en/articles/1005054/) — **38.6k views (самая читаемая статья)**, фев 2026
LM Studio — desktop app для локального инференса LLM (llama.cpp/GGUF на Windows/Linux, Apple MLX на M-чипах), MCP tool-call интеграция, OpenAI-совместимые REST эндпоинты, RAG/embeddings локально. Мотивация — полностью локальный AI-стек без зависимости от корпоративных API.
**Лучшая статья для:** роли с акцентом на приватность/self-hosting (Interloom явно self-host'ит модели на GPU — прямая параллель), демонстрация самой широкой аудитории (38.6k) как показатель технического авторитета в целом.

### [Voice AI Systems Powered by Jambonz: From Telephony to Human–Machine Dialogue](https://habr.com/en/articles/958670/) — 7.6k views (окт 2025)
Личная деталь: закончил Одесскую национальную академию связи им. А.С. Попова (телекоммуникации). PSTN/SIP/SIP trunk → Jambonz → backend → AI: полный разбор verbs (`say`, `gather`, `dial`, `hangup`), примеры кода webhook-обработчиков, dialog loop с LLM.
**Не релевантно для текущих 10 компаний** (ни одна не телеком/voice-AI фокус), но полезно, если появятся telecom/voice-AI вакансии в будущем поиске.

### [How a Call Works in Programmable Telephony: Inbound, Outbound, Leg A, and Leg B](https://habr.com/en/articles/1050446/) — июн 2026
Углублённый разбор одного звонка на уровне бэкенда: Leg A/Leg B, bridge, `activeCallId`, состояние звонка. Прямая параллель с WireBee-опытом (Cloud PBX Integration).
**Не релевантно для текущих 10 компаний** — как и предыдущая, держать про запас для telecom-специфичных вакансий.

## Проекты — доп. деталь по ASRP.science (для контекста Docling-статьи)

ASRP.science — научный журнал нового поколения, для которого разрабатывался Docling-based пайплайн парсинга академических документов (граф узлов вместо плоского текста, экспорт для peer-review и LLM-пайплайнов).

## Образование / работа

- Master's, Automation and Computer-Integrated Technologies, State University of Intelligent Technologies and Telecommunications (2017–2022)
- **EU citizenship — no visa/work-permit sponsorship needed anywhere in the EU.** Это отдельная строка, которую стоит явно указывать в CV (не прятать внутри общей фразы про remote-eligibility) — практически значимый плюс для любой EU-based компании (Interloom, N-iX, Sigma Software, CodeTiburon и т.д.), снимает вопрос спонсорства визы/разрешения на работу с самого начала разговора.
- Work authorization: EU citizenship + fully remote-eligible; access to US market via American entity, Asian markets via Kazakhstan-based entity.
- Berlin-based (physical location, EU citizen).

## Навыки — честная группировка (без переоценки)

- **Языки:** TypeScript/JavaScript (5+ yrs), Python (3 yrs), PHP (5 yrs, 2016-2021), SQL
- **Frontend:** Vue.js/Nuxt.js/Pinia (3-6 yrs), React (2 yrs, older), Angular (2 yrs, older)
- **Backend:** Node.js (5 yrs), FastAPI (1 yr), Laravel (2 yrs, older), GraphQL, tRPC, WebSockets
- **AI/ML:** LangChain/LangGraph (3 yrs, production), Google ADK/Vertex AI/Gemini (1 yr), OpenAI/GPT-4, multi-agent systems, PyTorch
- **Cloud/DevOps:** Docker (5 yrs), Terraform (3 yrs), CI/CD (5 yrs), AWS/GCP/Azure (mixed depth) — **Kubernetes: НЕ заявлять как реальный навык** (см. правило выше)
- **Databases:** PostgreSQL (6 yrs), Redis (5 yrs), MongoDB (2 yrs, older), Pinecone, Elasticsearch/ClickHouse (2 yrs, older) — CV skills-grid line: "PostgreSQL, Redis, MongoDB, Pinecone" (2026-07-23: добавлен Pinecone по запросу пользователя)
