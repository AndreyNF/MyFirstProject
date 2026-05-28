# Skill: visual-avito-images

Визуальный блок пайплайна Avito (MCP Kovcheg).

**Правила текста на изображении:** `shared/legis24-image-prompt-rules.md`

## Вход

`=== ПЕТРОВИЧ (КАРТОЧКА AVITO) ===` + ниша из ввода.

## Цепочка (канон)

```
I1: gpt-image-2 (text-to-image, 1:1, 1K)
  → при таймауте MCP: z-image
  → wordpress_upload_media (стабильный HTTPS на advokat-vsem.online)
```

Опционально (галерея 5–8 фото): flux2 → recraft → seedream — только если нужны варианты.

### I1 — gpt-image-2

- `aspect_ratio`: `1:1` (главное в XML), при галерее также `4:3`
- `resolution`: `1K`
- **Промпт** = **ниша объявления** (заголовок/услуга) + объекты + стиль + **русский текст**

**Шаблон промпта:**

```
{Ниша на английском для модели}: {объекты}. Russian tax legal documents on desk with readable Russian Cyrillic labels such as «Акт проверки», «Требование ФНС» — all document text in Russian only, no English words. Corporate navy blue office, soft daylight, photorealistic 1:1, no faces. Brand Legis24 optional.
```

**Запрещено в промпте:** `no text overlay` без уточнения про кириллицу — иначе модель рисует English.

**Хвост (всегда):** см. `legis24-image-prompt-rules.md` — Russian Cyrillic only, no English on papers.

### Хостинг

`wordpress_upload_media` после генерации → URL в `image_url` генератора XML.

## Итого в пакете

Минимум **1** URL на SKU; галерея — до 8.

## Выход

```markdown
=== ВИЗУАЛ-AVITO (ФОТО) ===
Статус: ✅ ГОТОВО
Ниша: ...
Промпт: ...

| # | URL | Назначение |
| 1 | ... | Главное 1:1 |
```

## Запреты

- Английские надписи на документах
- Лица реальных людей
- Чужие логотипы Avito
- Telegram (отдельный канал)
