=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**Тема:** A5 / ARB — арбитражный спор с кредитором  
**Режим:** контраст к светлому hero Алины (тёмный inset в теле статьи)  
**Техника:** static SVG + inline CSS — без `<canvas>` и `<script>`

```html
<section id="l24-boris-arb-kreditor-track" class="l24-boris-arb-kred" aria-label="Арбитражный спор с кредитором: развилка треков и первые 14 дней защиты">
<style>
.l24-boris-arb-kred {
  --arb-navy: #0c1f33;
  --arb-navy-soft: #152a45;
  --arb-gold: #d4a853;
  --arb-mint: #5eead4;
  --arb-accent: #f56565;
  --arb-blue: #63b3ed;
  --arb-ink: #e2e8f0;
  --arb-muted: #94a3b8;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-arb-kred__shell {
  background: linear-gradient(148deg, var(--arb-navy) 0%, #122640 52%, var(--arb-navy-soft) 100%);
  border: 1px solid rgba(212, 168, 83, 0.28);
  border-radius: 14px;
  padding: 32px 28px 28px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06), 0 20px 52px rgba(12, 31, 51, 0.35);
  color: var(--arb-ink);
}
.l24-boris-arb-kred__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--arb-gold);
}
.l24-boris-arb-kred__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-arb-kred__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--arb-muted);
  max-width: 68ch;
}
.l24-boris-arb-kred__lead strong { color: #fff; }
.l24-boris-arb-kred__split {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-arb-kred__panel {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-arb-kred__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--arb-gold);
}
.l24-boris-arb-kred__fork-svg,
.l24-boris-arb-kred__timeline-svg {
  display: block;
  width: 100%;
  height: auto;
}
.l24-boris-arb-kred__fork-svg { max-height: 200px; margin-bottom: 12px; }
.l24-boris-arb-kred__timeline-svg { max-height: 150px; }
.l24-boris-arb-kred__tracks {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-arb-kred__track {
  margin: 0;
  padding: 10px 8px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.22);
  border-top: 3px solid var(--arb-blue);
  font-size: 0.72rem;
  line-height: 1.38;
}
.l24-boris-arb-kred__track:nth-child(2) { border-top-color: var(--arb-mint); }
.l24-boris-arb-kred__track:nth-child(3) { border-top-color: var(--arb-accent); }
.l24-boris-arb-kred__track strong {
  display: block;
  color: #fff;
  font-size: 0.78rem;
  margin-bottom: 4px;
}
.l24-boris-arb-kred__days {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  margin: 14px 0 0;
  padding: 0;
  list-style: none;
}
.l24-boris-arb-kred__day {
  margin: 0;
  padding: 10px 7px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.2);
  border-left: 3px solid var(--arb-gold);
  font-size: 0.7rem;
  line-height: 1.35;
}
.l24-boris-arb-kred__day:nth-child(2) { border-left-color: var(--arb-blue); }
.l24-boris-arb-kred__day:nth-child(3) { border-left-color: var(--arb-mint); }
.l24-boris-arb-kred__day:nth-child(4) { border-left-color: var(--arb-accent); }
.l24-boris-arb-kred__day strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 3px;
}
.l24-boris-arb-kred__nums {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin: 0 0 12px;
}
.l24-boris-arb-kred__num {
  padding: 12px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.24);
  border: 1px solid rgba(255, 255, 255, 0.08);
}
.l24-boris-arb-kred__num--wide {
  grid-column: 1 / -1;
  border-color: rgba(212, 168, 83, 0.35);
  background: rgba(212, 168, 83, 0.08);
}
.l24-boris-arb-kred__num-label {
  display: block;
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--arb-muted);
  margin-bottom: 4px;
}
.l24-boris-arb-kred__num-value {
  font-size: 1.05rem;
  font-weight: 800;
  color: #fff;
  line-height: 1.2;
}
.l24-boris-arb-kred__note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--arb-muted);
}
.l24-boris-arb-kred__note em {
  font-style: normal;
  color: var(--arb-mint);
  font-weight: 600;
}
.l24-boris-arb-kred__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-arb-kred__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
  color: var(--arb-ink);
}
.l24-boris-arb-kred__tag--a { border: 1px solid var(--arb-blue); color: #bee3f8; }
.l24-boris-arb-kred__tag--b { border: 1px solid var(--arb-accent); color: #feb2b2; }
.l24-boris-arb-kred__tag--c { border: 1px solid var(--arb-gold); color: #faf089; }
@media (max-width: 900px) {
  .l24-boris-arb-kred__split { grid-template-columns: 1fr; }
  .l24-boris-arb-kred__tracks { grid-template-columns: 1fr; }
  .l24-boris-arb-kred__days { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 520px) {
  .l24-boris-arb-kred__days { grid-template-columns: 1fr; }
  .l24-boris-arb-kred__nums { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-arb-kred__shell">
    <p class="l24-boris-arb-kred__eyebrow">АПК · 127-ФЗ · ст. 131 / 196 / 61 · 2025–2026</p>
    <h3 class="l24-boris-arb-kred__title">Иск кредитора → три трека и 14 дней: не «15 дней по закону»</h3>
    <p class="l24-boris-arb-kred__lead">Слева — <strong>развилка</strong>: государственный арбитражный суд, <strong>третейский</strong> (при действующей оговорке) или <strong>банкротное дело</strong>. Справа — <strong>первые 14 дней</strong> после получения иска: срок отзыва берётся из <strong>определения суда</strong>, а не из мифа «15/30 дней»; параллельно — давность, обеспечение и контроль апелляции в банкротстве.</p>

    <div class="l24-boris-arb-kred__split">
      <div class="l24-boris-arb-kred__panel">
        <p class="l24-boris-arb-kred__panel-title">Развилка: куда ушёл спор</p>
        <svg class="l24-boris-arb-kred__fork-svg" viewBox="0 0 520 168" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <defs>
            <linearGradient id="arb-fork-bg" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#1e3a5f"/>
              <stop offset="100%" stop-color="#0f2744"/>
            </linearGradient>
          </defs>
          <rect width="520" height="168" rx="8" fill="url(#arb-fork-bg)" opacity="0.5"/>
          <text x="260" y="22" text-anchor="middle" fill="#d4a853" font-size="9" font-weight="700" letter-spacing="0.12em">ИСК / ТРЕБОВАНИЕ КРЕДИТОРА</text>
          <rect x="200" y="30" width="120" height="28" rx="6" fill="#2d3748" stroke="#d4a853" stroke-width="1.2"/>
          <text x="260" y="49" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">Ответчик</text>
          <path d="M260 58 L260 72" stroke="#718096" stroke-width="1.5"/>
          <path d="M260 72 L80 100" stroke="#63b3ed" stroke-width="1.5" fill="none"/>
          <path d="M260 72 L260 100" stroke="#5eead4" stroke-width="1.5" fill="none"/>
          <path d="M260 72 L440 100" stroke="#f56565" stroke-width="1.5" fill="none"/>
          <rect x="24" y="104" width="112" height="52" rx="8" fill="rgba(99,179,237,0.15)" stroke="#63b3ed" stroke-width="1.2"/>
          <text x="80" y="124" text-anchor="middle" fill="#bee3f8" font-size="9" font-weight="700">Трек A</text>
          <text x="80" y="140" text-anchor="middle" fill="#e2e8f0" font-size="8" font-weight="600">АС · иск о долге</text>
          <text x="80" y="152" text-anchor="middle" fill="#94a3b8" font-size="7">ст. 131 · 39 АПК</text>
          <rect x="204" y="104" width="112" height="52" rx="8" fill="rgba(94,234,212,0.12)" stroke="#5eead4" stroke-width="1.2"/>
          <text x="260" y="124" text-anchor="middle" fill="#99f6e4" font-size="9" font-weight="700">Оговорка</text>
          <text x="260" y="140" text-anchor="middle" fill="#e2e8f0" font-size="8" font-weight="600">Третейский суд</text>
          <text x="260" y="152" text-anchor="middle" fill="#94a3b8" font-size="7">не гос. АС</text>
          <rect x="384" y="104" width="112" height="52" rx="8" fill="rgba(245,101,101,0.12)" stroke="#f56565" stroke-width="1.2"/>
          <text x="440" y="124" text-anchor="middle" fill="#feb2b2" font-size="9" font-weight="700">Трек B/C</text>
          <text x="440" y="140" text-anchor="middle" fill="#e2e8f0" font-size="8" font-weight="600">127-ФЗ · реестр</text>
          <text x="440" y="152" text-anchor="middle" fill="#94a3b8" font-size="7">ст. 61 · 1 мес.</text>
        </svg>
        <ul class="l24-boris-arb-kred__tracks">
          <li class="l24-boris-arb-kred__track">
            <strong>Трек A — АС</strong>
            Отзыв, давность, подсудность, отмена обеспечения (ст. 93 АПК).
          </li>
          <li class="l24-boris-arb-kred__track">
            <strong>Третейский</strong>
            Проверить оговорку до отзыва; при действительности — не гос. арбитраж.
          </li>
          <li class="l24-boris-arb-kred__track">
            <strong>Трек B — банкротство</strong>
            Реестр, обособленный спор; не второй фронт по залогу вне дела.
          </li>
        </ul>
      </div>

      <div class="l24-boris-arb-kred__panel">
        <p class="l24-boris-arb-kred__panel-title">14 дней + цифры из практики</p>
        <svg class="l24-boris-arb-kred__timeline-svg" viewBox="0 0 520 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <line x1="40" y1="58" x2="480" y2="58" stroke="#4a5568" stroke-width="2" stroke-dasharray="6 4"/>
          <circle cx="56" cy="58" r="14" fill="#d4a853"/><text x="56" y="63" text-anchor="middle" fill="#1a202c" font-size="9" font-weight="800">0</text>
          <circle cx="168" cy="58" r="14" fill="#63b3ed"/><text x="168" y="63" text-anchor="middle" fill="#1a202c" font-size="9" font-weight="800">3</text>
          <circle cx="280" cy="58" r="14" fill="#5eead4"/><text x="280" y="63" text-anchor="middle" fill="#1a202c" font-size="9" font-weight="800">7</text>
          <circle cx="392" cy="58" r="14" fill="#ed8936"/><text x="392" y="63" text-anchor="middle" fill="#1a202c" font-size="9" font-weight="800">10</text>
          <circle cx="464" cy="58" r="14" fill="#f56565"/><text x="464" y="63" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">14</text>
          <text x="56" y="38" text-anchor="middle" fill="#d4a853" font-size="8" font-weight="600">иск получен</text>
          <text x="168" y="38" text-anchor="middle" fill="#bee3f8" font-size="8" font-weight="600">оговорка</text>
          <text x="280" y="38" text-anchor="middle" fill="#99f6e4" font-size="8" font-weight="600">определение</text>
          <text x="392" y="38" text-anchor="middle" fill="#faf089" font-size="8" font-weight="600">отзыв</text>
          <text x="464" y="38" text-anchor="middle" fill="#feb2b2" font-size="8" font-weight="600">заседание</text>
          <text x="56" y="92" text-anchor="middle" fill="#94a3b8" font-size="7">ст. 37 АПК</text>
          <text x="280" y="92" text-anchor="middle" fill="#94a3b8" font-size="7">срок ст. 131</text>
          <text x="464" y="92" text-anchor="middle" fill="#94a3b8" font-size="7">до начала</text>
        </svg>
        <ol class="l24-boris-arb-kred__days">
          <li class="l24-boris-arb-kred__day">
            <strong>День 0–1</strong>
            Определение о принятии: выписать срок отзыва из акта, не из «15 дней».
          </li>
          <li class="l24-boris-arb-kred__day">
            <strong>День 2–4</strong>
            Договор: третейский / договорная подсудность (ст. 37, 39 АПК).
          </li>
          <li class="l24-boris-arb-kred__day">
            <strong>День 5–9</strong>
            Заявление о давности (ст. 199 ГК): 3 года + 10 лет предел.
          </li>
          <li class="l24-boris-arb-kred__day">
            <strong>День 10–14</strong>
            Отзыв по каждому доводу; отмена обеспечения; зачёт / встречный иск.
          </li>
        </ol>
        <div class="l24-boris-arb-kred__nums" style="margin-top:16px">
          <div class="l24-boris-arb-kred__num l24-boris-arb-kred__num--wide">
            <span class="l24-boris-arb-kred__num-label">Отзыв (ст. 131 АПК)</span>
            <span class="l24-boris-arb-kred__num-value">Срок из определения суда</span>
          </div>
          <div class="l24-boris-arb-kred__num">
            <span class="l24-boris-arb-kred__num-label">Исковая давность</span>
            <span class="l24-boris-arb-kred__num-value">3 года</span>
          </div>
          <div class="l24-boris-arb-kred__num">
            <span class="l24-boris-arb-kred__num-label">Предельный срок</span>
            <span class="l24-boris-arb-kred__num-value">10 лет</span>
          </div>
          <div class="l24-boris-arb-kred__num">
            <span class="l24-boris-arb-kred__num-label">Банкротство · обособленный спор</span>
            <span class="l24-boris-arb-kred__num-value">1 месяц</span>
          </div>
          <div class="l24-boris-arb-kred__num">
            <span class="l24-boris-arb-kred__num-label">ст. 61 127-ФЗ</span>
            <span class="l24-boris-arb-kred__num-value">апелляция</span>
          </div>
        </div>
        <p class="l24-boris-arb-kred__note"><em>10 лет</em> — с даты сделки при оспаривании в банкротстве (ВС 04.07.2025 № 307-ЭС14-7082). <em>3 года</em> — только по заявлению стороны (ст. 199 ГК).</p>
      </div>
    </div>

    <div class="l24-boris-arb-kred__foot" aria-label="Треки защиты ответчика">
      <span class="l24-boris-arb-kred__tag l24-boris-arb-kred__tag--a">Трек A: отзыв + давность + подсудность</span>
      <span class="l24-boris-arb-kred__tag l24-boris-arb-kred__tag--b">Трек B: реестр · 1 мес. апелляция</span>
      <span class="l24-boris-arb-kred__tag l24-boris-arb-kred__tag--c">Трек C: иск + угроза банкротства — единая линия</span>
    </div>
  </div>
</section>
```

**Паспорт блока**

| Поле | Значение |
|------|----------|
| **id секции** | `l24-boris-arb-kreditor-track` |
| **Якорь для Наташи** | `#l24-boris-arb-kreditor-track` — вставка после H2 «Три трека защиты» (маркер `<!-- BORIS_ANCHOR -->` в теле лонгрида) |
| **Класс корня** | `l24-boris-arb-kred` |
| **Режим** | Контраст к светлому hero Алины: тёмный inset, золотой акцент |
| **Техника** | Только inline `<style>` + SVG; без canvas и script |
| **Цифры research** | Отзыв — из определения суда (ст. 131 АПК); **3 года** давность; **10 лет** предел; **1 месяц** апелляция в банкротстве (ст. 61 127-ФЗ); чеклист **14 дней** |

**Чеклист отличий от hero Алины**

- [x] Не первый экран — блок в теле статьи после 1–2 секций
- [x] Другой `id` (не hero canvas id Алины)
- [x] Тёмная сцена vs светлый hero
- [x] Сплит: развилка АС / третейский / банкротство + таймлайн 14 дней
- [x] Static SVG/CSS only
