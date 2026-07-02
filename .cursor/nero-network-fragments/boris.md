=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО
ЯКОРЬ: l24-boris-vs-osparivanie-sdelok-zhiloe

## Паспорт блока

| Параметр | Значение |
|----------|----------|
| **Статья** | Обзор ВС РФ 01.07.2026: оспаривание сделок с жильём в банкротстве — дарение, цена, мнимость |
| **SLUG** | `vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026` |
| **Якорь** | `l24-boris-vs-osparivanie-sdelok-zhiloe` |
| **Тема** | Горизонтальная «карта двух контуров»: гражданское оспаривание (ст. 178–179, обман, Долина) ↔ банкротное (ст. 61.2, ФУ, Чигарчакова) |
| **Размещение** | После H2 «Обзор ВС 2026: 20 позиций по оспариванию сделок с жильём» — перед H2 «Ст. 61.2 Закона о банкротстве» |
| **Режим** | Контраст к hero Алины: горизонтальная карта в теле статьи, не полноэкранная сцена; MCP-only — inline CSS + static SVG, без `<canvas>` и `<script>` |
| **Палитра** | Тёмный navy `#0a1628`–`#152a45`; гражданский контур: indigo `#6366f1` / `#a5b4fc`; банкротный: amber `#f59e0b` / `#fbbf24`; ВС: gold `#ecc94b`; жильё: teal `#2dd4bf` |

## Чеклист отличий от hero Алины

- [x] Не полноэкранный первый экран — блок в теле лонгрида
- [x] Другой `id`: `l24-boris-vs-osparivanie-sdelok-zhiloe` (не hero-id Алины)
- [x] Горизонтальная сплит-карта «Гражданский контур ↔ Банкротный контур» — не дублирует сцену hero
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG + grid
- [x] CTA в блоке **не вставлять**

