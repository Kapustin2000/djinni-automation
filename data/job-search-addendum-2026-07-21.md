# Расширенный поиск — новые ниши, 2026-07-21

Дополнение к [job-search-2026-07-20.md](job-search-2026-07-20.md). Только личный профиль. Новые `all_keywords`-запросы, не пробованные в первой сессии: fintech (шире форекса/гэмблинга), robotics/IoT, cybersecurity, data engineering + LLM, Berlin-локация, web3.

## Новые интересные находки

| Вакансия | Компания | Детали | Комментарий |
|---|---|---|---|
| Product Engineer (Onsite in Berlin) | **Telli** (найм через агентство PulseRise Technologies) | €85K-160K + equity, C1 англ. + **C1 немецкий**, офис в Берлине | AI voice-agent стартап (клиент — Sky), реально физически в Берлине. Но: (а) вакансия идёт через аутстафф-агентство PulseRise (Кипр) — реальный работодатель Telli, не PulseRise; (б) German C1 — блокер, не задокументирован в профиле; (в) культура интенсивная — «no code reviews», «ship to production day one», «work late for free dinner», не подходит под remote-first предпочтение |
| Backend Engineer / Senior Backend Engineer | **SUPERAGENT** | AI-native distribution layer for insurance ($7T рынок), C1, $$$$ | Найдено через поиск fintech backend. Ранняя стадия, стек и позиционирование близки к agentic AI, но deep diligence не делался |
| AI Head of Engineering / Backend Software Engineer (Java/Python) | **SpaceQuant** (продукт: Smart Capital Center) | AI-платформа для Commercial Real Estate, 2 открытые роли, A1 английский (низкий барьер) | AI Head of Engineering — необычно низкий языковой барьер (A1) для лид-роли; стоит проверить отдельно, почему |
| Data Engineer (Scraping, ETL, LLM Pipelines) | **JustSoftLab Inc.** | Real-time startup/investor data platform, C1, $$$$ | Прямое совпадение с LLM-pipeline опытом, не чистый DS |
| Senior Full-Stack Engineer (Node.js + React) with Web3 | **Upstaff** | до $6000, C1, 7 лет опыта | Стек совпадает (Node/React), но Web3-требование — разрыв в опыте |

## Что проверено и не дало нового

- **Robotics/IoT** (`all_keywords=robotics`) — 15 вакансий, почти все 🪖 DefTech (Miltech, NDA Robotics, Frontline Robotics, DroneOps) — подтверждает решение первой сессии не приоритизировать эту нишу, если явно не запрошено.
- **Cybersecurity** (`all_keywords=cybersecurity`) — 15 вакансий, в основном чистый security ops/sales, не fullstack+AI фит. Кроме уже известного Smirnov Labs (fintech, был в подборке).
- **Berlin-specific geo** (`all_keywords=Berlin`) — только 1 результат (Telli/PulseRise выше), других berlin-based находок нет за пределами уже известных Interloom/ONU Health.

## Методология

Поиск через `all_keywords` на Djinni (тот же недокументированный параметр формы поиска), один запрос на нишу, JS-экстракция карточек вакансий. Полных описаний вакансий не открывал, кроме Telli/PulseRise (для проверки локации/культуры). Данные на 2026-07-21.
