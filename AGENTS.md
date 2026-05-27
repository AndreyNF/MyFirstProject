# AGENTS.md — Legis24 / MyFirstProject

## Два пайплайна

| Пайплайн | Директор | Продукт |
|----------|----------|---------|
| **Статьи** (лонгриды WP) | `director` (ветка `origin/cursor/a3-a2ec`) | Страница на advokat-vsem.ru |
| **Avito** (объявления) | `director-avito` | Карточка SKU + фото + пакет (без Telegram) |

Общий контекст бренда: `shared/legis24-site-context.md`.

## Avito — агенты и роли

```mermaid
flowchart LR
  subgraph input [Ввод]
    P[Петрович: ниша регион SKU]
  end
  subgraph semantic [Семантика MCP]
    W[wordstat_get_top_requests x10-15]
    D[wordstat_get_dynamics]
    R[wordstat_get_regions]
  end
  subgraph parallel [Параллельно]
    A[Артём: конкуренты Avito веб]
    K[Коля-режим: кластеры мета]
  end
  subgraph copy [Текст]
    Z[Женя-режим: описание CTA]
    Pet[Петрович: заголовки цена]
  end
  subgraph visual [Картинки MCP]
    I1[flux2-pro / nano_banana]
    I2[recraft: без фона]
    I3[seedream-edit: варианты]
  end
  subgraph out [Выдача]
    Pack[Пакет: ядро + 5-8 фото]
  end
  P --> W
  W --> K
  P --> A
  K --> Z
  A --> Z
  Z --> Pet
  Pet --> I1
  I1 --> I2
  I2 --> I3
  I3 --> Pack
```

| Агент | Файл | Skill |
|-------|------|-------|
| Директор Avito | `.cursor/agents/director-avito.md` | `avito-ad-pipeline` |
| **Петрович (Avito)** | `.cursor/agents/petrovich.md` | `avito-ad-pipeline` |
| Коля (Avito) | `.cursor/agents/seo-kolya-avito.md` | `seo-kolya-avito-mode` |
| Артём (Avito) | `.cursor/agents/artyom-avito.md` | `researcher-artyom-avito-mode` |
| Женя (Avito) | `.cursor/agents/zhenya-avito.md` | `seo-writer-zhenya-avito-mode` |
| Визуал | `.cursor/agents/visual-avito.md` | `visual-avito-images` |

Handoff: `.cursor/legis24-avito-handoff.md`  
Инструкция запуска: `avito/AUTOMATION.md`

## Разделение зон

| Задача | Кто |
|--------|-----|
| **Новая страница сайта** (лонгрид, WP) | `director` → Кирилл, Коля, Артём, Женя, Артур, Алина, Борис, Наташа, Юра, … (ветка `origin/cursor/a3-a2ec`) |
| **Avito** (объявление, карточка, API) | `director-avito` → **Петрович** и `*-avito` агенты |

Петрович касается **только взаимодействия с Avito**. Страницу на advokat-vsem.ru он не делает.

**Связка:** после статьи можно запустить `@director-avito` с нишей из H1 — объявление отдельно от лонгрида.

## Секреты

- Avito API: `Avito_client-id`, `Avito_client_secret`
- MCP Kovcheg: Wordstat, изображения (Telegram для Avito не использовать)
- Сайт: https://advokat-vsem.ru

## Cloud Agent

Ветки: `cursor/<name>-81c8`. Перед пайплайном Avito: `@director-avito` + ниша, регион, SKU.
