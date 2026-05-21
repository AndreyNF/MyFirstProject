# Обязательная проверка читаемости (MCP-публикация)

Перед финалом и **после каждой публикации** на advokat-vsem.online:

## 1. Reveal без JavaScript

Если из HTML убраны `<script>` (MCP blob, WP REST), **нельзя** оставлять:

```css
.reveal { opacity: 0; }
.reveal-left / .reveal-right / .reveal-scale { opacity: 0; }
```

Без IntersectionObserver весь контент с классом `reveal` **невидим** (hero часто без `reveal` — виден только первый экран, дальше «пусто»).

**Фикс в CSS Наташи:** по умолчанию `opacity: 1 !important; transform: none !important` для `.reveal*`, либо не вешать `reveal` на секции при MCP-only.

## 2. Быстрая проверка live (QA / Директор)

- `curl` live URL: в HTML есть `id="vvedenie"` или первый H2 лонгрида **вне** hero.
- В CSS страницы **нет** пары `.reveal { opacity: 0` без fallback на видимость.
- Визуально: не только hero + картинка; есть TOC, H2, CTA, блок Бориса.

## 3. Связанные сбои

- `<script>` в теле → WP может обрезать/ломать HTML; скрипты убирать, контент не прятать через opacity.
- После republish — Ctrl+F5 / проверка без кэша.
