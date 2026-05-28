=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**Slug:** `isk-o-zashchite-is-protiv-vas-plan-otveta`  
**Режим:** продолжение IP-темы Алины (ответчик, иск, 214-ФЗ) — тёмный редакционный блок в теле; hero остаётся светлым «план ответа», Борис даёт **дерево решений 2026** и шкалу первых 14 дней.

**Вставка для Наташи:** заменяет маркер `<!-- BORIS_ANCHOR -->` сразу после H2 «Ответ на иск и возражение на исковое заявление» (после подразделов про отзыв и встречные требования), **перед** CTA Артура и H2 «Защита при иске о нарушении товарного знака». Главный CTA (консультация по отзыву) — **сразу после** закрывающего `</section>` Бориса.

**Техника:** только inline `<style>` + static SVG; **без** `<canvas>`, **без** `<script>`.

```html
<section id="l24-boris-ip-plan-b2" class="l24-boris-ip-plan-b2" aria-label="Иск по ИС против вас: дерево решений 2026 и календарь ответчика">
<style>
.l24-boris-ip-plan-b2 {
  --b2-navy: #0f2744;
  --b2-navy-soft: #1a365d;
  --b2-blue: #63b3ed;
  --b2-gold: #ecc94b;
  --b2-teal: #4fd1c5;
  --b2-accent: #fc8181;
  --b2-mint: #68d391;
  --b2-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-ip-plan-b2__shell {
  background: linear-gradient(148deg, var(--b2-navy) 0%, #122640 52%, var(--b2-navy-soft) 100%);
  border: 1px solid rgba(99, 179, 237, 0.24);
  border-radius: 14px;
  padding: 32px 28px 28px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06), 0 20px 52px rgba(15, 39, 68, 0.32);
  color: #e2e8f0;
}
.l24-boris-ip-plan-b2__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--b2-gold);
}
.l24-boris-ip-plan-b2__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-ip-plan-b2__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--b2-muted);
  max-width: 70ch;
}
.l24-boris-ip-plan-b2__lead strong { color: #fff; }
.l24-boris-ip-plan-b2__split {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.98fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-ip-plan-b2__panel {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-ip-plan-b2__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--b2-gold);
}
.l24-boris-ip-plan-b2__tree-svg,
.l24-boris-ip-plan-b2__timeline-svg {
  display: block;
  width: 100%;
  height: auto;
}
.l24-boris-ip-plan-b2__tree-svg { max-height: 200px; margin-bottom: 12px; }
.l24-boris-ip-plan-b2__timeline-svg { max-height: 118px; margin-bottom: 14px; }
.l24-boris-ip-plan-b2__branches {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-ip-plan-b2__branch {
  margin: 0;
  padding: 10px 9px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.22);
  border-top: 3px solid var(--b2-blue);
  font-size: 0.76rem;
  line-height: 1.4;
  color: #cbd5e0;
}
.l24-boris-ip-plan-b2__branch:nth-child(2) { border-top-color: var(--b2-gold); }
.l24-boris-ip-plan-b2__branch:nth-child(3) { border-top-color: var(--b2-teal); }
.l24-boris-ip-plan-b2__branch:nth-child(4) { border-top-color: var(--b2-mint); }
.l24-boris-ip-plan-b2__branch strong {
  display: block;
  color: #fff;
  font-size: 0.8rem;
  margin-bottom: 4px;
}
.l24-boris-ip-plan-b2__days {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  margin: 0 0 14px;
  padding: 0;
  list-style: none;
}
.l24-boris-ip-plan-b2__day {
  margin: 0;
  padding: 10px 8px;
  text-align: center;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.72rem;
  line-height: 1.35;
}
.l24-boris-ip-plan-b2__day strong {
  display: block;
  font-size: 1rem;
  color: var(--b2-gold);
  margin-bottom: 2px;
}
.l24-boris-ip-plan-b2__levers {
  display: grid;
  grid-template-columns: 1fr;
  gap: 8px;
}
.l24-boris-ip-plan-b2__lever {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 12px;
  align-items: start;
  padding: 12px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.08);
}
.l24-boris-ip-plan-b2__lever--refuse { border-left: 3px solid var(--b2-mint); }
.l24-boris-ip-plan-b2__lever--reduce { border-left: 3px solid var(--b2-gold); }
.l24-boris-ip-plan-b2__lever--1486 { border-left: 3px solid var(--b2-blue); }
.l24-boris-ip-plan-b2__lever-tag {
  font-size: 0.65rem;
  font-weight: 800;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  padding: 5px 8px;
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  white-space: nowrap;
}
.l24-boris-ip-plan-b2__lever-title {
  margin: 0 0 4px;
  font-size: 0.84rem;
  font-weight: 700;
  color: #fff;
}
.l24-boris-ip-plan-b2__lever-text {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--b2-muted);
}
.l24-boris-ip-plan-b2__lever-text em {
  font-style: normal;
  color: var(--b2-teal);
  font-weight: 600;
}
.l24-boris-ip-plan-b2__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-ip-plan-b2__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
  color: #e2e8f0;
}
.l24-boris-ip-plan-b2__tag--ok { border: 1px solid var(--b2-mint); color: #9ae6b4; }
.l24-boris-ip-plan-b2__tag--sum { border: 1px solid var(--b2-gold); color: #faf089; }
.l24-boris-ip-plan-b2__tag--tz { border: 1px solid var(--b2-blue); color: #bee3f8; }
.l24-boris-ip-plan-b2__caption {
  margin: 14px 0 0;
  font-size: 0.74rem;
  line-height: 1.45;
  color: var(--b2-muted);
}
@media (max-width: 900px) {
  .l24-boris-ip-plan-b2__split { grid-template-columns: 1fr; }
  .l24-boris-ip-plan-b2__branches { grid-template-columns: 1fr; }
  .l24-boris-ip-plan-b2__days { grid-template-columns: repeat(2, 1fr); }
}
</style>

  <div class="l24-boris-ip-plan-b2__shell">
    <p class="l24-boris-ip-plan-b2__eyebrow">214-ФЗ · ст. 131 АПК · ответчик 2026</p>
    <h3 class="l24-boris-ip-plan-b2__title" id="l24-anchor-ip-decision-tree-2026">Дерево решений и первые 14 дней: отказ, снижение компенсации, ст. 1486</h3>
    <p class="l24-boris-ip-plan-b2__lead">После вручения иска не выбирайте одну линию «на глаз»: слева — <strong>развилка защиты</strong> (отказ в иске vs оспаривание суммы vs встречный иск). Справа — <strong>календарь 0–14</strong> и три рычага 2026: <strong>отказ</strong> (КС № 57-П при повторной 2× компенсации), <strong>снижение</strong> (ст. 1252.1, п. 7, 28-П), <strong>ст. 1486</strong> (неиспользование ТЗ истца).</p>

    <div class="l24-boris-ip-plan-b2__split">
      <div class="l24-boris-ip-plan-b2__panel">
        <p class="l24-boris-ip-plan-b2__panel-title">Развилка: что заявлять в отзыве</p>
        <svg class="l24-boris-ip-plan-b2__tree-svg" viewBox="0 0 520 196" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <defs>
            <linearGradient id="b2-ip-tree-stem" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#63b3ed"/>
              <stop offset="100%" stop-color="#4fd1c5"/>
            </linearGradient>
          </defs>
          <rect x="196" y="8" width="128" height="34" rx="8" fill="#c53030" stroke="#fff" stroke-width="1.5"/>
          <text x="260" y="30" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">Иск по ИС получен</text>
          <line x1="260" y1="42" x2="260" y2="58" stroke="url(#b2-ip-tree-stem)" stroke-width="3"/>
          <line x1="72" y1="58" x2="448" y2="58" stroke="#63b3ed" stroke-width="2.5" stroke-linecap="round"/>
          <line x1="72" y1="58" x2="72" y2="72" stroke="#68d391" stroke-width="2"/>
          <line x1="200" y1="58" x2="200" y2="72" stroke="#ecc94b" stroke-width="2"/>
          <line x1="328" y1="58" x2="328" y2="72" stroke="#4fd1c5" stroke-width="2"/>
          <line x1="448" y1="58" x2="448" y2="72" stroke="#63b3ed" stroke-width="2"/>
          <rect x="16" y="72" width="112" height="52" rx="7" fill="rgba(104,211,145,0.2)" stroke="#68d391"/>
          <text x="72" y="92" text-anchor="middle" fill="#9ae6b4" font-size="8" font-weight="700">Нет права / нет</text>
          <text x="72" y="106" text-anchor="middle" fill="#e2e8f0" font-size="8">нарушения / давность</text>
          <text x="72" y="168" text-anchor="middle" fill="#68d391" font-size="8" font-weight="600">→ отказ в иске</text>
          <rect x="144" y="72" width="112" height="52" rx="7" fill="rgba(236,201,75,0.15)" stroke="#ecc94b"/>
          <text x="200" y="92" text-anchor="middle" fill="#faf089" font-size="8" font-weight="700">Состав спорен</text>
          <text x="200" y="106" text-anchor="middle" fill="#e2e8f0" font-size="8">сходство, объект</text>
          <text x="200" y="168" text-anchor="middle" fill="#ecc94b" font-size="8" font-weight="600">→ экспертиза</text>
          <rect x="272" y="72" width="112" height="52" rx="7" fill="rgba(79,209,197,0.15)" stroke="#4fd1c5"/>
          <text x="328" y="92" text-anchor="middle" fill="#b2f5ea" font-size="8" font-weight="700">Компенсация</text>
          <text x="328" y="106" text-anchor="middle" fill="#e2e8f0" font-size="8">завышена</text>
          <text x="328" y="168" text-anchor="middle" fill="#4fd1c5" font-size="8" font-weight="600">→ 1252.1 · 57-П</text>
          <rect x="392" y="72" width="112" height="52" rx="7" fill="rgba(99,179,237,0.18)" stroke="#63b3ed"/>
          <text x="448" y="92" text-anchor="middle" fill="#bee3f8" font-size="8" font-weight="700">Параллельно</text>
          <text x="448" y="106" text-anchor="middle" fill="#e2e8f0" font-size="8">ст. 1486 ТЗ</text>
          <text x="448" y="168" text-anchor="middle" fill="#63b3ed" font-size="8" font-weight="600">→ 2 мес + 30 дн.</text>
          <path d="M 260 124 Q 260 140 72 140" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1" stroke-dasharray="4 3"/>
          <path d="M 260 124 Q 260 140 328 140" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1" stroke-dasharray="4 3"/>
        </svg>
        <ul class="l24-boris-ip-plan-b2__branches">
          <li class="l24-boris-ip-plan-b2__branch">
            <strong>Отказ в иске</strong>
            Нет прав у истца, иное обозначение, прекращение до иска, нарушен претензионный порядок (п. 5.1 ст. 1252).
          </li>
          <li class="l24-boris-ip-plan-b2__branch">
            <strong>Оспорить состав</strong>
            Нет смешения, иной способ (п. 1.1 ст. 1252), лицензия, исчерпание — ходатайство об экспертизе.
          </li>
          <li class="l24-boris-ip-plan-b2__branch">
            <strong>Смягчить сумму</strong>
            Смена способа расчёта, «один товар — одно нарушение», добросовестность (п. 7), КС № 28-П / 57-П.
          </li>
          <li class="l24-boris-ip-plan-b2__branch">
            <strong>Ст. 1486</strong>
            Встречный иск о прекращении ТЗ истца за неиспользование: претензия 2 мес., иск в 30 дней после отказа.
          </li>
        </ul>
      </div>

      <div class="l24-boris-ip-plan-b2__panel">
        <p class="l24-boris-ip-plan-b2__panel-title">Шкала 0–14 дней + три рычага 2026</p>
        <svg class="l24-boris-ip-plan-b2__timeline-svg" viewBox="0 0 520 110" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <defs>
            <linearGradient id="b2-ip-timeline" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#fc8181"/>
              <stop offset="35%" stop-color="#ecc94b"/>
              <stop offset="100%" stop-color="#68d391"/>
            </linearGradient>
          </defs>
          <line x1="40" y1="55" x2="480" y2="55" stroke="url(#b2-ip-timeline)" stroke-width="4" stroke-linecap="round"/>
          <circle cx="56" cy="55" r="16" fill="#c53030" stroke="#fff" stroke-width="2"/>
          <text x="56" y="60" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">0</text>
          <circle cx="178" cy="55" r="14" fill="#d69e2e" stroke="#fff" stroke-width="2"/>
          <text x="178" y="59" text-anchor="middle" fill="#1a202c" font-size="8" font-weight="700">3</text>
          <circle cx="300" cy="55" r="14" fill="#2b6cb0" stroke="#fff" stroke-width="2"/>
          <text x="300" y="59" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">7</text>
          <circle cx="464" cy="55" r="16" fill="#2f855a" stroke="#fff" stroke-width="2"/>
          <text x="464" y="60" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">14</text>
          <text x="56" y="28" text-anchor="middle" fill="#feb2b2" font-size="8" font-weight="600">kad + фиксация</text>
          <text x="178" y="28" text-anchor="middle" fill="#faf089" font-size="8" font-weight="600">претензия 30д</text>
          <text x="300" y="28" text-anchor="middle" fill="#90cdf4" font-size="8" font-weight="600">аудит ИС</text>
          <text x="464" y="28" text-anchor="middle" fill="#9ae6b4" font-size="8" font-weight="600">отзыв 131 АПК</text>
          <text x="56" y="88" text-anchor="middle" fill="#a0aec0" font-size="7">не удалять доказательства</text>
          <text x="464" y="88" text-anchor="middle" fill="#a0aec0" font-size="7">по каждому доводу</text>
        </svg>
        <ol class="l24-boris-ip-plan-b2__days" aria-label="Календарь ответчика">
          <li class="l24-boris-ip-plan-b2__day"><strong>0</strong>дата вручения, kad.arbitr.ru</li>
          <li class="l24-boris-ip-plan-b2__day"><strong>1–3</strong>материалы ст. 41 АПК</li>
          <li class="l24-boris-ip-plan-b2__day"><strong>3–7</strong>реестр ТЗ, лицензии</li>
          <li class="l24-boris-ip-plan-b2__day"><strong>7–14</strong>отзыв + ходатайства</li>
        </ol>
        <div class="l24-boris-ip-plan-b2__levers" aria-label="Три рычага защиты 2026">
          <div class="l24-boris-ip-plan-b2__lever l24-boris-ip-plan-b2__lever--refuse">
            <span class="l24-boris-ip-plan-b2__lever-tag">Отказ</span>
            <div>
              <p class="l24-boris-ip-plan-b2__lever-title">КС РФ № 57-П · серийные иски</p>
              <p class="l24-boris-ip-plan-b2__lever-text">При повторной <em>двукратной</em> компенсации за тот же товар суд вправе <em>отказать</em> или снизить ниже минимума — соберите решения и платежи по закрытым эпизодам.</p>
            </div>
          </div>
          <div class="l24-boris-ip-plan-b2__lever l24-boris-ip-plan-b2__lever--reduce">
            <span class="l24-boris-ip-plan-b2__lever-tag">Снизить</span>
            <div>
              <p class="l24-boris-ip-plan-b2__lever-title">Ст. 1252.1 · 214-ФЗ</p>
              <p class="l24-boris-ip-plan-b2__lever-text">Замена способа расчёта, один эпизод, коридор <em>10–500 тыс.</em> (п. 7), ниже 10 000 ₽ — КС № 28-П; Пленум ВС № 10 — разумность суммы.</p>
            </div>
          </div>
          <div class="l24-boris-ip-plan-b2__lever l24-boris-ip-plan-b2__lever--1486">
            <span class="l24-boris-ip-plan-b2__lever-tag">1486</span>
            <div>
              <p class="l24-boris-ip-plan-b2__lever-title">Неиспользование ТЗ истца</p>
              <p class="l24-boris-ip-plan-b2__lever-text">Встречный иск + переговоры: претензия <em>2 месяца</em>, иск в <em>30 дней</em> после отказа; практика СИП (СИП-1194/2022) при доказанном неиспользовании.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="l24-boris-ip-plan-b2__foot" aria-label="Связка стратегии и сроков">
      <span class="l24-boris-ip-plan-b2__tag l24-boris-ip-plan-b2__tag--ok">Отказ ≠ молчание до заседания</span>
      <span class="l24-boris-ip-plan-b2__tag l24-boris-ip-plan-b2__tag--sum">Снижение — только с математикой в отзыве</span>
      <span class="l24-boris-ip-plan-b2__tag l24-boris-ip-plan-b2__tag--tz">1486 — параллельно основной линии</span>
      <span class="l24-boris-ip-plan-b2__tag">Пропуск отзыва → риск взыскания по доводам истца</span>
    </div>
    <p class="l24-boris-ip-plan-b2__caption">Схема к разделу «Ответ на иск» — не заменяет юридическую консультацию; сроки уточняйте по определению суда и дате вручения.</p>
  </div>
</section>
```

