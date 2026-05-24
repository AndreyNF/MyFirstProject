=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**Slug:** otvet-na-pretensiyu-po-intellektualnoj-sobstvennosti  
**Тема:** ответ на претензию по ИС — календарь сроков ответчика  
**Якорь вставки:** после H2 «Сроки ответа на претензию: что проверить в первую очередь» (1–2 секции от начала лонгрида)  
**Режим:** продолжение метафоры Алины — hero показывает «претензия → ответ → щит ИС» и три срока в списке; Борис раскрывает **практический календарь** и различие режимов на тёмной редакционной сетке.

**Чеклист отличий от hero Алины:**
- Не full-viewport, не первый экран — блок в теле статьи (`margin: 48px 0`).
- Тёмный фон и split/grid вместо светлого hero с двухколоночным H1.
- Свой `id` секции — не `l24-hero-ip-pret-otvet`.
- Без CTA-кнопки — только информационная карта с подписью.
- Static SVG + inline CSS, без `<canvas>` и `<script>` (Legis24 MCP-only).

```html
<section id="l24-boris-ip-pret-sroki-track" class="l24-boris-ip-pret-sroki" aria-label="Календарь ответчика: сроки ответа на претензию по интеллектуальной собственности">
<style>
.l24-boris-ip-pret-sroki {
  --ip-navy: #0f2744;
  --ip-navy-soft: #1a365d;
  --ip-blue: #63b3ed;
  --ip-gold: #ecc94b;
  --ip-teal: #4fd1c5;
  --ip-accent: #fc8181;
  --ip-ink: #e2e8f0;
  --ip-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-ip-pret-sroki__shell {
  background: linear-gradient(148deg, var(--ip-navy) 0%, #122640 52%, var(--ip-navy-soft) 100%);
  border: 1px solid rgba(99, 179, 237, 0.24);
  border-radius: 14px;
  padding: 32px 28px 28px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06), 0 20px 52px rgba(15, 39, 68, 0.32);
  color: var(--ip-ink);
}
.l24-boris-ip-pret-sroki__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ip-gold);
}
.l24-boris-ip-pret-sroki__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-ip-pret-sroki__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--ip-muted);
  max-width: 68ch;
}
.l24-boris-ip-pret-sroki__lead strong { color: #fff; }
.l24-boris-ip-pret-sroki__split {
  display: grid;
  grid-template-columns: minmax(0, 1.12fr) minmax(0, 0.98fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-ip-pret-sroki__panel {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-ip-pret-sroki__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--ip-gold);
}
.l24-boris-ip-pret-sroki__calendar-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 200px;
  margin-bottom: 14px;
}
.l24-boris-ip-pret-sroki__steps {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-ip-pret-sroki__step {
  margin: 0;
  padding: 12px 10px;
  background: rgba(0, 0, 0, 0.22);
  border-radius: 8px;
  border-left: 3px solid var(--ip-blue);
  font-size: 0.78rem;
  line-height: 1.4;
}
.l24-boris-ip-pret-sroki__step:nth-child(2) { border-left-color: var(--ip-gold); }
.l24-boris-ip-pret-sroki__step:nth-child(3) { border-left-color: var(--ip-teal); }
.l24-boris-ip-pret-sroki__step:nth-child(4) { border-left-color: #68d391; grid-column: 1 / -1; }
.l24-boris-ip-pret-sroki__step strong {
  display: block;
  color: #fff;
  font-size: 0.82rem;
  margin-bottom: 4px;
}
.l24-boris-ip-pret-sroki__regime-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
  margin: 0 0 14px;
}
.l24-boris-ip-pret-sroki__regime {
  padding: 12px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.24);
  border: 1px solid rgba(255, 255, 255, 0.08);
}
.l24-boris-ip-pret-sroki__regime--soft { border-left: 3px solid var(--ip-muted); }
.l24-boris-ip-pret-sroki__regime--key {
  border-left: 3px solid var(--ip-blue);
  border-color: rgba(99, 179, 237, 0.35);
  background: rgba(30, 64, 175, 0.14);
}
.l24-boris-ip-pret-sroki__regime--spec {
  border-left: 3px solid var(--ip-teal);
  border-color: rgba(79, 209, 197, 0.35);
  background: rgba(15, 118, 110, 0.12);
}
.l24-boris-ip-pret-sroki__regime-head {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 6px;
}
.l24-boris-ip-pret-sroki__regime-tag {
  flex-shrink: 0;
  padding: 4px 8px;
  border-radius: 5px;
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
.l24-boris-ip-pret-sroki__regime--soft .l24-boris-ip-pret-sroki__regime-tag {
  background: rgba(160, 174, 192, 0.2);
  color: var(--ip-muted);
}
.l24-boris-ip-pret-sroki__regime--key .l24-boris-ip-pret-sroki__regime-tag {
  background: rgba(99, 179, 237, 0.25);
  color: var(--ip-blue);
}
.l24-boris-ip-pret-sroki__regime--spec .l24-boris-ip-pret-sroki__regime-tag {
  background: rgba(79, 209, 197, 0.22);
  color: var(--ip-teal);
}
.l24-boris-ip-pret-sroki__regime-name {
  font-size: 0.82rem;
  font-weight: 700;
  color: #fff;
}
.l24-boris-ip-pret-sroki__regime-text {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--ip-muted);
}
.l24-boris-ip-pret-sroki__regime-text em {
  font-style: normal;
  color: var(--ip-accent);
  font-weight: 600;
}
.l24-boris-ip-pret-sroki__note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--ip-muted);
}
.l24-boris-ip-pret-sroki__note em {
  font-style: normal;
  color: var(--ip-teal);
  font-weight: 600;
}
.l24-boris-ip-pret-sroki__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-ip-pret-sroki__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--ip-ink);
  border: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-ip-pret-sroki__tag--warn { border-color: rgba(252, 129, 129, 0.45); color: #fed7d7; }
.l24-boris-ip-pret-sroki__tag--ok { border-color: rgba(104, 211, 145, 0.45); color: #c6f6d5; }
.l24-boris-ip-pret-sroki__caption {
  margin: 14px 0 0;
  font-size: 0.72rem;
  line-height: 1.4;
  color: rgba(160, 174, 192, 0.85);
  text-align: center;
  letter-spacing: 0.02em;
}
@media (max-width: 900px) {
  .l24-boris-ip-pret-sroki__split { grid-template-columns: 1fr; }
  .l24-boris-ip-pret-sroki__steps { grid-template-columns: 1fr; }
  .l24-boris-ip-pret-sroki__step:nth-child(4) { grid-column: auto; }
}
</style>

  <div class="l24-boris-ip-pret-sroki__shell">
    <p class="l24-boris-ip-pret-sroki__eyebrow">ст. 1252 · 1486 · ч. 5 ст. 4 АПК · календарь ответчика</p>
    <h3 class="l24-boris-ip-pret-sroki__title">Три срока в претензии — одна шкала действий до иска</h3>
    <p class="l24-boris-ip-pret-sroki__lead">Слева — <strong>практический маршрут</strong> с дня получения письма до мотивированного ответа. Справа — <strong>три юридических режима</strong>: «10 дней» из шапки, 30 календарных дней по comp/убыткам и 2 месяца по неиспользованию ТЗ. Путаница между ними — главная ошибка ответчика.</p>

    <div class="l24-boris-ip-pret-sroki__split">
      <div class="l24-boris-ip-pret-sroki__panel">
        <p class="l24-boris-ip-pret-sroki__panel-title">Практический календарь (ст. 1252)</p>
        <svg class="l24-boris-ip-pret-sroki__calendar-svg" viewBox="0 0 540 168" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <defs>
            <linearGradient id="boris-ip-sroki-line" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#63b3ed"/>
              <stop offset="45%" stop-color="#ecc94b"/>
              <stop offset="100%" stop-color="#4fd1c5"/>
            </linearGradient>
          </defs>
          <line x1="40" y1="78" x2="500" y2="78" stroke="url(#boris-ip-sroki-line)" stroke-width="4" stroke-linecap="round"/>
          <circle cx="56" cy="78" r="20" fill="#1e40af" stroke="#fff" stroke-width="2"/>
          <text x="56" y="83" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">Д0</text>
          <circle cx="168" cy="78" r="18" fill="#2b6cb0" stroke="#fff" stroke-width="2"/>
          <text x="168" y="83" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">1–3</text>
          <circle cx="280" cy="78" r="18" fill="#d69e2e" stroke="#fff" stroke-width="2"/>
          <text x="280" y="83" text-anchor="middle" fill="#1a202c" font-size="8" font-weight="700">3–10</text>
          <circle cx="392" cy="78" r="18" fill="#319795" stroke="#fff" stroke-width="2"/>
          <text x="392" y="83" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">…</text>
          <circle cx="484" cy="78" r="22" fill="#276749" stroke="#ecc94b" stroke-width="2.5"/>
          <text x="484" y="83" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">30</text>
          <text x="56" y="38" text-anchor="middle" fill="#bee3f8" font-size="9" font-weight="600">получение</text>
          <text x="168" y="38" text-anchor="middle" fill="#bee3f8" font-size="9" font-weight="600">проверка</text>
          <text x="280" y="38" text-anchor="middle" fill="#faf089" font-size="9" font-weight="600">доказательства</text>
          <text x="484" y="38" text-anchor="middle" fill="#9ae6b4" font-size="9" font-weight="600">ответ</text>
          <rect x="24" y="118" width="120" height="28" rx="5" fill="rgba(0,0,0,0.35)"/>
          <text x="84" y="136" text-anchor="middle" fill="#e2e8f0" font-size="8.5">штамп · ЭДО · акт</text>
          <rect x="156" y="118" width="120" height="28" rx="5" fill="rgba(0,0,0,0.35)"/>
          <text x="216" y="136" text-anchor="middle" fill="#e2e8f0" font-size="8.5">полномочия · объект ИС</text>
          <rect x="288" y="118" width="120" height="28" rx="5" fill="rgba(0,0,0,0.35)"/>
          <text x="348" y="136" text-anchor="middle" fill="#e2e8f0" font-size="8.5">стратегия · лицензии</text>
          <rect x="420" y="118" width="108" height="28" rx="5" fill="rgba(39,103,73,0.45)" stroke="rgba(104,211,145,0.4)" stroke-width="1"/>
          <text x="474" y="136" text-anchor="middle" fill="#c6f6d5" font-size="8.5" font-weight="600">→ основа отзыва</text>
          <rect x="200" y="152" width="140" height="12" rx="3" fill="rgba(252,129,129,0.25)"/>
          <text x="270" y="161" text-anchor="middle" fill="#fed7d7" font-size="7.5" font-weight="600">«10 дней» в шапке — не дедлайн</text>
        </svg>
        <ol class="l24-boris-ip-pret-sroki__steps">
          <li class="l24-boris-ip-pret-sroki__step">
            <strong>День 0 — фиксация</strong>
            Дата получения: штамп на конверте, уведомление ЭДО, акт курьера. Без этого сложно оспорить срок направления претензии.
          </li>
          <li class="l24-boris-ip-pret-sroki__step">
            <strong>Дни 1–3 — проверка</strong>
            Полномочия подписанта, объект ИС в реестре, состав требований: comp vs убытки vs запрет (последний — без 30 дней).
          </li>
          <li class="l24-boris-ip-pret-sroki__step">
            <strong>Дни 3–10 — доказательства</strong>
            Лицензии, сравнение знаков/контента, prior use, переписка. Стратегия: оспорить, точечно прекратить, переговоры.
          </li>
          <li class="l24-boris-ip-pret-sroki__step">
            <strong>До 30-го дня — мотивированный ответ</strong>
            По пунктам, без лишних признаний, с контрасчётом comp (214-ФЗ, ст. 1252.1) и заявлением об исковой давности. Доказательства отправки — обязательны.
          </li>
        </ol>
      </div>

      <div class="l24-boris-ip-pret-sroki__panel">
        <p class="l24-boris-ip-pret-sroki__panel-title">Три режима сроков</p>
        <div class="l24-boris-ip-pret-sroki__regime-grid">
          <div class="l24-boris-ip-pret-sroki__regime l24-boris-ip-pret-sroki__regime--soft">
            <div class="l24-boris-ip-pret-sroki__regime-head">
              <span class="l24-boris-ip-pret-sroki__regime-tag">7–14 дн.</span>
              <span class="l24-boris-ip-pret-sroki__regime-name">Срок «из шапки претензии»</span>
            </div>
            <p class="l24-boris-ip-pret-sroki__regime-text"><em>Не установлен законом.</em> Инструмент психологического давления: пропуск не влечёт автоматических санкций и не улучшает позицию истца сам по себе.</p>
          </div>
          <div class="l24-boris-ip-pret-sroki__regime l24-boris-ip-pret-sroki__regime--key">
            <div class="l24-boris-ip-pret-sroki__regime-head">
              <span class="l24-boris-ip-pret-sroki__regime-tag">30 дн.</span>
              <span class="l24-boris-ip-pret-sroki__regime-name">п. 5.1 ст. 1252 ГК РФ</span>
            </div>
            <p class="l24-boris-ip-pret-sroki__regime-text">Обязателен перед иском о <strong style="color:#fff">comp/убытках</strong> в арбитраже (юрлица/ИП). Иск — при отказе или неполучении ответа. Иной срок возможен по <strong style="color:#fff">договору</strong>.</p>
          </div>
          <div class="l24-boris-ip-pret-sroki__regime l24-boris-ip-pret-sroki__regime--spec">
            <div class="l24-boris-ip-pret-sroki__regime-head">
              <span class="l24-boris-ip-pret-sroki__regime-tag">2 мес.</span>
              <span class="l24-boris-ip-pret-sroki__regime-name">ст. 1486 ГК РФ</span>
            </div>
            <p class="l24-boris-ip-pret-sroki__regime-text">Спецрежим <strong style="color:#fff">неиспользования ТЗ</strong>: иной срок для правообладателя, иные последствия пропуска. Не смешивать с 30 днями по comp.</p>
          </div>
        </div>
        <p class="l24-boris-ip-pret-sroki__note"><em>Запрет использования и изъятие</em> (пп. 1, 2, 4, 5 п. 1 ст. 1252) — претензия не обязательна, иск возможен сразу. В <strong style="color:#fff">СОЮ</strong> досудебный порядок для ИС формально не обязателен — но ответ фиксирует позицию для отзыва.</p>
      </div>
    </div>

    <div class="l24-boris-ip-pret-sroki__foot" aria-label="Ключевые оговорки для ответчика">
      <span class="l24-boris-ip-pret-sroki__tag l24-boris-ip-pret-sroki__tag--warn">comp в претензии — пределы, не обязательна точная сумма</span>
      <span class="l24-boris-ip-pret-sroki__tag l24-boris-ip-pret-sroki__tag--warn">убытки — нужна конкретная сумма в претензии</span>
      <span class="l24-boris-ip-pret-sroki__tag l24-boris-ip-pret-sroki__tag--ok">30 дней истекли ≠ автоматический иск</span>
      <span class="l24-boris-ip-pret-sroki__tag">214-ФЗ · comp до 10 млн ₽ по ТЗ</span>
    </div>
    <p class="l24-boris-ip-pret-sroki__caption">Подпись блока: календарь ответчика на претензию по ИС — не путать давление «10 дней», процессуальные 30 дней и спецрежим 1486.</p>
  </div>
</section>
```

**Паспорт блока**
- **Anchor id:** `l24-boris-ip-pret-sroki-track`
- **Класс корня:** `l24-boris-ip-pret-sroki`
- **Legis24 MCP:** static SVG + inline CSS only (без canvas/script)
- **Hero Алины (не дублировать):** `#l24-hero-ip-pret-otvet`
