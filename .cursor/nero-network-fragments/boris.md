=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** `ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026`  
**Якорь:** `l24-boris-st159-ch4-ch5-matrix`  
**Размещение:** сразу после H3 «Таблица сравнения: состав, ущерб, санкции, сроки» (внутри H2 «Ч. 4 и ч. 5 ст. 159 УК РФ — в чём разница»), перед H2 «Ошибочная практика судов до постановления КС» — якорь для Natasha.  
**Режим:** тёмная панель в теле статьи (контраст со светлым hero Алины) — **сравнительная сетка ч. 4 vs ч. 5 ст. 159 + SVG «ловушка порогов»** по делу Шеврюкова (КС № 43-П/2026, ВС № 64-УД26-2-К9).  
**Legis24 MCP-only:** static SVG + inline CSS, без `<canvas>` и `<script>`.

```html
<section id="l24-boris-st159-ch4-ch5-matrix" class="l24-boris-st159-ch4-ch5-matrix" aria-label="Сравнение ч. 4 и ч. 5 ст. 159 УК РФ: состав, ущерб, санкции и ловушка порогов в деле Шеврюкова">
<style>
.l24-boris-st159-ch4-ch5-matrix {
  --st159-navy: #0f1c2e;
  --st159-navy-soft: #1a3050;
  --st159-ch4: #fc8181;
  --st159-ch4-soft: #fed7d7;
  --st159-ch5: #68d391;
  --st159-ch5-soft: #c6f6d5;
  --st159-gold: #ecc94b;
  --st159-blue: #63b3ed;
  --st159-ink: #e2e8f0;
  --st159-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-st159-ch4-ch5-matrix__shell {
  background: linear-gradient(155deg, var(--st159-navy) 0%, #152a45 50%, var(--st159-navy-soft) 100%);
  border: 1px solid rgba(99, 179, 237, 0.28);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: 0 18px 48px rgba(15, 28, 46, 0.34);
  color: var(--st159-ink);
}
.l24-boris-st159-ch4-ch5-matrix__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--st159-gold);
}
.l24-boris-st159-ch4-ch5-matrix__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-st159-ch4-ch5-matrix__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--st159-muted);
  max-width: 72ch;
}
.l24-boris-st159-ch4-ch5-matrix__lead strong { color: #fff; }
.l24-boris-st159-ch4-ch5-matrix__split {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1.15fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-st159-ch4-ch5-matrix__panel {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-st159-ch4-ch5-matrix__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--st159-gold);
}
.l24-boris-st159-ch4-ch5-matrix__scheme-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 360px;
  margin-bottom: 12px;
}
.l24-boris-st159-ch4-ch5-matrix__verdict {
  margin: 0;
  padding: 12px 14px;
  border-radius: 8px;
  background: rgba(236, 201, 75, 0.12);
  border: 1px solid rgba(236, 201, 75, 0.38);
  font-size: 0.78rem;
  line-height: 1.45;
  color: var(--st159-ink);
}
.l24-boris-st159-ch4-ch5-matrix__verdict strong { color: var(--st159-gold); }
.l24-boris-st159-ch4-ch5-matrix__caption {
  margin: 10px 0 0;
  font-size: 0.7rem;
  line-height: 1.4;
  color: rgba(160, 174, 192, 0.88);
  text-align: center;
}
.l24-boris-st159-ch4-ch5-matrix__compare-head {
  display: grid;
  grid-template-columns: minmax(0, 0.9fr) minmax(0, 1fr) minmax(0, 1fr);
  gap: 8px;
  margin: 0 0 8px;
  padding: 0 4px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
.l24-boris-st159-ch4-ch5-matrix__compare-head span:nth-child(2) { color: var(--st159-ch4-soft); text-align: center; }
.l24-boris-st159-ch4-ch5-matrix__compare-head span:nth-child(3) { color: var(--st159-ch5-soft); text-align: center; }
.l24-boris-st159-ch4-ch5-matrix__grid {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin: 0 0 14px;
}
.l24-boris-st159-ch4-ch5-matrix__row {
  display: grid;
  grid-template-columns: minmax(0, 0.9fr) minmax(0, 1fr) minmax(0, 1fr);
  gap: 8px;
  align-items: start;
  padding: 10px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.74rem;
  line-height: 1.38;
}
.l24-boris-st159-ch4-ch5-matrix__row--key { border-left: 3px solid var(--st159-gold); }
.l24-boris-st159-ch4-ch5-matrix__row-label {
  font-weight: 700;
  color: #fff;
  font-size: 0.76rem;
}
.l24-boris-st159-ch4-ch5-matrix__cell {
  color: var(--st159-muted);
  padding: 4px 8px;
  border-radius: 6px;
}
.l24-boris-st159-ch4-ch5-matrix__cell--ch4 {
  background: rgba(252, 129, 129, 0.12);
  border: 1px solid rgba(252, 129, 129, 0.28);
}
.l24-boris-st159-ch4-ch5-matrix__cell--ch5 {
  background: rgba(104, 211, 145, 0.12);
  border: 1px solid rgba(104, 211, 145, 0.28);
}
.l24-boris-st159-ch4-ch5-matrix__cell em {
  font-style: normal;
  font-weight: 600;
  color: #fff;
}
.l24-boris-st159-ch4-ch5-matrix__cell--ch4 em { color: var(--st159-ch4-soft); }
.l24-boris-st159-ch4-ch5-matrix__cell--ch5 em { color: var(--st159-ch5-soft); }
.l24-boris-st159-ch4-ch5-matrix__case-bar {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 0 0 10px;
}
.l24-boris-st159-ch4-ch5-matrix__case-card {
  padding: 10px 12px;
  border-radius: 8px;
  font-size: 0.72rem;
  line-height: 1.4;
}
.l24-boris-st159-ch4-ch5-matrix__case-card--before {
  background: rgba(252, 129, 129, 0.14);
  border: 1px solid rgba(252, 129, 129, 0.4);
}
.l24-boris-st159-ch4-ch5-matrix__case-card--after {
  background: rgba(104, 211, 145, 0.14);
  border: 1px solid rgba(104, 211, 145, 0.4);
}
.l24-boris-st159-ch4-ch5-matrix__case-card strong {
  display: block;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-st159-ch4-ch5-matrix__case-card--before strong { color: var(--st159-ch4-soft); }
.l24-boris-st159-ch4-ch5-matrix__case-card--after strong { color: var(--st159-ch5-soft); }
.l24-boris-st159-ch4-ch5-matrix__note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--st159-muted);
}
.l24-boris-st159-ch4-ch5-matrix__note em {
  font-style: normal;
  color: #bee3f8;
  font-weight: 600;
}
.l24-boris-st159-ch4-ch5-matrix__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-st159-ch4-ch5-matrix__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--st159-ink);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.l24-boris-st159-ch4-ch5-matrix__tag--case {
  border-color: rgba(236, 201, 75, 0.5);
  color: var(--st159-gold);
}
.l24-boris-st159-ch4-ch5-matrix__tag--art { border-color: rgba(99, 179, 237, 0.45); color: #bee3f8; }
.l24-boris-st159-ch4-ch5-matrix__tag--def { border-color: rgba(104, 211, 145, 0.45); color: #c6f6d5; }
@media (max-width: 900px) {
  .l24-boris-st159-ch4-ch5-matrix__split { grid-template-columns: 1fr; }
  .l24-boris-st159-ch4-ch5-matrix__compare-head { display: none; }
  .l24-boris-st159-ch4-ch5-matrix__row {
    grid-template-columns: 1fr;
    gap: 6px;
  }
  .l24-boris-st159-ch4-ch5-matrix__cell--ch4::before,
  .l24-boris-st159-ch4-ch5-matrix__cell--ch5::before {
    display: block;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-bottom: 3px;
  }
  .l24-boris-st159-ch4-ch5-matrix__cell--ch4::before { content: "ч. 4 ст. 159"; color: var(--st159-ch4-soft); }
  .l24-boris-st159-ch4-ch5-matrix__cell--ch5::before { content: "ч. 5 ст. 159"; color: var(--st159-ch5-soft); }
  .l24-boris-st159-ch4-ch5-matrix__case-bar { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-st159-ch4-ch5-matrix__shell">
    <p class="l24-boris-st159-ch4-ch5-matrix__eyebrow">ст. 159 УК · ч. 4 vs ч. 5 · КС № 43-П/2026 · ВС № 64-УД26-2-К9 · дело Шеврюкова</p>
    <h3 class="l24-boris-st159-ch4-ch5-matrix__title">Переквалификация мошенничества: ч. 4 (тяжкое) ↔ ч. 5 (предпринимательское)</h3>
    <p class="l24-boris-st159-ch4-ch5-matrix__lead">Один и тот же ущерб <strong>2 159 315,11 ₽</strong> в деле Шеврюкова (подряд с ПАО «Сахалинэнерго») по общей норме — <strong>особо крупный</strong> (ч. 4, до 10 лет), по специальной шкале ч. 5–7 — лишь <strong>значительный</strong> (до 5 лет). ВС переквалифицировал состав; КС признал неконституционной практику отказа из‑за госакционера.</p>

    <div class="l24-boris-st159-ch4-ch5-matrix__split">
      <div class="l24-boris-st159-ch4-ch5-matrix__panel">
        <p class="l24-boris-st159-ch4-ch5-matrix__panel-title">Ловушка порогов: две шкалы ущерба при ~2,16 млн ₽</p>
        <svg class="l24-boris-st159-ch4-ch5-matrix__scheme-svg" viewBox="0 0 600 350" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="st159-scheme-title st159-scheme-desc">
          <title id="st159-scheme-title">Схема переквалификации мошенничества с ч. 4 на ч. 5 ст. 159 УК РФ</title>
          <desc id="st159-scheme-desc">Ущерб 2,16 млн рублей квалифицируется как особо крупный по ч. 4 и как значительный по ч. 5; дело Шеврюкова — переквалификация ВС и постановление КС № 43-П/2026</desc>
          <defs>
            <linearGradient id="st159-flow" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#fc8181"/>
              <stop offset="50%" stop-color="#ecc94b"/>
              <stop offset="100%" stop-color="#68d391"/>
            </linearGradient>
            <marker id="st159-arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0,0 L8,4 L0,8 Z" fill="#ecc94b"/>
            </marker>
          </defs>

          <text x="300" y="16" text-anchor="middle" fill="#ecc94b" font-size="8" font-weight="600">дело Шеврюкова · ПАО «Сахалинэнерго» · ущерб 2 159 315,11 ₽</text>

          <!-- Damage marker -->
          <rect x="220" y="26" width="160" height="28" rx="6" fill="rgba(236,201,75,0.2)" stroke="#ecc94b" stroke-width="1.5"/>
          <text x="300" y="44" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">2,16 млн ₽</text>

          <!-- Fork arrows -->
          <path d="M 260 54 L 140 78" stroke="#fc8181" stroke-width="2" fill="none" marker-end="url(#st159-arrow)"/>
          <path d="M 340 54 L 460 78" stroke="#68d391" stroke-width="2" fill="none" marker-end="url(#st159-arrow)"/>

          <!-- Ch4 scale -->
          <rect x="24" y="80" width="232" height="108" rx="8" fill="rgba(252,129,129,0.15)" stroke="#fc8181" stroke-width="1.5"/>
          <text x="140" y="98" text-anchor="middle" fill="#fed7d7" font-size="9" font-weight="700">ч. 4 ст. 159 — общий состав</text>
          <text x="140" y="112" text-anchor="middle" fill="#fc8181" font-size="7.5" font-weight="600">особо крупный размер ≥ 1 000 000 ₽</text>
          <!-- scale bar ch4 -->
          <rect x="40" y="122" width="200" height="12" rx="3" fill="rgba(0,0,0,0.3)"/>
          <rect x="40" y="122" width="200" height="12" rx="3" fill="#fc8181" opacity="0.7"/>
          <line x1="40" y1="118" x2="40" y2="138" stroke="#fff" stroke-width="1"/>
          <text x="40" y="148" text-anchor="middle" fill="#a0aec0" font-size="5.5">0</text>
          <line x1="140" y1="118" x2="140" y2="138" stroke="#ecc94b" stroke-width="1.5"/>
          <text x="140" y="148" text-anchor="middle" fill="#ecc94b" font-size="5.5">1 млн</text>
          <circle cx="195" cy="128" r="6" fill="#fff" stroke="#fc8181" stroke-width="2"/>
          <text x="195" y="160" text-anchor="middle" fill="#fed7d7" font-size="6.5" font-weight="600">2,16 млн = ОКР</text>
          <text x="140" y="174" text-anchor="middle" fill="#feb2b2" font-size="7">тяжкое · до 10 лет ЛС</text>
          <text x="140" y="184" text-anchor="middle" fill="#a0aec0" font-size="6">арест по общим правилам УПК</text>

          <!-- Ch5 scale -->
          <rect x="344" y="80" width="232" height="108" rx="8" fill="rgba(104,211,145,0.15)" stroke="#68d391" stroke-width="1.5"/>
          <text x="460" y="98" text-anchor="middle" fill="#c6f6d5" font-size="9" font-weight="700">ч. 5 ст. 159 — предпринимательское</text>
          <text x="460" y="112" text-anchor="middle" fill="#68d391" font-size="7.5" font-weight="600">значительный ущерб ≥ 250 000 ₽</text>
          <rect x="360" y="122" width="200" height="12" rx="3" fill="rgba(0,0,0,0.3)"/>
          <rect x="360" y="122" width="52" height="12" rx="3" fill="#68d391" opacity="0.7"/>
          <line x1="360" y1="118" x2="360" y2="138" stroke="#fff" stroke-width="1"/>
          <text x="360" y="148" text-anchor="middle" fill="#a0aec0" font-size="5.5">0</text>
          <line x1="412" y1="118" x2="412" y2="138" stroke="#ecc94b" stroke-width="1.5"/>
          <text x="412" y="148" text-anchor="middle" fill="#ecc94b" font-size="5.5">250 тыс</text>
          <circle cx="430" cy="128" r="6" fill="#fff" stroke="#68d391" stroke-width="2"/>
          <text x="430" y="160" text-anchor="middle" fill="#c6f6d5" font-size="6.5" font-weight="600">2,16 млн = значит.</text>
          <text x="460" y="174" text-anchor="middle" fill="#9ae6b4" font-size="7">средней тяжести · до 5 лет</text>
          <text x="460" y="184" text-anchor="middle" fill="#a0aec0" font-size="6">запрет ареста (ч. 1.1 ст. 108 УПК)</text>

          <!-- Requalification arrow -->
          <path d="M 140 192 L 300 218 L 460 192" stroke="url(#st159-flow)" stroke-width="2.5" fill="none" marker-end="url(#st159-arrow)"/>
          <rect x="200" y="222" width="200" height="36" rx="8" fill="rgba(99,179,237,0.18)" stroke="#63b3ed" stroke-width="1.5"/>
          <text x="300" y="238" text-anchor="middle" fill="#bee3f8" font-size="8" font-weight="700">ПЕРЕКВАЛИФИКАЦИЯ ч. 4 → ч. 5</text>
          <text x="300" y="250" text-anchor="middle" fill="#e2e8f0" font-size="6.5">ВС № 64-УД26-2-К9 · 25.02.2026</text>

          <!-- Sentence comparison -->
          <rect x="48" y="268" width="220" height="44" rx="8" fill="rgba(252,129,129,0.2)" stroke="#fc8181" stroke-width="1.5"/>
          <text x="158" y="286" text-anchor="middle" fill="#fed7d7" font-size="8" font-weight="700">ДО: ч. 4</text>
          <text x="158" y="300" text-anchor="middle" fill="#feb2b2" font-size="7">4 года ЛС условно · исп. срок 3 года</text>

          <rect x="332" y="268" width="220" height="44" rx="8" fill="rgba(104,211,145,0.18)" stroke="#68d391" stroke-width="1.5" stroke-dasharray="4 2"/>
          <text x="442" y="286" text-anchor="middle" fill="#c6f6d5" font-size="8" font-weight="700">ПОСЛЕ: ч. 5</text>
          <text x="442" y="300" text-anchor="middle" fill="#9ae6b4" font-size="7">2 года ЛС условно · исп. срок 2 года</text>

          <!-- KS bar -->
          <rect x="48" y="322" width="504" height="22" rx="5" fill="rgba(236,201,75,0.12)" stroke="rgba(236,201,75,0.45)" stroke-width="1"/>
          <text x="300" y="336" text-anchor="middle" fill="#ecc94b" font-size="7" font-weight="600">КС № 43-П/2026 · 29.06.2026 · госдоля в акционерах не блокирует ч. 5–7</text>
        </svg>

        <p class="l24-boris-st159-ch4-ch5-matrix__verdict"><strong>Ключ для защиты:</strong> при подряде с ПАО/АО с госучастием расчёт ущерба по <em>двум шкалам</em> — аргумент переквалификации, а не только смягчения наказания. Состав акционеров «не имеет значения» (ВС).</p>
        <p class="l24-boris-st159-ch4-ch5-matrix__caption">Схема по определению ВС № 64-УД26-2-К9 и постановлению КС № 43-П/2026</p>
      </div>

      <div class="l24-boris-st159-ch4-ch5-matrix__panel">
        <p class="l24-boris-st159-ch4-ch5-matrix__panel-title">Сравнительная сетка: состав, ущерб, санкции, процесс</p>

        <div class="l24-boris-st159-ch4-ch5-matrix__compare-head" aria-hidden="true">
          <span>Критерий</span>
          <span>ч. 4</span>
          <span>ч. 5</span>
        </div>

        <div class="l24-boris-st159-ch4-ch5-matrix__grid" role="table" aria-label="Таблица сравнения ч. 4 и ч. 5 ст. 159 УК РФ">
          <div class="l24-boris-st159-ch4-ch5-matrix__row l24-boris-st159-ch4-ch5-matrix__row--key" role="row">
            <span class="l24-boris-st159-ch4-ch5-matrix__row-label" role="rowheader">Квалифицирующий признак</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch4" role="cell">Организованная группа <em>или особо крупный размер</em></span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch5" role="cell"><em>Преднамеренное неисполнение</em> договорных обязательств в предпринимательской сфере + значительный ущерб</span>
          </div>
          <div class="l24-boris-st159-ch4-ch5-matrix__row" role="row">
            <span class="l24-boris-st159-ch4-ch5-matrix__row-label" role="rowheader">Порог ущерба</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch4" role="cell">Особо крупный: <em>≥ 1 000 000 ₽</em> (прим. к ст. 158)</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch5" role="cell">Значит.: <em>≥ 250 000 ₽</em>; крупный: &gt; 4,5 млн; ОКР: &gt; 18 млн (прим. к ст. 159)</span>
          </div>
          <div class="l24-boris-st159-ch4-ch5-matrix__row" role="row">
            <span class="l24-boris-st159-ch4-ch5-matrix__row-label" role="rowheader">Категория</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch4" role="cell"><em>Тяжкое</em> преступление</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch5" role="cell"><em>Средней тяжести</em></span>
          </div>
          <div class="l24-boris-st159-ch4-ch5-matrix__row" role="row">
            <span class="l24-boris-st159-ch4-ch5-matrix__row-label" role="rowheader">Макс. наказание</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch4" role="cell">До <em>10 лет</em> лишения свободы</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch5" role="cell">До <em>5 лет</em> ЛС (+ штраф, обязательные/исправительные работы)</span>
          </div>
          <div class="l24-boris-st159-ch4-ch5-matrix__row" role="row">
            <span class="l24-boris-st159-ch4-ch5-matrix__row-label" role="rowheader">Заключение под стражу</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch4" role="cell">По <em>общим правилам</em> УПК</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch5" role="cell"><em>Запрещено</em> по общему правилу (ч. 1.1 ст. 108 УПК), кроме исключений</span>
          </div>
          <div class="l24-boris-st159-ch4-ch5-matrix__row" role="row">
            <span class="l24-boris-st159-ch4-ch5-matrix__row-label" role="rowheader">Возбуждение дела</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch4" role="cell">По общим правилам УПК</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch5" role="cell">По заявлению потерпевшика-коммерсанта (ч. 3 ст. 20 УПК)</span>
          </div>
          <div class="l24-boris-st159-ch4-ch5-matrix__row" role="row">
            <span class="l24-boris-st159-ch4-ch5-matrix__row-label" role="rowheader">Стороны договора</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch4" role="cell">Не требуется</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch5" role="cell">Обе — ИП и/или <em>коммерческие организации</em> (прим. 2 к ст. 159)</span>
          </div>
          <div class="l24-boris-st159-ch4-ch5-matrix__row" role="row">
            <span class="l24-boris-st159-ch4-ch5-matrix__row-label" role="rowheader">Момент умысла</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch4" role="cell">До получения имущества (общая практика)</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch5" role="cell">Может возникнуть <em>до, при или в процессе</em> исполнения договора (ВС, п. 9 Пленума № 48)</span>
          </div>
          <div class="l24-boris-st159-ch4-ch5-matrix__row" role="row">
            <span class="l24-boris-st159-ch4-ch5-matrix__row-label" role="rowheader">Судебный штраф</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch4" role="cell">Ограниченно</span>
            <span class="l24-boris-st159-ch4-ch5-matrix__cell l24-boris-st159-ch4-ch5-matrix__cell--ch5" role="cell">ст. 76.2 УК РФ — при соблюдении условий</span>
          </div>
        </div>

        <div class="l24-boris-st159-ch4-ch5-matrix__case-bar" aria-label="Исход дела Шеврюкова">
          <div class="l24-boris-st159-ch4-ch5-matrix__case-card l24-boris-st159-ch4-ch5-matrix__case-card--before">
            <strong>Нижестоящие суды: ч. 4</strong>
            Отказ в ч. 5 из‑за госакционера ПАО «Сахалинэнерго» и момента умысла «в процессе договора».
          </div>
          <div class="l24-boris-st159-ch4-ch5-matrix__case-card l24-boris-st159-ch4-ch5-matrix__case-card--after">
            <strong>ВС + КС: ч. 5</strong>
            Обе стороны — коммерческие организации; ущерб по спец. шкале — значительный; практика фильтра по госдоле — неконституционна.
          </div>
        </div>
        <p class="l24-boris-st159-ch4-ch5-matrix__note"><em>Статистика 2024:</em> по ч. 4 осуждено 5 817 чел., по ч. 5 — 42. Следствие нередко квалифицирует договорные споры по ч. 4, обходя запрет ареста по ч. 5.</p>
      </div>
    </div>

    <div class="l24-boris-st159-ch4-ch5-matrix__foot" aria-label="Контекст практики КС и ВС 2026">
      <span class="l24-boris-st159-ch4-ch5-matrix__tag l24-boris-st159-ch4-ch5-matrix__tag--case">Шеврюков · 2 159 315,11 ₽</span>
      <span class="l24-boris-st159-ch4-ch5-matrix__tag l24-boris-st159-ch4-ch5-matrix__tag--art">ч. 4 vs ч. 5 ст. 159 УК</span>
      <span class="l24-boris-st159-ch4-ch5-matrix__tag l24-boris-st159-ch4-ch5-matrix__tag--def">КС 43-П/2026 · ВС 64-УД26-2-К9</span>
    </div>
  </div>
</section>
```

**Чеклист отличий от hero Алины**
- [x] Не полноэкранный блок; в теле статьи после H3 «Таблица сравнения: состав, ущерб, санкции, сроки»
- [x] Свой `id`: `l24-boris-st159-ch4-ch5-matrix` (не hero `#l24-hero-…`)
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Тёмная панель — контраст со светлым hero Алины (UG / мошенничество ст. 159, КС 2026)
- [x] Сплит «SVG ловушка порогов (2,16 млн ₽) | сравнительная сетка ч. 4 vs ч. 5 + исход дела Шеврюкова»
