=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** vs-kreditor-dobrosovestnost-neosnovatelnoe-obogaschenie-bankrotstvo-2026  
**Якорь:** `#l24-boris-kreditor-timeline-matrix`  
**Режим:** контраст к hero Алины — светлый hero → тёмный slate/teal блок-матрица таймлайна в теле статьи  
**Техника:** static SVG + inline CSS · без `<canvas>` · без `<script>`

## Место вставки для Наташи

Вставить **после закрывающего абзаца H2 §3** «Спор с кредитором в арбитраже: когда кредитор предъявляет иск параллельно банкротству» (после H3 §3.2 «Риски для кредитора при агрессивном взыскании в период банкротства») и **перед** `<h2>` §4 «Неосновательное обогащение за пользование недвижимостью».

Якорь для Наташи: после H2 §3, id `l24-boris-kreditor-timeline-matrix`

## Чеклист отличий от hero Алины

| | Hero Алины | Блок Бориса |
|---|---|---|
| Позиция | первый экран | тело статьи, после H2 §3 |
| Фон | светлый (#fefefe) | тёмный slate/teal gradient |
| Смысл | факты дела № А65-968/2025 | **таймлайн 4 дел** — цепочка ~94,4 млн ₽ |
| id | `l24-hero-vs-kreditor-dobrosovestnost` | `l24-boris-kreditor-timeline-matrix` |
| canvas/script | нет (MCP-only SVG) | нет |

```html
<section id="l24-boris-kreditor-timeline-matrix" class="l24-boris-kred-tl" aria-label="Таймлайн 4 связанных дел: цепочка требований Электрона к Возрождению — около 94,4 млн ₽">
<style>
.l24-boris-kred-tl {
  --bk-slate: #0f172a;
  --bk-slate-mid: #1e293b;
  --bk-slate-soft: #334155;
  --bk-teal: #14b8a6;
  --bk-teal-soft: #5eead4;
  --bk-teal-glow: rgba(20, 184, 166, 0.18);
  --bk-amber: #fbbf24;
  --bk-amber-soft: #fde68a;
  --bk-muted: #94a3b8;
  --bk-txt: #e2e8f0;
  margin: 48px 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-kred-tl__shell {
  background: linear-gradient(155deg, var(--bk-slate) 0%, #152238 42%, #0d3d38 100%);
  border: 1px solid rgba(20, 184, 166, 0.28);
  border-radius: 14px;
  padding: 32px 28px 24px;
  color: var(--bk-txt);
  box-shadow: 0 18px 48px rgba(15, 23, 42, 0.38);
}
.l24-boris-kred-tl__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--bk-teal-soft);
}
.l24-boris-kred-tl__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-kred-tl__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--bk-muted);
  max-width: 72ch;
}
.l24-boris-kred-tl__lead strong { color: #fff; }
.l24-boris-kred-tl__split {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.85fr);
  gap: 22px;
  align-items: stretch;
  margin-bottom: 20px;
}
.l24-boris-kred-tl__timeline-svg {
  display: block;
  width: 100%;
  height: auto;
}
.l24-boris-kred-tl__cards {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
}
.l24-boris-kred-tl__card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 12px 14px;
  border-left: 3px solid var(--bk-teal);
}
.l24-boris-kred-tl__card:nth-child(2) { border-left-color: #38bdf8; }
.l24-boris-kred-tl__card:nth-child(3) { border-left-color: var(--bk-amber); }
.l24-boris-kred-tl__card:nth-child(4) { border-left-color: #a78bfa; }
.l24-boris-kred-tl__card-case {
  display: block;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.04em;
  color: var(--bk-teal-soft);
  margin-bottom: 4px;
}
.l24-boris-kred-tl__card-sum {
  margin: 0 0 4px;
  font-size: 1rem;
  font-weight: 800;
  color: #fff;
  line-height: 1.2;
}
.l24-boris-kred-tl__card-sum--muted {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--bk-amber-soft);
}
.l24-boris-kred-tl__card-meta {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.4;
  color: #cbd5e1;
}
.l24-boris-kred-tl__total {
  margin: 0 0 16px;
  padding: 14px 16px;
  border-radius: 10px;
  background: rgba(20, 184, 166, 0.1);
  border: 1px solid rgba(20, 184, 166, 0.32);
  font-size: 0.84rem;
  line-height: 1.5;
  color: var(--bk-muted);
}
.l24-boris-kred-tl__total strong { color: var(--bk-teal-soft); }
.l24-boris-kred-tl__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-kred-tl__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  color: var(--bk-txt);
  border: 1px solid rgba(255, 255, 255, 0.13);
}
.l24-boris-kred-tl__tag--teal { border-color: rgba(20, 184, 166, 0.5); color: var(--bk-teal-soft); }
.l24-boris-kred-tl__tag--case { border-color: rgba(251, 191, 36, 0.45); color: var(--bk-amber-soft); }
.l24-boris-kred-tl__tag--law { border-color: rgba(56, 189, 248, 0.45); color: #bae6fd; }
@media (max-width: 860px) {
  .l24-boris-kred-tl__split { grid-template-columns: 1fr; }
  .l24-boris-kred-tl__shell { padding: 24px 18px 20px; }
}
</style>

<div class="l24-boris-kred-tl__shell">
  <p class="l24-boris-kred-tl__eyebrow">ARB · цепочка дел · ООО «Электрон» → ООО «Возрождение» · определение ВС 18.08.2026</p>
  <h3 class="l24-boris-kred-tl__title">4 дела — одна сага на ~94,4 млн ₽</h3>
  <p class="l24-boris-kred-tl__lead">Параллельный иск о неосновательном обогащении в деле № <strong>А65-968/2025</strong> — финальный этап цепочки из четырёх связанных производств. ВС отменил взыскание <strong>56,8 млн ₽</strong> и указал: преюдиция прошлых периодов не заменяет доказательства пользования в новом.</p>

  <div class="l24-boris-kred-tl__split">
    <svg class="l24-boris-kred-tl__timeline-svg" viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="bkTlT bkTlD">
      <title id="bkTlT">Таймлайн 4 дел: А65-30187 → А65-3718 → А40-30995 → А65-968</title>
      <desc id="bkTlD">Горизонтальная ось 2020–2026: четыре точки — взыскания НО 6,7 и 30,9 млн, банкротство Возрождения, иск 56,8 млн и отмена ВС</desc>
      <defs>
        <marker id="bkTl-arr" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
          <polygon points="0 0, 8 3.5, 0 7" fill="#14b8a6"/>
        </marker>
        <filter id="bkTl-glow" x="-30%" y="-30%" width="160%" height="160%">
          <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#000" flood-opacity="0.4"/>
        </filter>
        <linearGradient id="bkTl-line" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#14b8a6"/>
          <stop offset="50%" stop-color="#38bdf8"/>
          <stop offset="100%" stop-color="#a78bfa"/>
        </linearGradient>
      </defs>

      <!-- Фон -->
      <rect x="16" y="16" width="608" height="268" rx="12" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>

      <!-- Ось времени -->
      <line x1="56" y1="148" x2="584" y2="148" stroke="url(#bkTl-line)" stroke-width="3" stroke-linecap="round"/>
      <line x1="56" y1="148" x2="584" y2="148" stroke="rgba(20,184,166,0.25)" stroke-width="8" stroke-linecap="round"/>

      <!-- Годовые метки -->
      <text x="80" y="178" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600" font-family="system-ui,sans-serif">2020</text>
      <text x="200" y="178" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600" font-family="system-ui,sans-serif">2021</text>
      <text x="320" y="178" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600" font-family="system-ui,sans-serif">2022</text>
      <text x="440" y="178" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600" font-family="system-ui,sans-serif">2023</text>
      <text x="540" y="178" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600" font-family="system-ui,sans-serif">2024</text>
      <text x="600" y="178" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600" font-family="system-ui,sans-serif">2026</text>

      <!-- Точка 1: А65-30187 -->
      <circle cx="108" cy="148" r="14" fill="#0f172a" stroke="#14b8a6" stroke-width="2.5" filter="url(#bkTl-glow)"/>
      <circle cx="108" cy="148" r="5" fill="#14b8a6"/>
      <rect x="36" y="36" width="144" height="88" rx="8" fill="rgba(20,184,166,0.12)" stroke="#14b8a6" stroke-width="1.2"/>
      <text x="48" y="54" fill="#5eead4" font-size="7.5" font-weight="800" font-family="system-ui,sans-serif">① А65-30187/2021</text>
      <text x="48" y="70" fill="#fff" font-size="9" font-weight="800" font-family="system-ui,sans-serif">6,7 млн ₽</text>
      <text x="48" y="84" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">09.2020 — 09.2021</text>
      <text x="48" y="98" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">НО · договор незаключён</text>
      <text x="48" y="112" fill="#94a3b8" font-size="5.8" font-style="italic" font-family="system-ui,sans-serif">апелл. 22.02.2023</text>
      <line x1="108" y1="124" x2="108" y2="134" stroke="#14b8a6" stroke-width="1.2" stroke-dasharray="3,2"/>

      <!-- Точка 2: А65-3718 -->
      <circle cx="248" cy="148" r="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5" filter="url(#bkTl-glow)"/>
      <circle cx="248" cy="148" r="5" fill="#38bdf8"/>
      <rect x="176" y="196" width="144" height="76" rx="8" fill="rgba(56,189,248,0.1)" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="188" y="214" fill="#7dd3fc" font-size="7.5" font-weight="800" font-family="system-ui,sans-serif">② А65-3718/2023</text>
      <text x="188" y="230" fill="#fff" font-size="9" font-weight="800" font-family="system-ui,sans-serif">30,9 млн ₽</text>
      <text x="188" y="244" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">10.2021 — 11.2022</text>
      <text x="188" y="258" fill="#94a3b8" font-size="5.8" font-style="italic" font-family="system-ui,sans-serif">решение 20.11.2023</text>
      <line x1="248" y1="162" x2="248" y2="192" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="3,2"/>

      <!-- Точка 3: А40-30995 банкротство -->
      <circle cx="388" cy="148" r="14" fill="#0f172a" stroke="#fbbf24" stroke-width="2.5" filter="url(#bkTl-glow)"/>
      <circle cx="388" cy="148" r="5" fill="#fbbf24"/>
      <rect x="316" y="36" width="144" height="88" rx="8" fill="rgba(251,191,36,0.1)" stroke="#fbbf24" stroke-width="1.2"/>
      <text x="328" y="54" fill="#fde68a" font-size="7.5" font-weight="800" font-family="system-ui,sans-serif">③ А40-30995/2023</text>
      <text x="328" y="70" fill="#fff" font-size="8" font-weight="800" font-family="system-ui,sans-serif">Банкротство</text>
      <text x="328" y="84" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">возб. 20.02.2023</text>
      <text x="328" y="98" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">банкрот 05.12.2023</text>
      <text x="328" y="112" fill="#94a3b8" font-size="5.8" font-style="italic" font-family="system-ui,sans-serif">ООО «Возрождение»</text>
      <line x1="388" y1="124" x2="388" y2="134" stroke="#fbbf24" stroke-width="1.2" stroke-dasharray="3,2"/>

      <!-- Точка 4: А65-968 -->
      <circle cx="548" cy="148" r="16" fill="#1e293b" stroke="#a78bfa" stroke-width="3" filter="url(#bkTl-glow)"/>
      <circle cx="548" cy="148" r="6" fill="#a78bfa"/>
      <rect x="476" y="196" width="152" height="88" rx="8" fill="rgba(167,139,250,0.12)" stroke="#a78bfa" stroke-width="1.4"/>
      <text x="488" y="214" fill="#c4b5fd" font-size="7.5" font-weight="800" font-family="system-ui,sans-serif">④ А65-968/2025</text>
      <text x="488" y="230" fill="#fff" font-size="9" font-weight="800" font-family="system-ui,sans-serif">56,8 млн ₽</text>
      <text x="488" y="244" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">20.02.2023 — 17.07.2024</text>
      <text x="488" y="258" fill="#fca5a5" font-size="6" font-weight="700" font-family="system-ui,sans-serif">ВС 18.08.2026 — отмена</text>
      <text x="488" y="272" fill="#94a3b8" font-size="5.8" font-style="italic" font-family="system-ui,sans-serif">текущие платежи · НО</text>
      <line x1="548" y1="162" x2="548" y2="192" stroke="#a78bfa" stroke-width="1.2" stroke-dasharray="3,2"/>

      <!-- Стрелки связи -->
      <path d="M122 148 L234 148" fill="none" stroke="#14b8a6" stroke-width="1.2" marker-end="url(#bkTl-arr)" opacity="0.7"/>
      <path d="M262 148 L374 148" fill="none" stroke="#38bdf8" stroke-width="1.2" marker-end="url(#bkTl-arr)" opacity="0.7"/>
      <path d="M402 148 L532 148" fill="none" stroke="#fbbf24" stroke-width="1.2" marker-end="url(#bkTl-arr)" opacity="0.7"/>

      <!-- Итоговая сумма -->
      <rect x="200" y="268" width="240" height="0" fill="none"/>
      <text x="320" y="290" text-anchor="middle" fill="#5eead4" font-size="8" font-weight="800" font-family="system-ui,sans-serif" letter-spacing="0.04em">СОВОКУПНО: 6,7 + 30,9 + 56,8 ≈ 94,4 МЛН ₽</text>
    </svg>

    <div class="l24-boris-kred-tl__cards" role="list" aria-label="Карточки 4 дел цепочки">
      <div class="l24-boris-kred-tl__card" role="listitem">
        <span class="l24-boris-kred-tl__card-case">① А65-30187/2021</span>
        <p class="l24-boris-kred-tl__card-sum">6 730 540,96 ₽</p>
        <p class="l24-boris-kred-tl__card-meta">НО за 09.2020–09.2021 · договор аренды признан незаключённым (ст. 432 ГК) · апелляция 22.02.2023</p>
      </div>
      <div class="l24-boris-kred-tl__card" role="listitem">
        <span class="l24-boris-kred-tl__card-case">② А65-3718/2023</span>
        <p class="l24-boris-kred-tl__card-sum">30 882 637,39 ₽</p>
        <p class="l24-boris-kred-tl__card-meta">НО за 10.2021–11.2022 · решение АС РТ 20.11.2023 · акт возврата 11.11.2021 не оценён</p>
      </div>
      <div class="l24-boris-kred-tl__card" role="listitem">
        <span class="l24-boris-kred-tl__card-case">③ А40-30995/2023</span>
        <p class="l24-boris-kred-tl__card-sum l24-boris-kred-tl__card-sum--muted">Банкротство «Возрождение»</p>
        <p class="l24-boris-kred-tl__card-meta">Возбуждение 20.02.2023 · признание банкротом 05.12.2023 · граница текущих vs реестровых платежей</p>
      </div>
      <div class="l24-boris-kred-tl__card" role="listitem">
        <span class="l24-boris-kred-tl__card-case">④ А65-968/2025</span>
        <p class="l24-boris-kred-tl__card-sum">56 829 324,48 ₽</p>
        <p class="l24-boris-kred-tl__card-meta">Текущие платежи · период 20.02.2023–17.07.2024 · ВС 18.08.2026 отменил акты → новое рассмотрение</p>
      </div>
    </div>
  </div>

  <p class="l24-boris-kred-tl__total"><strong>Ключевой вывод ВС:</strong> преюдиция дел № А65-30187/2021 и А65-3718/2023 не заменяет доказательства фактического пользования в спорный период. На кредитора «Электрон», знающего о банкротстве, возложен <strong>повышенный стандарт доказывания</strong> и оценка добросовестности (ст. 10 ГК).</p>

  <div class="l24-boris-kred-tl__foot">
    <span class="l24-boris-kred-tl__tag l24-boris-kred-tl__tag--case">№ 306-ЭС26-695</span>
    <span class="l24-boris-kred-tl__tag l24-boris-kred-tl__tag--teal">~94,4 млн ₽</span>
    <span class="l24-boris-kred-tl__tag l24-boris-kred-tl__tag--law">ст. 1102 ГК · ст. 10 ГК</span>
    <span class="l24-boris-kred-tl__tag">13 объектов · Казань</span>
    <span class="l24-boris-kred-tl__tag">текущие платежи</span>
  </div>
</div>
</section>
```
