=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО
ЯКОРЬ: l24-boris-vs-prodazha-kvartiry-evidence

## Паспорт блока

| Параметр | Значение |
|----------|----------|
| **Статья** | Обзор ВС РФ 01.07.2026 — продажа квартиры под влиянием мошенников: уголовные риски ст. 159, защита на проверке и в суде |
| **SLUG** | `vs-prodazha-kvartiry-moshenniki-st-159-zashchita-2026` |
| **Якорь** | `l24-boris-vs-prodazha-kvartiry-evidence` |
| **Тема** | Горизонтальная «карта двух контуров»: гражданское оспаривание (ст. 178–179 ГК) ↔ уголовная ответственность (ст. 159, 33 УК) — матрица «знал / должен был знать» |
| **Размещение** | После H2 «Ст. 178–179 ГК РФ и ст. 159 УК: гражданское оспаривание и уголовная защита» — перед H2 «Риски для покупателя квартиры: знал или должен был знать» |
| **Режим** | Контраст к hero Алины: редакционная матрица в теле статьи, не полноэкранная сцена; MCP-only — inline CSS + static SVG, без `<canvas>` и `<script>` |
| **Палитра** | Тёмный navy `#0a1628`–`#152a45`; гражданский контур: indigo `#6366f1` / `#a5b4fc`; уголовный: crimson `#dc2626` / `#fca5a5`; ВС: gold `#ecc94b`; жильё: teal `#2dd4bf` |

## Чеклист отличий от hero Алины

- [x] Не полноэкранный первый экран — блок в теле лонгрида
- [x] Другой `id`: `l24-boris-vs-prodazha-kvartiry-evidence` (не hero-id Алины)
- [x] Горизонтальная сплит-карта «ст. 179 ГК ↔ ст. 159 УК» — не дублирует сцену hero
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG + grid
- [x] CTA в блоке **не вставлять**

