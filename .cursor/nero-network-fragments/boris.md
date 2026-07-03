=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО
ЯКОРЬ: l24-boris-vs-sro-sozidanie-evidence

## Паспорт блока

| Параметр | Значение |
|----------|----------|
| **Статья** | Президиум ВС 01.07.2026: штраф 3,5 млн СРО «Созидание» за запрет неаккредитованных ЭТП — дело № А40-232008/2023 |
| **SLUG** | `vs-sro-sozidanie-fas-35-mln-akreditaciya-ploshchadok-2026` |
| **Якорь** | `l24-boris-vs-sro-sozidanie-evidence` |
| **id / class секции** | `id="l24-boris-vs-sro-sozidanie-evidence"` · `class="l24-boris-vs-sro-sozidanie"` |
| **Тема** | Сплит «ФАС vs СРО»: маятник инстанций (СКЭС 11.2025 → Президиум 07.2026) + карта выбора ЭТП для арбитражного управляющего |
| **Размещение** | После H2 «Хронология спора ФАС vs СРО: дело № А40-232008/2023» — перед H2 «Фабула дела: управляющий Петрова, ЭТП „Арбитат" и дисциплинарка 50 000 ₽» |
| **Режим** | Контраст к светлому hero Алины (ARB-navy/blue); редакционная карта в теле, не полноэкранная сцена; MCP-only — inline CSS + static SVG |
| **Палитра** | Shell navy `#0a1628`–`#152a45`; ФАС: amber `#f59e0b` / `#fcd34d`; СРО: emerald `#10b981` / `#6ee7b7`; ВС: gold `#ecc94b`; ЭТП: `#2563eb`; продолжение hero: `#1a365d`, `#4338ca` |

## Чеклист отличий от hero Алины

- [x] Не полноэкранный первый экран — блок в теле лонгрида после 1–2 H2
- [x] Другой `id`: `l24-boris-vs-sro-sozidanie-evidence` (не hero-id Алины)
- [x] Горизонтальная сплит-карта «ФАС ↔ СРО» + сетка ЭТП — не дублирует сцену hero
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG + grid
- [x] CTA в блоке **не вставлять**

