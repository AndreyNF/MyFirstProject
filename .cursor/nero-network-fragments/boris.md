=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** `vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns`  
**Якорь:** `l24-boris-vs4-asset-matrix`  
**Размещение:** сразу после H2 «Движимое vs недвижимое имущество: позиция ВС и риски переквалификации» (после 2–3 секций H2, перед H2 «Оборудование или сооружение: кейсы ГЭС и производственных линий») — якорь для Natasha.  
**Режим:** тёмная панель в теле статьи (контраст со светлым hero Алины) — **матрица классификации активов** по обзору ВС № 4/2026: движимое vs недвижимое vs сооружение → налог / освобождение в арбитражном споре с ФНС.  
**Legis24 MCP-only:** static SVG + inline CSS, без `<canvas>` и `<script>`.

```html
<section id="l24-boris-vs4-asset-matrix" class="l24-boris-vs4-asset-matrix" aria-label="Матрица активов по обзору ВС № 4/2026: движимое, недвижимое и сооружение в споре о налоге на имущество организаций">
<style>
.l24-boris-vs4-asset-matrix {
  --vs4-navy: #0f1c2e;
  --vs4-navy-soft: #1a3050;
  --vs4-movable: #48bb78;
  --vs4-movable-dim: #276749;
  --vs4-immovable: #4299e1;
  --vs4-structure: #ed8936;
  --vs4-fns: #fc8181;
  --vs4-gold: #ecc94b;
  --vs4-ink: #e2e8f0;
  --vs4-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-vs4-asset-matrix__shell {
  background: linear-gradient(155deg, var(--vs4-navy) 0%, #152a45 50%, var(--vs4-navy-soft) 100%);
  border: 1px solid rgba(66, 153, 225, 0.28);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: 0 18px 48px rgba(15, 28, 46, 0.34);
  color: var(--vs4-ink);
}
.l24-boris-vs4-asset-matrix__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--vs4-gold);
}
.l24-boris-vs4-asset-matrix__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-vs4-asset-matrix__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--vs4-muted);
  max-width: 72ch;
}
.l24-boris-vs4-asset-matrix__lead strong { color: #fff; }
.l24-boris-vs4-asset-matrix__split {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-vs4-asset-matrix__panel {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-vs4-asset-matrix__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--vs4-gold);
}
.l24-boris-vs4-asset-matrix__scheme-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 320px;
  margin-bottom: 12px;
}
.l24-boris-vs4-asset-matrix__legend {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 0 0 12px;
  padding: 0;
  list-style: none;
}
.l24-boris-vs4-asset-matrix__legend-item {
  margin: 0;
  padding: 10px 9px;
  background: rgba(0, 0, 0, 0.22);
  border-radius: 8px;
  border-top: 3px solid var(--vs4-movable);
  font-size: 0.72rem;
  line-height: 1.38;
}
.l24-boris-vs4-asset-matrix__legend-item:nth-child(2) { border-top-color: var(--vs4-immovable); }
.l24-boris-vs4-asset-matrix__legend-item:nth-child(3) { border-top-color: var(--vs4-structure); }
.l24-boris-vs4-asset-matrix__legend-item strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-vs4-asset-matrix__verdict {
  margin: 0;
  padding: 12px 14px;
  border-radius: 8px;
  background: rgba(236, 201, 75, 0.12);
  border: 1px solid rgba(236, 201, 75, 0.38);
  font-size: 0.78rem;
  line-height: 1.45;
  color: var(--vs4-ink);
}
.l24-boris-vs4-asset-matrix__verdict strong { color: var(--vs4-gold); }
.l24-boris-vs4-asset-matrix__caption {
  margin: 10px 0 0;
  font-size: 0.7rem;
  line-height: 1.4;
  color: rgba(160, 174, 192, 0.88);
  text-align: center;
}
.l24-boris-vs4-asset-matrix__matrix {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 0 0 12px;
}
.l24-boris-vs4-asset-matrix__row {
  display: grid;
  grid-template-columns: minmax(0, 0.85fr) minmax(0, 0.55fr) minmax(0, 1.1fr);
  gap: 8px 10px;
  align-items: start;
  padding: 10px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.74rem;
  line-height: 1.38;
}
.l24-boris-vs4-asset-matrix__row--movable { border-left: 3px solid var(--vs4-movable); }
.l24-boris-vs4-asset-matrix__row--immovable { border-left: 3px solid var(--vs4-immovable); }
.l24-boris-vs4-asset-matrix__row--structure { border-left: 3px solid var(--vs4-structure); }
.l24-boris-vs4-asset-matrix__row-label {
  font-weight: 700;
  color: #fff;
  font-size: 0.78rem;
}
.l24-boris-vs4-asset-matrix__row-tax {
  font-weight: 700;
  font-size: 0.72rem;
  padding: 3px 7px;
  border-radius: 4px;
  text-align: center;
  align-self: start;
}
.l24-boris-vs4-asset-matrix__row-tax--no {
  background: rgba(72, 187, 120, 0.2);
  color: #9ae6b4;
  border: 1px solid rgba(72, 187, 120, 0.45);
}
.l24-boris-vs4-asset-matrix__row-tax--yes {
  background: rgba(252, 129, 129, 0.18);
  color: #fed7d7;
  border: 1px solid rgba(252, 129, 129, 0.45);
}
.l24-boris-vs4-asset-matrix__row-tax--risk {
  background: rgba(237, 137, 54, 0.18);
  color: #fbd38d;
  border: 1px solid rgba(237, 137, 54, 0.45);
}
.l24-boris-vs4-asset-matrix__row-text { color: var(--vs4-muted); }
.l24-boris-vs4-asset-matrix__row-text em {
  font-style: normal;
  color: #fff;
  font-weight: 600;
}
.l24-boris-vs4-asset-matrix__vs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 0 0 10px;
}
.l24-boris-vs4-asset-matrix__vs-card {
  padding: 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.72rem;
  line-height: 1.4;
}
.l24-boris-vs4-asset-matrix__vs-card--fns { border-color: rgba(252, 129, 129, 0.45); }
.l24-boris-vs4-asset-matrix__vs-card--np { border-color: rgba(72, 187, 120, 0.45); }
.l24-boris-vs4-asset-matrix__vs-card strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-vs4-asset-matrix__note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--vs4-muted);
}
.l24-boris-vs4-asset-matrix__note em {
  font-style: normal;
  color: #bee3f8;
  font-weight: 600;
}
.l24-boris-vs4-asset-matrix__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-vs4-asset-matrix__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--vs4-ink);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.l24-boris-vs4-asset-matrix__tag--case {
  border-color: rgba(236, 201, 75, 0.5);
  color: var(--vs4-gold);
}
.l24-boris-vs4-asset-matrix__tag--art { border-color: rgba(66, 153, 225, 0.45); color: #bee3f8; }
.l24-boris-vs4-asset-matrix__tag--def { border-color: rgba(72, 187, 120, 0.45); color: #c6f6d5; }
@media (max-width: 900px) {
  .l24-boris-vs4-asset-matrix__split { grid-template-columns: 1fr; }
  .l24-boris-vs4-asset-matrix__legend { grid-template-columns: 1fr; }
  .l24-boris-vs4-asset-matrix__row { grid-template-columns: 1fr; gap: 4px; }
  .l24-boris-vs4-asset-matrix__row-tax { justify-self: start; }
  .l24-boris-vs4-asset-matrix__vs { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-vs4-asset-matrix__shell">
    <p class="l24-boris-vs4-asset-matrix__eyebrow">гл. 30 НК РФ · обзор ВС № 4/2026 · письмо ФНС № БС-36-21/3766@ · 29.04.2026</p>
    <h3 class="l24-boris-vs4-asset-matrix__title">Матрица активов: движимое, недвижимое и сооружение</h3>
    <p class="l24-boris-vs4-asset-matrix__lead">С 2019 года объект налога на имущество организаций — только <strong>недвижимость</strong> (п. 1 ст. 374 НК РФ), но единых налоговых критериев движимое/недвижимое закон не содержит. Обзор ВС № 4/2026 и письмо ФНС от 07.05.2026 задают логику переквалификации: <strong>отдельные ОС</strong> → освобождение; <strong>здания и сооружения</strong> → доначисление; <strong>серая зона сооружений</strong> — спор без записи в ЕГРН.</p>

    <div class="l24-boris-vs4-asset-matrix__split">
      <div class="l24-boris-vs4-asset-matrix__panel">
        <p class="l24-boris-vs4-asset-matrix__panel-title">Три типа активов → исход в арбитражном споре с ФНС</p>
        <svg class="l24-boris-vs4-asset-matrix__scheme-svg" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="vs4-scheme-title vs4-scheme-desc">
          <title id="vs4-scheme-title">Матрица классификации активов по обзору ВС № 4/2026 для налога на имущество организаций</title>
          <desc id="vs4-scheme-desc">Три колонки — движимое, недвижимое и сооружение — сходятся к блоку арбитражного спора; движимое освобождается, недвижимое облагается, сооружение зависит от капитальности и бремени доказывания ФНС</desc>
          <defs>
            <linearGradient id="vs4-flow" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#48bb78"/>
              <stop offset="50%" stop-color="#4299e1"/>
              <stop offset="100%" stop-color="#ed8936"/>
            </linearGradient>
            <marker id="vs4-arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0,0 L8,4 L0,8 Z" fill="#ecc94b"/>
            </marker>
            <pattern id="vs4-grid" width="10" height="10" patternUnits="userSpaceOnUse">
              <path d="M10 0 L0 0 0 10" fill="none" stroke="rgba(66,153,225,0.2)" stroke-width="0.5"/>
            </pattern>
          </defs>

          <text x="300" y="18" text-anchor="middle" fill="#ecc94b" font-size="8" font-weight="600">Классификация актива → налоговый исход (обзор 4/2026)</text>

          <!-- Движимое -->
          <rect x="20" y="32" width="168" height="118" rx="8" fill="rgba(39,103,73,0.35)" stroke="#48bb78" stroke-width="1.5"/>
          <text x="104" y="50" text-anchor="middle" fill="#9ae6b4" font-size="9" font-weight="700">ДВИЖИМОЕ</text>
          <rect x="36" y="60" width="48" height="36" rx="4" fill="rgba(0,0,0,0.25)" stroke="#68d391" stroke-width="1"/>
          <circle cx="60" cy="72" r="6" fill="none" stroke="#9ae6b4" stroke-width="1.5"/>
          <circle cx="72" cy="84" r="5" fill="none" stroke="#9ae6b4" stroke-width="1.5"/>
          <rect x="92" y="64" width="80" height="28" rx="3" fill="rgba(0,0,0,0.2)"/>
          <text x="132" y="76" text-anchor="middle" fill="#e2e8f0" font-size="7">линия розлива</text>
          <text x="132" y="88" text-anchor="middle" fill="#e2e8f0" font-size="7">компрессор ГЭС</text>
          <text x="104" y="112" text-anchor="middle" fill="#a0aec0" font-size="7">ОКОФ «Машины и оборудование»</text>
          <text x="104" y="124" text-anchor="middle" fill="#a0aec0" font-size="7">отдельные инв. номера · п. 1, 8</text>
          <rect x="44" y="134" width="120" height="14" rx="3" fill="rgba(72,187,120,0.25)" stroke="#48bb78" stroke-width="1"/>
          <text x="104" y="144" text-anchor="middle" fill="#9ae6b4" font-size="7.5" font-weight="700">НЕ ОБЛАГАЕТСЯ</text>

          <!-- Недвижимое -->
          <rect x="216" y="32" width="168" height="118" rx="8" fill="rgba(49,130,206,0.28)" stroke="#4299e1" stroke-width="1.5"/>
          <text x="300" y="50" text-anchor="middle" fill="#bee3f8" font-size="9" font-weight="700">НЕДВИЖИМОЕ</text>
          <rect x="232" y="58" width="136" height="56" rx="4" fill="url(#vs4-grid)" stroke="#90cdf4" stroke-width="1"/>
          <rect x="248" y="72" width="28" height="20" rx="2" fill="rgba(66,153,225,0.4)" stroke="#bee3f8" stroke-width="0.8"/>
          <rect x="284" y="72" width="28" height="20" rx="2" fill="rgba(66,153,225,0.4)" stroke="#bee3f8" stroke-width="0.8"/>
          <rect x="320" y="72" width="28" height="20" rx="2" fill="rgba(66,153,225,0.4)" stroke="#bee3f8" stroke-width="0.8"/>
          <text x="300" y="68" text-anchor="middle" fill="#bee3f8" font-size="6.5">здание · цех</text>
          <text x="300" y="112" text-anchor="middle" fill="#a0aec0" font-size="7">запись в ЕГРН · кадастр</text>
          <text x="300" y="124" text-anchor="middle" fill="#a0aec0" font-size="7">п. 16–17 · жилые объекты</text>
          <rect x="260" y="134" width="80" height="14" rx="3" fill="rgba(252,129,129,0.22)" stroke="#fc8181" stroke-width="1"/>
          <text x="300" y="144" text-anchor="middle" fill="#fed7d7" font-size="7.5" font-weight="700">ОБЛАГАЕТСЯ</text>

          <!-- Сооружение -->
          <rect x="412" y="32" width="168" height="118" rx="8" fill="rgba(192,86,33,0.28)" stroke="#ed8936" stroke-width="1.5"/>
          <text x="496" y="50" text-anchor="middle" fill="#fbd38d" font-size="9" font-weight="700">СООРУЖЕНИЕ</text>
          <line x1="428" y1="100" x2="564" y2="100" stroke="#ed8936" stroke-width="3"/>
          <line x1="448" y1="72" x2="448" y2="108" stroke="#ed8936" stroke-width="2"/>
          <line x1="544" y1="72" x2="544" y2="108" stroke="#ed8936" stroke-width="2"/>
          <rect x="460" y="108" width="72" height="8" rx="2" fill="#c05621"/>
          <text x="496" y="68" text-anchor="middle" fill="#fbd38d" font-size="6.5">трубопровод · элеватор</text>
          <text x="496" y="112" text-anchor="middle" fill="#a0aec0" font-size="7">капстроительство · фундамент</text>
          <text x="496" y="124" text-anchor="middle" fill="#a0aec0" font-size="7">п. 5–6 · без ЕГРН возможно</text>
          <rect x="428" y="134" width="136" height="14" rx="3" fill="rgba(237,137,54,0.22)" stroke="#ed8936" stroke-width="1"/>
          <text x="496" y="144" text-anchor="middle" fill="#fbd38d" font-size="7.5" font-weight="700">СПОР · БРЕМЯ НА ФНС</text>

          <!-- Convergence arrows -->
          <path d="M 104 158 L 104 182 L 300 182 L 300 200" stroke="#48bb78" stroke-width="2" fill="none" marker-end="url(#vs4-arrow)"/>
          <path d="M 300 158 L 300 182" stroke="#4299e1" stroke-width="2" fill="none"/>
          <path d="M 496 158 L 496 182 L 300 182" stroke="#ed8936" stroke-width="2" fill="none"/>

          <!-- Arbitration block -->
          <rect x="140" y="204" width="320" height="40" rx="8" fill="rgba(0,0,0,0.35)" stroke="url(#vs4-flow)" stroke-width="1.5"/>
          <text x="300" y="220" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="700">Арбитражный спор с ФНС · гл. 25 АПК</text>
          <text x="300" y="234" text-anchor="middle" fill="#a0aec0" font-size="7.5">ОКОФ · инв. карточки · проектная документация · бремя доказывания</text>

          <!-- FNS vs NP outcomes -->
          <rect x="60" y="254" width="200" height="36" rx="6" fill="rgba(252,129,129,0.18)" stroke="#fc8181" stroke-width="1.2"/>
          <text x="160" y="270" text-anchor="middle" fill="#fed7d7" font-size="7.5" font-weight="600">ФНС: переквалификация в сооружение</text>
          <text x="160" y="282" text-anchor="middle" fill="#feb2b2" font-size="7">п. 5–7 · единый объект · трубопроводы целиком</text>

          <rect x="340" y="254" width="200" height="36" rx="6" fill="rgba(72,187,120,0.18)" stroke="#48bb78" stroke-width="1.2"/>
          <text x="440" y="270" text-anchor="middle" fill="#c6f6d5" font-size="7.5" font-weight="600">Налогоплательщик: отдельные ОС</text>
          <text x="440" y="282" text-anchor="middle" fill="#9ae6b4" font-size="7">п. 1, 3, 8 · бухучёт и назначение актива</text>
        </svg>

        <ul class="l24-boris-vs4-asset-matrix__legend" aria-label="Три категории активов по обзору ВС № 4/2026">
          <li class="l24-boris-vs4-asset-matrix__legend-item">
            <strong>Движимое</strong>
            Технологическое оборудование, отдельные ОС на сч. 07/08. Монтаж на фундамент в цехе не лишает освобождения (п. 1).
          </li>
          <li class="l24-boris-vs4-asset-matrix__legend-item">
            <strong>Недвижимое</strong>
            Здания, помещения, объекты с кадастром. Облагаются по среднегодовой или кадастровой стоимости (п. 16–17).
          </li>
          <li class="l24-boris-vs4-asset-matrix__legend-item">
            <strong>Сооружение</strong>
            Капитальные объекты с признаками недвижимости — даже без ЕГРН. Элеваторы, трубопроводы на эстакадах (п. 5–6).
          </li>
        </ul>
        <p class="l24-boris-vs4-asset-matrix__verdict"><strong>Логика ВС:</strong> приоритет бухучёта (ОКОФ, инвентарные объекты) и целевого назначения актива над формальной связью с землёй; капитальность сооружения доказывает <strong>ФНС</strong> (ч. 5 ст. 200 АПК).</p>
        <p class="l24-boris-vs4-asset-matrix__caption">Схема по обзору ВС № 4/2026 (утв. 29.04.2026 № 6А/2026) · письмо ФНС № БС-36-21/3766@ от 07.05.2026</p>
      </div>

      <div class="l24-boris-vs4-asset-matrix__panel">
        <p class="l24-boris-vs4-asset-matrix__panel-title">Матрица классификации (чек-лист для арбитража)</p>
        <div class="l24-boris-vs4-asset-matrix__vs">
          <div class="l24-boris-vs4-asset-matrix__vs-card l24-boris-vs4-asset-matrix__vs-card--fns">
            <strong>Позиция ФНС</strong>
            Объединить оборудование в «комплекс сочленённых предметов» или сооружение; доначислить налог без учёта отдельных ОС (п. 6–7).
          </div>
          <div class="l24-boris-vs4-asset-matrix__vs-card l24-boris-vs4-asset-matrix__vs-card--np">
            <strong>Позиция налогоплательщика</strong>
            Сохранить раздельный бухучёт: инв. карточки, ОКОФ, договоры поставки как движимое, акты ввода (п. 1, 8).
          </div>
        </div>
        <div class="l24-boris-vs4-asset-matrix__matrix">
          <div class="l24-boris-vs4-asset-matrix__row l24-boris-vs4-asset-matrix__row--movable">
            <span class="l24-boris-vs4-asset-matrix__row-label">Движимое</span>
            <span class="l24-boris-vs4-asset-matrix__row-tax l24-boris-vs4-asset-matrix__row-tax--no">0%</span>
            <span class="l24-boris-vs4-asset-matrix__row-text">Линии розлива, станки, компрессоры ГЭС как <em>отдельные ОС</em>. Критерий «несоразмерного ущерба» при демонтаже — <em>не налоговый</em> (п. 2).</span>
          </div>
          <div class="l24-boris-vs4-asset-matrix__row l24-boris-vs4-asset-matrix__row--immovable">
            <span class="l24-boris-vs4-asset-matrix__row-label">Недвижимое</span>
            <span class="l24-boris-vs4-asset-matrix__row-tax l24-boris-vs4-asset-matrix__row-tax--yes">Налог</span>
            <span class="l24-boris-vs4-asset-matrix__row-text">Здания, МКД, гаражи — база по кадастру <em>вне зависимости от ВРИ земли</em> (п. 16). Незавершёнка с кадастром — тоже (п. 17).</span>
          </div>
          <div class="l24-boris-vs4-asset-matrix__row l24-boris-vs4-asset-matrix__row--structure">
            <span class="l24-boris-vs4-asset-matrix__row-label">Сооружение</span>
            <span class="l24-boris-vs4-asset-matrix__row-tax l24-boris-vs4-asset-matrix__row-tax--risk">Спор</span>
            <span class="l24-boris-vs4-asset-matrix__row-text">Элеватор без ЕГРН — недвижимость по факту (п. 5). Трубопроводы на эстакадах — <em>целиком</em> (п. 6). ЛЭП без фундаментов — движимость.</span>
          </div>
        </div>
        <p class="l24-boris-vs4-asset-matrix__note"><em>Граница п. 6 и п. 8:</em> ФНС присоединяет оборудование к сооружению или дробит единый объект — проверяйте каждый актив в возражениях (ст. 100 НК) и иске в арбитраж (ч. 4 ст. 198 АПК).</p>
      </div>
    </div>

    <div class="l24-boris-vs4-asset-matrix__foot" aria-label="Контекст обзора">
      <span class="l24-boris-vs4-asset-matrix__tag l24-boris-vs4-asset-matrix__tag--case">ВС № 4/2026 · № 6А/2026 · 29.04.2026</span>
      <span class="l24-boris-vs4-asset-matrix__tag l24-boris-vs4-asset-matrix__tag--art">гл. 30 НК · п. 1, 5–8 обзора</span>
      <span class="l24-boris-vs4-asset-matrix__tag l24-boris-vs4-asset-matrix__tag--def">Защита: ОКОФ + инв. карточки + проект</span>
    </div>
  </div>
</section>
```

**Чеклист отличий от hero Алины**
- [x] Не полноэкранный блок; в теле статьи после H2 «Движимое vs недвижимое…» (2–3 секция)
- [x] Свой `id`: `l24-boris-vs4-asset-matrix` (не hero `#l24-hero-…`)
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Тёмная панель — контраст со светлым hero Алины (налог на имущество / арбитраж с ФНС)
- [x] Сплит «схема трёх типов активов + исход в арбитраже | матрица классификации с налоговым статусом»
