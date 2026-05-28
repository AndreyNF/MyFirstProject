# Legis24 — правила промптов для генерации изображений (Avito + Telegram)

MCP: **`gpt-image-2`** (основной), при таймауте `z-image`.

## Русский текст на картинке (обязательно)

На документах, экранах, печатях, папках, табличках — **только русский язык (кириллица)**.

| Можно | Нельзя |
|-------|--------|
| «Акт камеральной проверки», «Требование ФНС», «Возражение», «Исковое заявление», «Налоговая инспекция» | Tax Act, Notice, Invoice, Legal Services |
| «Legis24» (бренд латиницей) | Random English paragraphs on papers |
| Размытый / мелкий текст без читаемого английского | Крупные English headlines |

**Хвост промпта (добавлять всегда):**

```
All visible text on documents and screens must be in Russian Cyrillic only. No English words on papers. Brand name Legis24 allowed in Latin. Photorealistic, no real human faces.
```

**Короткая версия:**

```
Russian Cyrillic text only on documents, no English words, no faces
```

## Тема поста / SKU (Telegram, Avito)

- **Telegram:** промпт строится от **темы поста** (см. `legis24-telegram-post/SKILL.md`)
- **Avito:** промпт от **ниши объявления** (заголовок / услуга)

## Техника

- Avito / TG feed: **1:1** главное фото; TG канал — **16:9**
- После генерации: `wordpress_upload_media` для стабильного URL в XML
- Telegram отправка: tempfile URL (WP иногда 400 у серверов Telegram)