```html
<section id="l24-boris-vs-osparivanie-sdelok-zhiloe" class="l24-boris-vs-osparivanie-sdelok-zhiloe" aria-label="Два контура оспаривания сделок с жильём: гражданское право и банкротство по обзору ВС 01.07.2026">
<style>
.l24-boris-vs-osparivanie-sdelok-zhiloe {
  --bo-navy: #0a1628;
  --bo-navy-soft: #152a45;
  --bo-civil: #6366f1;
  --bo-civil-soft: #a5b4fc;
  --bo-civil-bg: rgba(99, 102, 241, 0.14);
  --bo-arb: #f59e0b;
  --bo-arb-soft: #fbbf24;
  --bo-arb-bg: rgba(245, 158, 11, 0.12);
  --bo-gold: #ecc94b;
  --bo-teal: #2dd4bf;
  --bo-muted: #94a3b8;
  --bo-txt: #e2e8f0;
  margin: 48px 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__shell {
  background: linear-gradient(155deg, var(--bo-navy) 0%, #0f2038 46%, var(--bo-navy-soft) 100%);
  border: 1px solid rgba(99, 102, 241, 0.28);
  border-radius: 14px;
  padding: 32px 28px 24px;
  color: var(--bo-txt);
  box-shadow: 0 18px 48px rgba(10, 22, 40, 0.34);
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--bo-gold);
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--bo-muted);
  max-width: 74ch;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__lead strong { color: #fff; }
.l24-boris-vs-osparivanie-sdelok-zhiloe__map {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 52px minmax(0, 1fr);
  gap: 0;
  margin-bottom: 20px;
  align-items: stretch;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour {
  border-radius: 12px;
  padding: 18px 16px 16px;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour--civil {
  background: var(--bo-civil-bg);
  border: 1px solid rgba(99, 102, 241, 0.38);
  border-radius: 12px 0 0 12px;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour--arb {
  background: var(--bo-arb-bg);
  border: 1px solid rgba(245, 158, 11, 0.38);
  border-radius: 0 12px 12px 0;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour-hd {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 0 0 10px;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour-icon {
  flex-shrink: 0;
  width: 36px;
  height: 36px;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour-title {
  margin: 0;
  font-size: 0.82rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  line-height: 1.2;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour--civil .l24-boris-vs-osparivanie-sdelok-zhiloe__contour-title { color: #c7d2fe; }
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour--arb .l24-boris-vs-osparivanie-sdelok-zhiloe__contour-title { color: #fde68a; }
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour-case {
  margin: 0 0 12px;
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--bo-gold);
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour-list {
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour-item {
  margin: 0 0 8px;
  padding: 8px 10px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.76rem;
  line-height: 1.4;
  color: #cbd5e1;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour-item strong {
  display: block;
  font-size: 0.7rem;
  font-weight: 700;
  margin-bottom: 3px;
  letter-spacing: 0.03em;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour--civil .l24-boris-vs-osparivanie-sdelok-zhiloe__contour-item strong { color: var(--bo-civil-soft); }
.l24-boris-vs-osparivanie-sdelok-zhiloe__contour--arb .l24-boris-vs-osparivanie-sdelok-zhiloe__contour-item strong { color: var(--bo-arb-soft); }
.l24-boris-vs-osparivanie-sdelok-zhiloe__bridge {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 1;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__bridge-line {
  width: 2px;
  flex: 1;
  min-height: 40px;
  background: linear-gradient(180deg, rgba(99,102,241,0.5), rgba(236,201,75,0.7), rgba(245,158,11,0.5));
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__bridge-badge {
  margin: 6px 0;
  padding: 8px 6px;
  border-radius: 8px;
  background: rgba(236, 201, 75, 0.16);
  border: 1px solid rgba(236, 201, 75, 0.45);
  font-size: 0.62rem;
  font-weight: 800;
  letter-spacing: 0.04em;
  text-align: center;
  color: var(--bo-gold);
  line-height: 1.3;
  writing-mode: vertical-rl;
  text-orientation: mixed;
  transform: rotate(180deg);
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__scheme-svg {
  display: block;
  width: 100%;
  height: auto;
  margin-bottom: 20px;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-bottom: 18px;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__cell {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 12px 10px;
  text-align: center;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__cell-label {
  display: block;
  font-size: 0.66rem;
  font-weight: 700;
  color: var(--bo-muted);
  margin-bottom: 6px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__cell-civil,
.l24-boris-vs-osparivanie-sdelok-zhiloe__cell-arb {
  display: block;
  font-size: 0.76rem;
  line-height: 1.35;
  font-weight: 600;
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__cell-civil { color: var(--bo-civil-soft); }
.l24-boris-vs-osparivanie-sdelok-zhiloe__cell-arb { color: var(--bo-arb-soft); }
.l24-boris-vs-osparivanie-sdelok-zhiloe__verdict {
  margin: 0 0 16px;
  padding: 14px 16px;
  border-radius: 10px;
  background: rgba(45, 212, 191, 0.1);
  border: 1px solid rgba(45, 212, 191, 0.32);
  font-size: 0.84rem;
  line-height: 1.5;
  color: var(--bo-muted);
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__verdict strong { color: var(--bo-teal); }
.l24-boris-vs-osparivanie-sdelok-zhiloe__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  color: var(--bo-txt);
  border: 1px solid rgba(255, 255, 255, 0.13);
}
.l24-boris-vs-osparivanie-sdelok-zhiloe__tag--civil { border-color: rgba(99, 102, 241, 0.45); color: #c7d2fe; }
.l24-boris-vs-osparivanie-sdelok-zhiloe__tag--arb { border-color: rgba(245, 158, 11, 0.45); color: #fde68a; }
.l24-boris-vs-osparivanie-sdelok-zhiloe__tag--case { border-color: rgba(236, 201, 75, 0.5); color: var(--bo-gold); }
.l24-boris-vs-osparivanie-sdelok-zhiloe__tag--law { border-color: rgba(45, 212, 191, 0.4); color: #99f6e4; }
@media (max-width: 800px) {
  .l24-boris-vs-osparivanie-sdelok-zhiloe__map {
    grid-template-columns: 1fr;
    gap: 0;
  }
  .l24-boris-vs-osparivanie-sdelok-zhiloe__contour--civil { border-radius: 12px 12px 0 0; }
  .l24-boris-vs-osparivanie-sdelok-zhiloe__contour--arb { border-radius: 0 0 12px 12px; }
  .l24-boris-vs-osparivanie-sdelok-zhiloe__bridge {
    flex-direction: row;
    padding: 10px 0;
  }
  .l24-boris-vs-osparivanie-sdelok-zhiloe__bridge-line {
    width: auto;
    height: 2px;
    flex: 1;
    min-height: 0;
    background: linear-gradient(90deg, rgba(99,102,241,0.5), rgba(236,201,75,0.7), rgba(245,158,11,0.5));
  }
  .l24-boris-vs-osparivanie-sdelok-zhiloe__bridge-badge {
    writing-mode: horizontal-tb;
    transform: none;
    padding: 6px 12px;
  }
  .l24-boris-vs-osparivanie-sdelok-zhiloe__grid { grid-template-columns: 1fr 1fr; }
  .l24-boris-vs-osparivanie-sdelok-zhiloe__shell { padding: 24px 18px 20px; }
}
@media (max-width: 480px) {
  .l24-boris-vs-osparivanie-sdelok-zhiloe__grid { grid-template-columns: 1fr; }
}
</style>

<div class="l24-boris-vs-osparivanie-sdelok-zhiloe__shell">
  <p class="l24-boris-vs-osparivanie-sdelok-zhiloe__eyebrow">ARB · обзор ВС 01.07.2026 · 20 позиций · жильё · ст. 61.2</p>
  <h3 class="l24-boris-vs-osparivanie-sdelok-zhiloe__title">Два контура оспаривания: гражданское право ↔ банкротство</h3>
  <p class="l24-boris-vs-osparivanie-sdelok-zhiloe__lead">Обзор ВС объединяет <strong>гражданское оспаривание</strong> (мошенники, заблуждение, обман — «эффект Долиной») и <strong>банкротный контур</strong> (подозрительные сделки по ст. 61.2 — дело Чигарчаковой). Покупатель квартиры рискует попасть в оба процесса, если не различить основания, сроки и бремя доказывания.</p>

  <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__map" role="group" aria-label="Карта двух контуров оспаривания сделок с жильём">
    <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour l24-boris-vs-osparivanie-sdelok-zhiloe__contour--civil">
      <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-hd">
        <svg class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-icon" viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <rect x="2" y="2" width="32" height="32" rx="8" fill="rgba(99,102,241,0.2)" stroke="#6366f1" stroke-width="1.5"/>
          <path d="M10 26V14l8-6 8 6v12" fill="none" stroke="#a5b4fc" stroke-width="1.8" stroke-linejoin="round"/>
          <rect x="14" y="18" width="8" height="8" rx="1" fill="rgba(165,180,252,0.35)" stroke="#c7d2fe" stroke-width="1"/>
          <circle cx="18" cy="10" r="2" fill="#ecc94b"/>
        </svg>
        <p class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-title">Гражданское оспаривание</p>
      </div>
      <p class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-case">Дело Долина–Лурье · № 5-КГ25-174-К2</p>
      <ul class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-list">
        <li class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-item"><strong>ст. 178 п. 3 ГК</strong>Заблуждение продавца о мотивах сделки — недостаточно для недействительности</li>
        <li class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-item"><strong>ст. 179 ГК · обман</strong>Квартира возвращается только если покупатель знал или должен был знать об обмане мошенников</li>
        <li class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-item"><strong>Суд общей юрисдикции</strong>Иск потерпевшего-продавца · срок 1 год (ст. 181 ГК) · двусторонняя реституция (ст. 167)</li>
      </ul>
    </div>

    <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__bridge" aria-hidden="true">
      <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__bridge-line"></div>
      <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__bridge-badge">ВС 01.07.2026</span>
      <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__bridge-line"></div>
    </div>

    <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour l24-boris-vs-osparivanie-sdelok-zhiloe__contour--arb">
      <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-hd">
        <svg class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-icon" viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <rect x="2" y="2" width="32" height="32" rx="8" fill="rgba(245,158,11,0.15)" stroke="#f59e0b" stroke-width="1.5"/>
          <path d="M8 28h20" stroke="#fbbf24" stroke-width="1.5" stroke-linecap="round"/>
          <rect x="10" y="10" width="16" height="14" rx="2" fill="rgba(251,191,36,0.2)" stroke="#fde68a" stroke-width="1.2"/>
          <path d="M14 16h8M14 20h5" stroke="#fde68a" stroke-width="1.2" stroke-linecap="round"/>
          <circle cx="26" cy="8" r="4" fill="#ecc94b" stroke="#f59e0b" stroke-width="1"/>
          <text x="26" y="10" text-anchor="middle" fill="#0a1628" font-size="5" font-weight="800" font-family="system-ui,sans-serif">ФУ</text>
        </svg>
        <p class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-title">Банкротное оспаривание</p>
      </div>
      <p class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-case">Дело Чигарчакова · № 307-ЭС25-13338</p>
      <ul class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-list">
        <li class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-item"><strong>п. 1 ст. 61.2 127-ФЗ</strong>Неравноценность: отклонение &gt;20% от рынка — недостаточно; нужна совокупность обстоятельств</li>
        <li class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-item"><strong>п. 2 ст. 61.2 · дарение</strong>Подозрительная сделка при доказанной цели вреда кредиторам · look-back 3 года</li>
        <li class="l24-boris-vs-osparivanie-sdelok-zhiloe__contour-item"><strong>Арбитражный суд</strong>Заявление ФУ/АУ/кредитора · добросовестность покупателя (ст. 61.4) · реституция в массу</li>
      </ul>
    </div>
  </div>

  <svg class="l24-boris-vs-osparivanie-sdelok-zhiloe__scheme-svg" viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="boZhT boZhD">
    <title id="boZhT">Схема двух контуров оспаривания сделок с жильём: гражданское и банкротное</title>
    <desc id="boZhD">Слева — гражданский контур (ст. 178–179, Долина); справа — банкротный (ст. 61.2, ФУ, Чигарчакова); в центре — обзор ВС 01.07.2026</desc>
    <defs>
      <marker id="boZh-arr-c" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
        <polygon points="0 0, 8 3.5, 0 7" fill="#6366f1"/>
      </marker>
      <marker id="boZh-arr-a" markerWidth="8" markerHeight="7" refX="1" refY="3.5" orient="auto">
        <polygon points="8 0, 0 3.5, 8 7" fill="#f59e0b"/>
      </marker>
    </defs>

    <!-- Центральная ось -->
    <line x1="360" y1="16" x2="360" y2="184" stroke="rgba(236,201,75,0.4)" stroke-width="2" stroke-dasharray="5,4"/>
    <rect x="296" y="78" width="128" height="44" rx="8" fill="rgba(236,201,75,0.14)" stroke="#ecc94b" stroke-width="1.5"/>
    <text x="360" y="98" text-anchor="middle" fill="#ecc94b" font-size="7.5" font-weight="800" font-family="system-ui,sans-serif">ОБЗОР ВС</text>
    <text x="360" y="112" text-anchor="middle" fill="#fde68a" font-size="6.5" font-family="system-ui,sans-serif">01.07.2026 · 20 позиций</text>

    <!-- Левый контур: гражданский -->
    <rect x="14" y="24" width="158" height="152" rx="10" fill="rgba(99,102,241,0.12)" stroke="#6366f1" stroke-width="1.5"/>
    <text x="93" y="44" text-anchor="middle" fill="#c7d2fe" font-size="8" font-weight="800" font-family="system-ui,sans-serif">ГРАЖДАНСКИЙ</text>
    <text x="93" y="58" text-anchor="middle" fill="#a5b4fc" font-size="7" font-family="system-ui,sans-serif">ст. 178–179 ГК</text>
    <!-- дом-иконка -->
    <path d="M78 72 L93 62 L108 72 V88 H78 Z" fill="none" stroke="#a5b4fc" stroke-width="1.3" stroke-linejoin="round"/>
    <rect x="86" y="78" width="14" height="10" rx="1" fill="rgba(165,180,252,0.3)"/>
    <text x="93" y="102" text-anchor="middle" fill="#ecc94b" font-size="6.5" font-weight="700" font-family="system-ui,sans-serif">Долина–Лурье</text>
    <text x="93" y="116" text-anchor="middle" fill="#94a3b8" font-size="5.8" font-family="system-ui,sans-serif">5-КГ25-174-К2</text>
    <rect x="28" y="124" width="130" height="20" rx="5" fill="rgba(99,102,241,0.2)" stroke="#6366f1" stroke-width="1"/>
    <text x="93" y="137" text-anchor="middle" fill="#c7d2fe" font-size="6.2" font-weight="600" font-family="system-ui,sans-serif">обман · заблуждение · реституция</text>
    <text x="93" y="162" text-anchor="middle" fill="#64748b" font-size="5.8" font-family="system-ui,sans-serif">суд общей юрисдикции · 1 год</text>
    <line x1="172" y1="100" x2="296" y2="100" stroke="#6366f1" stroke-width="1.4" marker-end="url(#boZh-arr-c)"/>

    <!-- Правый контур: банкротный -->
    <rect x="548" y="24" width="158" height="152" rx="10" fill="rgba(245,158,11,0.1)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="627" y="44" text-anchor="middle" fill="#fde68a" font-size="8" font-weight="800" font-family="system-ui,sans-serif">БАНКРОТНЫЙ</text>
    <text x="627" y="58" text-anchor="middle" fill="#fbbf24" font-size="7" font-family="system-ui,sans-serif">ст. 61.2 127-ФЗ</text>
    <!-- весы арбитража -->
    <line x1="607" y1="68" x2="647" y2="68" stroke="#fbbf24" stroke-width="1.5"/>
    <line x1="627" y1="68" x2="627" y2="78" stroke="#fbbf24" stroke-width="1.5"/>
    <line x1="612" y1="78" x2="612" y2="86" stroke="#94a3b8" stroke-width="1"/>
    <line x1="642" y1="78" x2="642" y2="86" stroke="#94a3b8" stroke-width="1"/>
    <ellipse cx="612" cy="88" rx="10" ry="3" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="1"/>
    <ellipse cx="642" cy="88" rx="10" ry="3" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="1"/>
    <text x="627" y="102" text-anchor="middle" fill="#ecc94b" font-size="6.5" font-weight="700" font-family="system-ui,sans-serif">Чигарчакова</text>
    <text x="627" y="116" text-anchor="middle" fill="#94a3b8" font-size="5.8" font-family="system-ui,sans-serif">307-ЭС25-13338</text>
    <rect x="562" y="124" width="130" height="20" rx="5" fill="rgba(245,158,11,0.18)" stroke="#f59e0b" stroke-width="1"/>
    <text x="627" y="137" text-anchor="middle" fill="#fde68a" font-size="6.2" font-weight="600" font-family="system-ui,sans-serif">ФУ · цена · добросовестность</text>
    <text x="627" y="162" text-anchor="middle" fill="#64748b" font-size="5.8" font-family="system-ui,sans-serif">арбитраж · look-back 1–3 года</text>
    <line x1="548" y1="100" x2="424" y2="100" stroke="#f59e0b" stroke-width="1.4" marker-end="url(#boZh-arr-a)"/>

  </svg>

  <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__grid" role="table" aria-label="Сравнение двух контуров">
    <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell" role="cell">
      <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell-label">Кто оспаривает</span>
      <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell-civil">Потерпевший-продавец</span>
      <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell-arb">ФУ / АУ / кредитор</span>
    </div>
    <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell" role="cell">
      <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell-label">Суд</span>
      <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell-civil">Общая юрисдикция</span>
      <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell-arb">Арбитраж</span>
    </div>
    <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell" role="cell">
      <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell-label">Срок</span>
      <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell-civil">1 год (ст. 181 ГК)</span>
      <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell-arb">1–3 года look-back + 1 год ФУ</span>
    </div>
    <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell" role="cell">
      <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell-label">Защита покупателя</span>
      <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell-civil">Не знал об обмане (ст. 179)</span>
      <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__cell-arb">Добросовестность (ст. 61.4)</span>
    </div>
  </div>

  <p class="l24-boris-vs-osparivanie-sdelok-zhiloe__verdict"><strong>Практический вывод:</strong> после «эффекта Долиной» покупатель в гражданском споре защищается отсутствием знания об обмане; в банкротстве — осмотрительностью и заверениями (ячейка, ЕГРН, отсутствие намерения банкротиться). Один и тот же ДКП может стать предметом обоих контуров — но основания, сроки и бремя доказывания различаются.</p>

  <div class="l24-boris-vs-osparivanie-sdelok-zhiloe__foot" aria-label="Нормативная база блока">
    <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__tag l24-boris-vs-osparivanie-sdelok-zhiloe__tag--case">ВС 01.07.2026 · обзор по жилью</span>
    <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__tag l24-boris-vs-osparivanie-sdelok-zhiloe__tag--civil">ст. 178–179 ГК · Долина</span>
    <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__tag l24-boris-vs-osparivanie-sdelok-zhiloe__tag--arb">ст. 61.2 · Чигарчакова</span>
    <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__tag l24-boris-vs-osparivanie-sdelok-zhiloe__tag--law">ст. 61.4 · добросовестный покупатель</span>
    <span class="l24-boris-vs-osparivanie-sdelok-zhiloe__tag l24-boris-vs-osparivanie-sdelok-zhiloe__tag--law">ст. 167 ГК · двусторонняя реституция</span>
  </div>
</div>
</section>
```

## Передача Наташе

- **Якорь:** `l24-boris-vs-osparivanie-sdelok-zhiloe`
- **После H2:** «Обзор ВС 2026: 20 позиций по оспариванию сделок с жильём»
- **Перед:** H2 «Ст. 61.2 Закона о банкротстве: подозрительные сделки с недвижимостью»
- **MCP-only:** без `<canvas>` и `<script>` — только inline CSS + static SVG + grid
- **script:** нет
