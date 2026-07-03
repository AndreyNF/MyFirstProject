=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО
ЯКОРЬ: l24-boris-vs-maloznachitelnost-k6-path

## Паспорт блока

| Параметр | Значение |
|----------|----------|
| **Статья** | ВС РФ прекратил дело о краже в гипермаркете как малозначительное — кассация № 11-УД26-3-К6 (ч. 2 ст. 14 УК, ч. 1 ст. 158 УК) |
| **SLUG** | `vs-maloznachitelnost-krazha-st-14-zashchita-kassaciya-2026` |
| **Якорь** | `l24-boris-vs-maloznachitelnost-k6-path` |
| **id / class секции** | `id="l24-boris-vs-maloznachitelnost-k6-path"` · `class="l24-boris-vs-maloznachitelnost-k6"` |
| **Тема** | Сплит: путь дела по инстанциям (мировой → апелляция → 6-й КС → ВС) + сетка критериев малозначительности по п. 25.4 Пленума № 29 на фактах дела |
| **Размещение** | После H2 «Признаки и критерии малозначительности: п. 25.4 Пленума ВС № 29» — перед H2 «Формальный состав кражи (ч. 1 ст. 158 УК) vs реальная общественная опасность» |
| **Режим** | Контраст к светлому hero Алины (гипермаркет / формальный состав); тёмная редакционная схема в теле — MCP-only, inline CSS + static SVG |
| **Палитра** | Shell `#0c1424`–`#1a2744`; нижние инстанции: coral `#f87171` / `#fca5a5`; ВС: gold `#ecc94b`; прекращение: emerald `#34d399`; норма: indigo `#6366f1`; ч. 2 ст. 14: `#818cf8` |

## Чеклист отличий от hero Алины

- [x] Не полноэкранный первый экран — блок в теле лонгрида после 2–3 H2
- [x] Другой `id`: `l24-boris-vs-maloznachitelnost-k6-path` (не hero-id Алины)
- [x] Горизонтальная схема инстанций + сетка критериев п. 25.4 — не дублирует сцену hero
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG + grid
- [x] CTA в блоке **не вставлять**

