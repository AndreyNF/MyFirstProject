=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** `vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026`  
**Якорь:** `l24-boris-vs73-matrix`  
**Размещение:** сразу после H3 «Роль ст. 88 УПК: оценка всей совокупности доказательств» (внутри H2 «Статья 73 УК РФ — когда суд обязан назначить условный срок»), перед H2 «Как защита добивается условного наказания за ДТП» — якорь для Natasha.  
**Режим:** тёмная панель в теле статьи (контраст со светлым hero Алины) — **матрица смягчающих обстоятельств + механизм ст. 73 УК + чеклист защиты по ДТП** по определению ВС № 41-УД26-25-К4 (июнь 2026).  
**Legis24 MCP-only:** static SVG + inline CSS, без `<canvas>` и `<script>`.

```html
<section id="l24-boris-vs73-matrix" class="l24-boris-vs73-matrix" aria-label="Смягчающие обстоятельства, ст. 73 УК РФ и чеклист защиты по уголовному делу о ДТП — определение ВС № 41-УД26-25-К4">
<style>
.l24-boris-vs73-matrix {
  --vs73-navy: #0f1c2e;
  --vs73-navy-soft: #1a3050;
  --vs73-smag: #68d391;
  --vs73-cond: #63b3ed;
  --vs73-real: #fc8181;
  --vs73-gold: #ecc94b;
  --vs73-violet: #b794f4;
  --vs73-ink: #e2e8f0;
  --vs73-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-vs73-matrix__shell {
  background: linear-gradient(155deg, var(--vs73-navy) 0%, #152a45 50%, var(--vs73-navy-soft) 100%);
  border: 1px solid rgba(99, 179, 237, 0.28);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: 0 18px 48px rgba(15, 28, 46, 0.34);
  color: var(--vs73-ink);
}
.l24-boris-vs73-matrix__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--vs73-gold);
}
.l24-boris-vs73-matrix__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-vs73-matrix__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--vs73-muted);
  max-width: 72ch;
}
.l24-boris-vs73-matrix__lead strong { color: #fff; }
.l24-boris-vs73-matrix__split {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-vs73-matrix__panel {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-vs73-matrix__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--vs73-gold);
}
.l24-boris-vs73-matrix__scheme-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 340px;
  margin-bottom: 12px;
}
.l24-boris-vs73-matrix__smag-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 6px;
  margin: 0 0 12px;
  padding: 0;
  list-style: none;
}
.l24-boris-vs73-matrix__smag-item {
  margin: 0;
  padding: 8px 7px;
  background: rgba(0, 0, 0, 0.22);
  border-radius: 6px;
  border-top: 2px solid var(--vs73-smag);
  font-size: 0.68rem;
  line-height: 1.35;
  color: var(--vs73-muted);
}
.l24-boris-vs73-matrix__smag-item strong {
  display: block;
  color: #c6f6d5;
  font-size: 0.7rem;
  margin-bottom: 2px;
}
.l24-boris-vs73-matrix__smag-item:nth-child(4),
.l24-boris-vs73-matrix__smag-item:nth-child(5),
.l24-boris-vs73-matrix__smag-item:nth-child(6) { border-top-color: var(--vs73-cond); }
.l24-boris-vs73-matrix__smag-item:nth-child(7),
.l24-boris-vs73-matrix__smag-item:nth-child(8),
.l24-boris-vs73-matrix__smag-item:nth-child(9) { border-top-color: var(--vs73-violet); }
.l24-boris-vs73-matrix__smag-item:nth-child(10),
.l24-boris-vs73-matrix__smag-item:nth-child(11) {
  grid-column: span 1;
  border-top-color: var(--vs73-gold);
}
.l24-boris-vs73-matrix__verdict {
  margin: 0;
  padding: 12px 14px;
  border-radius: 8px;
  background: rgba(236, 201, 75, 0.12);
  border: 1px solid rgba(236, 201, 75, 0.38);
  font-size: 0.78rem;
  line-height: 1.45;
  color: var(--vs73-ink);
}
.l24-boris-vs73-matrix__verdict strong { color: var(--vs73-gold); }
.l24-boris-vs73-matrix__caption {
  margin: 10px 0 0;
  font-size: 0.7rem;
  line-height: 1.4;
  color: rgba(160, 174, 192, 0.88);
  text-align: center;
}
.l24-boris-vs73-matrix__vs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 0 0 12px;
}
.l24-boris-vs73-matrix__vs-card {
  padding: 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.72rem;
  line-height: 1.4;
}
.l24-boris-vs73-matrix__vs-card--court { border-color: rgba(252, 129, 129, 0.45); }
.l24-boris-vs73-matrix__vs-card--def { border-color: rgba(104, 211, 145, 0.45); }
.l24-boris-vs73-matrix__vs-card strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-vs73-matrix__matrix {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 0 0 12px;
}
.l24-boris-vs73-matrix__row {
  display: grid;
  grid-template-columns: minmax(0, 0.85fr) minmax(0, 0.55fr) minmax(0, 1.2fr);
  gap: 8px 10px;
  align-items: start;
  padding: 10px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.74rem;
  line-height: 1.38;
}
.l24-boris-vs73-matrix__row--follow { border-left: 3px solid var(--vs73-cond); }
.l24-boris-vs73-matrix__row--court { border-left: 3px solid var(--vs73-real); }
.l24-boris-vs73-matrix__row--cass { border-left: 3px solid var(--vs73-gold); }
.l24-boris-vs73-matrix__row--norm { border-left: 3px solid var(--vs73-violet); }
.l24-boris-vs73-matrix__row-label {
  font-weight: 700;
  color: #fff;
  font-size: 0.78rem;
}
.l24-boris-vs73-matrix__row-stage {
  font-weight: 700;
  font-size: 0.68rem;
  padding: 3px 7px;
  border-radius: 4px;
  text-align: center;
  align-self: start;
  background: rgba(99, 179, 237, 0.2);
  color: #bee3f8;
  border: 1px solid rgba(99, 179, 237, 0.45);
}
.l24-boris-vs73-matrix__row-stage--court {
  background: rgba(252, 129, 129, 0.2);
  color: #fed7d7;
  border-color: rgba(252, 129, 129, 0.45);
}
.l24-boris-vs73-matrix__row-stage--cass {
  background: rgba(236, 201, 75, 0.2);
  color: #faf089;
  border-color: rgba(236, 201, 75, 0.45);
}
.l24-boris-vs73-matrix__row-text { color: var(--vs73-muted); }
.l24-boris-vs73-matrix__row-text em {
  font-style: normal;
  color: #fff;
  font-weight: 600;
}
.l24-boris-vs73-matrix__fork {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 0 0 10px;
}
.l24-boris-vs73-matrix__fork-card {
  padding: 10px;
  border-radius: 8px;
  font-size: 0.72rem;
  line-height: 1.4;
}
.l24-boris-vs73-matrix__fork-card--real {
  background: rgba(252, 129, 129, 0.14);
  border: 1px solid rgba(252, 129, 129, 0.4);
}
.l24-boris-vs73-matrix__fork-card--cond {
  background: rgba(99, 179, 237, 0.14);
  border: 1px solid rgba(99, 179, 237, 0.4);
}
.l24-boris-vs73-matrix__fork-card strong {
  display: block;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-vs73-matrix__fork-card--real strong { color: #fed7d7; }
.l24-boris-vs73-matrix__fork-card--cond strong { color: #bee3f8; }
.l24-boris-vs73-matrix__note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--vs73-muted);
}
.l24-boris-vs73-matrix__note em {
  font-style: normal;
  color: #bee3f8;
  font-weight: 600;
}
.l24-boris-vs73-matrix__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-vs73-matrix__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--vs73-ink);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.l24-boris-vs73-matrix__tag--case {
  border-color: rgba(236, 201, 75, 0.5);
  color: var(--vs73-gold);
}
.l24-boris-vs73-matrix__tag--art { border-color: rgba(99, 179, 237, 0.45); color: #bee3f8; }
.l24-boris-vs73-matrix__tag--def { border-color: rgba(104, 211, 145, 0.45); color: #c6f6d5; }
@media (max-width: 900px) {
  .l24-boris-vs73-matrix__split { grid-template-columns: 1fr; }
  .l24-boris-vs73-matrix__smag-grid { grid-template-columns: 1fr 1fr; }
  .l24-boris-vs73-matrix__row { grid-template-columns: 1fr; gap: 4px; }
  .l24-boris-vs73-matrix__row-stage { justify-self: start; }
  .l24-boris-vs73-matrix__vs { grid-template-columns: 1fr; }
  .l24-boris-vs73-matrix__fork { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-vs73-matrix__shell">
    <p class="l24-boris-vs73-matrix__eyebrow">ст. 73 УК · ст. 88 УПК · ч. 3 ст. 264 УК · определение № 41-УД26-25-К4 · 05.06.2026</p>
    <h3 class="l24-boris-vs73-matrix__title">Смягчающие обстоятельства → ст. 73 УК: матрица и чеклист защиты по ДТП</h3>
    <p class="l24-boris-vs73-matrix__lead">В деле студентки ВС заменил <strong>2 года реального</strong> срока условными и освободил из колонии: <strong>11 смягчающих</strong>, <strong>0 отягчающих</strong>, но ключ — суд первой инстанции <strong>не мотивировал отказ</strong> от ст. 73 УК. Защита по уголовному делу о ДТП строится на документировании смягчающих, требовании мотивировки и кассации при её отсутствии.</p>

    <div class="l24-boris-vs73-matrix__split">
      <div class="l24-boris-vs73-matrix__panel">
        <p class="l24-boris-vs73-matrix__panel-title">Схема: совокупность смягчающих → ст. 73 УК → немотивированный отказ → ВС</p>
        <svg class="l24-boris-vs73-matrix__scheme-svg" viewBox="0 0 600 330" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="vs73-scheme-title vs73-scheme-desc">
          <title id="vs73-scheme-title">Механизм условного осуждения по ст. 73 УК РФ при ДТП с погибшим</title>
          <desc id="vs73-scheme-desc">Смягчающие обстоятельства формируют основание для ст. 73 УК; при немотивированном отказе суда ВС заменяет реальный срок условным по делу № 41-УД26-25-К4</desc>
          <defs>
            <linearGradient id="vs73-flow" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#68d391"/>
              <stop offset="50%" stop-color="#63b3ed"/>
              <stop offset="100%" stop-color="#ecc94b"/>
            </linearGradient>
            <marker id="vs73-arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0,0 L8,4 L0,8 Z" fill="#ecc94b"/>
            </marker>
          </defs>

          <text x="300" y="16" text-anchor="middle" fill="#ecc94b" font-size="8" font-weight="600">ч. 3 ст. 264 УК · ДТП с погибшим · срок до 5 лет → лимит ст. 73 УК (до 8 лет)</text>

          <!-- Smagchayushchie stack -->
          <rect x="24" y="28" width="552" height="72" rx="8" fill="rgba(104,211,145,0.12)" stroke="#68d391" stroke-width="1.5"/>
          <text x="300" y="44" text-anchor="middle" fill="#c6f6d5" font-size="8.5" font-weight="700">11 СМЯГЧАЮЩИХ · 0 ОТЯГЧАЮЩИХ (дело № 41-УД26-25-К4)</text>
          <rect x="36" y="52" width="78" height="18" rx="3" fill="rgba(104,211,145,0.25)" stroke="#68d391" stroke-width="0.8"/>
          <text x="75" y="64" text-anchor="middle" fill="#e2e8f0" font-size="6">признание вины</text>
          <rect x="120" y="52" width="78" height="18" rx="3" fill="rgba(104,211,145,0.25)" stroke="#68d391" stroke-width="0.8"/>
          <text x="159" y="64" text-anchor="middle" fill="#e2e8f0" font-size="6">возмещение вреда</text>
          <rect x="204" y="52" width="78" height="18" rx="3" fill="rgba(104,211,145,0.25)" stroke="#68d391" stroke-width="0.8"/>
          <text x="243" y="64" text-anchor="middle" fill="#e2e8f0" font-size="6">волонтёрство</text>
          <rect x="288" y="52" width="78" height="18" rx="3" fill="rgba(104,211,145,0.25)" stroke="#68d391" stroke-width="0.8"/>
          <text x="327" y="64" text-anchor="middle" fill="#e2e8f0" font-size="6">мать-инвалид</text>
          <rect x="372" y="52" width="78" height="18" rx="3" fill="rgba(104,211,145,0.25)" stroke="#68d391" stroke-width="0.8"/>
          <text x="411" y="64" text-anchor="middle" fill="#e2e8f0" font-size="6">отчим — СВО</text>
          <rect x="456" y="52" width="78" height="18" rx="3" fill="rgba(104,211,145,0.25)" stroke="#68d391" stroke-width="0.8"/>
          <text x="495" y="64" text-anchor="middle" fill="#e2e8f0" font-size="6">потерпевшие</text>
          <text x="300" y="88" text-anchor="middle" fill="#a0aec0" font-size="6.5">+ травмы в ДТП · посткриминальное поведение · отсутствие судимостей · ст. 88 УПК — оценка в совокупности</text>

          <!-- Arrow down -->
          <path d="M 300 100 L 300 118" stroke="#68d391" stroke-width="2" fill="none" marker-end="url(#vs73-arrow)"/>

          <!-- St 73 UK gate -->
          <rect x="180" y="120" width="240" height="44" rx="8" fill="rgba(99,179,237,0.22)" stroke="#63b3ed" stroke-width="1.5"/>
          <text x="300" y="136" text-anchor="middle" fill="#bee3f8" font-size="9" font-weight="700">ст. 73 УК РФ</text>
          <text x="300" y="150" text-anchor="middle" fill="#e2e8f0" font-size="7">исправление без реального отбывания · испытательный срок</text>
          <text x="300" y="160" text-anchor="middle" fill="#a0aec0" font-size="6.5">Пленум ВС № 58: отказ = конкретные данные о личности</text>

          <!-- Fork arrows -->
          <path d="M 240 164 L 140 188" stroke="#fc8181" stroke-width="2" fill="none" marker-end="url(#vs73-arrow)"/>
          <path d="M 360 164 L 460 188" stroke="#63b3ed" stroke-width="2" fill="none" marker-end="url(#vs73-arrow)"/>

          <!-- Real srok (lower court error) -->
          <rect x="48" y="190" width="184" height="56" rx="8" fill="rgba(252,129,129,0.22)" stroke="#fc8181" stroke-width="1.5"/>
          <text x="140" y="208" text-anchor="middle" fill="#fed7d7" font-size="8" font-weight="700">СУД 1-й / АП / КАС</text>
          <text x="140" y="222" text-anchor="middle" fill="#feb2b2" font-size="7">2 года РЕАЛЬНО</text>
          <text x="140" y="234" text-anchor="middle" fill="#a0aec0" font-size="6.5">отказ от ст. 73 без мотивировки</text>
          <text x="140" y="244" text-anchor="middle" fill="#fc8181" font-size="6.5" font-weight="600">«тяжесть содеянного» — клише</text>

          <!-- Conditional (VS) -->
          <rect x="368" y="190" width="184" height="56" rx="8" fill="rgba(99,179,237,0.18)" stroke="#63b3ed" stroke-width="1.5" stroke-dasharray="4 2"/>
          <text x="460" y="208" text-anchor="middle" fill="#bee3f8" font-size="8" font-weight="700">ДОЛЖНО БЫТЬ</text>
          <text x="460" y="222" text-anchor="middle" fill="#90cdf4" font-size="7">2 года УСЛОВНО</text>
          <text x="460" y="234" text-anchor="middle" fill="#a0aec0" font-size="6.5">испытательный срок 2 года</text>
          <text x="460" y="244" text-anchor="middle" fill="#63b3ed" font-size="6.5">+ освобождение из колонии</text>

          <!-- VS correction bar -->
          <rect x="48" y="258" width="504" height="32" rx="8" fill="rgba(236,201,75,0.15)" stroke="url(#vs73-flow)" stroke-width="1.5"/>
          <text x="300" y="272" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="700">ВС РФ № 41-УД26-25-К4 · 05.06.2026 · замена реального срока условным + освобождение</text>
          <text x="300" y="284" text-anchor="middle" fill="#ecc94b" font-size="7">«суд должным образом не мотивировал… почему не находит оснований для ст. 73 УК»</text>

          <!-- Process route -->
          <rect x="48" y="300" width="504" height="22" rx="5" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
          <rect x="56" y="306" width="100" height="10" rx="2" fill="rgba(104,211,145,0.35)"/>
          <rect x="164" y="306" width="88" height="10" rx="2" fill="rgba(99,179,237,0.35)"/>
          <rect x="260" y="306" width="88" height="10" rx="2" fill="rgba(252,129,129,0.35)"/>
          <rect x="356" y="306" width="188" height="10" rx="2" fill="rgba(236,201,75,0.35)"/>
          <text x="106" y="314" text-anchor="middle" fill="#c6f6d5" font-size="5.5">следствие</text>
          <text x="208" y="314" text-anchor="middle" fill="#bee3f8" font-size="5.5">суд 1 инст.</text>
          <text x="304" y="314" text-anchor="middle" fill="#fed7d7" font-size="5.5">апелл./касс.</text>
          <text x="450" y="314" text-anchor="middle" fill="#faf089" font-size="5.5">ВС · кассация по ст. 73 + ст. 88 УПК</text>
        </svg>

        <ul class="l24-boris-vs73-matrix__smag-grid" aria-label="Смягчающие обстоятельства из определения ВС № 41-УД26-25-К4">
          <li class="l24-boris-vs73-matrix__smag-item"><strong>Признание вины</strong>Полное, с раскаянием (п. «и» ч. 1 ст. 61 УК)</li>
          <li class="l24-boris-vs73-matrix__smag-item"><strong>Возмещение вреда</strong>Моральный и материальный ущерб — добровольно, с документами</li>
          <li class="l24-boris-vs73-matrix__smag-item"><strong>Волонтёрство</strong>Благотворительность, пожертвования СВО и храмам</li>
          <li class="l24-boris-vs73-matrix__smag-item"><strong>Характеристики</strong>Учёба, работа, грамоты и благодарности</li>
          <li class="l24-boris-vs73-matrix__smag-item"><strong>Мать-инвалид II</strong>Совместное проживание — уход под угрозой при реальном сроке</li>
          <li class="l24-boris-vs73-matrix__smag-item"><strong>Отчим — СВО</strong>Участник с 2022 г.; перевёл деньги потерпевшим</li>
          <li class="l24-boris-vs73-matrix__smag-item"><strong>Травмы в ДТП</strong>Реабилитация, ортопедический режим vs условия колонии</li>
          <li class="l24-boris-vs73-matrix__smag-item"><strong>Посткриминальное</strong>Не замечена в предосудительном с момента ДТП</li>
          <li class="l24-boris-vs73-matrix__smag-item"><strong>Потерпевшие</strong>Просили прекращение или наказание без лишения свободы</li>
          <li class="l24-boris-vs73-matrix__smag-item"><strong>Без судимостей</strong>Не на учёте у нарколога и психиатра</li>
          <li class="l24-boris-vs73-matrix__smag-item"><strong>0 отягчающих</strong>Суд не установил ни одного отягчающего обстоятельства</li>
        </ul>
        <p class="l24-boris-vs73-matrix__verdict"><strong>Инструмент кассации:</strong> немотивированный отказ от ст. 73 УК при совокупности смягчающих — самостоятельное основание жалобы; апелляция не вправе «подтвердить» приговор без новых доводов.</p>
        <p class="l24-boris-vs73-matrix__caption">Схема по определению СК по уголовным делам ВС РФ № 41-УД26-25-К4 · РАПСИ 05.06.2026</p>
      </div>

      <div class="l24-boris-vs73-matrix__panel">
        <p class="l24-boris-vs73-matrix__panel-title">Чеклист защиты по ДТП: следствие → суд → кассация</p>
        <div class="l24-boris-vs73-matrix__vs">
          <div class="l24-boris-vs73-matrix__vs-card l24-boris-vs73-matrix__vs-card--court">
            <strong>Ошибка суда</strong>
            «Тяжесть преступления», «исправление в изоляции» без анализа личности; игнорирование позиции потерпевших; перечисление смягчающих без вывода по ст. 73.
          </div>
          <div class="l24-boris-vs73-matrix__vs-card l24-boris-vs73-matrix__vs-card--def">
            <strong>Задача защиты</strong>
            Документировать смягчающие с первого допроса; требовать мотивировку в прениях; при отказе — кассация с ссылкой на ст. 88 УПК и Пленум ВС № 58.
          </div>
        </div>
        <div class="l24-boris-vs73-matrix__matrix">
          <div class="l24-boris-vs73-matrix__row l24-boris-vs73-matrix__row--follow">
            <span class="l24-boris-vs73-matrix__row-label">Признание вины</span>
            <span class="l24-boris-vs73-matrix__row-stage">Следствие</span>
            <span class="l24-boris-vs73-matrix__row-text">Только с адвокатом на допросах; не давать показания против себя по отягчающим. Зафиксировать <em>полное признание</em> как смягчающее (ст. 61 УК).</span>
          </div>
          <div class="l24-boris-vs73-matrix__row l24-boris-vs73-matrix__row--follow">
            <span class="l24-boris-vs73-matrix__row-label">Возмещение вреда</span>
            <span class="l24-boris-vs73-matrix__row-stage">Следствие</span>
            <span class="l24-boris-vs73-matrix__row-text">Расписки, платёжки, нотариальные соглашения — <em>добровольный</em> характер выплат. В деле № 41-УД26-25-К4 перевод через отчима-участника СВО.</span>
          </div>
          <div class="l24-boris-vs73-matrix__row l24-boris-vs73-matrix__row--follow">
            <span class="l24-boris-vs73-matrix__row-label">Потерпевшие</span>
            <span class="l24-boris-vs73-matrix__row-stage">Следствие</span>
            <span class="l24-boris-vs73-matrix__row-text">Письменное заявление о примирении или просьба не лишать свободы. Суд обязан учесть или <em>мотивировать игнорирование</em> (ст. 43 УК).</span>
          </div>
          <div class="l24-boris-vs73-matrix__row l24-boris-vs73-matrix__row--court">
            <span class="l24-boris-vs73-matrix__row-label">Ходатайство ст. 73</span>
            <span class="l24-boris-vs73-matrix__row-stage l24-boris-vs73-matrix__row-stage--court">Суд 1 инст.</span>
            <span class="l24-boris-vs73-matrix__row-text">В прениях — прямой вопрос: «Почему <em>именно этот человек</em> не может быть исправлен без изоляции?» Создаёт процессуальную обязанность ответа в приговоре.</span>
          </div>
          <div class="l24-boris-vs73-matrix__row l24-boris-vs73-matrix__row--norm">
            <span class="l24-boris-vs73-matrix__row-label">ст. 88 УПК</span>
            <span class="l24-boris-vs73-matrix__row-stage l24-boris-vs73-matrix__row-stage--court">Суд 1 инст.</span>
            <span class="l24-boris-vs73-matrix__row-text">Требовать <em>совокупную оценку</em> личности: поведение после ДТП, здоровье, семья, смягчающие — не вырывать «гибель человека» из контекста 11 факторов.</span>
          </div>
          <div class="l24-boris-vs73-matrix__row l24-boris-vs73-matrix__row--cass">
            <span class="l24-boris-vs73-matrix__row-label">Кассация в ВС</span>
            <span class="l24-boris-vs73-matrix__row-stage l24-boris-vs73-matrix__row-stage--cass">Кассация</span>
            <span class="l24-boris-vs73-matrix__row-text">Нет развёрнутой мотивировки отказа от ст. 73 — <em>процессуальная ошибка</em>. Указать нарушенные нормы, материалы дела, позиции апелляции без новых доводов.</span>
          </div>
        </div>
        <div class="l24-boris-vs73-matrix__fork" aria-label="Исход по ст. 73 УК РФ">
          <div class="l24-boris-vs73-matrix__fork-card l24-boris-vs73-matrix__fork-card--real">
            <strong>Реальный срок (ошибка)</strong>
            Клише о тяжести деяния; формальный перечень смягчающих; игнор потерпевших — основание для кассации по № 41-УД26-25-К4.
          </div>
          <div class="l24-boris-vs73-matrix__fork-card l24-boris-vs73-matrix__fork-card--cond">
            <strong>Условный срок (цель)</strong>
            Испытательный срок + контроль; лишение права управления — реально. ВС: исправление возможно без изоляции при данной совокупности.
          </div>
        </div>
        <p class="l24-boris-vs73-matrix__note"><em>Граница гуманизации:</em> опьянение (ч. 4–6 ст. 264), бегство с места ДТП, рецидив — условный срок маловероятен. При неосторожном ДТП без отягчающих фокус — доказательная база смягчающих и мотивировка суда.</p>
      </div>
    </div>

    <div class="l24-boris-vs73-matrix__foot" aria-label="Контекст практики ВС 2026">
      <span class="l24-boris-vs73-matrix__tag l24-boris-vs73-matrix__tag--case">№ 41-УД26-25-К4 · 05.06.2026</span>
      <span class="l24-boris-vs73-matrix__tag l24-boris-vs73-matrix__tag--art">ст. 73 УК · ст. 88 УПК · ч. 3 ст. 264 УК</span>
      <span class="l24-boris-vs73-matrix__tag l24-boris-vs73-matrix__tag--def">Защита: 11 смягчающих + требование мотивировки</span>
    </div>
  </div>
</section>
```

**Чеклист отличий от hero Алины**
- [x] Не полноэкранный блок; в теле статьи после H3 «Роль ст. 88 УПК…» (внутри H2 «Статья 73 УК РФ»)
- [x] Свой `id`: `l24-boris-vs73-matrix` (не hero `#l24-hero-…`)
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Тёмная панель — контраст со светлым hero Алины (UG / условное наказание за ДТП)
- [x] Сплит «схема смягчающих → ст. 73 УК → ВС | чеклист защиты по ДТП (следствие → суд → кассация)»
