
=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**Режим:** контраст к hero Алины (светлый «реестр/витрина» → плотная тёмная карта в теле статьи).  
**Якорь для Наташи:** вставить после H2 «Досудебная защита: претензия по товарному знаку и ответ», перед H2 «Иск по товарному знаку…».  
**ID секции:** `l24-boris-tz-ip-track` (не пересекается с hero/canvas Алины).

### Чеклист отличий от hero
- [x] Не первый экран, не fullscreen
- [x] Без `<canvas>` и `<script>` — только static SVG + CSS
- [x] Свой `id` секции: `l24-boris-tz-ip-track`
- [x] Контраст: тёмный inset (#0f2744) vs светлый hero
- [x] Сплит: таймлайн МП → претензия → суд + сетка «цена ошибки 2026»
- [x] `aria-label` и семантика `<section>`

---

```html
<section id="l24-boris-tz-ip-track" class="l24-boris-tz-ip" aria-label="Товарный знак: маркетплейс, претензия, суд и компенсация 2026">
<style>
.l24-boris-tz-ip {
  --tz-navy: #0f2744;
  --tz-navy-soft: #1a365d;
  --tz-accent: #c53030;
  --tz-gold: #ecc94b;
  --tz-mint: #68d391;
  --tz-ink: #e2e8f0;
  --tz-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-tz-ip__shell {
  background: linear-gradient(145deg, var(--tz-navy) 0%, #152a45 55%, var(--tz-navy-soft) 100%);
  border: 1px solid rgba(236, 201, 75, 0.22);
  border-radius: 14px;
  padding: 32px 28px 28px;
  box-shadow: 0 18px 48px rgba(15, 39, 68, 0.28);
  color: var(--tz-ink);
}
.l24-boris-tz-ip__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--tz-gold);
}
.l24-boris-tz-ip__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.4rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-tz-ip__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--tz-muted);
  max-width: 62ch;
}
.l24-boris-tz-ip__lead strong { color: #fff; }
.l24-boris-tz-ip__split {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.95fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-tz-ip__panel {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-tz-ip__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--tz-gold);
}
.l24-boris-tz-ip__timeline-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 220px;
}
.l24-boris-tz-ip__steps {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin: 16px 0 0;
  padding: 0;
  list-style: none;
}
.l24-boris-tz-ip__step {
  margin: 0;
  padding: 12px 10px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  border-left: 3px solid var(--tz-accent);
  font-size: 0.78rem;
  line-height: 1.4;
}
.l24-boris-tz-ip__step:nth-child(2) { border-left-color: var(--tz-gold); }
.l24-boris-tz-ip__step:nth-child(3) { border-left-color: var(--tz-mint); }
.l24-boris-tz-ip__step strong {
  display: block;
  color: #fff;
  font-size: 0.82rem;
  margin-bottom: 4px;
}
.l24-boris-tz-ip__comp-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin: 0 0 14px;
}
.l24-boris-tz-ip__comp-card {
  padding: 12px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.22);
  border: 1px solid rgba(255, 255, 255, 0.08);
}
.l24-boris-tz-ip__comp-card--wide {
  grid-column: 1 / -1;
  border-color: rgba(236, 201, 75, 0.35);
  background: rgba(197, 48, 48, 0.15);
}
.l24-boris-tz-ip__comp-label {
  display: block;
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--tz-muted);
  margin-bottom: 4px;
}
.l24-boris-tz-ip__comp-value {
  font-size: 1.05rem;
  font-weight: 800;
  color: #fff;
  line-height: 1.2;
}
.l24-boris-tz-ip__comp-note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--tz-muted);
}
.l24-boris-tz-ip__comp-note em {
  font-style: normal;
  color: var(--tz-mint);
  font-weight: 600;
}
.l24-boris-tz-ip__roles {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-tz-ip__role {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
  color: var(--tz-ink);
}
.l24-boris-tz-ip__role--owner { border: 1px solid var(--tz-gold); color: var(--tz-gold); }
.l24-boris-tz-ip__role--def { border: 1px solid var(--tz-mint); color: var(--tz-mint); }
@media (max-width: 900px) {
  .l24-boris-tz-ip__split { grid-template-columns: 1fr; }
  .l24-boris-tz-ip__steps { grid-template-columns: 1fr; }
  .l24-boris-tz-ip__comp-grid { grid-template-columns: 1fr; }
  .l24-boris-tz-ip__comp-card--wide { grid-column: auto; }
}
</style>

  <div class="l24-boris-tz-ip__shell">
    <p class="l24-boris-tz-ip__eyebrow">214-ФЗ · с 04.01.2026 · ГК РФ ч. 4</p>
    <h3 class="l24-boris-tz-ip__title">МП → претензия → суд: одна шкала времени и «цена ошибки»</h3>
    <p class="l24-boris-tz-ip__lead">Спор по <strong>товарному знаку</strong> у селлера редко стартует в СИП: сначала <strong>маркетплейс</strong> (жалоба и блокировка), затем <strong>досудебная претензия</strong> (30 дней по ст. 1252 ГК РФ), затем <strong>иск</strong> и отзыв по ст. 131 АПК. Справа — лимиты компенсации после реформы и поле для снижения по ст. 1252.1.</p>

    <div class="l24-boris-tz-ip__split">
      <div class="l24-boris-tz-ip__panel">
        <p class="l24-boris-tz-ip__panel-title">Сквозной маршрут</p>
        <svg class="l24-boris-tz-ip__timeline-svg" viewBox="0 0 520 140" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <defs>
            <linearGradient id="tz-ip-line" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#c53030"/>
              <stop offset="50%" stop-color="#ecc94b"/>
              <stop offset="100%" stop-color="#68d391"/>
            </linearGradient>
          </defs>
          <line x1="48" y1="70" x2="472" y2="70" stroke="url(#tz-ip-line)" stroke-width="4" stroke-linecap="round"/>
          <circle cx="72" cy="70" r="22" fill="#c53030" stroke="#fff" stroke-width="2"/>
          <text x="72" y="76" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">МП</text>
          <circle cx="260" cy="70" r="22" fill="#d69e2e" stroke="#fff" stroke-width="2"/>
          <text x="260" y="74" text-anchor="middle" fill="#1a202c" font-size="10" font-weight="700">30д</text>
          <circle cx="448" cy="70" r="22" fill="#2f855a" stroke="#fff" stroke-width="2"/>
          <text x="448" y="76" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">СИП</text>
          <rect x="24" y="108" width="130" height="26" rx="5" fill="rgba(0,0,0,0.35)"/>
          <text x="89" y="125" text-anchor="middle" fill="#e2e8f0" font-size="9">~24 ч апелляция</text>
          <rect x="195" y="108" width="130" height="26" rx="5" fill="rgba(0,0,0,0.35)"/>
          <text x="260" y="125" text-anchor="middle" fill="#e2e8f0" font-size="9">ст. 1252 ГК РФ</text>
          <rect x="366" y="108" width="130" height="26" rx="5" fill="rgba(0,0,0,0.35)"/>
          <text x="431" y="125" text-anchor="middle" fill="#e2e8f0" font-size="9">отзыв ст. 131 АПК</text>
          <text x="72" y="38" text-anchor="middle" fill="#feb2b2" font-size="9" font-weight="600">WB / Ozon</text>
          <text x="260" y="38" text-anchor="middle" fill="#faf089" font-size="9" font-weight="600">претензия</text>
          <text x="448" y="38" text-anchor="middle" fill="#9ae6b4" font-size="9" font-weight="600">компенсация</text>
        </svg>
        <ol class="l24-boris-tz-ip__steps">
          <li class="l24-boris-tz-ip__step">
            <strong>Маркетплейс</strong>
            Жалоба → блокировка карточки; WB до 10 раб. дн., Ozon 5–14 раб. дн. Пакет: свидетельство, лицензия, сравнение знаков.
          </li>
          <li class="l24-boris-tz-ip__step">
            <strong>Претензия</strong>
            30 дней до иска (ст. 1252). Ответ: сходство, однородность, расчёт компенсации, добросовестность.
          </li>
          <li class="l24-boris-tz-ip__step">
            <strong>Суд</strong>
            Иск в СИП → отзыв → ст. 1486 (неиспользование знака истца) + оспаривание суммы по ст. 1252.1.
          </li>
        </ol>
      </div>

      <div class="l24-boris-tz-ip__panel">
        <p class="l24-boris-tz-ip__panel-title">Компенсация 2026 (ст. 1515, 1252.1)</p>
        <div class="l24-boris-tz-ip__comp-grid">
          <div class="l24-boris-tz-ip__comp-card">
            <span class="l24-boris-tz-ip__comp-label">Твёрдая</span>
            <span class="l24-boris-tz-ip__comp-value">10–20 млн ₽</span>
          </div>
          <div class="l24-boris-tz-ip__comp-card">
            <span class="l24-boris-tz-ip__comp-label">Снижение без вины</span>
            <span class="l24-boris-tz-ip__comp-value">10–500 тыс.</span>
          </div>
          <div class="l24-boris-tz-ip__comp-card l24-boris-tz-ip__comp-card--wide">
            <span class="l24-boris-tz-ip__comp-label">2× товар или 2× лицензия — без потолка</span>
            <span class="l24-boris-tz-ip__comp-value">десятки–сотни млн</span>
          </div>
        </div>
        <p class="l24-boris-tz-ip__comp-note"><em>Один товар — одно нарушение</em> (ст. 1252.1): нельзя умножать ТЗ + дизайн + фото на одной карточке без самостоятельной ценности каждого способа.</p>
      </div>
    </div>

    <div class="l24-boris-tz-ip__roles" aria-label="Две роли в одном маршруте">
      <span class="l24-boris-tz-ip__role l24-boris-tz-ip__role--owner">Правообладатель: мониторинг МП → претензия → иск</span>
      <span class="l24-boris-tz-ip__role l24-boris-tz-ip__role--def">Ответчик: апелляция → ответ 30 дн. → отзыв + 1486 / 1252.1</span>
    </div>
  </div>
</section>
```

**Паспорт блока (для Наташи):** slug `zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstvennosti`; тема — сквозная шкала из research Артёма; ключевые цифры: 24 ч МП, 30 дн. претензия, 10/20 млн, 10–500 тыс., ст. 1252.1 «один товар — одно нарушение».