```html
<section id="l24-boris-vs-maloznachitelnost-k6-path" class="l24-boris-vs-maloznachitelnost-k6" aria-label="Дело № 11-УД26-3-К6: путь по инстанциям и критерии малозначительности по ч. 2 ст. 14 УК и п. 25.4 Пленума ВС № 29">
<style>
.l24-boris-vs-maloznachitelnost-k6 {
  --bk-navy: #0c1424;
  --bk-navy-soft: #1a2744;
  --bk-muted: #94a3b8;
  --bk-txt: #e2e8f0;
  --bk-lower: #f87171;
  --bk-lower-soft: #fca5a5;
  --bk-lower-bg: rgba(248, 113, 113, 0.12);
  --bk-vs: #ecc94b;
  --bk-vs-bg: rgba(236, 201, 75, 0.14);
  --bk-ok: #34d399;
  --bk-ok-soft: #6ee7b7;
  --bk-ok-bg: rgba(52, 211, 153, 0.12);
  --bk-law: #818cf8;
  --bk-law-bg: rgba(99, 102, 241, 0.14);
  margin: 48px 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-vs-maloznachitelnost-k6__shell {
  background: linear-gradient(155deg, var(--bk-navy) 0%, #111d33 48%, var(--bk-navy-soft) 100%);
  border: 1px solid rgba(129, 140, 248, 0.28);
  border-radius: 14px;
  padding: 32px 28px 24px;
  color: var(--bk-txt);
  box-shadow: 0 18px 48px rgba(12, 20, 36, 0.38);
}
.l24-boris-vs-maloznachitelnost-k6__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--bk-vs);
}
.l24-boris-vs-maloznachitelnost-k6__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-vs-maloznachitelnost-k6__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--bk-muted);
  max-width: 78ch;
}
.l24-boris-vs-maloznachitelnost-k6__lead strong { color: #fff; }
.l24-boris-vs-maloznachitelnost-k6__split {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.85fr);
  gap: 22px;
  margin-bottom: 22px;
  align-items: start;
}
.l24-boris-vs-maloznachitelnost-k6__path-hd,
.l24-boris-vs-maloznachitelnost-k6__crit-hd {
  margin: 0 0 12px;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.l24-boris-vs-maloznachitelnost-k6__path-hd { color: var(--bk-lower-soft); }
.l24-boris-vs-maloznachitelnost-k6__crit-hd { color: var(--bk-law); }
.l24-boris-vs-maloznachitelnost-k6__scheme-svg {
  display: block;
  width: 100%;
  height: auto;
  margin-bottom: 14px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
}
.l24-boris-vs-maloznachitelnost-k6__contrast {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-bottom: 4px;
}
.l24-boris-vs-maloznachitelnost-k6__contrast-card {
  padding: 12px 12px 10px;
  border-radius: 10px;
  font-size: 0.74rem;
  line-height: 1.42;
  color: #cbd5e1;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-vs-maloznachitelnost-k6__contrast-card strong {
  display: block;
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  margin-bottom: 5px;
}
.l24-boris-vs-maloznachitelnost-k6__contrast-card--trap {
  border-color: rgba(248, 113, 113, 0.42);
  border-top: 3px solid var(--bk-lower);
}
.l24-boris-vs-maloznachitelnost-k6__contrast-card--trap strong { color: var(--bk-lower-soft); }
.l24-boris-vs-maloznachitelnost-k6__contrast-card--win {
  border-color: rgba(52, 211, 153, 0.42);
  border-top: 3px solid var(--bk-ok);
}
.l24-boris-vs-maloznachitelnost-k6__contrast-card--win strong { color: var(--bk-ok-soft); }
.l24-boris-vs-maloznachitelnost-k6__crit-panel {
  border-radius: 12px;
  padding: 16px 14px 14px;
  background: var(--bk-law-bg);
  border: 1px solid rgba(129, 140, 248, 0.35);
  height: 100%;
  box-sizing: border-box;
}
.l24-boris-vs-maloznachitelnost-k6__crit-ref {
  margin: 0 0 12px;
  padding: 8px 10px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.05);
  border-left: 3px solid var(--bk-law);
  font-size: 0.72rem;
  line-height: 1.45;
  color: #c7d2fe;
}
.l24-boris-vs-maloznachitelnost-k6__crit-list {
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-vs-maloznachitelnost-k6__crit-item {
  display: grid;
  grid-template-columns: 22px minmax(0, 1fr);
  gap: 10px;
  align-items: start;
  margin: 0 0 9px;
  padding: 9px 10px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.07);
  font-size: 0.74rem;
  line-height: 1.4;
  color: #cbd5e1;
}
.l24-boris-vs-maloznachitelnost-k6__crit-item:last-child { margin-bottom: 0; }
.l24-boris-vs-maloznachitelnost-k6__crit-mark {
  width: 20px;
  height: 20px;
  margin-top: 1px;
}
.l24-boris-vs-maloznachitelnost-k6__crit-item strong {
  display: block;
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  color: var(--bk-law);
  margin-bottom: 3px;
}
.l24-boris-vs-maloznachitelnost-k6__crit-val {
  color: var(--bk-ok-soft);
  font-weight: 600;
}
.l24-boris-vs-maloznachitelnost-k6__matrix {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr) minmax(0, 1fr);
  gap: 0;
  margin-bottom: 18px;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-vs-maloznachitelnost-k6__matrix-h {
  padding: 10px 12px;
  font-size: 0.66rem;
  font-weight: 800;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  background: rgba(255, 255, 255, 0.08);
  color: #e2e8f0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-vs-maloznachitelnost-k6__matrix-h--lower { color: var(--bk-lower-soft); }
.l24-boris-vs-maloznachitelnost-k6__matrix-h--vs { color: var(--bk-vs); }
.l24-boris-vs-maloznachitelnost-k6__matrix-row { display: contents; }
.l24-boris-vs-maloznachitelnost-k6__matrix-cell {
  padding: 10px 12px;
  font-size: 0.74rem;
  line-height: 1.4;
  color: #cbd5e1;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  background: rgba(255, 255, 255, 0.03);
}
.l24-boris-vs-maloznachitelnost-k6__matrix-cell--inst {
  font-weight: 600;
  color: #e2e8f0;
  background: rgba(255, 255, 255, 0.05);
}
.l24-boris-vs-maloznachitelnost-k6__matrix-cell--lower { color: #fecaca; }
.l24-boris-vs-maloznachitelnost-k6__matrix-cell--vs { color: #fde68a; font-weight: 600; }
.l24-boris-vs-maloznachitelnost-k6__matrix-row:last-child .l24-boris-vs-maloznachitelnost-k6__matrix-cell { border-bottom: none; }
.l24-boris-vs-maloznachitelnost-k6__verdict {
  margin: 0 0 16px;
  padding: 14px 16px;
  border-radius: 10px;
  background: var(--bk-ok-bg);
  border: 1px solid rgba(52, 211, 153, 0.32);
  font-size: 0.84rem;
  line-height: 1.5;
  color: var(--bk-muted);
}
.l24-boris-vs-maloznachitelnost-k6__verdict strong { color: var(--bk-ok-soft); }
.l24-boris-vs-maloznachitelnost-k6__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-vs-maloznachitelnost-k6__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  color: var(--bk-txt);
  border: 1px solid rgba(255, 255, 255, 0.13);
}
.l24-boris-vs-maloznachitelnost-k6__tag--case { border-color: rgba(236, 201, 75, 0.5); color: var(--bk-vs); }
.l24-boris-vs-maloznachitelnost-k6__tag--law { border-color: rgba(129, 140, 248, 0.45); color: #c7d2fe; }
.l24-boris-vs-maloznachitelnost-k6__tag--ok { border-color: rgba(52, 211, 153, 0.45); color: var(--bk-ok-soft); }
.l24-boris-vs-maloznachitelnost-k6__tag--lower { border-color: rgba(248, 113, 113, 0.45); color: var(--bk-lower-soft); }
@media (max-width: 860px) {
  .l24-boris-vs-maloznachitelnost-k6__split { grid-template-columns: 1fr; }
  .l24-boris-vs-maloznachitelnost-k6__contrast { grid-template-columns: 1fr; }
  .l24-boris-vs-maloznachitelnost-k6__matrix { grid-template-columns: 1fr; }
  .l24-boris-vs-maloznachitelnost-k6__matrix-h:not(:first-child) { display: none; }
  .l24-boris-vs-maloznachitelnost-k6__matrix-cell--lower::before,
  .l24-boris-vs-maloznachitelnost-k6__matrix-cell--vs::before {
    display: block; font-size: 0.6rem; font-weight: 800;
    letter-spacing: 0.04em; text-transform: uppercase; margin-bottom: 4px; opacity: 0.75;
  }
  .l24-boris-vs-maloznachitelnost-k6__matrix-cell--lower::before { content: "3 инстанции"; color: var(--bk-lower-soft); }
  .l24-boris-vs-maloznachitelnost-k6__matrix-cell--vs::before { content: "ВС РФ"; color: var(--bk-vs); }
  .l24-boris-vs-maloznachitelnost-k6__shell { padding: 24px 18px 20px; }
}
</style>

<div class="l24-boris-vs-maloznachitelnost-k6__shell">
  <p class="l24-boris-vs-maloznachitelnost-k6__eyebrow">UG · кассация ВС 14.04.2026 · № 11-УД26-3-К6 · ч. 2 ст. 14 УК</p>
  <h3 class="l24-boris-vs-maloznachitelnost-k6__title">Путь дела и критерии малозначительности: от «мягкого приговора» к прекращению</h3>
  <p class="l24-boris-vs-maloznachitelnost-k6__lead">Три нижестоящие инстанции признали вину по <strong>ч. 1 ст. 158 УК</strong> и применили освобождение от наказания (<strong>ст. 92 УК</strong>) с ПМВВ. Верховный суд отменил все акты: формальный состав кражи на <strong>5 674,25 ₽</strong> не равен преступлению при совокупности критериев <strong>п. 25.4 Пленума № 29</strong>.</p>

  <div class="l24-boris-vs-maloznachitelnost-k6__split">
    <div class="l24-boris-vs-maloznachitelnost-k6__path-col">
      <p class="l24-boris-vs-maloznachitelnost-k6__path-hd">Путь дела по инстанциям</p>

      <svg class="l24-boris-vs-maloznachitelnost-k6__scheme-svg" viewBox="0 0 720 248" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="bkMalT bkMalD">
        <title id="bkMalT">Хронология дела № 11-УД26-3-К6: мировой суд → апелляция → 6-й кассационный суд → ВС РФ</title>
        <desc id="bkMalD">Три нижестоящие инстанции оставили вину и мягкий исход; ВС 14.04.2026 отменил приговор и прекратил дело по ч. 2 ст. 14 УК с реабилитацией</desc>
        <defs>
          <marker id="bkMal-arr" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
            <polygon points="0 0, 8 3.5, 0 7" fill="#94a3b8"/>
          </marker>
          <marker id="bkMal-arr-gold" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
            <polygon points="0 0, 8 3.5, 0 7" fill="#ecc94b"/>
          </marker>
          <linearGradient id="bkMal-line" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#f87171"/>
            <stop offset="72%" stop-color="#f87171"/>
            <stop offset="100%" stop-color="#ecc94b"/>
          </linearGradient>
        </defs>

        <text x="360" y="20" text-anchor="middle" fill="#94a3b8" font-size="7.5" font-weight="800" font-family="system-ui,sans-serif" letter-spacing="0.06em">КРАЖА В «МАГНИТЕ» · 5 674,25 ₽ · НЕСОВЕРШЕННОЛЕТНЯЯ 16 ЛЕТ</text>

        <line x1="72" y1="108" x2="648" y2="108" stroke="url(#bkMal-line)" stroke-width="2.5" marker-end="url(#bkMal-arr-gold)"/>

        <circle cx="96" cy="108" r="11" fill="#f87171" stroke="#fca5a5" stroke-width="1.5"/>
        <text x="96" y="78" text-anchor="middle" fill="#fecaca" font-size="6.5" font-weight="800" font-family="system-ui,sans-serif">МИРОВОЙ</text>
        <text x="96" y="90" text-anchor="middle" fill="#94a3b8" font-size="5.5" font-family="system-ui,sans-serif">29.04.2025</text>
        <text x="96" y="132" text-anchor="middle" fill="#fca5a5" font-size="5.8" font-weight="700" font-family="system-ui,sans-serif">виновна</text>
        <text x="96" y="144" text-anchor="middle" fill="#94a3b8" font-size="5.2" font-family="system-ui,sans-serif">ст. 92 + ПМВВ</text>

        <circle cx="264" cy="108" r="10" fill="#f87171" stroke="#fca5a5" stroke-width="1.4"/>
        <text x="264" y="78" text-anchor="middle" fill="#fecaca" font-size="6.2" font-weight="800" font-family="system-ui,sans-serif">АПЕЛЛЯЦИЯ</text>
        <text x="264" y="90" text-anchor="middle" fill="#94a3b8" font-size="5.5" font-family="system-ui,sans-serif">11.06.2025</text>
        <text x="264" y="132" text-anchor="middle" fill="#fca5a5" font-size="5.8" font-weight="700" font-family="system-ui,sans-serif">без изменений</text>
        <text x="264" y="144" text-anchor="middle" fill="#94a3b8" font-size="5.2" font-family="system-ui,sans-serif">малознач. не обсуждали</text>

        <circle cx="432" cy="108" r="10" fill="#f87171" stroke="#fca5a5" stroke-width="1.4"/>
        <text x="432" y="74" text-anchor="middle" fill="#fecaca" font-size="6" font-weight="800" font-family="system-ui,sans-serif">6-й КСОЮ</text>
        <text x="432" y="86" text-anchor="middle" fill="#94a3b8" font-size="5.5" font-family="system-ui,sans-serif">24.09.2025</text>
        <text x="432" y="132" text-anchor="middle" fill="#fca5a5" font-size="5.8" font-weight="700" font-family="system-ui,sans-serif">без изменений</text>
        <text x="432" y="144" text-anchor="middle" fill="#94a3b8" font-size="5.2" font-family="system-ui,sans-serif">п. 25.4 проигнорирован</text>

        <circle cx="624" cy="108" r="13" fill="#4338ca" stroke="#ecc94b" stroke-width="2"/>
        <text x="624" y="74" text-anchor="middle" fill="#fde68a" font-size="6.5" font-weight="800" font-family="system-ui,sans-serif">ВС РФ</text>
        <text x="624" y="86" text-anchor="middle" fill="#94a3b8" font-size="5.5" font-family="system-ui,sans-serif">14.04.2026</text>
        <text x="624" y="132" text-anchor="middle" fill="#6ee7b7" font-size="5.8" font-weight="800" font-family="system-ui,sans-serif">отмена всех актов</text>
        <text x="624" y="144" text-anchor="middle" fill="#a7f3d0" font-size="5.2" font-family="system-ui,sans-serif">ч. 2 ст. 14 · реабилитация</text>

        <path d="M96 121 Q360 168 624 121" fill="none" stroke="#34d399" stroke-width="1.2" stroke-dasharray="5 4" opacity="0.55"/>

        <rect x="24" y="178" width="672" height="58" rx="10" fill="rgba(129,140,248,0.1)" stroke="#818cf8" stroke-width="1.2"/>
        <text x="360" y="196" text-anchor="middle" fill="#c7d2fe" font-size="6.8" font-weight="800" font-family="system-ui,sans-serif">ФОРМАЛЬНЫЙ СОСТАВ ≠ ПРЕСТУПЛЕНИЕ · ч. 2 ст. 14 УК · п. 2 ч. 1 ст. 24 УПК</text>
        <text x="180" y="216" text-anchor="middle" fill="#fca5a5" font-size="5.5" font-family="system-ui,sans-serif">3 инстанции: вина признана</text>
        <text x="360" y="216" text-anchor="middle" fill="#94a3b8" font-size="5.5" font-family="system-ui,sans-serif">общественная опасность не оценена</text>
        <text x="540" y="216" text-anchor="middle" fill="#6ee7b7" font-size="5.5" font-weight="700" font-family="system-ui,sans-serif">ВС: состава нет → прекращение</text>
        <text x="360" y="228" text-anchor="middle" fill="#fde68a" font-size="5.2" font-family="system-ui,sans-serif">возмещение родственниками · ущерб гипермаркету фактически отсутствует</text>
      </svg>

      <div class="l24-boris-vs-maloznachitelnost-k6__contrast" role="group" aria-label="Контраст мягкого приговора и прекращения дела">
        <div class="l24-boris-vs-maloznachitelnost-k6__contrast-card l24-boris-vs-maloznachitelnost-k6__contrast-card--trap">
          <strong>Ловушка «мягкого» исхода</strong>
          ст. 92 УК + ПМВВ: вина формально установлена, малозначительность не обсуждалась — судимость и ограничения досуга остаются риском.
        </div>
        <div class="l24-boris-vs-maloznachitelnost-k6__contrast-card l24-boris-vs-maloznachitelnost-k6__contrast-card--win">
          <strong>Исход ВС по ч. 2 ст. 14</strong>
          Прекращение по п. 2 ч. 1 ст. 24 УПК: вины нет, право на реабилитацию (ст. 133 УПК) — целевой запрос кассационной жалобы.
        </div>
      </div>
    </div>

    <div class="l24-boris-vs-maloznachitelnost-k6__crit-col">
      <p class="l24-boris-vs-maloznachitelnost-k6__crit-hd">Критерии п. 25.4 · совокупность в деле</p>
      <div class="l24-boris-vs-maloznachitelnost-k6__crit-panel">
        <p class="l24-boris-vs-maloznachitelnost-k6__crit-ref">П. 25.4 Пленума ВС № 29: при кражe учитывать <strong>совокупность</strong> — степень реализации умысла, размер похищенного, роль в соучастии, обстоятельства деяния и иные факторы + ч. 2 ст. 14 УК.</p>
        <ul class="l24-boris-vs-maloznachitelnost-k6__crit-list">
          <li class="l24-boris-vs-maloznachitelnost-k6__crit-item">
            <svg class="l24-boris-vs-maloznachitelnost-k6__crit-mark" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="9" fill="rgba(129,140,248,0.2)" stroke="#818cf8" stroke-width="1.2"/><path d="M6 10.5l2.5 2.5 5.5-6" fill="none" stroke="#c7d2fe" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <div><strong>Степень реализации умысла</strong>Кража через кассу самообслуживания — умысел подтверждён, но <span class="l24-boris-vs-maloznachitelnost-k6__crit-val">общественная опасность недостаточна</span></div>
          </li>
          <li class="l24-boris-vs-maloznachitelnost-k6__crit-item">
            <svg class="l24-boris-vs-maloznachitelnost-k6__crit-mark" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="9" fill="rgba(129,140,248,0.2)" stroke="#818cf8" stroke-width="1.2"/><path d="M6 10.5l2.5 2.5 5.5-6" fill="none" stroke="#c7d2fe" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <div><strong>Размер похищенного</strong><span class="l24-boris-vs-maloznachitelnost-k6__crit-val">5 674,25 ₽</span> — уголовная ч. 1 ст. 158 (~2,3× порога 2 500 ₽), но мало для крупного гипермаркета</div>
          </li>
          <li class="l24-boris-vs-maloznachitelnost-k6__crit-item">
            <svg class="l24-boris-vs-maloznachitelnost-k6__crit-mark" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="9" fill="rgba(129,140,248,0.2)" stroke="#818cf8" stroke-width="1.2"/><path d="M6 10.5l2.5 2.5 5.5-6" fill="none" stroke="#c7d2fe" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <div><strong>Роль в соучастии</strong>Единоличное деяние, без организаторской роли — <span class="l24-boris-vs-maloznachitelnost-k6__crit-val">фактор не усиливает опасность</span></div>
          </li>
          <li class="l24-boris-vs-maloznachitelnost-k6__crit-item">
            <svg class="l24-boris-vs-maloznachitelnost-k6__crit-mark" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="9" fill="rgba(129,140,248,0.2)" stroke="#818cf8" stroke-width="1.2"/><path d="M6 10.5l2.5 2.5 5.5-6" fill="none" stroke="#c7d2fe" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <div><strong>Обстоятельства деяния</strong>Полное <span class="l24-boris-vs-maloznachitelnost-k6__crit-val">возмещение родственниками</span> до суда; негативных последствий для «Магнита» нет</div>
          </li>
          <li class="l24-boris-vs-maloznachitelnost-k6__crit-item">
            <svg class="l24-boris-vs-maloznachitelnost-k6__crit-mark" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="9" fill="rgba(129,140,248,0.2)" stroke="#818cf8" stroke-width="1.2"/><path d="M6 10.5l2.5 2.5 5.5-6" fill="none" stroke="#c7d2fe" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <div><strong>Личность · иные факторы</strong><span class="l24-boris-vs-maloznachitelnost-k6__crit-val">16 лет</span>, не судима, положительная характеристика — ВС учёл при оценке вреда обществу</div>
          </li>
        </ul>
      </div>
    </div>
  </div>

  <div class="l24-boris-vs-maloznachitelnost-k6__matrix" role="table" aria-label="Сравнение позиций нижестоящих судов и ВС РФ по делу о малозначительности">
    <div class="l24-boris-vs-maloznachitelnost-k6__matrix-h">Инстанция</div>
    <div class="l24-boris-vs-maloznachitelnost-k6__matrix-h l24-boris-vs-maloznachitelnost-k6__matrix-h--lower">3 инстанции до ВС</div>
    <div class="l24-boris-vs-maloznachitelnost-k6__matrix-h l24-boris-vs-maloznachitelnost-k6__matrix-h--vs">ВС РФ · 14.04.2026</div>

    <div class="l24-boris-vs-maloznachitelnost-k6__matrix-row" role="row">
      <div class="l24-boris-vs-maloznachitelnost-k6__matrix-cell l24-boris-vs-maloznachitelnost-k6__matrix-cell--inst" role="cell">Вопрос о составе</div>
      <div class="l24-boris-vs-maloznachitelnost-k6__matrix-cell l24-boris-vs-maloznachitelnost-k6__matrix-cell--lower" role="cell">Признаки ч. 1 ст. 158 → вина установлена</div>
      <div class="l24-boris-vs-maloznachitelnost-k6__matrix-cell l24-boris-vs-maloznachitelnost-k6__matrix-cell--vs" role="cell">Общественная опасность недостаточна → состава нет</div>
    </div>
    <div class="l24-boris-vs-maloznachitelnost-k6__matrix-row" role="row">
      <div class="l24-boris-vs-maloznachitelnost-k6__matrix-cell l24-boris-vs-maloznachitelnost-k6__matrix-cell--inst" role="cell">Малозначительность</div>
      <div class="l24-boris-vs-maloznachitelnost-k6__matrix-cell l24-boris-vs-maloznachitelnost-k6__matrix-cell--lower" role="cell">Не обсуждалась — нарушение п. 25.4</div>
      <div class="l24-boris-vs-maloznachitelnost-k6__matrix-cell l24-boris-vs-maloznachitelnost-k6__matrix-cell--vs" role="cell">Ч. 2 ст. 14 УК применена — дело прекращено</div>
    </div>
    <div class="l24-boris-vs-maloznachitelnost-k6__matrix-row" role="row">
      <div class="l24-boris-vs-maloznachitelnost-k6__matrix-cell l24-boris-vs-maloznachitelnost-k6__matrix-cell--inst" role="cell">Процессуальный итог</div>
      <div class="l24-boris-vs-maloznachitelnost-k6__matrix-cell l24-boris-vs-maloznachitelnost-k6__matrix-cell--lower" role="cell">ст. 92 УК + ПМВВ (ограничение досуга 6 мес.)</div>
      <div class="l24-boris-vs-maloznachitelnost-k6__matrix-cell l24-boris-vs-maloznachitelnost-k6__matrix-cell--vs" role="cell">п. 2 ч. 1 ст. 24 УПК + реабилитация ст. 133 УПК</div>
    </div>
    <div class="l24-boris-vs-maloznachitelnost-k6__matrix-row" role="row">
      <div class="l24-boris-vs-maloznachitelnost-k6__matrix-cell l24-boris-vs-maloznachitelnost-k6__matrix-cell--inst" role="cell">Ущерб потерпевшему</div>
      <div class="l24-boris-vs-maloznachitelnost-k6__matrix-cell l24-boris-vs-maloznachitelnost-k6__matrix-cell--lower" role="cell">Сумма зафиксирована, возмещение не учтено</div>
      <div class="l24-boris-vs-maloznachitelnost-k6__matrix-cell l24-boris-vs-maloznachitelnost-k6__matrix-cell--vs" role="cell">Фактический ущерб отсутствует — ключевой фактор ВС</div>
    </div>
  </div>

  <p class="l24-boris-vs-maloznachitelnost-k6__verdict"><strong>Для защиты в кассации:</strong> ссылаться на совокупность п. 25.4 (не только сумму), процессуальное нарушение — суды не мотивировали отказ от ч. 2 ст. 14 УК, требовать прекращение и реабилитацию, а не замену наказания. Прецедент № 11-УД26-3-К6 — дайджест ВС «Уголовный процесс» № 7, июль 2026.</p>

  <div class="l24-boris-vs-maloznachitelnost-k6__foot" aria-label="Нормативная база блока">
    <span class="l24-boris-vs-maloznachitelnost-k6__tag l24-boris-vs-maloznachitelnost-k6__tag--case">ВС 14.04.2026 · № 11-УД26-3-К6</span>
    <span class="l24-boris-vs-maloznachitelnost-k6__tag l24-boris-vs-maloznachitelnost-k6__tag--law">ч. 2 ст. 14 УК</span>
    <span class="l24-boris-vs-maloznachitelnost-k6__tag l24-boris-vs-maloznachitelnost-k6__tag--law">п. 25.4 Пленума № 29</span>
    <span class="l24-boris-vs-maloznachitelnost-k6__tag l24-boris-vs-maloznachitelnost-k6__tag--law">ч. 1 ст. 158 УК · 5 674,25 ₽</span>
    <span class="l24-boris-vs-maloznachitelnost-k6__tag l24-boris-vs-maloznachitelnost-k6__tag--lower">ст. 92 УК ≠ прекращение</span>
    <span class="l24-boris-vs-maloznachitelnost-k6__tag l24-boris-vs-maloznachitelnost-k6__tag--ok">ст. 133 УПК · реабилитация</span>
  </div>
</div>
</section>
```

## Передача Наташе

- **Якорь:** `l24-boris-vs-maloznachitelnost-k6-path`
- **class секции:** `l24-boris-vs-maloznachitelnost-k6`
- **После H2:** «Признаки и критерии малозначительности: п. 25.4 Пленума ВС № 29»
- **Перед:** H2 «Формальный состав кражи (ч. 1 ст. 158 УК) vs реальная общественная опасность»
- **MCP-only:** без `<canvas>` и `<script>` — только inline CSS + static SVG + grid
- **script:** нет
