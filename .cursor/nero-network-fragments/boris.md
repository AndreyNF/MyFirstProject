=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** vs-kassaciya-zapret-obvinitelnyh-prognozov-zashchita-2026  
**Якорь:** `#l24-boris-kassaciya-prognoz-matrix`  
**Режим:** контраст к hero Алины — светлый hero с SVG «цепочкой инстанций» → тёмный редакционный блок-матрица чек-листа в теле статьи  
**Техника:** static SVG + inline CSS · без `<canvas>` · без `<script>`

## Место вставки для Наташи

Вставить **после закрывающего абзаца H3 §3.1** («Дело № 53 — иллюстрация второго сценария: кассация вышла за рамки проверки законности.») и **перед** `<h3 id="l24-h3-3-2">Апелляция и кассация: различие для стратегии защиты</h3>` внутри секции `<h2 id="l24-h2-3">`.

Точный маркер в лонгриде Жени: строка с текстом «Дело № 53 — иллюстрация второго сценария» → **сюда блок Бориса** → далее H3 §3.2 и таблица апелляция/кассация.

## Чеклист отличий от hero Алины

| | Hero Алины | Блок Бориса |
|---|---|---|
| Позиция | первый экран | тело статьи, после H2 §3 / H3 §3.1 |
| Фон | светлый (#fefefe) | тёмный navy gradient |
| Смысл | цепочка инстанций дела № 53 | **4 признака** обвинительного прогноза (чек-лист Артёма) |
| id | `l24-hero-vs-kassaciya-zapret` | `l24-boris-kassaciya-prognoz-matrix` |
| canvas/script | нет (MCP-only SVG) | нет |

```html
<section id="l24-boris-kassaciya-prognoz-matrix" class="l24-boris-kass-prog" aria-label="4 признака обвинительного прогноза кассации — чек-лист для жалобы в ВС РФ">
<style>
.l24-boris-kass-prog {
  --bk-navy: #0f2744;
  --bk-navy-soft: #1a365d;
  --bk-gold: #ecc94b;
  --bk-gold-soft: #fde68a;
  --bk-red: #f87171;
  --bk-red-soft: #fecaca;
  --bk-red-bg: rgba(248, 113, 113, 0.12);
  --bk-blue: #818cf8;
  --bk-ok: #34d399;
  --bk-muted: #a0aec0;
  --bk-txt: #e2e8f0;
  margin: 48px 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-kass-prog__shell {
  background: linear-gradient(152deg, var(--bk-navy) 0%, #122a42 48%, var(--bk-navy-soft) 100%);
  border: 1px solid rgba(236, 201, 75, 0.24);
  border-radius: 14px;
  padding: 32px 28px 24px;
  color: var(--bk-txt);
  box-shadow: 0 18px 48px rgba(15, 39, 68, 0.32);
}
.l24-boris-kass-prog__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--bk-gold);
}
.l24-boris-kass-prog__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-kass-prog__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--bk-muted);
  max-width: 72ch;
}
.l24-boris-kass-prog__lead strong { color: #fff; }
.l24-boris-kass-prog__split {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr);
  gap: 22px;
  align-items: stretch;
  margin-bottom: 20px;
}
.l24-boris-kass-prog__matrix-svg {
  display: block;
  width: 100%;
  height: auto;
}
.l24-boris-kass-prog__cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}
.l24-boris-kass-prog__card {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 14px 12px;
  border-top: 3px solid var(--bk-red);
}
.l24-boris-kass-prog__card:nth-child(2) { border-top-color: #fb923c; }
.l24-boris-kass-prog__card:nth-child(3) { border-top-color: var(--bk-gold); }
.l24-boris-kass-prog__card:nth-child(4) { border-top-color: var(--bk-blue); }
.l24-boris-kass-prog__card-n {
  display: block;
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  color: var(--bk-gold);
  margin-bottom: 6px;
}
.l24-boris-kass-prog__card-t {
  margin: 0;
  font-size: 0.78rem;
  line-height: 1.4;
  color: #cbd5e1;
  font-weight: 600;
}
.l24-boris-kass-prog__card-t em {
  font-style: normal;
  color: var(--bk-red-soft);
}
.l24-boris-kass-prog__verdict {
  margin: 0 0 16px;
  padding: 14px 16px;
  border-radius: 10px;
  background: rgba(236, 201, 75, 0.1);
  border: 1px solid rgba(236, 201, 75, 0.32);
  font-size: 0.84rem;
  line-height: 1.5;
  color: var(--bk-muted);
}
.l24-boris-kass-prog__verdict strong { color: var(--bk-gold-soft); }
.l24-boris-kass-prog__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-kass-prog__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  color: var(--bk-txt);
  border: 1px solid rgba(255, 255, 255, 0.13);
}
.l24-boris-kass-prog__tag--case { border-color: rgba(236, 201, 75, 0.5); color: var(--bk-gold); }
.l24-boris-kass-prog__tag--law { border-color: rgba(129, 140, 248, 0.45); color: #c7d2fe; }
.l24-boris-kass-prog__tag--warn { border-color: rgba(248, 113, 113, 0.45); color: var(--bk-red-soft); }
@media (max-width: 860px) {
  .l24-boris-kass-prog__split { grid-template-columns: 1fr; }
  .l24-boris-kass-prog__shell { padding: 24px 18px 20px; }
}
@media (max-width: 480px) {
  .l24-boris-kass-prog__cards { grid-template-columns: 1fr; }
}
</style>

<div class="l24-boris-kass-prog__shell">
  <p class="l24-boris-kass-prog__eyebrow">UG · чек-лист защиты · дело № 53-УД26-9-К8 · дайджест ВС 22.08.2026</p>
  <h3 class="l24-boris-kass-prog__title">4 признака обвинительного прогноза кассации</h3>
  <p class="l24-boris-kass-prog__lead">Если постановление кассации содержит <strong>хотя бы один</strong> из признаков ниже, защита вправе ссылаться на позицию ВС: кассация проверяет <strong>законность</strong>, но не подменяет суд первой инстанции и не «назначает» виновность. В деле № 53 <strong>8-й КСОЮ</strong> нарушил <strong>все четыре</strong> — ВС направил дело на новое кассационное рассмотрение в ином составе.</p>

  <div class="l24-boris-kass-prog__split">
    <svg class="l24-boris-kass-prog__matrix-svg" viewBox="0 0 520 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="bkProgT bkProgD">
      <title id="bkProgT">Матрица 4 признаков обвинительного прогноза кассации по делу № 53-УД26-9-К8</title>
      <desc id="bkProgD">Центр — запрет кассации предрешать виновность; четыре квадранта: новые факты, оценка достоверности, незаконное освобождение, статья и мера наказания</desc>
      <defs>
        <marker id="bkProg-arr" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
          <polygon points="0 0, 7 3, 0 6" fill="#f87171"/>
        </marker>
        <filter id="bkProg-glow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.35"/>
        </filter>
      </defs>

      <!-- Фоновая сетка 2×2 -->
      <rect x="24" y="24" width="472" height="312" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
      <line x1="260" y1="24" x2="260" y2="336" stroke="rgba(236,201,75,0.22)" stroke-width="1.5" stroke-dasharray="5,4"/>
      <line x1="24" y1="180" x2="496" y2="180" stroke="rgba(236,201,75,0.22)" stroke-width="1.5" stroke-dasharray="5,4"/>

      <!-- Центральный хаб -->
      <circle cx="260" cy="180" r="52" fill="#1a365d" stroke="#ecc94b" stroke-width="2.2" filter="url(#bkProg-glow)"/>
      <text x="260" y="168" text-anchor="middle" fill="#fde68a" font-size="7" font-weight="800" font-family="system-ui,sans-serif" letter-spacing="0.04em">ЗАПРЕТ ВС</text>
      <text x="260" y="182" text-anchor="middle" fill="#fff" font-size="6.2" font-weight="700" font-family="system-ui,sans-serif">кассация ≠</text>
      <text x="260" y="194" text-anchor="middle" fill="#fff" font-size="6.2" font-weight="700" font-family="system-ui,sans-serif">суд по фактам</text>
      <text x="260" y="208" text-anchor="middle" fill="#94a3b8" font-size="5.5" font-family="system-ui,sans-serif">№ 53 · 05.08.2026</text>

      <!-- Стрелки нарушений к центру -->
      <path d="M118 118 L210 158" fill="none" stroke="#f87171" stroke-width="1.4" marker-end="url(#bkProg-arr)" opacity="0.85"/>
      <path d="M402 118 L310 158" fill="none" stroke="#fb923c" stroke-width="1.4" marker-end="url(#bkProg-arr)" opacity="0.85"/>
      <path d="M118 242 L210 202" fill="none" stroke="#ecc94b" stroke-width="1.4" marker-end="url(#bkProg-arr)" opacity="0.85"/>
      <path d="M402 242 L310 202" fill="none" stroke="#818cf8" stroke-width="1.4" marker-end="url(#bkProg-arr)" opacity="0.85"/>

      <!-- Квадрант 1 — верхний левый -->
      <rect x="36" y="36" width="210" height="132" rx="10" fill="rgba(248,113,113,0.1)" stroke="#f87171" stroke-width="1.2"/>
      <text x="48" y="58" fill="#fecaca" font-size="8" font-weight="800" font-family="system-ui,sans-serif">1 · НОВЫЕ ФАКТЫ</text>
      <text x="48" y="78" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">Установила обстоятельства,</text>
      <text x="48" y="92" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">не найденные судами</text>
      <text x="48" y="106" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">1–2 инстанций</text>
      <text x="48" y="128" fill="#94a3b8" font-size="5.8" font-style="italic" font-family="system-ui,sans-serif">8-й КСОЮ · № 7У-208/2026</text>
      <text x="48" y="148" fill="#fca5a5" font-size="6" font-weight="700" font-family="system-ui,sans-serif">✕ нарушение</text>

      <!-- Квадрант 2 — верхний правый -->
      <rect x="274" y="36" width="210" height="132" rx="10" fill="rgba(251,146,60,0.08)" stroke="#fb923c" stroke-width="1.2"/>
      <text x="286" y="58" fill="#fed7aa" font-size="8" font-weight="800" font-family="system-ui,sans-serif">2 · ДОСТОВЕРНОСТЬ</text>
      <text x="286" y="78" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">Оценила достоверность</text>
      <text x="286" y="92" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">доказательств вместо</text>
      <text x="286" y="106" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">проверки законности</text>
      <text x="286" y="128" fill="#94a3b8" font-size="5.8" font-style="italic" font-family="system-ui,sans-serif">заново оценила док-ва</text>
      <text x="286" y="148" fill="#fdba74" font-size="6" font-weight="700" font-family="system-ui,sans-serif">✕ нарушение</text>

      <!-- Квадрант 3 — нижний левый -->
      <rect x="36" y="192" width="210" height="132" rx="10" fill="rgba(236,201,75,0.08)" stroke="#ecc94b" stroke-width="1.2"/>
      <text x="48" y="214" fill="#fde68a" font-size="8" font-weight="800" font-family="system-ui,sans-serif">3 · ОБВИНИТ. ИСХОД</text>
      <text x="48" y="234" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">«Незаконное и</text>
      <text x="48" y="248" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">необоснованное</text>
      <text x="48" y="262" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">освобождение»</text>
      <text x="48" y="284" fill="#94a3b8" font-size="5.8" font-style="italic" font-family="system-ui,sans-serif">предрешила виновность</text>
      <text x="48" y="304" fill="#fde68a" font-size="6" font-weight="700" font-family="system-ui,sans-serif">✕ нарушение</text>

      <!-- Квадрант 4 — нижний правый -->
      <rect x="274" y="192" width="210" height="132" rx="10" fill="rgba(129,140,248,0.1)" stroke="#818cf8" stroke-width="1.2"/>
      <text x="286" y="214" fill="#c7d2fe" font-size="8" font-weight="800" font-family="system-ui,sans-serif">4 · СТАТЬЯ / МЕРА</text>
      <text x="286" y="234" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">Определила статью УК</text>
      <text x="286" y="248" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">или меру наказания</text>
      <text x="286" y="262" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">для нового рассмотрения</text>
      <text x="286" y="284" fill="#94a3b8" font-size="5.8" font-style="italic" font-family="system-ui,sans-serif">ч. 7 ст. 401.16 УПК</text>
      <text x="286" y="304" fill="#a5b4fc" font-size="6" font-weight="700" font-family="system-ui,sans-serif">✕ нарушение</text>

      <!-- Нижняя легенда: граница полномочий -->
      <rect x="24" y="344" width="472" height="0" fill="none"/>
      <text x="260" y="352" text-anchor="middle" fill="#64748b" font-size="6" font-weight="700" font-family="system-ui,sans-serif" letter-spacing="0.05em">КАССАЦИЯ → ПРОВЕРКА ЗАКОННОСТИ · НЕ ПОДМЕНА СУДА 1 ИНСТАНЦИИ</text>
    </svg>

    <div class="l24-boris-kass-prog__cards" role="list" aria-label="Чек-лист признаков для кассационной жалобы">
      <div class="l24-boris-kass-prog__card" role="listitem">
        <span class="l24-boris-kass-prog__card-n">Признак 1</span>
        <p class="l24-boris-kass-prog__card-t">Кассация <em>установила факты</em>, не найденные судом первой или апелляционной инстанции</p>
      </div>
      <div class="l24-boris-kass-prog__card" role="listitem">
        <span class="l24-boris-kass-prog__card-n">Признак 2</span>
        <p class="l24-boris-kass-prog__card-t">Оценила <em>достоверность</em> доказательств вместо проверки законности их получения и оценки в приговоре</p>
      </div>
      <div class="l24-boris-kass-prog__card" role="listitem">
        <span class="l24-boris-kass-prog__card-n">Признак 3</span>
        <p class="l24-boris-kass-prog__card-t">Использовала формулировки «незаконное освобождение» — <em>предрешила обвинительный</em> исход нового рассмотрения</p>
      </div>
      <div class="l24-boris-kass-prog__card" role="listitem">
        <span class="l24-boris-kass-prog__card-n">Признак 4</span>
        <p class="l24-boris-kass-prog__card-t">Определила <em>статью УК</em> или <em>меру наказания</em> для суда при повторном рассмотрении</p>
      </div>
    </div>
  </div>

  <p class="l24-boris-kass-prog__verdict"><strong>Дело № 53-УД26-9-К8:</strong> оправдательный приговор (февраль 2025, Красноярск) → отмена 8-м КСОЮ с нарушением всех четырёх признаков → ВС 05.08.2026 отменил постановление кассации и направил дело на <strong>новое кассационное рассмотрение в ином составе</strong>. Нормативный якорь жалобы — <strong>ч. 7 ст. 401.16 УПК РФ</strong>.</p>

  <div class="l24-boris-kass-prog__foot">
    <span class="l24-boris-kass-prog__tag l24-boris-kass-prog__tag--case">№ 53-УД26-9-К8</span>
    <span class="l24-boris-kass-prog__tag l24-boris-kass-prog__tag--law">ч. 7 ст. 401.16 УПК</span>
    <span class="l24-boris-kass-prog__tag l24-boris-kass-prog__tag--warn">8-й КСОЮ · № 7У-208/2026</span>
    <span class="l24-boris-kass-prog__tag">ч. 1 ст. 286 УК</span>
    <span class="l24-boris-kass-prog__tag">дайджест 22.08.2026</span>
  </div>
</div>
</section>
```
