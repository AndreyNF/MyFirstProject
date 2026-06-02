=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** `fns-strahovye-vznosy-vtoraya-ochered-bankrotstvo-vs`  
**Якорь:** `l24-boris-fns-vznosy-queue`  
**Размещение:** сразу после H2 «Вторая и третья очередь реестра требований кредиторов» (перед H3 «Абз. 3 п. 4 ст. 134…» или после абзаца про кредиторов 3-й очереди).  
**Режим:** продолжение темы hero — не новостной кадр, а **карта очередей и сумм** по делу Ташлинского (до/после ВС 06.05.2026).  
**Legis24 MCP-only:** static SVG + inline CSS, без `<canvas>` и `<script>`.

```html
<section id="l24-boris-fns-vznosy-queue" class="l24-boris-fns-vznosy" aria-label="Страховые взносы ФНС: перенос из 3-й во 2-ю очередь реестра — схема и суммы дела А47-12711/2023">
<style>
.l24-boris-fns-vznosy {
  --fns-navy: #0c1f33;
  --fns-navy-soft: #152a45;
  --fns-gold: #d4a853;
  --fns-blue: #63b3ed;
  --fns-mint: #5eead4;
  --fns-rose: #fc8181;
  --fns-amber: #f6ad55;
  --fns-muted: #a0aec0;
  margin: 48px 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-fns-vznosy__shell {
  background: linear-gradient(148deg, var(--fns-navy) 0%, #122640 52%, var(--fns-navy-soft) 100%);
  border: 1px solid rgba(212, 168, 83, 0.28);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06), 0 20px 52px rgba(12, 31, 51, 0.35);
}
.l24-boris-fns-vznosy__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--fns-gold);
}
.l24-boris-fns-vznosy__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-fns-vznosy__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--fns-muted);
  max-width: 72ch;
}
.l24-boris-fns-vznosy__lead strong { color: #fff; }
.l24-boris-fns-vznosy__split {
  display: grid;
  grid-template-columns: minmax(0, 1.12fr) minmax(0, 0.98fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-fns-vznosy__panel {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-fns-vznosy__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--fns-gold);
}
.l24-boris-fns-vznosy__queue-svg,
.l24-boris-fns-vznosy__shift-svg {
  display: block;
  width: 100%;
  height: auto;
}
.l24-boris-fns-vznosy__queue-svg { max-height: 220px; margin-bottom: 12px; }
.l24-boris-fns-vznosy__shift-svg { max-height: 200px; margin-bottom: 14px; }
.l24-boris-fns-vznosy__lanes {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-fns-vznosy__lane {
  margin: 0;
  padding: 10px 8px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.22);
  border-top: 3px solid var(--fns-blue);
  font-size: 0.74rem;
  line-height: 1.4;
  color: #cbd5e0;
}
.l24-boris-fns-vznosy__lane:nth-child(2) { border-top-color: var(--fns-gold); }
.l24-boris-fns-vznosy__lane:nth-child(3) { border-top-color: var(--fns-rose); }
.l24-boris-fns-vznosy__lane strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-fns-vznosy__amounts {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin: 0 0 12px;
}
.l24-boris-fns-vznosy__amount {
  padding: 12px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.24);
  border: 1px solid rgba(255, 255, 255, 0.08);
}
.l24-boris-fns-vznosy__amount--vs {
  grid-column: 1 / -1;
  border-color: rgba(94, 234, 212, 0.45);
  background: rgba(94, 234, 212, 0.1);
}
.l24-boris-fns-vznosy__amount-label {
  display: block;
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--fns-muted);
  margin-bottom: 4px;
}
.l24-boris-fns-vznosy__amount-value {
  font-size: 1.02rem;
  font-weight: 800;
  color: #fff;
  line-height: 1.2;
}
.l24-boris-fns-vznosy__amount-note {
  display: block;
  margin-top: 4px;
  font-size: 0.7rem;
  color: var(--fns-muted);
  line-height: 1.35;
}
.l24-boris-fns-vznosy__share {
  margin: 0;
  padding: 12px 14px;
  border-radius: 8px;
  border: 1px dashed rgba(212, 168, 83, 0.4);
  background: rgba(212, 168, 83, 0.08);
  font-size: 0.8rem;
  line-height: 1.45;
  color: #e2e8f0;
}
.l24-boris-fns-vznosy__share em {
  font-style: normal;
  color: var(--fns-gold);
  font-weight: 700;
}
.l24-boris-fns-vznosy__caption {
  margin: 18px 0 0;
  padding-top: 14px;
  border-top: 1px dashed rgba(212, 168, 83, 0.35);
  font-size: 0.82rem;
  line-height: 1.5;
  color: var(--fns-muted);
}
.l24-boris-fns-vznosy__caption strong { color: #fff; font-weight: 600; }
.l24-boris-fns-vznosy__roles {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 14px;
}
.l24-boris-fns-vznosy__role {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
}
.l24-boris-fns-vznosy__role--fns { border: 1px solid var(--fns-amber); color: #fbd38d; }
.l24-boris-fns-vznosy__role--cred { border: 1px solid var(--fns-rose); color: #fed7d7; }
.l24-boris-fns-vznosy__role--ku { border: 1px solid var(--fns-mint); color: #b2f5ea; }
@media (max-width: 900px) {
  .l24-boris-fns-vznosy__split { grid-template-columns: 1fr; }
  .l24-boris-fns-vznosy__lanes { grid-template-columns: 1fr; }
}
@media (max-width: 520px) {
  .l24-boris-fns-vznosy__amounts { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-fns-vznosy__shell">
    <p class="l24-boris-fns-vznosy__eyebrow">абз. 3 п. 4 ст. 134 · единый тариф с 01.01.2023 · дело № А47-12711/2023</p>
    <h3 class="l24-boris-fns-vznosy__title">Из 3-й во 2-ю: что «переехало» в реестре и сколько осталось у кредиторов 3-й очереди</h3>
    <p class="l24-boris-fns-vznosy__lead">Слева — <strong>очереди реестра требований кредиторов</strong>: до определения ВС от <strong>6 мая 2026 года</strong> ОМС и соцстрахование стояли в <strong>третьей очереди</strong> (инерция Обзора № 3/2017). Справа — суммы по заявлению УФНС: <strong>981 628,14 руб.</strong> перенесены во <strong>вторую очередь</strong> без нового рассмотрения по существу долга.</p>

    <div class="l24-boris-fns-vznosy__split">
      <div class="l24-boris-fns-vznosy__panel">
        <p class="l24-boris-fns-vznosy__panel-title">Карта очередей реестра</p>
        <svg class="l24-boris-fns-vznosy__queue-svg" viewBox="0 0 520 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="fns-boris-queue-title fns-boris-queue-desc">
          <title id="fns-boris-queue-title">Очереди реестра: перенос взносов ОМС и соцстрахования из 3-й во 2-ю</title>
          <desc id="fns-boris-queue-desc">Три полосы очередей реестра. Из третьей очереди блок ОМС и соцстрахование 981 628 рублей переносится во вторую очередь по определению ВС.</desc>
          <defs>
            <linearGradient id="fns-boris-bg" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#1e3a5f"/>
              <stop offset="100%" stop-color="#0f2744"/>
            </linearGradient>
            <marker id="fns-boris-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0 0 L8 4 L0 8 Z" fill="#5eead4"/>
            </marker>
          </defs>
          <rect x="8" y="8" width="504" height="224" rx="12" fill="url(#fns-boris-bg)" stroke="#334155" stroke-width="1"/>

          <!-- Queue 1 -->
          <text x="28" y="32" fill="#a0aec0" font-size="9" font-weight="700">1-я очередь</text>
          <rect x="28" y="40" width="464" height="28" rx="6" fill="rgba(99,179,237,0.12)" stroke="#63b3ed" stroke-width="1"/>
          <text x="44" y="58" fill="#bee3f8" font-size="8">зарплата, выходные, авторские — без спора по взносам</text>

          <!-- Queue 2 before -->
          <text x="28" y="88" fill="#d4a853" font-size="9" font-weight="700">2-я очередь · до ВС</text>
          <rect x="28" y="96" width="300" height="36" rx="6" fill="rgba(212,168,83,0.18)" stroke="#d4a853" stroke-width="1.4"/>
          <text x="44" y="112" fill="#faf089" font-size="8" font-weight="700">ОПС (единый тариф)</text>
          <text x="44" y="126" fill="#e2e8f0" font-size="8">2 696 107,26 ₽</text>

          <!-- Queue 3 before -->
          <text x="28" y="148" fill="#fc8181" font-size="9" font-weight="700">3-я очередь · до ВС</text>
          <rect x="28" y="156" width="220" height="36" rx="6" fill="rgba(252,129,129,0.15)" stroke="#fc8181" stroke-width="1.4" stroke-dasharray="5 3"/>
          <text x="44" y="172" fill="#fed7d7" font-size="8" font-weight="700">ОМС + соцстрах</text>
          <text x="44" y="186" fill="#e2e8f0" font-size="8">981 628,14 ₽</text>

          <!-- Arrow move -->
          <path d="M260 174 C300 174 300 118 340 118" stroke="#5eead4" stroke-width="2.4" fill="none" marker-end="url(#fns-boris-arr)"/>
          <text x="278" y="152" fill="#5eead4" font-size="8" font-weight="700">ВС 06.05.2026</text>

          <!-- Queue 2 after extension -->
          <rect x="340" y="96" width="152" height="36" rx="6" fill="rgba(94,234,212,0.14)" stroke="#5eead4" stroke-width="1.6"/>
          <text x="356" y="112" fill="#b2f5ea" font-size="8" font-weight="700">+ ОМС / соц</text>
          <text x="356" y="126" fill="#fff" font-size="8">981 628,14 ₽</text>

          <!-- Queue 2 total hint -->
          <rect x="28" y="204" width="464" height="22" rx="6" fill="rgba(94,234,212,0.08)" stroke="rgba(94,234,212,0.35)" stroke-width="1"/>
          <text x="44" y="219" fill="#b2f5ea" font-size="8">После ВС: весь основной долг по единому тарифу с 2023 г. — режим 2-й очереди (абз. 3 п. 4 ст. 134)</text>

          <text x="468" y="58" text-anchor="end" fill="#a0aec0" font-size="7">налоги 102+ млн</text>
          <text x="468" y="70" text-anchor="end" fill="#a0aec0" font-size="7">остались в 3-й</text>
        </svg>
        <ul class="l24-boris-fns-vznosy__lanes">
          <li class="l24-boris-fns-vznosy__lane">
            <strong>1-я</strong>
            Выплаты работникам и приравненные требования — вне спора по взносам ФНС.
          </li>
          <li class="l24-boris-fns-vznosy__lane">
            <strong>2-я</strong>
            Зарплата + взносы на соцстрахование по перечисленным выплатам; после реформы — единый тариф целиком.
          </li>
          <li class="l24-boris-fns-vznosy__lane">
            <strong>3-я</strong>
            Конкурсные кредиторы; каждый рубль взносов во 2-й очереди сужает массу после погашения 1–2 очередей.
          </li>
        </ul>
      </div>

      <div class="l24-boris-fns-vznosy__panel">
        <p class="l24-boris-fns-vznosy__panel-title">Дело «Ташлинский»: суммы заявления УФНС</p>
        <svg class="l24-boris-fns-vznosy__shift-svg" viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <rect x="12" y="12" width="496" height="176" rx="10" fill="rgba(0,0,0,0.25)" stroke="rgba(212,168,83,0.35)" stroke-width="1"/>
          <text x="28" y="34" fill="#d4a853" font-size="9" font-weight="700">ЗАЯВЛЕНИЕ 16.10.2023 · СТРАХОВЫЕ ВЗНОСЫ 1-е полугодие 2023</text>

          <text x="28" y="58" fill="#a0aec0" font-size="8">Всего по взносам</text>
          <text x="28" y="76" fill="#fff" font-size="14" font-weight="700">3 678 236,59 ₽</text>

          <rect x="28" y="88" width="220" height="14" rx="4" fill="rgba(212,168,83,0.35)"/>
          <text x="36" y="99" fill="#1a202c" font-size="7.5" font-weight="700">2-я · ОПС 2 696 107 ₽ (73%)</text>

          <rect x="28" y="108" width="80" height="14" rx="4" fill="rgba(252,129,129,0.45)"/>
          <text x="36" y="119" fill="#1a202c" font-size="7.5" font-weight="700">3-я · 982 тыс. (27%)</text>

          <path d="M280 130 L280 88 L420 88" stroke="#5eead4" stroke-width="2" fill="none" marker-end="url(#fns-boris-arr)"/>
          <rect x="280" y="132" width="220" height="48" rx="8" fill="rgba(94,234,212,0.12)" stroke="#5eead4" stroke-width="1.4"/>
          <text x="296" y="152" fill="#b2f5ea" font-size="8" font-weight="700">Определение СКЭС ВС</text>
          <text x="296" y="168" fill="#fff" font-size="10" font-weight="700">981 628,14 ₽ → 2-я очередь</text>

          <text x="28" y="162" fill="#a0aec0" font-size="7.5">ОМС 625 006,68 + соц 356 621,46</text>
          <text x="28" y="176" fill="#a0aec0" font-size="7.5">Обзор № 3/2017 вопрос 2 — исключён</text>
        </svg>

        <div class="l24-boris-fns-vznosy__amounts">
          <div class="l24-boris-fns-vznosy__amount">
            <span class="l24-boris-fns-vznosy__amount-label">Суды до ВС · 2-я</span>
            <span class="l24-boris-fns-vznosy__amount-value">2 696 107 ₽</span>
            <span class="l24-boris-fns-vznosy__amount-note">только «пенсионная» доля</span>
          </div>
          <div class="l24-boris-fns-vznosy__amount">
            <span class="l24-boris-fns-vznosy__amount-label">Суды до ВС · 3-я</span>
            <span class="l24-boris-fns-vznosy__amount-value">981 628 ₽</span>
            <span class="l24-boris-fns-vznosy__amount-note">ОМС + соцстрахование</span>
          </div>
          <div class="l24-boris-fns-vznosy__amount l24-boris-fns-vznosy__amount--vs">
            <span class="l24-boris-fns-vznosy__amount-label">ВС 06.05.2026 · без нового рассмотрения</span>
            <span class="l24-boris-fns-vznosy__amount-value">+981 628,14 ₽ во 2-ю очередь</span>
            <span class="l24-boris-fns-vznosy__amount-note">№ 309-ЭС24-8891 (3) · п. 3 обзора № 5/2026</span>
          </div>
        </div>

        <p class="l24-boris-fns-vznosy__share"><em>~27%</em> заявленных взносов «переехало» из 3-й во 2-ю — наглядный ориентир для банков и поставщиков при оценке конкурсной массы.</p>
      </div>
    </div>

    <p class="l24-boris-fns-vznosy__caption"><strong>Редакционная подпись.</strong> Схема не заменяет расчёт по вашему делу: пени, штрафы и налоги ФНС (в Ташлинском — свыше 102 млн ₽) квалифицируются отдельно и часто остаются в 3-й очереди. Для начислений <strong>с 01.01.2023</strong> не дробите единый платёж по КБК без правового основания — опирайтесь на определения СКЭС 2025–2026 и абз. 3 п. 4 ст. 134.</p>

    <div class="l24-boris-fns-vznosy__roles" aria-label="Три роли в одном споре">
      <span class="l24-boris-fns-vznosy__role l24-boris-fns-vznosy__role--fns">ФНС: единый тариф → 2-я очередь реестра</span>
      <span class="l24-boris-fns-vznosy__role l24-boris-fns-vznosy__role--cred">Кредитор 3-й: возражения по периоду и «телу» долга</span>
      <span class="l24-boris-fns-vznosy__role l24-boris-fns-vznosy__role--ku">УК: отделить пени/штрафы от основного взноса</span>
    </div>
  </div>
</section>
```

**Чеклист отличий от hero Алины**
- [x] Не полноэкранный блок; в теле статьи после H2 про очереди реестра
- [x] Свой `id`: `l24-boris-fns-vznosy-queue` (не hero `#l24-hero-fns-vznosy-vtoraya-ochered`)
- [x] Без `<canvas>` и `<script>` — только inline CSS + SVG
- [x] Сплит-сетка «карта очередей | суммы дела», не сцена hero с определением ВС
