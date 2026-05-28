=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**Slug:** arbitrazhnyj-upravlyayushchij-osparivanie-sdelok  
**Режим:** контраст к hero Алины (светлый ARB-экран → тёмный редакционный блок в теле); та же тема — банкротство, арбитражный управляющий, оспаривание сделок.

**Вставка для Наташи:** заменяет маркер `<!-- BORIS_ANCHOR -->` сразу после markdown-таблицы «дорожная карта сроков» в H2 «Сроки оспаривания и исковая давность», **перед** H3 «Срок оспаривания сделок арбитражным управляющим». Главный CTA Артура (сроки) — **сразу после** закрывающего `</section>` Бориса, не внутри блока.

**Техника:** только inline `<style>` + static SVG; **без** `<canvas>`, **без** `<script>`.

```html
<section id="l24-boris-ospar-sroki-a11" class="l24-boris-ospar-a11" aria-label="Оспаривание сделок: look-back и исковая давность — два часа">
<style>
.l24-boris-ospar-a11 {
  --ospar-navy: #0c1f33;
  --ospar-navy-soft: #152a45;
  --ospar-gold: #d4a853;
  --ospar-blue: #63b3ed;
  --ospar-mint: #5eead4;
  --ospar-accent: #fc8181;
  --ospar-warn: #f6ad55;
  --ospar-muted: #a0aec0;
  margin: 48px 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-ospar-a11__shell {
  background: linear-gradient(148deg, var(--ospar-navy) 0%, #122640 50%, var(--ospar-navy-soft) 100%);
  border: 1px solid rgba(212, 168, 83, 0.28);
  border-radius: 14px;
  padding: 32px 28px 28px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06), 0 20px 52px rgba(12, 31, 51, 0.35);
  color: #e2e8f0;
}
.l24-boris-ospar-a11__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ospar-gold);
}
.l24-boris-ospar-a11__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-ospar-a11__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--ospar-muted);
  max-width: 72ch;
}
.l24-boris-ospar-a11__lead strong { color: #fff; }
.l24-boris-ospar-a11__split {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-ospar-a11__panel {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-ospar-a11__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--ospar-gold);
}
.l24-boris-ospar-a11__clocks-svg,
.l24-boris-ospar-a11__matrix-svg {
  display: block;
  width: 100%;
  height: auto;
}
.l24-boris-ospar-a11__clocks-svg { max-height: 200px; margin-bottom: 14px; }
.l24-boris-ospar-a11__matrix-svg { max-height: 72px; margin-bottom: 12px; }
.l24-boris-ospar-a11__lookback {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  margin: 0 0 12px;
  padding: 0;
  list-style: none;
}
.l24-boris-ospar-a11__lb {
  margin: 0;
  padding: 10px 8px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.22);
  border-top: 3px solid var(--ospar-blue);
  font-size: 0.74rem;
  line-height: 1.35;
  text-align: center;
}
.l24-boris-ospar-a11__lb:nth-child(2) { border-top-color: var(--ospar-warn); }
.l24-boris-ospar-a11__lb:nth-child(3) { border-top-color: var(--ospar-mint); }
.l24-boris-ospar-a11__lb:nth-child(4) { border-top-color: var(--ospar-accent); }
.l24-boris-ospar-a11__lb strong {
  display: block;
  color: #fff;
  font-size: 0.95rem;
  margin-bottom: 2px;
}
.l24-boris-ospar-a11__lb span {
  display: block;
  font-size: 0.68rem;
  color: var(--ospar-muted);
}
.l24-boris-ospar-a11__t0 {
  margin: 0;
  padding: 10px 12px;
  border-radius: 8px;
  background: rgba(212, 168, 83, 0.12);
  border: 1px dashed rgba(212, 168, 83, 0.45);
  font-size: 0.76rem;
  line-height: 1.45;
  color: #faf089;
}
.l24-boris-ospar-a11__t0 em {
  font-style: normal;
  font-weight: 700;
  color: #fff;
}
.l24-boris-ospar-a11__matrix {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 0 0 12px;
}
.l24-boris-ospar-a11__row {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(72px, 0.55fr) minmax(72px, 0.55fr) minmax(0, 1fr);
  gap: 8px;
  align-items: start;
  padding: 10px 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.22);
  border-left: 3px solid var(--ospar-blue);
  font-size: 0.74rem;
  line-height: 1.4;
}
.l24-boris-ospar-a11__row--62 { border-left-color: var(--ospar-accent); }
.l24-boris-ospar-a11__row--613 { border-left-color: var(--ospar-warn); }
.l24-boris-ospar-a11__row--gk { border-left-color: var(--ospar-mint); }
.l24-boris-ospar-a11__row--10 { border-left-color: var(--ospar-muted); }
.l24-boris-ospar-a11__row-base {
  font-weight: 600;
  color: #fff;
}
.l24-boris-ospar-a11__row-base small {
  display: block;
  font-weight: 400;
  color: var(--ospar-muted);
  font-size: 0.68rem;
  margin-top: 2px;
}
.l24-boris-ospar-a11__row-lb,
.l24-boris-ospar-a11__row-du {
  font-weight: 800;
  color: #fff;
  font-size: 0.82rem;
}
.l24-boris-ospar-a11__row-def {
  color: #cbd5e0;
  font-size: 0.7rem;
}
.l24-boris-ospar-a11__row-def em {
  font-style: normal;
  color: var(--ospar-mint);
  font-weight: 600;
}
.l24-boris-ospar-a11__head {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(72px, 0.55fr) minmax(72px, 0.55fr) minmax(0, 1fr);
  gap: 8px;
  padding: 0 10px 6px;
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--ospar-muted);
  font-weight: 700;
}
.l24-boris-ospar-a11__au-year {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 0 0 12px;
  padding: 14px 14px;
  border-radius: 10px;
  background: rgba(252, 129, 129, 0.12);
  border: 1px solid rgba(252, 129, 129, 0.35);
}
.l24-boris-ospar-a11__au-year-value {
  flex-shrink: 0;
  font-size: 1.65rem;
  font-weight: 800;
  color: #fff;
  line-height: 1;
}
.l24-boris-ospar-a11__au-year-text {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--ospar-muted);
}
.l24-boris-ospar-a11__au-year-text strong { color: #fff; }
.l24-boris-ospar-a11__note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--ospar-muted);
}
.l24-boris-ospar-a11__note em {
  font-style: normal;
  color: var(--ospar-mint);
  font-weight: 600;
}
.l24-boris-ospar-a11__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-ospar-a11__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
}
.l24-boris-ospar-a11__tag--lb { border: 1px solid var(--ospar-blue); color: #bee3f8; }
.l24-boris-ospar-a11__tag--du { border: 1px solid var(--ospar-accent); color: #fed7d7; }
.l24-boris-ospar-a11__tag--vs { border: 1px solid var(--ospar-gold); color: #faf089; }
.l24-boris-ospar-a11__tag--def { border: 1px solid var(--ospar-mint); color: #b2f5ea; }
.l24-boris-ospar-a11__caption {
  margin: 12px 0 0;
  font-size: 0.7rem;
  color: var(--ospar-muted);
  line-height: 1.4;
}
@media (max-width: 900px) {
  .l24-boris-ospar-a11__split { grid-template-columns: 1fr; }
  .l24-boris-ospar-a11__lookback { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 520px) {
  .l24-boris-ospar-a11__row,
  .l24-boris-ospar-a11__head {
    grid-template-columns: 1fr;
  }
  .l24-boris-ospar-a11__head { display: none; }
  .l24-boris-ospar-a11__row-lb::before { content: "Look-back: "; color: var(--ospar-muted); font-weight: 400; }
  .l24-boris-ospar-a11__row-du::before { content: "Давность АУ: "; color: var(--ospar-muted); font-weight: 400; }
}
</style>

  <div class="l24-boris-ospar-a11__shell">
    <p class="l24-boris-ospar-a11__eyebrow">127-ФЗ · ст. 61.2–61.3 · 61.9 · Пленум ВАС № 63 · обзор ВС 5/2026</p>
    <h3 class="l24-boris-ospar-a11__title">Два «часа»: look-back в прошлое и год на иск управляющего</h3>
    <p class="l24-boris-ospar-a11__lead">Слева — <strong>период подозрительности</strong>: насколько далеко закон смотрит на сделки <em>до</em> принятия заявления о банкротстве (объективно, без «увидел ли АУ»). Справа — <strong>исковая давность на заявление АУ</strong>: обычно <strong>1 год</strong> с момента, когда управляющий узнал или должен был узнать об основании (ст. 61.9, п. 32 Пленума № 63). Путать «три года» look-back по п. 2 ст. 61.2 с безграничным сроком на иск — типичная ошибка должника.</p>

    <div class="l24-boris-ospar-a11__split">
      <div class="l24-boris-ospar-a11__panel">
        <p class="l24-boris-ospar-a11__panel-title">Час 1 · look-back (до T₀)</p>
        <svg class="l24-boris-ospar-a11__clocks-svg" viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <defs>
            <linearGradient id="a11-boris-lb-line" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#63b3ed"/>
              <stop offset="35%" stop-color="#f6ad55"/>
              <stop offset="65%" stop-color="#5eead4"/>
              <stop offset="100%" stop-color="#fc8181"/>
            </linearGradient>
          </defs>
          <rect x="8" y="8" width="504" height="184" rx="12" fill="rgba(0,0,0,0.28)" stroke="rgba(212,168,83,0.35)" stroke-width="1"/>
          <text x="28" y="32" fill="#d4a853" font-size="9" font-weight="700">← ПРОШЛОЕ · СДЕЛКА · T₀ →</text>
          <line x1="48" y1="118" x2="472" y2="118" stroke="url(#a11-boris-lb-line)" stroke-width="5" stroke-linecap="round"/>
          <circle cx="472" cy="118" r="20" fill="#d4a853" stroke="#fff" stroke-width="2"/>
          <text x="472" y="114" text-anchor="middle" fill="#1a202c" font-size="8" font-weight="800">T₀</text>
          <text x="472" y="126" text-anchor="middle" fill="#1a202c" font-size="6.5">заявл.</text>
          <rect x="400" y="88" width="52" height="22" rx="5" fill="rgba(246,173,85,0.25)" stroke="#f6ad55"/>
          <text x="426" y="103" text-anchor="middle" fill="#faf089" font-size="7" font-weight="700">1 мес.</text>
          <rect x="318" y="88" width="72" height="22" rx="5" fill="rgba(246,173,85,0.2)" stroke="#f6ad55"/>
          <text x="354" y="103" text-anchor="middle" fill="#faf089" font-size="7" font-weight="700">6 мес.</text>
          <rect x="210" y="88" width="96" height="22" rx="5" fill="rgba(94,234,212,0.2)" stroke="#5eead4"/>
          <text x="258" y="103" text-anchor="middle" fill="#b2f5ea" font-size="7" font-weight="700">1 год · 61.2 п.1</text>
          <rect x="48" y="88" width="150" height="22" rx="5" fill="rgba(252,129,129,0.2)" stroke="#fc8181"/>
          <text x="123" y="103" text-anchor="middle" fill="#fed7d7" font-size="7" font-weight="700">3 года · 61.2 п.2</text>
          <path d="M48 118 L48 148" stroke="#63b3ed" stroke-width="1.5" stroke-dasharray="3 2"/>
          <text x="48" y="162" fill="#a0aec0" font-size="7">дальше — вне look-back</text>
          <rect x="28" y="44" width="200" height="36" rx="6" fill="rgba(99,179,237,0.12)" stroke="#63b3ed"/>
          <text x="128" y="58" text-anchor="middle" fill="#bee3f8" font-size="8" font-weight="700">ОБЪЕКТИВНО</text>
          <text x="128" y="72" text-anchor="middle" fill="#e2e8f0" font-size="7">не зависит от отчётности АУ</text>
          <rect x="292" y="44" width="200" height="36" rx="6" fill="rgba(252,129,129,0.1)" stroke="#fc8181"/>
          <text x="392" y="58" text-anchor="middle" fill="#fed7d7" font-size="8" font-weight="700">СУБЪЕКТИВНО · ЧАС 2</text>
          <text x="392" y="72" text-anchor="middle" fill="#e2e8f0" font-size="7">1 год на иск → панель справа</text>
        </svg>
        <ul class="l24-boris-ospar-a11__lookback">
          <li class="l24-boris-ospar-a11__lb">
            <strong>1 мес.</strong>
            <span>ст. 61.3</span>
          </li>
          <li class="l24-boris-ospar-a11__lb">
            <strong>6 мес.</strong>
            <span>61.3 · знал о неплатёж.</span>
          </li>
          <li class="l24-boris-ospar-a11__lb">
            <strong>1 год</strong>
            <span>61.2 п. 1</span>
          </li>
          <li class="l24-boris-ospar-a11__lb">
            <strong>3 года</strong>
            <span>61.2 п. 2</span>
          </li>
        </ul>
        <p class="l24-boris-ospar-a11__t0"><em>T₀</em> — дата принятия судом заявления о банкротстве. Сделка за пределами look-back по выбранному основанию — частый довод в отзыве (вместе с неверной квалификацией 61.2 / 61.3, п. 10 обзора ВС 5/2026).</p>
      </div>

      <div class="l24-boris-ospar-a11__panel">
        <p class="l24-boris-ospar-a11__panel-title">Час 2 · исковая давность заявления АУ</p>
        <svg class="l24-boris-ospar-a11__matrix-svg" viewBox="0 0 520 72" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <rect x="10" y="10" width="500" height="52" rx="10" fill="rgba(0,0,0,0.25)" stroke="rgba(252,129,129,0.35)"/>
          <text x="28" y="30" fill="#fed7d7" font-size="9" font-weight="700">СТ. 61.2 / 61.3 → как правило 1 ГОД</text>
          <text x="28" y="48" fill="#a0aec0" font-size="8">с момента, когда АУ узнал / должен был узнать · ст. 199 ГК — заявить о пропуске</text>
          <circle cx="468" cy="36" r="18" fill="rgba(252,129,129,0.35)" stroke="#fc8181" stroke-width="1.5"/>
          <text x="468" y="40" text-anchor="middle" fill="#fff" font-size="11" font-weight="800">1г</text>
        </svg>
        <div class="l24-boris-ospar-a11__au-year">
          <span class="l24-boris-ospar-a11__au-year-value" aria-hidden="true">1 год</span>
          <p class="l24-boris-ospar-a11__au-year-text"><strong>На иск управляющего</strong> по ст. 61.2 и 61.3 (п. 2 ст. 181 ГК, п. 32 Пленума № 63). Течёт с утверждения АУ и фактов, когда ему стало известно об основании — доказывайте в отзыве дату документов и запросов.</p>
        </div>
        <div class="l24-boris-ospar-a11__head" aria-hidden="true">
          <span>Основание</span>
          <span>Look-back</span>
          <span>Иск АУ</span>
          <span>Защита в отзыве</span>
        </div>
        <div class="l24-boris-ospar-a11__matrix" role="table" aria-label="Сроки look-back и давность по основаниям">
          <div class="l24-boris-ospar-a11__row" role="row">
            <span class="l24-boris-ospar-a11__row-base" role="cell">ст. 61.2 п. 1<small>неравноценность</small></span>
            <span class="l24-boris-ospar-a11__row-lb" role="cell">1 год</span>
            <span class="l24-boris-ospar-a11__row-du" role="cell">1 год</span>
            <span class="l24-boris-ospar-a11__row-def" role="cell"><em>оценка</em>, 61.4, обычная деятельность</span>
          </div>
          <div class="l24-boris-ospar-a11__row l24-boris-ospar-a11__row--62" role="row">
            <span class="l24-boris-ospar-a11__row-base" role="cell">ст. 61.2 п. 2<small>вред кредиторам</small></span>
            <span class="l24-boris-ospar-a11__row-lb" role="cell">3 года</span>
            <span class="l24-boris-ospar-a11__row-du" role="cell">1 год</span>
            <span class="l24-boris-ospar-a11__row-def" role="cell"><em>оплата</em>, цель, нет вреда</span>
          </div>
          <div class="l24-boris-ospar-a11__row l24-boris-ospar-a11__row--613" role="row">
            <span class="l24-boris-ospar-a11__row-base" role="cell">ст. 61.3<small>предпочтение</small></span>
            <span class="l24-boris-ospar-a11__row-lb" role="cell">1 / 6 мес.</span>
            <span class="l24-boris-ospar-a11__row-du" role="cell">1 год</span>
            <span class="l24-boris-ospar-a11__row-def" role="cell"><em>нет предпочтения</em>, общий порядок</span>
          </div>
          <div class="l24-boris-ospar-a11__row l24-boris-ospar-a11__row--gk" role="row">
            <span class="l24-boris-ospar-a11__row-base" role="cell">ст. 10, 168, 170 ГК<small>общие основания</small></span>
            <span class="l24-boris-ospar-a11__row-lb" role="cell">иные</span>
            <span class="l24-boris-ospar-a11__row-du" role="cell">≈ 3 года</span>
            <span class="l24-boris-ospar-a11__row-def" role="cell"><em>не подменять</em> 61.2/61.3</span>
          </div>
          <div class="l24-boris-ospar-a11__row l24-boris-ospar-a11__row--10" role="row">
            <span class="l24-boris-ospar-a11__row-base" role="cell">ст. 196, 200 ГК<small>общий предел</small></span>
            <span class="l24-boris-ospar-a11__row-lb" role="cell">—</span>
            <span class="l24-boris-ospar-a11__row-du" role="cell">10 лет</span>
            <span class="l24-boris-ospar-a11__row-def" role="cell"><em>пресекательный</em> срок</span>
          </div>
        </div>
        <p class="l24-boris-ospar-a11__note"><em>«Прошёл год — сделка в безопасности»</em> — миф: look-back до 3 лет + общие основания ГК. При пропуске года АУ — ходатайство по ст. 199 ГК; при явных основаниях кредиторы вправе требовать убытков с управляющего (ст. 20.3 ЗоБ).</p>
      </div>
    </div>

    <div class="l24-boris-ospar-a11__foot" aria-label="Связка двух часов">
      <span class="l24-boris-ospar-a11__tag l24-boris-ospar-a11__tag--lb">Look-back · объективен</span>
      <span class="l24-boris-ospar-a11__tag l24-boris-ospar-a11__tag--du">Давность АУ · 1 год (61.2/61.3)</span>
      <span class="l24-boris-ospar-a11__tag l24-boris-ospar-a11__tag--vs">«3 года» ≠ срок на иск</span>
      <span class="l24-boris-ospar-a11__tag l24-boris-ospar-a11__tag--def">Отзыв: T₀ + дата знания АУ</span>
    </div>
    <p class="l24-boris-ospar-a11__caption">Визуальная «дорожная карта» к таблице в тексте — для директора ООО/ИП и контрагента; конкретика по датам — в материалах дела.</p>
  </div>
</section>
```

**Паспорт блока**

| Поле | Значение |
|------|----------|
| `id` секции | `#l24-boris-ospar-sroki-a11` |
| Класс корня | `l24-boris-ospar-a11` |
| Якорь вставки | `<!-- BORIS_ANCHOR -->` (замена, не дублировать комментарий в HTML) |
| Композиция | сплит 2 колонки: SVG-шкала look-back + CSS-матрица оснований |
| Hero Алины | не дублировать: без fullscreen, без тех же `id`/`canvas` |
| MCP | без `<script>` и `<canvas>` |

### Чеклист отличий от hero Алины

- [x] Не hero: блок в теле лонгрида (`margin: 48px 0`), не `min-height: 100vh`
- [x] Контраст: тёмный градиент ARB (navy + gold), hero — светлый ARB-фон
- [x] Тема продолжения: банкротство / АУ / ст. 61.2–61.3 — углубление **сроков**, не «кто оспаривает»
- [x] Редакционная обвязка: eyebrow, lead, матрица, подпись, теги внизу
- [x] Static SVG + inline CSS только
- [x] Уникальные префиксы классов и `id` SVG-градиентов (`a11-boris-*`)
- [x] Якорь Артура: вставка на месте `BORIS_ANCHOR`; CTA — после секции
