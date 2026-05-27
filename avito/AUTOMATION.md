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
8. Сбор `avito/out/{sku}.md` (без Telegram)

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

## Публикация (разрешено)

### Автозагрузка XML (основной способ)

**Канон:** `shared/legis24-avito-xml-rules.md` — все новые объявления только по этому формату (проверено xmlcheck).

```bash
python3 scripts/avito-generate-autoload-xml.py
```

Файл: `avito/autoload/legis24-new-ads.xml` (8 новых объявлений).

Обязательные поля (дубль в rules-файле, эталон №8159283806):
- `ServiceType` → `Деловые услуги`
- `ServiceSubtype` → `Юридические услуги`
- `ServiceSubspecies` → `Составление договоров, доверенностей, исков`
- `Prepayment` → `Нужна`
- `WorkWithContract` → `Да`
- `Consultations` → `Нет`
- `Place` → `Удалённо`
- `WorkExperience` → `4–7 лет`

1. Откройте https://www.avito.ru/professionals/autoload (или «Автозагрузка» в кабинете).
2. Проверка: https://autoload.avito.ru/format/xmlcheck/
3. «Настройки» → ручная загрузка → выберите XML → «Загрузить».
4. Смотрите отчёт через ~1 час.

### API

Текущие ключи (`client_credentials`) дают **чтение** объявлений; создание через API возвращает 404 — нужны расширенные scope в приложении Avito или автозагрузка.

Примеры текстов: `avito/seriya-novyh-obyavleniy-petrovich.md`

## MCP

| Этап | Инструменты |
|------|-------------|
| Семантика | `wordstat_get_top_requests`, `wordstat_get_dynamics`, `wordstat_get_regions` |
| Фото | `flux2-pro-text-to-image`, `recraft_remove_background`, `seedream-4_5-edit` |
| Telegram | **не использовать** (отдельный канал) |
