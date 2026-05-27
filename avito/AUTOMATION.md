# Avito — автоматизация пайплайна Legis24

## Быстрый старт

Запрос пользователю Cloud Agent:

```
@director-avito
Ниша: возражение на акт ФНС
Регион: вся РФ
SKU: vozrazhenie-fns-rf
```

## Шаги (Директор)

1. Сброс `.cursor/legis24-avito-handoff.md`
2. `Task(petrovich)` — ввод
3. `Task(seo-kolya-avito)` — Wordstat 10–15 + dynamics + regions
4. Параллельно `Task(artyom-avito)` — конкуренты Avito
5. `Task(zhenya-avito)` — описание
6. `Task(petrovich)` — заголовок ≤50, цена
7. `Task(visual-avito)` — 5–8 фото (MCP)
8. Сбор `avito/out/{sku}.md` + `telegram_send_message`

## Выходной файл

Шаблон `avito/out/{sku}.md`:

```markdown
# {Заголовок}
Цена: {N} ₽
SKU: {sku}

## Описание
...

## SEO-ядро (кратко)
...

## Фото
1. ...
```

## Ручная публикация

API Avito для создания объявлений ограничен; после пакета — загрузка в кабинет Legis24 или автозагрузка.

Примеры готовых текстов: `avito/seriya-novyh-obyavleniy-petrovich.md`

## MCP

| Этап | Инструменты |
|------|-------------|
| Семантика | `wordstat_get_top_requests`, `wordstat_get_dynamics`, `wordstat_get_regions` |
| Фото | `flux2-pro-text-to-image`, `recraft_remove_background`, `seedream-4_5-edit` |
| Превью | `telegram_send_message` |
