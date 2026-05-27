# Avito — автоматизация пайплайна Legis24

## Режим работы

Пользователь **просто пишет в чат** («освежи объявления», «добавь объявление про …», «смени цену»).  
Агент обновляет XML и **пушит на URL фида** — Avito подхватывает по ссылке. Ручная загрузка не нужна.

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

### Автозагрузка по URL (основной способ)

В кабинете Legis24 настроена **загрузка по ссылке**. Подробно: `avito/autoload/FEED-URL.md`.

**Канон XML:** `shared/legis24-avito-xml-rules.md`

```bash
python3 scripts/avito-generate-autoload-xml.py
git add avito/autoload/legis24-new-ads.xml && git commit -m "Update Avito feed" && git push
bash scripts/avito-print-feed-url.sh    # показать URL для кабинета
```

**URL фида (ветка `cursor/legis24-avito-pipeline-81c8`):**

`https://raw.githubusercontent.com/AndreyNF/MyFirstProject/cursor/legis24-avito-pipeline-81c8/avito/autoload/legis24-new-ads.xml`

После merge в `main` — та же ссылка с `/main/` в пути (стабильнее для Avito).

1. Проверка: https://autoload.avito.ru/format/xmlcheck/
2. Кабинет → Автозагрузка → Настройки → **загрузка по ссылке** → URL → расписание → Сохранить
3. Отчёт через ~1 ч в разделе «Автозагрузка»

Ручная загрузка файла — запасной вариант, если ссылка недоступна.

### API

`client_credentials` — только чтение объявлений; создание через API недоступно (404). Публикация — фид по URL.

Примеры текстов: `avito/seriya-novyh-obyavleniy-petrovich.md`

## MCP

| Этап | Инструменты |
|------|-------------|
| Семантика | `wordstat_get_top_requests`, `wordstat_get_dynamics`, `wordstat_get_regions` |
| Фото | `gpt-image-2` (основной), при таймауте `z-image` → `wordpress_upload_media` → `<Images>` в фиде |
| Telegram | **не использовать** (отдельный канал) |
