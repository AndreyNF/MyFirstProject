=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**Тема:** A10 / UG — защита на стадии проверки и в суде (два трека, 72 ч, ст. 144)  
**Режим:** контраст к светлому hero Алины (тёмный inset в теле статьи)  
**Техника:** static SVG + inline CSS — без `<canvas>` и `<script>`

```html
<section id="l24-boris-ug-defense-stages" class="l24-boris-ug-def" aria-label="Уголовная защита: стадии проверки и подозреваемого, сроки ст. 144 и чеклист 72 часа">
<style>
.l24-boris-ug-def {
  --ug-navy: #0f1a24;
  --ug-navy-soft: #1a2d3d;
  --ug-amber: #e8b84a;
  --ug-crimson: #e85d6a;
  --ug-teal: #4fd1c5;
  --ug-blue: #63b3ed;
  --ug-ink: #e8edf2;
  --ug-muted: #8fa3b8;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-ug-def__shell {
  background: linear-gradient(152deg, var(--ug-navy) 0%, #152535 48%, var(--ug-navy-soft) 100%);
  border: 1px solid rgba(232, 184, 74, 0.26);
  border-radius: 14px;
  padding: 32px 28px 28px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05), 0 20px 52px rgba(15, 26, 36, 0.4);
  color: var(--ug-ink);
}
.l24-boris-ug-def__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ug-amber);
}
.l24-boris-ug-def__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-ug-def__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--ug-muted);
  max-width: 68ch;
}
.l24-boris-ug-def__lead strong { color: #fff; }
.l24-boris-ug-def__split {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-ug-def__panel {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.09);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-ug-def__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--ug-amber);
}
.l24-boris-ug-def__fork-svg,
.l24-boris-ug-def__timeline-svg {
  display: block;
  width: 100%;
  height: auto;
}
.l24-boris-ug-def__fork-svg { max-height: 200px; margin-bottom: 12px; }
.l24-boris-ug-def__timeline-svg { max-height: 148px; margin-bottom: 10px; }
.l24-boris-ug-def__stages {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-ug-def__stage {
  margin: 0;
  padding: 10px 8px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.24);
  border-top: 3px solid var(--ug-blue);
  font-size: 0.72rem;
  line-height: 1.38;
}
.l24-boris-ug-def__stage:nth-child(2) { border-top-color: var(--ug-crimson); }
.l24-boris-ug-def__stage:nth-child(3) { border-top-color: var(--ug-teal); }
.l24-boris-ug-def__stage strong {
  display: block;
  color: #fff;
  font-size: 0.78rem;
  margin-bottom: 4px;
}
.l24-boris-ug-def__hours {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
  margin: 12px 0 0;
  padding: 0;
  list-style: none;
}
.l24-boris-ug-def__hour {
  margin: 0;
  padding: 10px 8px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.22);
  border-left: 3px solid var(--ug-amber);
  font-size: 0.7rem;
  line-height: 1.35;
}
.l24-boris-ug-def__hour:nth-child(2) { border-left-color: var(--ug-crimson); }
.l24-boris-ug-def__hour:nth-child(3) { border-left-color: var(--ug-blue); }
.l24-boris-ug-def__hour:nth-child(4) { border-left-color: var(--ug-teal); }
.l24-boris-ug-def__hour:nth-child(5) { border-left-color: var(--ug-amber); grid-column: 1 / -1; }
.l24-boris-ug-def__hour strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 3px;
}
.l24-boris-ug-def__nums {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 0 0 10px;
}
.l24-boris-ug-def__num {
  padding: 11px 9px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.26);
  border: 1px solid rgba(255, 255, 255, 0.07);
}
.l24-boris-ug-def__num--wide {
  grid-column: 1 / -1;
  border-color: rgba(232, 184, 74, 0.32);
  background: rgba(232, 184, 74, 0.07);
}
.l24-boris-ug-def__num-label {
  display: block;
  font-size: 0.66rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--ug-muted);
  margin-bottom: 4px;
}
.l24-boris-ug-def__num-value {
  font-size: 1rem;
  font-weight: 800;
  color: #fff;
  line-height: 1.2;
}
.l24-boris-ug-def__rights {
  margin: 0;
  padding: 0;
  list-style: none;
  font-size: 0.72rem;
  line-height: 1.42;
  color: var(--ug-muted);
}
.l24-boris-ug-def__rights li {
  margin: 0 0 6px;
  padding-left: 14px;
  position: relative;
}
.l24-boris-ug-def__rights li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0.45em;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--ug-teal);
}
.l24-boris-ug-def__rights strong { color: #fff; }
.l24-boris-ug-def__note {
  margin: 10px 0 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--ug-muted);
}
.l24-boris-ug-def__note em {
  font-style: normal;
  color: var(--ug-teal);
  font-weight: 600;
}
.l24-boris-ug-def__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-ug-def__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.07);
  color: var(--ug-ink);
}
.l24-boris-ug-def__tag--t1 { border: 1px solid var(--ug-crimson); color: #feb2b2; }
.l24-boris-ug-def__tag--t2 { border: 1px solid var(--ug-teal); color: #99f6e4; }
.l24-boris-ug-def__tag--law { border: 1px solid var(--ug-amber); color: #faf089; }
@media (max-width: 900px) {
  .l24-boris-ug-def__split { grid-template-columns: 1fr; }
  .l24-boris-ug-def__stages { grid-template-columns: 1fr; }
  .l24-boris-ug-def__nums { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 520px) {
  .l24-boris-ug-def__hours { grid-template-columns: 1fr; }
  .l24-boris-ug-def__nums { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-ug-def__shell">
    <p class="l24-boris-ug-def__eyebrow">УПК · ст. 144.1.1 · 46–53 · 217 · 2025–2026</p>
    <h3 class="l24-boris-ug-def__title">Проверка → подозреваемый → суд: два трека и 72 часа без самооговора</h3>
    <p class="l24-boris-ug-def__lead">Слева — <strong>развилка стадий</strong>: материал проверки (КРСП), дознание/следствие после возбуждения, суд. Справа — <strong>чеклист 72 часов</strong> и сроки из research: <strong>3 / 10 / 30 суток</strong> по ст. 144, <strong>48 ч</strong> задержание, <strong>2 месяца</strong> предварительное следствие. Не путать «проверку» с уже возбуждённым делом — права по ч. 1.1 ст. 144 действуют ещё до статуса подозреваемого.</p>

    <div class="l24-boris-ug-def__split">
      <div class="l24-boris-ug-def__panel">
        <p class="l24-boris-ug-def__panel-title">Стадии: куда вы сейчас</p>
        <svg class="l24-boris-ug-def__fork-svg" viewBox="0 0 520 172" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <defs>
            <linearGradient id="ug-fork-bg" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#1e3348"/>
              <stop offset="100%" stop-color="#0f1f2e"/>
            </linearGradient>
          </defs>
          <rect width="520" height="172" rx="8" fill="url(#ug-fork-bg)" opacity="0.55"/>
          <text x="260" y="20" text-anchor="middle" fill="#e8b84a" font-size="9" font-weight="700" letter-spacing="0.1em">КОНТАКТ С ОРГАНОМ / ВЫЗОВ / ОБЫСК</text>
          <rect x="200" y="28" width="120" height="26" rx="6" fill="#243447" stroke="#e8b84a" stroke-width="1.2"/>
          <text x="260" y="45" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">Уточнить статус</text>
          <path d="M260 54 L260 68" stroke="#5a6f82" stroke-width="1.5"/>
          <path d="M260 68 L72 98" stroke="#63b3ed" stroke-width="1.5" fill="none"/>
          <path d="M260 68 L260 98" stroke="#e85d6a" stroke-width="1.5" fill="none"/>
          <path d="M260 68 L448 98" stroke="#4fd1c5" stroke-width="1.5" fill="none"/>
          <rect x="16" y="102" width="112" height="58" rx="8" fill="rgba(99,179,237,0.14)" stroke="#63b3ed" stroke-width="1.2"/>
          <text x="72" y="122" text-anchor="middle" fill="#bee3f8" font-size="9" font-weight="700">Проверка</text>
          <text x="72" y="138" text-anchor="middle" fill="#e8edf2" font-size="8" font-weight="600">КРСП · ст. 144</text>
          <text x="72" y="152" text-anchor="middle" fill="#8fa3b8" font-size="7">ч. 1.1 — адвокат, молчание</text>
          <rect x="204" y="102" width="112" height="58" rx="8" fill="rgba(232,93,106,0.12)" stroke="#e85d6a" stroke-width="1.2"/>
          <text x="260" y="122" text-anchor="middle" fill="#feb2b2" font-size="9" font-weight="700">Подозреваемый</text>
          <text x="260" y="138" text-anchor="middle" fill="#e8edf2" font-size="8" font-weight="600">дознание / следствие</text>
          <text x="260" y="152" text-anchor="middle" fill="#8fa3b8" font-size="7">ст. 46–53 · 216 · 217</text>
          <rect x="392" y="102" width="112" height="58" rx="8" fill="rgba(79,209,197,0.1)" stroke="#4fd1c5" stroke-width="1.2"/>
          <text x="448" y="122" text-anchor="middle" fill="#99f6e4" font-size="9" font-weight="700">Суд</text>
          <text x="448" y="138" text-anchor="middle" fill="#e8edf2" font-size="8" font-weight="600">подсудимый</text>
          <text x="448" y="152" text-anchor="middle" fill="#8fa3b8" font-size="7">Пленум № 29 · ст. 51</text>
        </svg>
        <ul class="l24-boris-ug-def__stages">
          <li class="l24-boris-ug-def__stage">
            <strong>Проверка</strong>
            Часто без статуса подозреваемого; ч. 1.1 ст. 144 — отказ от объяснений, адвокат, жалобы гл. 16.
          </li>
          <li class="l24-boris-ug-def__stage">
            <strong>После возбуждения</strong>
            Подозреваемый → обвиняемый; допрос с защитником (ст. 51); дознание 30 сут. / следствие 2 мес.
          </li>
          <li class="l24-boris-ug-def__stage">
            <strong>Суд</strong>
            Линия после ст. 217: недопустимые (ст. 75) → судебное следствие → последнее слово.
          </li>
        </ul>
      </div>

      <div class="l24-boris-ug-def__panel">
        <p class="l24-boris-ug-def__panel-title">72 часа + сроки ст. 144 / 91 / 162</p>
        <svg class="l24-boris-ug-def__timeline-svg" viewBox="0 0 520 118" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <line x1="36" y1="56" x2="484" y2="56" stroke="#3d5266" stroke-width="2" stroke-dasharray="5 4"/>
          <circle cx="52" cy="56" r="13" fill="#e8b84a"/><text x="52" y="61" text-anchor="middle" fill="#1a202c" font-size="8" font-weight="800">0</text>
          <circle cx="148" cy="56" r="13" fill="#e85d6a"/><text x="148" y="61" text-anchor="middle" fill="#fff" font-size="8" font-weight="800">24</text>
          <circle cx="244" cy="56" r="13" fill="#63b3ed"/><text x="244" y="61" text-anchor="middle" fill="#1a202c" font-size="8" font-weight="800">3</text>
          <circle cx="340" cy="56" r="13" fill="#4fd1c5"/><text x="340" y="61" text-anchor="middle" fill="#1a202c" font-size="8" font-weight="800">48</text>
          <circle cx="468" cy="56" r="13" fill="#e8b84a"/><text x="468" y="61" text-anchor="middle" fill="#1a202c" font-size="8" font-weight="800">72</text>
          <text x="52" y="36" text-anchor="middle" fill="#e8b84a" font-size="7.5" font-weight="600">ордер</text>
          <text x="148" y="36" text-anchor="middle" fill="#feb2b2" font-size="7.5" font-weight="600">задержание</text>
          <text x="244" y="36" text-anchor="middle" fill="#bee3f8" font-size="7.5" font-weight="600">ст. 144</text>
          <text x="340" y="36" text-anchor="middle" fill="#99f6e4" font-size="7.5" font-weight="600">допрос</text>
          <text x="468" y="36" text-anchor="middle" fill="#faf089" font-size="7.5" font-weight="600">ст. 217</text>
          <text x="52" y="88" text-anchor="middle" fill="#8fa3b8" font-size="7">0–2 ч</text>
          <text x="148" y="88" text-anchor="middle" fill="#8fa3b8" font-size="7">свидание</text>
          <text x="244" y="88" text-anchor="middle" fill="#8fa3b8" font-size="7">решение</text>
          <text x="340" y="88" text-anchor="middle" fill="#8fa3b8" font-size="7">ст. 91</text>
          <text x="468" y="88" text-anchor="middle" fill="#8fa3b8" font-size="7">подготовка</text>
        </svg>
        <div class="l24-boris-ug-def__nums">
          <div class="l24-boris-ug-def__num l24-boris-ug-def__num--wide">
            <span class="l24-boris-ug-def__num-label">Проверка сообщения · ст. 144 УПК</span>
            <span class="l24-boris-ug-def__num-value">3 → 10 → 30 суток</span>
          </div>
          <div class="l24-boris-ug-def__num">
            <span class="l24-boris-ug-def__num-label">Задержание</span>
            <span class="l24-boris-ug-def__num-value">до 48 ч</span>
          </div>
          <div class="l24-boris-ug-def__num">
            <span class="l24-boris-ug-def__num-label">Допрос задержанного</span>
            <span class="l24-boris-ug-def__num-value">24 ч</span>
          </div>
          <div class="l24-boris-ug-def__num">
            <span class="l24-boris-ug-def__num-label">Следствие · ст. 162</span>
            <span class="l24-boris-ug-def__num-value">2 месяца</span>
          </div>
          <div class="l24-boris-ug-def__num">
            <span class="l24-boris-ug-def__num-label">Жалоба / ходатайство</span>
            <span class="l24-boris-ug-def__num-value">3 / 10 сут.</span>
          </div>
          <div class="l24-boris-ug-def__num">
            <span class="l24-boris-ug-def__num-label">Дознание · ст. 223</span>
            <span class="l24-boris-ug-def__num-value">30 суток</span>
          </div>
        </div>
        <ol class="l24-boris-ug-def__hours">
          <li class="l24-boris-ug-def__hour">
            <strong>0–2 ч</strong>
            Ордер адвоката; не давать объяснений без защитника; ФИО должностных, № КРСП/дела.
          </li>
          <li class="l24-boris-ug-def__hour">
            <strong>До 24 ч</strong>
            При задержании — свидание с адвокатом; не подписывать незнакомые бумаги (ст. 91, ч. 2 ст. 46).
          </li>
          <li class="l24-boris-ug-def__hour">
            <strong>3 суток</strong>
            Решение по ст. 144; при затягивании — жалоба на незаконное продление (гл. 16).
          </li>
          <li class="l24-boris-ug-def__hour">
            <strong>При возбуждении</strong>
            Копия постановления; не «объяснять версию» без стратегии; ходатайства по мерам.
          </li>
          <li class="l24-boris-ug-def__hour">
            <strong>До ст. 216–217</strong>
            Документы по треку 2; 3–5 целевых ходатайств по слабым местам обвинения.
          </li>
        </ol>
        <ul class="l24-boris-ug-def__rights" aria-label="Ключевые права на проверке и следствии">
          <li><strong>Молчание:</strong> п. 2 ч. 4 ст. 46 / п. 3 ст. 47 — не признание вины</li>
          <li><strong>Адвокат:</strong> ч. 1.1 ст. 144, ст. 49–50; досудебно — только адвокат</li>
          <li><strong>Обыск:</strong> защитник присутствует (ч. 11 ст. 182); ст. 450.1 — тайна</li>
        </ul>
        <p class="l24-boris-ug-def__note"><em>3 / 10 / 30</em> — продления проверки только с конкретными фактами в постановлении. <em>2 месяца</em> — базовый срок следствия (+ до 3 / 12 / далее по ст. 162). По ряду статей УК задержание — до <em>72 ч</em>.</p>
      </div>
    </div>

    <div class="l24-boris-ug-def__foot" aria-label="Два трека защиты">
      <span class="l24-boris-ug-def__tag l24-boris-ug-def__tag--t1">Трек 1: статус · адвокат · молчание · жалобы</span>
      <span class="l24-boris-ug-def__tag l24-boris-ug-def__tag--t2">Трек 2: факты документами · ст. 217 · ст. 75</span>
      <span class="l24-boris-ug-def__tag l24-boris-ug-def__tag--law">Не A7: без таблиц составов 159/177</span>
    </div>
  </div>
</section>
```

