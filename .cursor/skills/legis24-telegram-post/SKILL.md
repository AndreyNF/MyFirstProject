# Skill: legis24-telegram-post

Посты Legis24 в Telegram. MCP: **`gpt-image-2`** → при сбое **`nano_banana_2`**; `telegram_send_photo`.

Правила изображений: `shared/legis24-image-prompt-rules.md`

## Обязательно

1. **Хештеги** — 5–10 в конце, всегда `#Legis24`
2. CTA: order@advokat-vsem.ru, https://advokat-vsem.ru
3. Без гарантии «победы в суде»
4. Цены из `shared/legis24-site-context.md`

## Промпт обложки = **название поста**

**Референс:** заголовок поста (строка `<b>…</b>`) **дословно** в начале промпта.

### Модели (только)

1. `gpt-image-2` — `aspect_ratio` **16:9**, `resolution` **2K**
2. При таймауте/ошибке — `nano_banana_2` (те же параметры, `output_format` png)

**Не использовать:** z-image, flux, seedream и др.

### Шаблон промпта

```
Post title reference: «{НАЗВАНИЕ ПОСТА КАК В TELEGRAM}». Visual scene for this title: {2-3 объекта из текста поста}. Professional Legis24 legal office, navy blue, 16:9 photorealistic. Russian Cyrillic text on documents only. No English words on papers. No human faces.
```

### Публикация

- Telegram: **tempfile URL** из ответа MCP (не WP — часто 400)
- `chat_id` **1332429170** или из `telegram_get_updates` после `/start`
- `parse_mode`: HTML, caption ≤ 1024 символа

## Структура поста

Заголовок → 2–3 абзаца → оффер/цена → CTA → хештеги

## Артефакт

`content/telegram/{slug}.md` — **Название поста**, текст, URL обложки, модель (gpt-image-2 / nano_banana_2)