```html
<section id="l24-boris-vs-prodazha-kvartiry-evidence" class="l24-boris-vs-prodazha-kvartiry" aria-label="Матрица гражданского оспаривания ст. 179 ГК и уголовной ответственности ст. 159 УК при продаже квартиры под влиянием мошенников">
<style>
.l24-boris-vs-prodazha-kvartiry {
  --bk-navy: #0a1628;
  --bk-navy-soft: #152a45;
  --bk-civil: #6366f1;
  --bk-civil-soft: #a5b4fc;
  --bk-civil-bg: rgba(99, 102, 241, 0.14);
  --bk-crim: #dc2626;
  --bk-crim-soft: #fca5a5;
  --bk-crim-bg: rgba(220, 38, 38, 0.12);
  --bk-gold: #ecc94b;
  --bk-teal: #2dd4bf;
  --bk-muted: #94a3b8;
  --bk-txt: #e2e8f0;
  margin: 48px 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-vs-prodazha-kvartiry__shell {
  background: linear-gradient(155deg, var(--bk-navy) 0%, #0f2038 46%, var(--bk-navy-soft) 100%);
  border: 1px solid rgba(220, 38, 38, 0.22);
  border-radius: 14px;
  padding: 32px 28px 24px;
  color: var(--bk-txt);
  box-shadow: 0 18px 48px rgba(10, 22, 40, 0.34);
}
.l24-boris-vs-prodazha-kvartiry__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--bk-gold);
}
.l24-boris-vs-prodazha-kvartiry__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-vs-prodazha-kvartiry__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--bk-muted);
  max-width: 74ch;
}
.l24-boris-vs-prodazha-kvartiry__lead strong { color: #fff; }
.l24-boris-vs-prodazha-kvartiry__map {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 52px minmax(0, 1fr);
  gap: 0;
  margin-bottom: 20px;
  align-items: stretch;
}
.l24-boris-vs-prodazha-kvartiry__contour {
  border-radius: 12px;
  padding: 18px 16px 16px;
}
.l24-boris-vs-prodazha-kvartiry__contour--civil {
  background: var(--bk-civil-bg);
  border: 1px solid rgba(99, 102, 241, 0.38);
  border-radius: 12px 0 0 12px;
}
.l24-boris-vs-prodazha-kvartiry__contour--crim {
  background: var(--bk-crim-bg);
  border: 1px solid rgba(220, 38, 38, 0.38);
  border-radius: 0 12px 12px 0;
}
.l24-boris-vs-prodazha-kvartiry__contour-hd {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 0 0 10px;
}
.l24-boris-vs-prodazha-kvartiry__contour-icon {
  flex-shrink: 0;
  width: 36px;
  height: 36px;
}
.l24-boris-vs-prodazha-kvartiry__contour-title {
  margin: 0;
  font-size: 0.82rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  line-height: 1.2;
}
.l24-boris-vs-prodazha-kvartiry__contour--civil .l24-boris-vs-prodazha-kvartiry__contour-title { color: #c7d2fe; }
.l24-boris-vs-prodazha-kvartiry__contour--crim .l24-boris-vs-prodazha-kvartiry__contour-title { color: #fecaca; }
.l24-boris-vs-prodazha-kvartiry__contour-case {
  margin: 0 0 12px;
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--bk-gold);
}
.l24-boris-vs-prodazha-kvartiry__contour-list {
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-vs-prodazha-kvartiry__contour-item {
  margin: 0 0 8px;
  padding: 8px 10px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.76rem;
  line-height: 1.4;
  color: #cbd5e1;
}
.l24-boris-vs-prodazha-kvartiry__contour-item strong {
  display: block;
  font-size: 0.7rem;
  font-weight: 700;
  margin-bottom: 3px;
  letter-spacing: 0.03em;
}
.l24-boris-vs-prodazha-kvartiry__contour--civil .l24-boris-vs-prodazha-kvartiry__contour-item strong { color: var(--bk-civil-soft); }
.l24-boris-vs-prodazha-kvartiry__contour--crim .l24-boris-vs-prodazha-kvartiry__contour-item strong { color: var(--bk-crim-soft); }
.l24-boris-vs-prodazha-kvartiry__bridge {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 1;
}
.l24-boris-vs-prodazha-kvartiry__bridge-line {
  width: 2px;
  flex: 1;
  min-height: 40px;
  background: linear-gradient(180deg, rgba(99,102,241,0.5), rgba(236,201,75,0.7), rgba(220,38,38,0.5));
}
.l24-boris-vs-prodazha-kvartiry__bridge-badge {
  margin: 6px 0;
  padding: 8px 6px;
  border-radius: 8px;
  background: rgba(236, 201, 75, 0.16);
  border: 1px solid rgba(236, 201, 75, 0.45);
  font-size: 0.62rem;
  font-weight: 800;
  letter-spacing: 0.04em;
  text-align: center;
  color: var(--bk-gold);
  line-height: 1.3;
  writing-mode: vertical-rl;
  text-orientation: mixed;
  transform: rotate(180deg);
}
.l24-boris-vs-prodazha-kvartiry__scheme-svg {
  display: block;
  width: 100%;
  height: auto;
  margin-bottom: 20px;
}
.l24-boris-vs-prodazha-kvartiry__matrix-hd {
  margin: 0 0 12px;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--bk-gold);
}
.l24-boris-vs-prodazha-kvartiry__matrix {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr) minmax(0, 1fr);
  gap: 0;
  margin-bottom: 18px;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-vs-prodazha-kvartiry__matrix-h {
  padding: 10px 12px;
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  background: rgba(255, 255, 255, 0.08);
  color: #e2e8f0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-vs-prodazha-kvartiry__matrix-h--civil { color: #c7d2fe; }
.l24-boris-vs-prodazha-kvartiry__matrix-h--crim { color: #fecaca; }
.l24-boris-vs-prodazha-kvartiry__matrix-row {
  display: contents;
}
.l24-boris-vs-prodazha-kvartiry__matrix-cell {
  padding: 10px 12px;
  font-size: 0.74rem;
  line-height: 1.4;
  color: #cbd5e1;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  background: rgba(255, 255, 255, 0.03);
}
.l24-boris-vs-prodazha-kvartiry__matrix-cell--sit {
  font-weight: 600;
  color: #e2e8f0;
  background: rgba(255, 255, 255, 0.05);
}
.l24-boris-vs-prodazha-kvartiry__matrix-cell--civil { color: #c7d2fe; }
.l24-boris-vs-prodazha-kvartiry__matrix-cell--crim { color: #fecaca; }
.l24-boris-vs-prodazha-kvartiry__matrix-row:last-child .l24-boris-vs-prodazha-kvartiry__matrix-cell { border-bottom: none; }
.l24-boris-vs-prodazha-kvartiry__cases {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 18px;
}
.l24-boris-vs-prodazha-kvartiry__case {
  border-radius: 10px;
  padding: 14px 14px 12px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-vs-prodazha-kvartiry__case--win { border-color: rgba(45, 212, 191, 0.35); }
.l24-boris-vs-prodazha-kvartiry__case--lose { border-color: rgba(220, 38, 38, 0.35); }
.l24-boris-vs-prodazha-kvartiry__case-label {
  display: block;
  font-size: 0.64rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-bottom: 6px;
  color: var(--bk-gold);
}
.l24-boris-vs-prodazha-kvartiry__case-title {
  margin: 0 0 6px;
  font-size: 0.82rem;
  font-weight: 700;
  color: #fff;
}
.l24-boris-vs-prodazha-kvartiry__case-text {
  margin: 0;
  font-size: 0.74rem;
  line-height: 1.45;
  color: var(--bk-muted);
}
.l24-boris-vs-prodazha-kvartiry__verdict {
  margin: 0 0 16px;
  padding: 14px 16px;
  border-radius: 10px;
  background: rgba(45, 212, 191, 0.1);
  border: 1px solid rgba(45, 212, 191, 0.32);
  font-size: 0.84rem;
  line-height: 1.5;
  color: var(--bk-muted);
}
.l24-boris-vs-prodazha-kvartiry__verdict strong { color: var(--bk-teal); }
.l24-boris-vs-prodazha-kvartiry__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-vs-prodazha-kvartiry__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  color: var(--bk-txt);
  border: 1px solid rgba(255, 255, 255, 0.13);
}
.l24-boris-vs-prodazha-kvartiry__tag--civil { border-color: rgba(99, 102, 241, 0.45); color: #c7d2fe; }
.l24-boris-vs-prodazha-kvartiry__tag--crim { border-color: rgba(220, 38, 38, 0.45); color: #fecaca; }
.l24-boris-vs-prodazha-kvartiry__tag--case { border-color: rgba(236, 201, 75, 0.5); color: var(--bk-gold); }
.l24-boris-vs-prodazha-kvartiry__tag--law { border-color: rgba(45, 212, 191, 0.4); color: #99f6e4; }
@media (max-width: 800px) {
  .l24-boris-vs-prodazha-kvartiry__map {
    grid-template-columns: 1fr;
    gap: 0;
  }
  .l24-boris-vs-prodazha-kvartiry__contour--civil { border-radius: 12px 12px 0 0; }
  .l24-boris-vs-prodazha-kvartiry__contour--crim { border-radius: 0 0 12px 12px; }
  .l24-boris-vs-prodazha-kvartiry__bridge {
    flex-direction: row;
    padding: 10px 0;
  }
  .l24-boris-vs-prodazha-kvartiry__bridge-line {
    width: auto;
    height: 2px;
    flex: 1;
    min-height: 0;
    background: linear-gradient(90deg, rgba(99,102,241,0.5), rgba(236,201,75,0.7), rgba(220,38,38,0.5));
  }
  .l24-boris-vs-prodazha-kvartiry__bridge-badge {
    writing-mode: horizontal-tb;
    transform: none;
    padding: 6px 12px;
  }
  .l24-boris-vs-prodazha-kvartiry__matrix {
    grid-template-columns: 1fr;
  }
  .l24-boris-vs-prodazha-kvartiry__matrix-h:not(:first-child) { display: none; }
  .l24-boris-vs-prodazha-kvartiry__matrix-cell--civil::before,
  .l24-boris-vs-prodazha-kvartiry__matrix-cell--crim::before {
    display: block;
    font-size: 0.62rem;
    font-weight: 800;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-bottom: 4px;
    opacity: 0.7;
  }
  .l24-boris-vs-prodazha-kvartiry__matrix-cell--civil::before { content: "ст. 178–179 ГК"; color: #c7d2fe; }
  .l24-boris-vs-prodazha-kvartiry__matrix-cell--crim::before { content: "ст. 159 УК"; color: #fecaca; }
  .l24-boris-vs-prodazha-kvartiry__cases { grid-template-columns: 1fr; }
  .l24-boris-vs-prodazha-kvartiry__shell { padding: 24px 18px 20px; }
}
</style>

<div class="l24-boris-vs-prodazha-kvartiry__shell">
  <p class="l24-boris-vs-prodazha-kvartiry__eyebrow">UG · обзор ВС 01.07.2026 · ст. 179 ГК ↔ ст. 159 УК · жильё</p>
  <h3 class="l24-boris-vs-prodazha-kvartiry__title">Два контура защиты: гражданское оспаривание и уголовное дело</h3>
  <p class="l24-boris-vs-prodazha-kvartiry__lead">Обзор ВС подчёркивает: <strong>уголовное дело по ст. 159 не аннулирует сделку автоматически</strong>, а гражданский иск по ст. 179 — только при доказанном знании покупателя об обмане. Параллельные контуры сходятся в вопросе «знал или должен был знать» — но последствия для покупателя различаются: отказ в иске vs статус подозреваемого.</p>

  <div class="l24-boris-vs-prodazha-kvartiry__map" role="group" aria-label="Карта двух контуров: гражданское оспаривание и уголовная ответственность">
    <div class="l24-boris-vs-prodazha-kvartiry__contour l24-boris-vs-prodazha-kvartiry__contour--civil">
      <div class="l24-boris-vs-prodazha-kvartiry__contour-hd">
        <svg class="l24-boris-vs-prodazha-kvartiry__contour-icon" viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <rect x="2" y="2" width="32" height="32" rx="8" fill="rgba(99,102,241,0.2)" stroke="#6366f1" stroke-width="1.5"/>
          <path d="M10 26V14l8-6 8 6v12" fill="none" stroke="#a5b4fc" stroke-width="1.8" stroke-linejoin="round"/>
          <rect x="14" y="18" width="8" height="8" rx="1" fill="rgba(165,180,252,0.35)" stroke="#c7d2fe" stroke-width="1"/>
          <circle cx="18" cy="10" r="2" fill="#ecc94b"/>
        </svg>
        <p class="l24-boris-vs-prodazha-kvartiry__contour-title">Гражданское оспаривание</p>
      </div>
      <p class="l24-boris-vs-prodazha-kvartiry__contour-case">ст. 178–179 ГК · срок 1 год (ст. 181)</p>
      <ul class="l24-boris-vs-prodazha-kvartiry__contour-list">
        <li class="l24-boris-vs-prodazha-kvartiry__contour-item"><strong>ст. 178 п. 3 ГК</strong>Заблуждение о мотивах («спецоперация») — недостаточно для недействительности</li>
        <li class="l24-boris-vs-prodazha-kvartiry__contour-item"><strong>ст. 179 ГК · обман</strong>Специальная норма для телефонных схем: продавец понимал, что продаёт</li>
        <li class="l24-boris-vs-prodazha-kvartiry__contour-item"><strong>Условие отмены</strong>Покупатель знал или должен был знать об обмане → недействительность + двусторонняя реституция (ст. 167)</li>
      </ul>
    </div>

    <div class="l24-boris-vs-prodazha-kvartiry__bridge" aria-hidden="true">
      <div class="l24-boris-vs-prodazha-kvartiry__bridge-line"></div>
      <span class="l24-boris-vs-prodazha-kvartiry__bridge-badge">ВС 01.07.2026</span>
      <div class="l24-boris-vs-prodazha-kvartiry__bridge-line"></div>
    </div>

    <div class="l24-boris-vs-prodazha-kvartiry__contour l24-boris-vs-prodazha-kvartiry__contour--crim">
      <div class="l24-boris-vs-prodazha-kvartiry__contour-hd">
        <svg class="l24-boris-vs-prodazha-kvartiry__contour-icon" viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <rect x="2" y="2" width="32" height="32" rx="8" fill="rgba(220,38,38,0.15)" stroke="#dc2626" stroke-width="1.5"/>
          <path d="M12 10h12v4H12z" fill="rgba(252,165,165,0.3)" stroke="#fca5a5" stroke-width="1"/>
          <path d="M10 16h16v12H10z" fill="rgba(220,38,38,0.12)" stroke="#fca5a5" stroke-width="1.2" rx="2"/>
          <line x1="14" y1="20" x2="22" y2="20" stroke="#fecaca" stroke-width="1.2" stroke-linecap="round"/>
          <line x1="14" y1="24" x2="20" y2="24" stroke="#fecaca" stroke-width="1.2" stroke-linecap="round"/>
          <circle cx="26" cy="8" r="4" fill="#ecc94b" stroke="#dc2626" stroke-width="1"/>
          <text x="26" y="10" text-anchor="middle" fill="#0a1628" font-size="5" font-weight="800" font-family="system-ui,sans-serif">159</text>
        </svg>
        <p class="l24-boris-vs-prodazha-kvartiry__contour-title">Уголовная ответственность</p>
      </div>
      <p class="l24-boris-vs-prodazha-kvartiry__contour-case">ч. 3–4 ст. 159 УК · соучастие ст. 33</p>
      <ul class="l24-boris-vs-prodazha-kvartiry__contour-list">
        <li class="l24-boris-vs-prodazha-kvartiry__contour-item"><strong>ч. 3–4 ст. 159</strong>Квартира в городе → крупный / особо крупный размер; квалификатор лишения права на жильё</li>
        <li class="l24-boris-vs-prodazha-kvartiry__contour-item"><strong>Продавец-жертва</strong>Статус потерпевшего; обвинение — к мошенникам, не к продавцу</li>
        <li class="l24-boris-vs-prodazha-kvartiry__contour-item"><strong>Приговор</strong>Преюдиция факта обмана (ст. 61 ГПК) + взыскание ущерба (ст. 44 УПК); УД ≠ отмена сделки</li>
      </ul>
    </div>
  </div>

  <svg class="l24-boris-vs-prodazha-kvartiry__scheme-svg" viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="bkVsT bkVsD">
    <title id="bkVsT">Схема параллельных контуров: ст. 179 ГК и ст. 159 УК при продаже квартиры под влиянием мошенников</title>
    <desc id="bkVsD">Слева — гражданский контур (ст. 178–179, иск потерпевшего); справа — уголовный (ч. 3–4 ст. 159, потерпевший-продавец); в центре — обзор ВС 01.07.2026</desc>
    <defs>
      <marker id="bkVs-arr-c" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
        <polygon points="0 0, 8 3.5, 0 7" fill="#6366f1"/>
      </marker>
      <marker id="bkVs-arr-r" markerWidth="8" markerHeight="7" refX="1" refY="3.5" orient="auto">
        <polygon points="8 0, 0 3.5, 8 7" fill="#dc2626"/>
      </marker>
    </defs>

    <line x1="360" y1="16" x2="360" y2="184" stroke="rgba(236,201,75,0.4)" stroke-width="2" stroke-dasharray="5,4"/>
    <rect x="280" y="78" width="160" height="44" rx="8" fill="rgba(236,201,75,0.14)" stroke="#ecc94b" stroke-width="1.5"/>
    <text x="360" y="96" text-anchor="middle" fill="#ecc94b" font-size="7.5" font-weight="800" font-family="system-ui,sans-serif">ОБЗОР ВС</text>
    <text x="360" y="110" text-anchor="middle" fill="#fde68a" font-size="6.5" font-family="system-ui,sans-serif">01.07.2026 · параллельные контуры</text>

    <rect x="14" y="24" width="158" height="152" rx="10" fill="rgba(99,102,241,0.12)" stroke="#6366f1" stroke-width="1.5"/>
    <text x="93" y="44" text-anchor="middle" fill="#c7d2fe" font-size="8" font-weight="800" font-family="system-ui,sans-serif">ГРАЖДАНСКИЙ</text>
    <text x="93" y="58" text-anchor="middle" fill="#a5b4fc" font-size="7" font-family="system-ui,sans-serif">ст. 179 ГК · обман</text>
    <path d="M78 72 L93 62 L108 72 V88 H78 Z" fill="none" stroke="#a5b4fc" stroke-width="1.3" stroke-linejoin="round"/>
    <rect x="86" y="78" width="14" height="10" rx="1" fill="rgba(165,180,252,0.3)"/>
    <text x="93" y="102" text-anchor="middle" fill="#ecc94b" font-size="6.5" font-weight="700" font-family="system-ui,sans-serif">иск потерпевшего</text>
    <text x="93" y="116" text-anchor="middle" fill="#94a3b8" font-size="5.8" font-family="system-ui,sans-serif">знал / должен знал</text>
    <rect x="28" y="124" width="130" height="20" rx="5" fill="rgba(99,102,241,0.2)" stroke="#6366f1" stroke-width="1"/>
    <text x="93" y="137" text-anchor="middle" fill="#c7d2fe" font-size="6.2" font-weight="600" font-family="system-ui,sans-serif">недействительность · реституция</text>
    <text x="93" y="162" text-anchor="middle" fill="#64748b" font-size="5.8" font-family="system-ui,sans-serif">суд общей юрисдикции · 1 год</text>
    <line x1="172" y1="100" x2="280" y2="100" stroke="#6366f1" stroke-width="1.4" marker-end="url(#bkVs-arr-c)"/>

    <rect x="548" y="24" width="158" height="152" rx="10" fill="rgba(220,38,38,0.1)" stroke="#dc2626" stroke-width="1.5"/>
    <text x="627" y="44" text-anchor="middle" fill="#fecaca" font-size="8" font-weight="800" font-family="system-ui,sans-serif">УГОЛОВНЫЙ</text>
    <text x="627" y="58" text-anchor="middle" fill="#fca5a5" font-size="7" font-family="system-ui,sans-serif">ч. 3–4 ст. 159 УК</text>
    <rect x="612" y="66" width="30" height="22" rx="3" fill="rgba(220,38,38,0.15)" stroke="#fca5a5" stroke-width="1.2"/>
    <text x="627" y="80" text-anchor="middle" fill="#fecaca" font-size="7" font-weight="800" font-family="system-ui,sans-serif">УД</text>
    <text x="627" y="102" text-anchor="middle" fill="#ecc94b" font-size="6.5" font-weight="700" font-family="system-ui,sans-serif">потерпевший-продавец</text>
    <text x="627" y="116" text-anchor="middle" fill="#94a3b8" font-size="5.8" font-family="system-ui,sans-serif">соучастие ст. 33</text>
    <rect x="562" y="124" width="130" height="20" rx="5" fill="rgba(220,38,38,0.15)" stroke="#dc2626" stroke-width="1"/>
    <text x="627" y="137" text-anchor="middle" fill="#fecaca" font-size="6.2" font-weight="600" font-family="system-ui,sans-serif">приговор · преюдиция · ущерб</text>
    <text x="627" y="162" text-anchor="middle" fill="#64748b" font-size="5.8" font-family="system-ui,sans-serif">УД не отменяет сделку само</text>
    <line x1="548" y1="100" x2="440" y2="100" stroke="#dc2626" stroke-width="1.4" marker-end="url(#bkVs-arr-r)"/>
  </svg>

  <p class="l24-boris-vs-prodazha-kvartiry__matrix-hd">Матрица: ситуация → последствия по ГК и УК</p>
  <div class="l24-boris-vs-prodazha-kvartiry__matrix" role="table" aria-label="Матрица гражданского оспаривания и уголовной ответственности">
    <div class="l24-boris-vs-prodazha-kvartiry__matrix-h">Ситуация</div>
    <div class="l24-boris-vs-prodazha-kvartiry__matrix-h l24-boris-vs-prodazha-kvartiry__matrix-h--civil">ст. 178–179 ГК</div>
    <div class="l24-boris-vs-prodazha-kvartiry__matrix-h l24-boris-vs-prodazha-kvartiry__matrix-h--crim">ст. 159 УК</div>

    <div class="l24-boris-vs-prodazha-kvartiry__matrix-row" role="row">
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--sit" role="cell">Продавец «помогал ФСБ», но понимал, что продаёт</div>
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--civil" role="cell">ст. 178 — мотивы не существенны (п. 3)</div>
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--crim" role="cell">Потерпевший; обвинение к мошенникам</div>
    </div>
    <div class="l24-boris-vs-prodazha-kvartiry__matrix-row" role="row">
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--sit" role="cell">Обман третьих лиц; покупатель не знал и не мог знать</div>
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--civil" role="cell">Иск отклоняется (ст. 179)</div>
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--crim" role="cell">Покупатель не в УД; защита добросовестности</div>
    </div>
    <div class="l24-boris-vs-prodazha-kvartiry__matrix-row" role="row">
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--sit" role="cell">Риелтор действовал в интересах мошенника</div>
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--civil" role="cell">Презумпция: покупатель знал / должен знал</div>
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--crim" role="cell">Риск соучастия (ст. 33) при прямом умысле</div>
    </div>
    <div class="l24-boris-vs-prodazha-kvartiry__matrix-row" role="row">
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--sit" role="cell">Покупатель — подставное лицо, знал схему</div>
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--civil" role="cell">Недействительность + реституция</div>
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--crim" role="cell">Соисполнитель / пособник ч. 3–4 ст. 159</div>
    </div>
    <div class="l24-boris-vs-prodazha-kvartiry__matrix-row" role="row">
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--sit" role="cell">«Не был в себе» без психиатрической экспертизы</div>
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--civil" role="cell">Отказ в иске (ст. 177 ГК)</div>
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--crim" role="cell">Не меняет квалификацию мошенников</div>
    </div>
    <div class="l24-boris-vs-prodazha-kvartiry__matrix-row" role="row">
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--sit" role="cell">Вступивший приговор по ст. 159</div>
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--civil" role="cell">Преюдиция факта обмана (ст. 61 ГПК)</div>
      <div class="l24-boris-vs-prodazha-kvartiry__matrix-cell l24-boris-vs-prodazha-kvartiry__matrix-cell--crim" role="cell">Основа иска и взыскания ущерба (ст. 44 УПК)</div>
    </div>
  </div>

  <div class="l24-boris-vs-prodazha-kvartiry__cases" role="group" aria-label="Два эталонных дела из обзора ВС">
    <div class="l24-boris-vs-prodazha-kvartiry__case l24-boris-vs-prodazha-kvartiry__case--lose">
      <span class="l24-boris-vs-prodazha-kvartiry__case-label">Эталон обзора · март 2023</span>
      <p class="l24-boris-vs-prodazha-kvartiry__case-title">Риелтор + особо крупный размер → сделка недействительна</p>
      <p class="l24-boris-vs-prodazha-kvartiry__case-text">Ложный «сотрудник» силовых и ЦБ; сделка через агентство мошенника. Уголовная вина признана, гражданский суд: покупатель не в неведении — посредничество риелтора = сведения об обмане (п. 2 ст. 179 ГК).</p>
    </div>
    <div class="l24-boris-vs-prodazha-kvartiry__case l24-boris-vs-prodazha-kvartiry__case--win">
      <span class="l24-boris-vs-prodazha-kvartiry__case-label">Дело Долиной · 5-КГ25-174-К2</span>
      <p class="l24-boris-vs-prodazha-kvartiry__case-title">Добросовестный покупатель → сделка действительна</p>
      <p class="l24-boris-vs-prodazha-kvartiry__case-text">ч. 4 ст. 159, приговор 4 фигурантам; Лурье не причастна. ВС 16.12.2025: знание покупателем не доказано → защита добросовестного приобретателя. Уклонение от экспертизы — против продавца.</p>
    </div>
  </div>

  <p class="l24-boris-vs-prodazha-kvartiry__verdict"><strong>Практический вывод:</strong> запускайте оба контура параллельно — заявление в полицию (ч. 4 ст. 159) и иск по ст. 179 (срок 1 год не ждёт УД). Покупателю критично доказать осмотрительность и отсутствие связи с риелтором аферистов; продавцу — ст. 179, а не 178, и готовность к экспертизе при ссылке на ст. 177.</p>

  <div class="l24-boris-vs-prodazha-kvartiry__foot" aria-label="Нормативная база блока">
    <span class="l24-boris-vs-prodazha-kvartiry__tag l24-boris-vs-prodazha-kvartiry__tag--case">ВС 01.07.2026 · обзор по жилью</span>
    <span class="l24-boris-vs-prodazha-kvartiry__tag l24-boris-vs-prodazha-kvartiry__tag--civil">ст. 179 ГК · обман третьих лиц</span>
    <span class="l24-boris-vs-prodazha-kvartiry__tag l24-boris-vs-prodazha-kvartiry__tag--crim">ч. 3–4 ст. 159 УК</span>
    <span class="l24-boris-vs-prodazha-kvartiry__tag l24-boris-vs-prodazha-kvartiry__tag--crim">ст. 33 УК · соучастие</span>
    <span class="l24-boris-vs-prodazha-kvartiry__tag l24-boris-vs-prodazha-kvartiry__tag--law">ст. 44 УПК · ущерб</span>
    <span class="l24-boris-vs-prodazha-kvartiry__tag l24-boris-vs-prodazha-kvartiry__tag--law">ст. 167 ГК · двусторонняя реституция</span>
  </div>
</div>
</section>
```

## Передача Наташе

- **Якорь:** `l24-boris-vs-prodazha-kvartiry-evidence`
- **После H2:** «Ст. 178–179 ГК РФ и ст. 159 УК: гражданское оспаривание и уголовная защита»
- **Перед:** H2 «Риски для покупателя квартиры: знал или должен был знать»
- **MCP-only:** без `<canvas>` и `<script>` — только inline CSS + static SVG + grid
- **script:** нет