**Паспорт блока**

| Поле | Значение |
|------|----------|
| **id секции** | `l24-boris-ug-defense-stages` |
| **Якорь для Наташи** | `#l24-boris-ug-defense-stages` — вставка после H2 «Два трека защиты и чеклист первых 72 часов» (маркер `<!-- BORIS_ANCHOR -->` в теле лонгрида) |
| **Класс корня** | `l24-boris-ug-def` |
| **Режим** | Контраст к светлому hero Алины: тёмный inset, янтарный/бирюзовый акцент UG |
| **Техника** | Только inline `<style>` + SVG; без canvas и script |
| **Цифры research** | **3 / 10 / 30 суток** проверка (ч. 1, 3 ст. 144); **48 ч** задержание (ст. 91); **24 ч** допрос задержанного; **2 месяца** следствие (ст. 162); **30 суток** дознание; жалоба **3** / ходатайство **10** суток (гл. 16); чеклист **72 часа** |

**Чеклист отличий от hero Алины**

- [x] Не первый экран — блок в теле статьи после 1–2 секций
- [x] Другой `id` (не hero canvas id Алины)
- [x] Тёмная сцена vs светлый hero
- [x] Сплит: развилка проверка / подозреваемый / суд + таймлайн 72 ч и сроки ст. 144
- [x] Static SVG/CSS only
- [x] Два трека в футере блока (процесс vs факты)