```html
<section id="l24-boris-vs-sro-sozidanie-evidence" class="l24-boris-vs-sro-sozidanie" aria-label="Карта спора ФАС против СРО «Созидание»: маятник инстанций ВС и выбор электронной площадки для торгов по банкротству">
<style>
.l24-boris-vs-sro-sozidanie {
  --bs-navy: #0a1628;
  --bs-navy-soft: #152a45;
  --bs-fas: #f59e0b;
  --bs-fas-soft: #fcd34d;
  --bs-fas-bg: rgba(245, 158, 11, 0.14);
  --bs-sro: #10b981;
  --bs-sro-soft: #6ee7b7;
  --bs-sro-bg: rgba(16, 185, 129, 0.12);
  --bs-gold: #ecc94b;
  --bs-vs: #4338ca;
  --bs-etp: #2563eb;
  --bs-muted: #94a3b8;
  --bs-txt: #e2e8f0;
  margin: 48px 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-vs-sro-sozidanie__shell {
  background: linear-gradient(155deg, var(--bs-navy) 0%, #0f2038 46%, var(--bs-navy-soft) 100%);
  border: 1px solid rgba(67, 56, 202, 0.28);
  border-radius: 14px;
  padding: 32px 28px 24px;
  color: var(--bs-txt);
  box-shadow: 0 18px 48px rgba(10, 22, 40, 0.34);
}
.l24-boris-vs-sro-sozidanie__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--bs-gold);
}
.l24-boris-vs-sro-sozidanie__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-vs-sro-sozidanie__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--bs-muted);
  max-width: 74ch;
}
.l24-boris-vs-sro-sozidanie__lead strong { color: #fff; }
.l24-boris-vs-sro-sozidanie__map {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 52px minmax(0, 1fr);
  gap: 0;
  margin-bottom: 20px;
  align-items: stretch;
}
.l24-boris-vs-sro-sozidanie__side {
  border-radius: 12px;
  padding: 18px 16px 16px;
}
.l24-boris-vs-sro-sozidanie__side--fas {
  background: var(--bs-fas-bg);
  border: 1px solid rgba(245, 158, 11, 0.38);
  border-radius: 12px 0 0 12px;
}
.l24-boris-vs-sro-sozidanie__side--sro {
  background: var(--bs-sro-bg);
  border: 1px solid rgba(16, 185, 129, 0.38);
  border-radius: 0 12px 12px 0;
}
.l24-boris-vs-sro-sozidanie__side-hd {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 0 0 10px;
}
.l24-boris-vs-sro-sozidanie__side-icon {
  flex-shrink: 0;
  width: 36px;
  height: 36px;
}
.l24-boris-vs-sro-sozidanie__side-title {
  margin: 0;
  font-size: 0.82rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  line-height: 1.2;
}
.l24-boris-vs-sro-sozidanie__side--fas .l24-boris-vs-sro-sozidanie__side-title { color: #fde68a; }
.l24-boris-vs-sro-sozidanie__side--sro .l24-boris-vs-sro-sozidanie__side-title { color: #a7f3d0; }
.l24-boris-vs-sro-sozidanie__side-case {
  margin: 0 0 12px;
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--bs-gold);
}
.l24-boris-vs-sro-sozidanie__side-list {
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-vs-sro-sozidanie__side-item {
  margin: 0 0 8px;
  padding: 8px 10px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.76rem;
  line-height: 1.4;
  color: #cbd5e1;
}
.l24-boris-vs-sro-sozidanie__side-item strong {
  display: block;
  font-size: 0.7rem;
  font-weight: 700;
  margin-bottom: 3px;
  letter-spacing: 0.03em;
}
.l24-boris-vs-sro-sozidanie__side--fas .l24-boris-vs-sro-sozidanie__side-item strong { color: var(--bs-fas-soft); }
.l24-boris-vs-sro-sozidanie__side--sro .l24-boris-vs-sro-sozidanie__side-item strong { color: var(--bs-sro-soft); }
.l24-boris-vs-sro-sozidanie__bridge {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 1;
}
.l24-boris-vs-sro-sozidanie__bridge-line {
  width: 2px;
  flex: 1;
  min-height: 40px;
  background: linear-gradient(180deg, rgba(245,158,11,0.5), rgba(236,201,75,0.7), rgba(16,185,129,0.5));
}
.l24-boris-vs-sro-sozidanie__bridge-badge {
  margin: 6px 0;
  padding: 8px 6px;
  border-radius: 8px;
  background: rgba(236, 201, 75, 0.16);
  border: 1px solid rgba(236, 201, 75, 0.45);
  font-size: 0.62rem;
  font-weight: 800;
  letter-spacing: 0.04em;
  text-align: center;
  color: var(--bs-gold);
  line-height: 1.3;
  writing-mode: vertical-rl;
  text-orientation: mixed;
  transform: rotate(180deg);
}
.l24-boris-vs-sro-sozidanie__scheme-svg {
  display: block;
  width: 100%;
  height: auto;
  margin-bottom: 20px;
}
.l24-boris-vs-sro-sozidanie__pendulum-hd {
  margin: 0 0 12px;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--bs-gold);
}
.l24-boris-vs-sro-sozidanie__etp-hd {
  margin: 0 0 12px;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--bs-etp);
}
.l24-boris-vs-sro-sozidanie__etp-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 10px;
  margin-bottom: 18px;
}
.l24-boris-vs-sro-sozidanie__etp-card {
  border-radius: 10px;
  padding: 12px 10px 10px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  text-align: center;
}
.l24-boris-vs-sro-sozidanie__etp-card--ok { border-color: rgba(16, 185, 129, 0.4); }
.l24-boris-vs-sro-sozidanie__etp-card--warn { border-color: rgba(245, 158, 11, 0.45); }
.l24-boris-vs-sro-sozidanie__etp-card--case { border-color: rgba(67, 56, 202, 0.5); background: rgba(67, 56, 202, 0.1); }
.l24-boris-vs-sro-sozidanie__etp-name {
  display: block;
  font-size: 0.78rem;
  font-weight: 800;
  color: #fff;
  margin-bottom: 4px;
}
.l24-boris-vs-sro-sozidanie__etp-status {
  display: block;
  font-size: 0.66rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  margin-bottom: 6px;
}
.l24-boris-vs-sro-sozidanie__etp-card--ok .l24-boris-vs-sro-sozidanie__etp-status { color: #6ee7b7; }
.l24-boris-vs-sro-sozidanie__etp-card--warn .l24-boris-vs-sro-sozidanie__etp-status { color: #fcd34d; }
.l24-boris-vs-sro-sozidanie__etp-card--case .l24-boris-vs-sro-sozidanie__etp-status { color: #a5b4fc; }
.l24-boris-vs-sro-sozidanie__etp-note {
  margin: 0;
  font-size: 0.68rem;
  line-height: 1.35;
  color: var(--bs-muted);
}
.l24-boris-vs-sro-sozidanie__matrix {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr) minmax(0, 1fr);
  gap: 0;
  margin-bottom: 18px;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-vs-sro-sozidanie__matrix-h {
  padding: 10px 12px;
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  background: rgba(255, 255, 255, 0.08);
  color: #e2e8f0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-vs-sro-sozidanie__matrix-h--fas { color: #fde68a; }
.l24-boris-vs-sro-sozidanie__matrix-h--sro { color: #a7f3d0; }
.l24-boris-vs-sro-sozidanie__matrix-row { display: contents; }
.l24-boris-vs-sro-sozidanie__matrix-cell {
  padding: 10px 12px;
  font-size: 0.74rem;
  line-height: 1.4;
  color: #cbd5e1;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  background: rgba(255, 255, 255, 0.03);
}
.l24-boris-vs-sro-sozidanie__matrix-cell--sit {
  font-weight: 600;
  color: #e2e8f0;
  background: rgba(255, 255, 255, 0.05);
}
.l24-boris-vs-sro-sozidanie__matrix-cell--fas { color: #fde68a; }
.l24-boris-vs-sro-sozidanie__matrix-cell--sro { color: #a7f3d0; }
.l24-boris-vs-sro-sozidanie__matrix-row:last-child .l24-boris-vs-sro-sozidanie__matrix-cell { border-bottom: none; }
.l24-boris-vs-sro-sozidanie__verdict {
  margin: 0 0 16px;
  padding: 14px 16px;
  border-radius: 10px;
  background: rgba(37, 99, 235, 0.12);
  border: 1px solid rgba(37, 99, 235, 0.32);
  font-size: 0.84rem;
  line-height: 1.5;
  color: var(--bs-muted);
}
.l24-boris-vs-sro-sozidanie__verdict strong { color: #93c5fd; }
.l24-boris-vs-sro-sozidanie__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-vs-sro-sozidanie__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  color: var(--bs-txt);
  border: 1px solid rgba(255, 255, 255, 0.13);
}
.l24-boris-vs-sro-sozidanie__tag--fas { border-color: rgba(245, 158, 11, 0.45); color: #fde68a; }
.l24-boris-vs-sro-sozidanie__tag--sro { border-color: rgba(16, 185, 129, 0.45); color: #a7f3d0; }
.l24-boris-vs-sro-sozidanie__tag--case { border-color: rgba(236, 201, 75, 0.5); color: var(--bs-gold); }
.l24-boris-vs-sro-sozidanie__tag--law { border-color: rgba(37, 99, 235, 0.4); color: #93c5fd; }
@media (max-width: 800px) {
  .l24-boris-vs-sro-sozidanie__map { grid-template-columns: 1fr; gap: 0; }
  .l24-boris-vs-sro-sozidanie__side--fas { border-radius: 12px 12px 0 0; }
  .l24-boris-vs-sro-sozidanie__side--sro { border-radius: 0 0 12px 12px; }
  .l24-boris-vs-sro-sozidanie__bridge { flex-direction: row; padding: 10px 0; }
  .l24-boris-vs-sro-sozidanie__bridge-line {
    width: auto; height: 2px; flex: 1; min-height: 0;
    background: linear-gradient(90deg, rgba(245,158,11,0.5), rgba(236,201,75,0.7), rgba(16,185,129,0.5));
  }
  .l24-boris-vs-sro-sozidanie__bridge-badge {
    writing-mode: horizontal-tb; transform: none; padding: 6px 12px;
  }
  .l24-boris-vs-sro-sozidanie__etp-grid { grid-template-columns: 1fr 1fr; }
  .l24-boris-vs-sro-sozidanie__matrix { grid-template-columns: 1fr; }
  .l24-boris-vs-sro-sozidanie__matrix-h:not(:first-child) { display: none; }
  .l24-boris-vs-sro-sozidanie__matrix-cell--fas::before,
  .l24-boris-vs-sro-sozidanie__matrix-cell--sro::before {
    display: block; font-size: 0.62rem; font-weight: 800;
    letter-spacing: 0.04em; text-transform: uppercase; margin-bottom: 4px; opacity: 0.7;
  }
  .l24-boris-vs-sro-sozidanie__matrix-cell--fas::before { content: "Позиция ФАС"; color: #fde68a; }
  .l24-boris-vs-sro-sozidanie__matrix-cell--sro::before { content: "Позиция СРО"; color: #a7f3d0; }
  .l24-boris-vs-sro-sozidanie__shell { padding: 24px 18px 20px; }
}
</style>

<div class="l24-boris-vs-sro-sozidanie__shell">
  <p class="l24-boris-vs-sro-sozidanie__eyebrow">ARB · Президиум ВС 01.07.2026 · А40-232008/2023 · торги по банкротству</p>
  <h3 class="l24-boris-vs-sro-sozidanie__title">ФАС vs СРО «Созидание»: маятник инстанций и выбор ЭТП</h3>
  <p class="l24-boris-vs-sro-sozidanie__lead">Спор дважды прошёл полный круг судов: сначала победа ФАС, затем переворот СКЭС в пользу СРО (05.11.2025), и снова <strong>восстановление штрафа 3,5 млн ₽</strong> Президиумом 01.07.2026. Для арбитражного управляющего ключевой практический вопрос — можно ли размещать торги на площадке, аккредитованной не в «вашей» СРО.</p>

  <div class="l24-boris-vs-sro-sozidanie__map" role="group" aria-label="Две позиции спора: ФАС и СРО Созидание">
    <div class="l24-boris-vs-sro-sozidanie__side l24-boris-vs-sro-sozidanie__side--fas">
      <div class="l24-boris-vs-sro-sozidanie__side-hd">
        <svg class="l24-boris-vs-sro-sozidanie__side-icon" viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <rect x="2" y="2" width="32" height="32" rx="8" fill="rgba(245,158,11,0.18)" stroke="#f59e0b" stroke-width="1.5"/>
          <path d="M10 26V12h6v14M20 26V8h6v18" fill="none" stroke="#fcd34d" stroke-width="2" stroke-linecap="round"/>
          <circle cx="28" cy="8" r="4" fill="#ecc94b" stroke="#f59e0b" stroke-width="1"/>
          <text x="28" y="10" text-anchor="middle" fill="#0a1628" font-size="4.5" font-weight="800" font-family="system-ui,sans-serif">11</text>
        </svg>
        <p class="l24-boris-vs-sro-sozidanie__side-title">ФАС России</p>
      </div>
      <p class="l24-boris-vs-sro-sozidanie__side-case">ч. 5 ст. 11 135-ФЗ · штраф 3,5 млн ₽</p>
      <ul class="l24-boris-vs-sro-sozidanie__side-list">
        <li class="l24-boris-vs-sro-sozidanie__side-item"><strong>Координация</strong>Устав п. 6.2 = согласование отказа АУ от неаккредитованных ЭТП и организаторов торгов</li>
        <li class="l24-boris-vs-sro-sozidanie__side-item"><strong>ст. 20.3 127-ФЗ</strong>Достаточно аккредитации в любой СРО АУ — не обязательно «своей»</li>
        <li class="l24-boris-vs-sro-sozidanie__side-item"><strong>Итог 01.07.2026</strong>Президиум отменил СКЭС, восстановил предписание и штраф СРО</li>
      </ul>
    </div>

    <div class="l24-boris-vs-sro-sozidanie__bridge" aria-hidden="true">
      <div class="l24-boris-vs-sro-sozidanie__bridge-line"></div>
      <span class="l24-boris-vs-sro-sozidanie__bridge-badge">ВС · маятник</span>
      <div class="l24-boris-vs-sro-sozidanie__bridge-line"></div>
    </div>

    <div class="l24-boris-vs-sro-sozidanie__side l24-boris-vs-sro-sozidanie__side--sro">
      <div class="l24-boris-vs-sro-sozidanie__side-hd">
        <svg class="l24-boris-vs-sro-sozidanie__side-icon" viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <rect x="2" y="2" width="32" height="32" rx="8" fill="rgba(16,185,129,0.15)" stroke="#10b981" stroke-width="1.5"/>
          <circle cx="18" cy="14" r="6" fill="none" stroke="#6ee7b7" stroke-width="1.5"/>
          <path d="M8 28c0-5.5 4.5-10 10-10s10 4.5 10 10" fill="none" stroke="#6ee7b7" stroke-width="1.5"/>
          <rect x="22" y="6" width="10" height="8" rx="2" fill="rgba(16,185,129,0.25)" stroke="#6ee7b7" stroke-width="1"/>
          <text x="27" y="12" text-anchor="middle" fill="#a7f3d0" font-size="4" font-weight="700" font-family="system-ui,sans-serif">СРО</text>
        </svg>
        <p class="l24-boris-vs-sro-sozidanie__side-title">СРО «Созидание»</p>
      </div>
      <p class="l24-boris-vs-sro-sozidanie__side-case">п. 6.2 Устава · дисциплинарка до 500 000 ₽</p>
      <ul class="l24-boris-vs-sro-sozidanie__side-list">
        <li class="l24-boris-vs-sro-sozidanie__side-item"><strong>Профконтроль</strong>Только аккредитованные при союзе ОТ и операторы ЭТП; платная аккредитация до 500 000 ₽</li>
        <li class="l24-boris-vs-sro-sozidanie__side-item"><strong>СКЭС 05.11.2025</strong>ФАС не доказала антиконкурентную направленность — победа СРО (отменена)</li>
        <li class="l24-boris-vs-sro-sozidanie__side-item"><strong>«Арбитат»</strong>Индивидуальный риск: приговор 2020 г. — не продлили аккредитацию</li>
      </ul>
    </div>
  </div>

  <svg class="l24-boris-vs-sro-sozidanie__scheme-svg" viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="bsSroT bsSroD">
    <title id="bsSroT">Маятник инстанций по делу А40-232008/2023: ФАС, суды, СКЭС и Президиум ВС</title>
    <desc id="bsSroD">Хронология от решения ФАС 2023–2024 через победу СКЭС в ноябре 2025 к восстановлению актов ФАС Президиумом 01.07.2026; внизу — выбор ЭТП арбитражным управляющим</desc>
    <defs>
      <marker id="bsSro-arr" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
        <polygon points="0 0, 8 3.5, 0 7" fill="#ecc94b"/>
      </marker>
      <linearGradient id="bsSro-pend" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#f59e0b"/>
        <stop offset="50%" stop-color="#ecc94b"/>
        <stop offset="100%" stop-color="#10b981"/>
      </linearGradient>
    </defs>

    <text x="360" y="18" text-anchor="middle" fill="#ecc94b" font-size="8" font-weight="800" font-family="system-ui,sans-serif">МАЯТНИК ИНСТАНЦИЙ · А40-232008/2023</text>

    <line x1="60" y1="100" x2="660" y2="100" stroke="rgba(148,163,184,0.35)" stroke-width="2"/>
    <circle cx="120" cy="100" r="8" fill="#f59e0b" stroke="#fcd34d" stroke-width="1.5"/>
    <text x="120" y="78" text-anchor="middle" fill="#fde68a" font-size="6.5" font-weight="700" font-family="system-ui,sans-serif">ФАС</text>
    <text x="120" y="124" text-anchor="middle" fill="#94a3b8" font-size="5.5" font-family="system-ui,sans-serif">09.2023</text>

    <circle cx="240" cy="100" r="7" fill="#4338ca" stroke="#a5b4fc" stroke-width="1.2"/>
    <text x="240" y="78" text-anchor="middle" fill="#c7d2fe" font-size="6" font-weight="700" font-family="system-ui,sans-serif">АСГМ·ААС·АСМО</text>
    <text x="240" y="124" text-anchor="middle" fill="#94a3b8" font-size="5.5" font-family="system-ui,sans-serif">за ФАС</text>

    <circle cx="400" cy="72" r="9" fill="#10b981" stroke="#6ee7b7" stroke-width="1.5"/>
    <text x="400" y="52" text-anchor="middle" fill="#a7f3d0" font-size="6.5" font-weight="800" font-family="system-ui,sans-serif">СКЭС ВС</text>
    <text x="400" y="96" text-anchor="middle" fill="#94a3b8" font-size="5.5" font-family="system-ui,sans-serif">05.11.2025</text>
    <text x="400" y="108" text-anchor="middle" fill="#6ee7b7" font-size="5.5" font-family="system-ui,sans-serif">за СРО</text>
    <path d="M400 81 Q480 40 560 72" fill="none" stroke="#10b981" stroke-width="1.2" stroke-dasharray="4 3"/>

    <circle cx="560" cy="72" r="10" fill="#4338ca" stroke="#ecc94b" stroke-width="2"/>
    <text x="560" y="52" text-anchor="middle" fill="#fde68a" font-size="6.5" font-weight="800" font-family="system-ui,sans-serif">ПРЕЗИДИУМ</text>
    <text x="560" y="96" text-anchor="middle" fill="#94a3b8" font-size="5.5" font-family="system-ui,sans-serif">01.07.2026</text>
    <text x="560" y="108" text-anchor="middle" fill="#fcd34d" font-size="5.5" font-weight="700" font-family="system-ui,sans-serif">за ФАС ✓</text>
    <path d="M560 82 Q480 120 400 109" fill="none" stroke="#f59e0b" stroke-width="1.4" marker-end="url(#bsSro-arr)"/>

    <rect x="14" y="142" width="692" height="68" rx="10" fill="rgba(37,99,235,0.1)" stroke="#2563eb" stroke-width="1.2"/>
    <text x="360" y="160" text-anchor="middle" fill="#93c5fd" font-size="7" font-weight="800" font-family="system-ui,sans-serif">ВЫБОР ЭТП АРБИТРАЖНЫМ УПРАВЛЯЮЩИМ (ст. 20.3 · 20.7 127-ФЗ)</text>

    <rect x="28" y="168" width="88" height="32" rx="6" fill="rgba(16,185,129,0.15)" stroke="#10b981" stroke-width="1"/>
    <text x="72" y="182" text-anchor="middle" fill="#6ee7b7" font-size="6" font-weight="700" font-family="system-ui,sans-serif">МЭТС</text>
    <text x="72" y="194" text-anchor="middle" fill="#94a3b8" font-size="5" font-family="system-ui,sans-serif">другая СРО ✓</text>

    <rect x="128" y="168" width="88" height="32" rx="6" fill="rgba(16,185,129,0.15)" stroke="#10b981" stroke-width="1"/>
    <text x="172" y="182" text-anchor="middle" fill="#6ee7b7" font-size="6" font-weight="700" font-family="system-ui,sans-serif">Альфа-Лот</text>
    <text x="172" y="194" text-anchor="middle" fill="#94a3b8" font-size="5" font-family="system-ui,sans-serif">другая СРО ✓</text>

    <rect x="228" y="168" width="88" height="32" rx="6" fill="rgba(16,185,129,0.15)" stroke="#10b981" stroke-width="1"/>
    <text x="272" y="182" text-anchor="middle" fill="#6ee7b7" font-size="6" font-weight="700" font-family="system-ui,sans-serif">ЦДТ</text>
    <text x="272" y="194" text-anchor="middle" fill="#94a3b8" font-size="5" font-family="system-ui,sans-serif">другая СРО ✓</text>

    <rect x="328" y="168" width="100" height="32" rx="6" fill="rgba(67,56,202,0.2)" stroke="#4338ca" stroke-width="1.2"/>
    <text x="378" y="182" text-anchor="middle" fill="#a5b4fc" font-size="6" font-weight="800" font-family="system-ui,sans-serif">«Арбитат»</text>
    <text x="378" y="194" text-anchor="middle" fill="#c7d2fe" font-size="5" font-family="system-ui,sans-serif">кейс Петровой</text>

    <rect x="448" y="168" width="120" height="32" rx="6" fill="rgba(245,158,11,0.12)" stroke="#f59e0b" stroke-width="1"/>
    <text x="508" y="182" text-anchor="middle" fill="#fcd34d" font-size="5.8" font-weight="700" font-family="system-ui,sans-serif">только «своя» СРО</text>
    <text x="508" y="194" text-anchor="middle" fill="#f87171" font-size="5" font-family="system-ui,sans-serif">устав → риск ФАС</text>

    <rect x="588" y="168" width="104" height="32" rx="6" fill="rgba(236,201,75,0.12)" stroke="#ecc94b" stroke-width="1"/>
    <text x="640" y="182" text-anchor="middle" fill="#fde68a" font-size="5.8" font-weight="700" font-family="system-ui,sans-serif">штраф 3,5 млн</text>
    <text x="640" y="194" text-anchor="middle" fill="#94a3b8" font-size="5" font-family="system-ui,sans-serif">ориентир СРО</text>
  </svg>

  <p class="l24-boris-vs-sro-sozidanie__etp-hd">Площадки на рынке: критерий после 01.07.2026</p>
  <div class="l24-boris-vs-sro-sozidanie__etp-grid" role="group" aria-label="Карта электронных площадок для торгов по банкротству">
    <div class="l24-boris-vs-sro-sozidanie__etp-card l24-boris-vs-sro-sozidanie__etp-card--ok">
      <span class="l24-boris-vs-sro-sozidanie__etp-name">МЭТС</span>
      <span class="l24-boris-vs-sro-sozidanie__etp-status">аккредитация в иной СРО</span>
      <p class="l24-boris-vs-sro-sozidanie__etp-note">Допустимо при соблюдении ст. 20.3 и лимита ст. 20.7</p>
    </div>
    <div class="l24-boris-vs-sro-sozidanie__etp-card l24-boris-vs-sro-sozidanie__etp-card--ok">
      <span class="l24-boris-vs-sro-sozidanie__etp-name">Альфа-Лот</span>
      <span class="l24-boris-vs-sro-sozidanie__etp-status">аккредитация в иной СРО</span>
      <p class="l24-boris-vs-sro-sozidanie__etp-note">Проверить заинтересованность и обоснованность расходов</p>
    </div>
    <div class="l24-boris-vs-sro-sozidanie__etp-card l24-boris-vs-sro-sozidanie__etp-card--ok">
      <span class="l24-boris-vs-sro-sozidanie__etp-name">ЦДТ</span>
      <span class="l24-boris-vs-sro-sozidanie__etp-status">аккредитация в иной СРО</span>
      <p class="l24-boris-vs-sro-sozidanie__etp-note">Конкуренция площадок усиливается после позиции ВС</p>
    </div>
    <div class="l24-boris-vs-sro-sozidanie__etp-card l24-boris-vs-sro-sozidanie__etp-card--case">
      <span class="l24-boris-vs-sro-sozidanie__etp-name">«Арбитат»</span>
      <span class="l24-boris-vs-sro-sozidanie__etp-status">не в «Созидании»</span>
      <p class="l24-boris-vs-sro-sozidanie__etp-note">Торги Петровой → дисциплинарка 50 000 ₽ → жалоба в ФАС</p>
    </div>
  </div>

  <p class="l24-boris-vs-sro-sozidanie__pendulum-hd">Матрица: ситуация → позиции ФАС и СРО</p>
  <div class="l24-boris-vs-sro-sozidanie__matrix" role="table" aria-label="Матрица позиций ФАС и СРО по выбору электронной площадки">
    <div class="l24-boris-vs-sro-sozidanie__matrix-h">Ситуация</div>
    <div class="l24-boris-vs-sro-sozidanie__matrix-h l24-boris-vs-sro-sozidanie__matrix-h--fas">ФАС / Президиум ВС</div>
    <div class="l24-boris-vs-sro-sozidanie__matrix-h l24-boris-vs-sro-sozidanie__matrix-h--sro">СРО «Созидание»</div>

    <div class="l24-boris-vs-sro-sozidanie__matrix-row" role="row">
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--sit" role="cell">ЭТП аккредитована в другой СРО АУ</div>
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--fas" role="cell">Законно: ст. 20.3 не требует «своей» СРО</div>
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--sro" role="cell">Нарушение п. 6.2 Устава → дисциплинарка</div>
    </div>
    <div class="l24-boris-vs-sro-sozidanie__matrix-row" role="row">
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--sit" role="cell">Безусловный запрет всех «чужих» площадок</div>
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--fas" role="cell">Незаконная координация ч. 5 ст. 11 135-ФЗ</div>
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--sro" role="cell">Профконтроль и защита кредиторов (ст. 22, 25)</div>
    </div>
    <div class="l24-boris-vs-sro-sozidanie__matrix-row" role="row">
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--sit" role="cell">Платная аккредитация оператора ЭТП</div>
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--fas" role="cell">Имущественная выгода СРО, барьер рынка</div>
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--sro" role="cell">Компенсационный фонд и риски за АУ</div>
    </div>
    <div class="l24-boris-vs-sro-sozidanie__matrix-row" role="row">
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--sit" role="cell">Уголовное дело руководства ЭТП («Арбитат»)</div>
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--fas" role="cell">Индивидуальный риск ≠ запрет всех неаккредитованных</div>
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--sro" role="cell">Обоснованный отказ в аккредитации конкретному лицу</div>
    </div>
    <div class="l24-boris-vs-sro-sozidanie__matrix-row" role="row">
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--sit" role="cell">Жалоба АУ в ФАС на уставные ограничения</div>
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--fas" role="cell">Прецедент Петровой → предписание + штраф 3,5 млн</div>
      <div class="l24-boris-vs-sro-sozidanie__matrix-cell l24-boris-vs-sro-sozidanie__matrix-cell--sro" role="cell">Оспаривание в арбитраже и надзор (неустойчиво)</div>
    </div>
  </div>

  <p class="l24-boris-vs-sro-sozidanie__verdict"><strong>Практический вывод:</strong> после 01.07.2026 ориентир — аккредитация ЭТП хотя бы в одной СРО арбитражных управляющих, а не реестр «только своего» союза. Дисциплинарка за «чужую» площадку уязвима; при конфликте с СРО ссылайтесь на дело № А40-232008/2023 и жалобу в ФАС. Перед торгами проверьте ст. 20.7 (лимит расходов) и репутационные риски площадки.</p>

  <div class="l24-boris-vs-sro-sozidanie__foot" aria-label="Нормативная база блока">
    <span class="l24-boris-vs-sro-sozidanie__tag l24-boris-vs-sro-sozidanie__tag--case">Президиум ВС 01.07.2026</span>
    <span class="l24-boris-vs-sro-sozidanie__tag l24-boris-vs-sro-sozidanie__tag--fas">ч. 5 ст. 11 135-ФЗ</span>
    <span class="l24-boris-vs-sro-sozidanie__tag l24-boris-vs-sro-sozidanie__tag--law">ст. 20.3 · 20.7 127-ФЗ</span>
    <span class="l24-boris-vs-sro-sozidanie__tag l24-boris-vs-sro-sozidanie__tag--sro">СРО «Созидание» · п. 6.2</span>
    <span class="l24-boris-vs-sro-sozidanie__tag l24-boris-vs-sro-sozidanie__tag--case">А40-232008/2023</span>
    <span class="l24-boris-vs-sro-sozidanie__tag l24-boris-vs-sro-sozidanie__tag--law">торги по банкротству · ЭТП</span>
  </div>
</div>
</section>
```

## Передача Наташе

- **Якорь:** `l24-boris-vs-sro-sozidanie-evidence`
- **class секции:** `l24-boris-vs-sro-sozidanie`
- **После H2:** «Хронология спора ФАС vs СРО: дело № А40-232008/2023»
- **Перед:** H2 «Фабула дела: управляющий Петрова, ЭТП „Арбитат" и дисциплинарка 50 000 ₽»
- **MCP-only:** без `<canvas>` и `<script>` — только inline CSS + static SVG + grid
- **script:** нет
