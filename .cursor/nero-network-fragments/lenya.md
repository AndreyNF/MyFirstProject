=== ЛЁНЯ (SEO-АУДИТ) ===

## Аудит Лёни

**Статус:** ❌ НУЖНА ПЕРЕСБОРКА  
**URL:** https://advokat-vsem.online/arbitrazhnyj-processualnyj-srok-podacha/  
**page_id:** 419  
**slug:** `arbitrazhnyj-processualnyj-srok-podacha`  
**Дата:** 2026-05-29  
**Метод:** live HTML (curl), сверка с `kolya.md` и handoff B1/ARB

---

### Сводка

| Критерий | Результат |
|----------|-----------|
| Title | ✅ Совпадает с Колей (91 симв. с « - Legis 24») |
| Description (meta) | ❌ `<meta name="description">` отсутствует |
| Description (og/itemprop) | ✅ Текст Коли (~158 симв.) |
| H1 (целевой hero) | ✅ «…как не пропустить подачу и возражения» |
| H1 (дубль) | ❌ Второй H1 темы Divi в DOM |
| H2 структура | ✅ 9 блоков по плану Коли |
| FAQ | ✅ 7 вопросов, `#b1-faq`, microdata FAQPage |
| CTA | ✅ 4+ ссылки на `https://advokat-vsem.ru/` (hero + ym-cta + inline) |
| Внутр. перелинковка (тело) | ❌ 0 ссылок на смежные B1 `.online` |
| GEO microdata | ✅ `main` → Article; FAQ → FAQPage; `itemprop` description/headline |
| JSON-LD в контенте | ✅ Нет (по ТЗ Наташи); Rank Math WebPage/Breadcrumb — от темы |
| Slug / canonical | ✅ `arbitrazhnyj-processualnyj-srok-podacha`, canonical OK |
| robots | ✅ index, follow |

**Артефакты IndexLift:** пакет `skills/indexlift-seo-auditor/` в workspace не найден — аудит ручной по live HTML.

---

### Что исправить Юре

1. **Meta Description:** в Rank Math / excerpt страницы 419 прописать description из Коли; сейчас в `<head>` есть только `og:description` и `itemprop="description"`, тега `<meta name="description" content="…">` нет — риск для сниппета Яндекса.
2. **Дубль H1:** в разметке два `<h1>` — скрытый `entry-title main_title` (текст title) и видимый `hero-arb-srok__h1` (текст Коли). CSS скрывает header, но робот видит оба. Оставить один H1 (hero); заголовок записи WP → не `<h1>` (Divi: отключить title / заменить на `p`/`div` с `aria`).
3. **Внутренние ссылки:** в лонгриде нет перелинковки на смежные B1 из ядра Коли (`isk-v-arbitrazhe-pri-bankrotstve-kogda-podavat`, материалы по обжалованию/представителю). Добавить 2–3 контекстных `<a href="https://advokat-vsem.online/…">` в H2-2/H2-3/финале.

### Приоритет

- **Critical:** meta `name="description"`
- **High:** единственный H1 в DOM
- **Medium:** внутренняя перелинковка B1

### Пройдено без доработок

- Title, og:title, canonical, slug  
- Структура 9×H2 + H3 по `kolya.md`  
- FAQ 7/7 с FAQPage microdata  
- Article на `<main>`, CTA на advokat-vsem.ru  
- Excerpt в WP совпадает с og:description (нужно пробросить в meta description)
