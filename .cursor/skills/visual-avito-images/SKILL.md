# Skill: visual-avito-images

Визуал Avito. Правила: `shared/legis24-image-prompt-rules.md`

## Модели (только)

1. **`gpt-image-2`** — 1:1, 1K
2. **`nano_banana_2`** — при таймауте gpt-image-2

**Запрещено:** z-image, flux, seedream, recraft.

## Референс = Title объявления

Промпт начинается с **заголовка Avito** (`<Title>`) дословно:

```
Ad title reference: «{Title из XML}». Visual scene for this ad: {ракурс 1|2|3}. ...
```

На SKU — **3 разных ракурса**, одно название.

## Шаблон

```
Ad title reference: «Возражение на акт ФНС — за 24 часа Legis24». Visual scene: {описание ракурса}. Russian Cyrillic on documents. Navy office, 1:1 photorealistic, no English, no faces.
```

## Хостинг

`wordpress_upload_media` → `image_urls` в `scripts/avito-generate-autoload-xml.py`

## Выход

`=== ВИЗУАЛ-AVITO (ФОТО) ===` — Title, модель, промпты, URLs.