**Паспорт блока**

| Поле | Значение |
|------|----------|
| `id` секции | `#l24-boris-ip-plan-b2` |
| Якорь TOC / Наташа | `#l24-anchor-ip-decision-tree-2026` (заголовок h3 внутри блока) |
| Класс корня | `l24-boris-ip-plan-b2` |
| Якорь вставки | `<!-- BORIS_ANCHOR -->` (замена, не дублировать комментарий в HTML) |
| Композиция | сплит: SVG-дерево решений + timeline 0–14 + карточки «отказ / снизить / 1486» |
| Hero Алины | не дублировать: без fullscreen, без тех же `id` |
| MCP | без `<script>` и `<canvas>` |

### Чеклист отличий от hero Алины

- [x] Не hero: блок в теле лонгрида (`margin: 48px 0`), не `min-height: 100vh`
- [x] Контраст: тёмный IP-navy + gold/teal (как A12/A9 Борис), hero — светлый «план ответа»
- [x] Тема продолжения: ответчик, иск, компенсация 2026 — углубление **стратегии**, не повтор hero-сцены
- [x] Редакционная обвязка: eyebrow, lead, split, ветки, рычаги, подпись, теги
- [x] Static SVG + inline CSS только
- [x] Уникальные префиксы и `id` градиентов (`b2-ip-tree-stem`, `b2-ip-timeline`)
- [x] Якорь Артура: вставка на месте `BORIS_ANCHOR`; CTA — после секции
