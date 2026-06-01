=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** `vs-obzor-5-2026-subsidiarnaya-otvetstvennost-kreditora`  
**Якорь:** `l24-boris-vs-obzor-subsidiar`  
**Размещение:** сразу после H2 «Субсидиарная ответственность при банкротстве по обзору: пункты 16–18» (перед H3-1).  
**Режим:** контраст к hero Алины — не canvas, горизонтальная «цепочка рисков» вместо полноэкранной сцены.  
**Отличия от Алины:** статический SVG-flowchart, узкая редакционная карта п. 16–18, без `<canvas>` и `<script>`.

```html
<section id="l24-boris-vs-obzor-subsidiar" class="l24-boris-vs-obzor" aria-label="Обзор ВС № 5/2026: три риска для кредитора — КДЛ, реестр и ст. 142">
<style>
.l24-boris-vs-obzor {
  --vs-ink: #1a0f14;
  --vs-plum: #2d1524;
  --vs-plum-soft: #3d1f32;
  --vs-copper: #c9782e;
  --vs-rose: #e879a9;
  --vs-sky: #7eb8da;
  --vs-sage: #6bc9a8;
  --vs-muted: #b8a8b0;
  margin: 44px 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-vs-obzor__shell {
  background: linear-gradient(118deg, var(--vs-ink) 0%, var(--vs-plum) 48%, var(--vs-plum-soft) 100%);
  border: 1px solid rgba(201, 120, 46, 0.32);
  border-radius: 14px;
  padding: 30px 26px 24px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05), 0 18px 48px rgba(26, 15, 20, 0.38);
}
.l24-boris-vs-obzor__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: var(--vs-copper);
}
.l24-boris-vs-obzor__title {
  margin: 0 0 10px;
  font-size: clamp(1.12rem, 2.3vw, 1.38rem);
  line-height: 1.28;
  color: #fff;
  font-weight: 700;
}
.l24-boris-vs-obzor__lead {
  margin: 0 0 22px;
  font-size: 0.94rem;
  line-height: 1.55;
  color: var(--vs-muted);
  max-width: 70ch;
}
.l24-boris-vs-obzor__lead strong { color: #fff; }
.l24-boris-vs-obzor__flow-wrap {
  background: rgba(0, 0, 0, 0.22);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 10px;
  padding: 16px 14px 10px;
  margin-bottom: 18px;
  overflow-x: auto;
}
.l24-boris-vs-obzor__flow-svg {
  display: block;
  width: 100%;
  min-width: 520px;
  height: auto;
}
.l24-boris-vs-obzor__risks {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-vs-obzor__risk {
  margin: 0;
  padding: 12px 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.24);
  border-left: 3px solid var(--vs-rose);
  font-size: 0.76rem;
  line-height: 1.42;
  color: #d4c4cc;
}
.l24-boris-vs-obzor__risk:nth-child(2) { border-left-color: var(--vs-sky); }
.l24-boris-vs-obzor__risk:nth-child(3) { border-left-color: var(--vs-sage); }
.l24-boris-vs-obzor__risk strong {
  display: block;
  color: #fff;
  font-size: 0.78rem;
  margin-bottom: 4px;
}
.l24-boris-vs-obzor__risk-tag {
  display: inline-block;
  margin-bottom: 6px;
  padding: 2px 7px;
  border-radius: 4px;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  background: rgba(201, 120, 46, 0.18);
  color: var(--vs-copper);
}
.l24-boris-vs-obzor__foot {
  margin-top: 14px;
  padding-top: 12px;
  border-top: 1px dashed rgba(201, 120, 46, 0.35);
  font-size: 0.8rem;
  line-height: 1.45;
  color: var(--vs-muted);
}
.l24-boris-vs-obzor__foot em { color: #f0d4e4; font-style: normal; }
@media (max-width: 720px) {
  .l24-boris-vs-obzor__risks { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-vs-obzor__shell">
    <p class="l24-boris-vs-obzor__eyebrow">Обзор ВС № 5/2026 · п. 16–18 · 127-ФЗ</p>
    <h3 class="l24-boris-vs-obzor__title">Три риска в одной процедуре: от «кредитора» до срока по ст. 142</h3>
    <p class="l24-boris-vs-obzor__lead">Верховный суд связывает позиции <strong>п. 16–18</strong> в одну цепочку: сначала — был ли кредитор <strong>КДЛ</strong> и причинил ли вред; затем — куда относить требование о субсидиарке (<strong>реестр</strong> или ошибочно <strong>текущие</strong>); наконец — <strong>2 месяца</strong> на включение в реестр банкрота-КДЛ с момента заявления о субсидиарке, а не суда по должнику.</p>

    <div class="l24-boris-vs-obzor__flow-wrap" role="group" aria-label="Схема: кредитор → КДЛ → реестр или текущие → ст. 142">
      <svg class="l24-boris-vs-obzor__flow-svg" viewBox="0 0 720 168" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="vs-boris-flow-title vs-boris-flow-desc">
        <title id="vs-boris-flow-title">Три риска обзора ВС: кредитор, КДЛ, реестр и ст. 142</title>
        <desc id="vs-boris-flow-desc">Горизонтальная цепочка: кредитор, контролирующее лицо по пункту 16, развилка реестрового и текущего требования по пункту 17, срок два месяца по статье 142 по пункту 18.</desc>
        <defs>
          <linearGradient id="vs-boris-lane" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#2d1524"/>
            <stop offset="100%" stop-color="#1a0f14"/>
          </linearGradient>
          <marker id="vs-boris-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
            <path d="M0 0 L8 4 L0 8 Z" fill="#c9782e"/>
          </marker>
        </defs>
        <rect x="4" y="4" width="712" height="160" rx="12" fill="url(#vs-boris-lane)" stroke="#5a3a4a" stroke-width="1"/>

        <!-- lane -->
        <line x1="48" y1="84" x2="672" y2="84" stroke="#5a3a4a" stroke-width="1.5" stroke-dasharray="6 5" opacity="0.55"/>

        <!-- 1 Кредитор -->
        <rect x="24" y="52" width="96" height="64" rx="10" fill="#3d1f32" stroke="#e879a9" stroke-width="2"/>
        <text x="72" y="78" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">Кредитор</text>
        <text x="72" y="96" text-anchor="middle" fill="#e879a9" font-size="9">банк / мажоритар</text>
        <path d="M120 84 H148" stroke="#c9782e" stroke-width="2.2" fill="none" marker-end="url(#vs-boris-arr)"/>

        <!-- 2 КДЛ п.16 -->
        <rect x="148" y="44" width="108" height="80" rx="10" fill="#4a2238" stroke="#c9782e" stroke-width="2"/>
        <text x="202" y="72" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">КДЛ</text>
        <text x="202" y="90" text-anchor="middle" fill="#c9782e" font-size="9" font-weight="600">п. 16 обзора</text>
        <text x="202" y="106" text-anchor="middle" fill="#b8a8b0" font-size="8">контроль + вред</text>
        <path d="M256 84 H284" stroke="#c9782e" stroke-width="2.2" fill="none" marker-end="url(#vs-boris-arr)"/>

        <!-- 3 fork hub -->
        <circle cx="318" cy="84" r="22" fill="#2d1524" stroke="#7eb8da" stroke-width="2"/>
        <text x="318" y="80" text-anchor="middle" fill="#7eb8da" font-size="8" font-weight="700">п. 17</text>
        <text x="318" y="94" text-anchor="middle" fill="#fff" font-size="8">реестр?</text>

        <!-- реестр -->
        <path d="M340 68 L408 48" stroke="#7eb8da" stroke-width="2" fill="none" marker-end="url(#vs-boris-arr)"/>
        <rect x="408" y="28" width="118" height="44" rx="8" fill="#1f3a4a" stroke="#7eb8da" stroke-width="1.8"/>
        <text x="467" y="48" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">Реестровое</text>
        <text x="467" y="62" text-anchor="middle" fill="#7eb8da" font-size="8">вред до банкротства</text>

        <!-- текущие -->
        <path d="M340 100 L408 120" stroke="#e879a9" stroke-width="2" fill="none" marker-end="url(#vs-boris-arr)"/>
        <rect x="408" y="108" width="118" height="44" rx="8" fill="#3d1f32" stroke="#e879a9" stroke-width="1.8" stroke-dasharray="5 3"/>
        <text x="467" y="128" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">Текущие</text>
        <text x="467" y="142" text-anchor="middle" fill="#e879a9" font-size="8">ошибка ВС отверг</text>

        <!-- merge to ст.142 -->
        <path d="M526 50 L562 84" stroke="#6bc9a8" stroke-width="1.8" fill="none"/>
        <path d="M526 130 L562 84" stroke="#6bc9a8" stroke-width="1.8" fill="none"/>
        <path d="M562 84 H588" stroke="#6bc9a8" stroke-width="2.2" fill="none" marker-end="url(#vs-boris-arr)"/>

        <!-- 4 ст.142 -->
        <rect x="588" y="44" width="108" height="80" rx="10" fill="#1a3328" stroke="#6bc9a8" stroke-width="2"/>
        <text x="642" y="72" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">ст. 142</text>
        <text x="642" y="90" text-anchor="middle" fill="#6bc9a8" font-size="9" font-weight="600">п. 18 · 2 мес.</text>
        <text x="642" y="106" text-anchor="middle" fill="#b8a8b0" font-size="8">реестр КДЛ</text>

        <text x="72" y="28" text-anchor="middle" fill="#e879a9" font-size="8" font-weight="600">старт</text>
        <text x="642" y="28" text-anchor="middle" fill="#6bc9a8" font-size="8" font-weight="600">срок</text>
      </svg>
    </div>

    <ul class="l24-boris-vs-obzor__risks">
      <li class="l24-boris-vs-obzor__risk">
        <span class="l24-boris-vs-obzor__risk-tag">п. 16</span>
        <strong>Кредитор как КДЛ</strong>
        Конкурсный кредитор, фактически управлявший должником и причинивший вред другим кредиторам, может быть привлечён к субсидиарной ответственности — даже если суды ссылались на отсутствие «конкретных решений».
      </li>
      <li class="l24-boris-vs-obzor__risk">
        <span class="l24-boris-vs-obzor__risk-tag">п. 17</span>
        <strong>Реестр vs текущие</strong>
        Если основание субсидиарки возникло до возбуждения дела о банкротстве должника, требование реестровое: момент причинения вреда важнее даты судебного акта.
      </li>
      <li class="l24-boris-vs-obzor__risk">
        <span class="l24-boris-vs-obzor__risk-tag">п. 18</span>
        <strong>Ст. 142 — 2 месяца</strong>
        При банкротстве КДЛ АУ подконтрольного лица подаёт заявление о включении в реестр КДЛ в срок п. 1 ст. 142 — от заявления о субсидиарке, не от решения по организации-должнику; цессия не спасает пропуск.
      </li>
    </ul>

    <p class="l24-boris-vs-obzor__foot"><em>Цепочка «должник → КДЛ»:</em> ошибка на любом звене (КДЛ, реестр/текущие, пропуск 2 мес.) обнуляет стратегию защиты долга в арбитражном деле о банкротстве.</p>
  </div>
</section>
```

**Чеклист отличий от hero Алины**
- [x] Не полноэкранный блок; в теле статьи после H2-2
- [x] Свой `id`: `l24-boris-vs-obzor-subsidiar` (не hero canvas)
- [x] Без `<canvas>` и `<script>` — только inline CSS + SVG
- [x] Горизонтальный flowchart «кредитор → КДЛ → реестр|текущие → ст. 142», не сцена hero
