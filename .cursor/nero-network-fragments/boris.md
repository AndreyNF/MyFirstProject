=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** rospatent-maugli-rot-front-annulirovanie-tovarnyj-znak-2026  
**Якорь:** `#boris-maugli-tz-flow`  
**Режим:** контраст к hero Алины — светлый hero с фактами дела → тёмный jungle/slate блок маршрута в теле статьи  
**Техника:** static SVG + inline CSS · без `<canvas>` · без `<script>`

## Место вставки для Наташи

Вставить **после закрывающего абзаца H2 §2** «Дело „Маугли“ и „Рот Фронт“: фабула, доводы сторон и позиция Роспатента» (после H3 §2.2 «Почему ссылки на Киплинга и Disney не сработали») и **перед** `<h2>` §3 «Возражение против товарного знака в Роспатенте».

Якорь для Наташи: после H2 §2, id `boris-maugli-tz-flow`

## Чеклист отличий от hero Алины

| | Hero Алины | Блок Бориса |
|---|---|---|
| Позиция | первый экран | тело статьи, после H2 §2 |
| Фон | светлый (#fefefe / #f0f7ff) | тёмный jungle gradient |
| Смысл | факты: ТЗ № 162034, стороны, ст. 1483 | **маршрут** возражение → решение → СИП |
| id | `l24-hero-rospatent-maugli` (Алина) | `boris-maugli-tz-flow` |
| canvas/script | нет (MCP-only SVG) | нет |

```html
<section id="boris-maugli-tz-flow" class="l24-boris-maugli-flow" aria-label="Аннулирование ТЗ «Маугли»: маршрут возражения в Роспатенте, решение ППС и обжалование в СИП">
<style>
.l24-boris-maugli-flow {
  --mg-jungle: #0c2418;
  --mg-jungle-mid: #143528;
  --mg-jungle-soft: #1e4d38;
  --mg-leaf: #34d399;
  --mg-leaf-soft: #6ee7b7;
  --mg-gold: #fbbf24;
  --mg-gold-soft: #fde68a;
  --mg-sip: #a78bfa;
  --mg-sip-soft: #c4b5fd;
  --mg-muted: #94a3b8;
  --mg-txt: #e2e8f0;
  margin: 48px 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-maugli-flow__shell {
  background: linear-gradient(152deg, var(--mg-jungle) 0%, var(--mg-jungle-mid) 46%, #0f2a4a 100%);
  border: 1px solid rgba(52, 211, 153, 0.28);
  border-radius: 14px;
  padding: 32px 28px 24px;
  color: var(--mg-txt);
  box-shadow: 0 18px 48px rgba(12, 36, 24, 0.42);
}
.l24-boris-maugli-flow__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mg-leaf-soft);
}
.l24-boris-maugli-flow__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-maugli-flow__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--mg-muted);
  max-width: 72ch;
}
.l24-boris-maugli-flow__lead strong { color: #fff; }
.l24-boris-maugli-flow__split {
  display: grid;
  grid-template-columns: minmax(0, 1.12fr) minmax(0, 0.88fr);
  gap: 22px;
  align-items: stretch;
  margin-bottom: 20px;
}
.l24-boris-maugli-flow__panel {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-maugli-flow__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--mg-gold-soft);
}
.l24-boris-maugli-flow__route-svg {
  display: block;
  width: 100%;
  height: auto;
  margin-bottom: 14px;
}
.l24-boris-maugli-flow__stages {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-maugli-flow__stage {
  padding: 11px 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border-top: 3px solid var(--mg-leaf);
  font-size: 0.72rem;
  line-height: 1.38;
  color: var(--mg-muted);
}
.l24-boris-maugli-flow__stage:nth-child(2) { border-top-color: var(--mg-gold); }
.l24-boris-maugli-flow__stage:nth-child(3) { border-top-color: var(--mg-sip); }
.l24-boris-maugli-flow__stage strong {
  display: block;
  color: #fff;
  font-size: 0.78rem;
  margin-bottom: 4px;
}
.l24-boris-maugli-flow__caption {
  margin: 10px 0 0;
  font-size: 0.68rem;
  line-height: 1.4;
  color: rgba(148, 163, 184, 0.88);
  text-align: center;
}
.l24-boris-maugli-flow__grounds {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 0 0 12px;
}
.l24-boris-maugli-flow__ground {
  display: grid;
  grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr);
  gap: 6px 10px;
  align-items: start;
  padding: 10px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.24);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.74rem;
  line-height: 1.38;
}
.l24-boris-maugli-flow__ground--pps { border-left: 3px solid var(--mg-leaf); }
.l24-boris-maugli-flow__ground--law { border-left: 3px solid var(--mg-gold); }
.l24-boris-maugli-flow__ground--sip { border-left: 3px solid var(--mg-sip); }
.l24-boris-maugli-flow__ground-label {
  font-weight: 700;
  color: #fff;
  font-size: 0.76rem;
}
.l24-boris-maugli-flow__ground-text {
  color: var(--mg-muted);
}
.l24-boris-maugli-flow__ground-text em {
  font-style: normal;
  color: #fff;
  font-weight: 600;
}
.l24-boris-maugli-flow__vs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 0 0 10px;
}
.l24-boris-maugli-flow__vs-card {
  padding: 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.72rem;
  line-height: 1.4;
}
.l24-boris-maugli-flow__vs-card--win { border-color: rgba(52, 211, 153, 0.45); }
.l24-boris-maugli-flow__vs-card--risk { border-color: rgba(251, 191, 36, 0.45); }
.l24-boris-maugli-flow__vs-card strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-maugli-flow__note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--mg-muted);
}
.l24-boris-maugli-flow__note em {
  font-style: normal;
  color: var(--mg-sip-soft);
  font-weight: 600;
}
.l24-boris-maugli-flow__total {
  margin: 0 0 16px;
  padding: 14px 16px;
  border-radius: 10px;
  background: rgba(52, 211, 153, 0.1);
  border: 1px solid rgba(52, 211, 153, 0.32);
  font-size: 0.84rem;
  line-height: 1.5;
  color: var(--mg-muted);
}
.l24-boris-maugli-flow__total strong { color: var(--mg-leaf-soft); }
.l24-boris-maugli-flow__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-maugli-flow__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  color: var(--mg-txt);
  border: 1px solid rgba(255, 255, 255, 0.13);
}
.l24-boris-maugli-flow__tag--case { border-color: rgba(251, 191, 36, 0.45); color: var(--mg-gold-soft); }
.l24-boris-maugli-flow__tag--law { border-color: rgba(52, 211, 153, 0.45); color: var(--mg-leaf-soft); }
.l24-boris-maugli-flow__tag--sip { border-color: rgba(167, 139, 250, 0.45); color: var(--mg-sip-soft); }
@media (max-width: 860px) {
  .l24-boris-maugli-flow__split { grid-template-columns: 1fr; }
  .l24-boris-maugli-flow__stages { grid-template-columns: 1fr; }
  .l24-boris-maugli-flow__ground { grid-template-columns: 1fr; gap: 4px; }
  .l24-boris-maugli-flow__vs { grid-template-columns: 1fr; }
  .l24-boris-maugli-flow__shell { padding: 24px 18px 20px; }
}
</style>

<div class="l24-boris-maugli-flow__shell">
  <p class="l24-boris-maugli-flow__eyebrow">ППС · ТЗ № 162034 · Союзмультфильм vs Рот Фронт · решение 24.08.2026</p>
  <h3 class="l24-boris-maugli-flow__title">Возражение → решение → СИП: как аннулировали «МАУГЛИ ДРАЖЕ»</h3>
  <p class="l24-boris-maugli-flow__lead">В деле «Маугли» спор о <strong>недействительности охраны</strong> прошёл административный рубеж: <strong>возражение</strong> «Союзмультфильма» → коллегия <strong>ППС</strong> → решение об <strong>аннулировании</strong> ТЗ <strong>№ 162034</strong>. Для «Рот Фронта» следующий этап — <strong>обжалование в СИП</strong> в срок <strong>3 месяца</strong> (ч. 4 ст. 198 АПК), но прецедент <strong>СИП-62/2023</strong> (Карлсон) ухудшает позицию правообладателя без согласия.</p>

  <div class="l24-boris-maugli-flow__split">
    <div class="l24-boris-maugli-flow__panel">
      <p class="l24-boris-maugli-flow__panel-title">Сквозной маршрут (дело «Маугли»)</p>
      <svg class="l24-boris-maugli-flow__route-svg" viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="mgFlowT mgFlowD">
        <title id="mgFlowT">Маршрут аннулирования ТЗ «МАУГЛИ ДРАЖЕ»: возражение, решение ППС, СИП</title>
        <desc id="mgFlowD">Три этапа: возражение Союзмультфильма 30.12.2025, решение ППС 24.08.2026 об аннулировании № 162034, опциональное обжалование Рот Фронта в СИП за 3 месяца</desc>
        <defs>
          <linearGradient id="mgFlowLine" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#34d399"/>
            <stop offset="50%" stop-color="#fbbf24"/>
            <stop offset="100%" stop-color="#a78bfa"/>
          </linearGradient>
          <marker id="mgFlowArr" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
            <polygon points="0 0, 8 3.5, 0 7" fill="#fbbf24"/>
          </marker>
          <filter id="mgFlowGlow" x="-30%" y="-30%" width="160%" height="160%">
            <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#000" flood-opacity="0.35"/>
          </filter>
        </defs>

        <rect x="12" y="12" width="576" height="196" rx="12" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>

        <line x1="88" y1="108" x2="512" y2="108" stroke="url(#mgFlowLine)" stroke-width="4" stroke-linecap="round"/>
        <line x1="88" y1="108" x2="512" y2="108" stroke="rgba(52,211,153,0.2)" stroke-width="10" stroke-linecap="round"/>

        <!-- Этап 1: Возражение -->
        <circle cx="108" cy="108" r="28" fill="#143528" stroke="#34d399" stroke-width="3" filter="url(#mgFlowGlow)"/>
        <circle cx="108" cy="108" r="10" fill="#34d399"/>
        <text x="108" y="52" text-anchor="middle" fill="#6ee7b7" font-size="8" font-weight="800" font-family="system-ui,sans-serif">① ВОЗРАЖЕНИЕ</text>
        <rect x="36" y="60" width="144" height="72" rx="8" fill="rgba(52,211,153,0.12)" stroke="#34d399" stroke-width="1.2"/>
        <text x="48" y="76" fill="#6ee7b7" font-size="7" font-weight="800" font-family="system-ui,sans-serif">Союзмультфильм</text>
        <text x="48" y="90" fill="#fff" font-size="8.5" font-weight="800" font-family="system-ui,sans-serif">30.12.2025</text>
        <text x="48" y="104" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">ВОЗ_18ТЗ · ППС</text>
        <text x="48" y="118" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">п. 9 ст. 1483 · без согласия</text>
        <line x1="108" y1="136" x2="108" y2="148" stroke="#34d399" stroke-width="1.2" stroke-dasharray="3,2"/>

        <!-- Этап 2: Решение -->
        <circle cx="300" cy="108" r="32" fill="#1e293b" stroke="#fbbf24" stroke-width="3.5" filter="url(#mgFlowGlow)"/>
        <circle cx="300" cy="108" r="11" fill="#fbbf24"/>
        <text x="300" y="44" text-anchor="middle" fill="#fde68a" font-size="8" font-weight="800" font-family="system-ui,sans-serif">② РЕШЕНИЕ ППС</text>
        <rect x="216" y="148" width="168" height="52" rx="8" fill="rgba(251,191,36,0.12)" stroke="#fbbf24" stroke-width="1.4"/>
        <text x="228" y="166" fill="#fde68a" font-size="7.5" font-weight="800" font-family="system-ui,sans-serif">Аннулирование № 162034</text>
        <text x="228" y="180" fill="#fff" font-size="8" font-weight="800" font-family="system-ui,sans-serif">24.08.2026 · РАПСИ</text>
        <text x="228" y="194" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">коллегия 15.05.2026 · Батищева</text>
        <line x1="300" y1="140" x2="300" y2="144" stroke="#fbbf24" stroke-width="1.2" stroke-dasharray="3,2"/>

        <!-- Этап 3: СИП -->
        <circle cx="492" cy="108" r="28" fill="#143528" stroke="#a78bfa" stroke-width="3" filter="url(#mgFlowGlow)"/>
        <circle cx="492" cy="108" r="10" fill="#a78bfa"/>
        <text x="492" y="52" text-anchor="middle" fill="#c4b5fd" font-size="8" font-weight="800" font-family="system-ui,sans-serif">③ СИП (опция)</text>
        <rect x="420" y="60" width="144" height="72" rx="8" fill="rgba(167,139,250,0.12)" stroke="#a78bfa" stroke-width="1.2"/>
        <text x="432" y="76" fill="#c4b5fd" font-size="7" font-weight="800" font-family="system-ui,sans-serif">Рот Фронт</text>
        <text x="432" y="90" fill="#fff" font-size="8.5" font-weight="800" font-family="system-ui,sans-serif">3 месяца</text>
        <text x="432" y="104" fill="#cbd5e1" font-size="6.5" font-family="system-ui,sans-serif">ч. 4 ст. 198 АПК</text>
        <text x="432" y="118" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">ст. 1248 — досудебный этап</text>
        <line x1="492" y1="136" x2="492" y2="148" stroke="#a78bfa" stroke-width="1.2" stroke-dasharray="3,2"/>

        <path d="M136 108 L264 108" fill="none" stroke="#34d399" stroke-width="1.5" marker-end="url(#mgFlowArr)" opacity="0.8"/>
        <path d="M332 108 L464 108" fill="none" stroke="#fbbf24" stroke-width="1.5" marker-end="url(#mgFlowArr)" opacity="0.8"/>

        <rect x="200" y="168" width="200" height="0" fill="none"/>
        <text x="300" y="28" text-anchor="middle" fill="#fde68a" font-size="7.5" font-weight="700" font-family="system-ui,sans-serif">«МАУГЛИ ДРАЖЕ» · класс 30 · приоритет 30.01.1996</text>
      </svg>

      <ol class="l24-boris-maugli-flow__stages" aria-label="Три этапа маршрута">
        <li class="l24-boris-maugli-flow__stage">
          <strong>Возражение в Роспатент</strong>
          Заинтересованное лицо (Союзмультфильм) · весь срок охраны для п. 9 ст. 1483 · пакет: известность персонажа, отсутствие согласия.
        </li>
        <li class="l24-boris-maugli-flow__stage">
          <strong>Решение ППС</strong>
          Признание охраны недействительной · тождественность «Маугли» с циклом мультфильма · доводы Киплинга/Disney отклонены.
        </li>
        <li class="l24-boris-maugli-flow__stage">
          <strong>Обжалование в СИП</strong>
          Для проигравшего правообладателя · госпошлина 6 000 ₽ · кассация: президиум СИП → ВС РФ.
        </li>
      </ol>
      <p class="l24-boris-maugli-flow__caption">Схема по РАПСИ 24.08.2026 и расписанию ППС ФИПС (май 2026)</p>
    </div>

    <div class="l24-boris-maugli-flow__panel">
      <p class="l24-boris-maugli-flow__panel-title">Что важно на каждом рубеже</p>
      <div class="l24-boris-maugli-flow__vs">
        <div class="l24-boris-maugli-flow__vs-card l24-boris-maugli-flow__vs-card--win">
          <strong>Союзмультфильм (победа ППС)</strong>
          Охрана ТЗ прекращена — «Рот Фронт» не может запрещать «Маугли» как знак. Риск по АП на образ сохраняется отдельно.
        </div>
        <div class="l24-boris-maugli-flow__vs-card l24-boris-maugli-flow__vs-card--risk">
          <strong>Рот Фронт (путь в СИП)</strong>
          Нужны документы согласия — без них прецедент СИП-62/2023 (Карлсон): суд подтвердил Роспатент по п. 9 ст. 1483.
        </div>
      </div>
      <div class="l24-boris-maugli-flow__grounds">
        <div class="l24-boris-maugli-flow__ground l24-boris-maugli-flow__ground--pps">
          <span class="l24-boris-maugli-flow__ground-label">ППС · доказательства</span>
          <span class="l24-boris-maugli-flow__ground-text">Известность цикла «Маугли» (1967–1973), <em>тождественность</em> словесного элемента, отсутствие согласия киностудии и наследников Киплинга.</span>
        </div>
        <div class="l24-boris-maugli-flow__ground l24-boris-maugli-flow__ground--law">
          <span class="l24-boris-maugli-flow__ground-label">ст. 1483 · 1512 ГК</span>
          <span class="l24-boris-maugli-flow__ground-text"><em>пп. 1 п. 9 ст. 1483</em> — персонаж без согласия; абсолютное основание по п. 2 ст. 1512 (весь срок охраны).</span>
        </div>
        <div class="l24-boris-maugli-flow__ground l24-boris-maugli-flow__ground--sip">
          <span class="l24-boris-maugli-flow__ground-label">СИП · сроки</span>
          <span class="l24-boris-maugli-flow__ground-text"><em>3 месяца</em> на иск (ч. 4 ст. 198 АПК) · досудебный порядок по ст. 1248 обязателен · ВС 12.08.2025 отказал в кассации по Карлсону.</span>
        </div>
      </div>
      <p class="l24-boris-maugli-flow__note"><em>≠ иск о нарушении:</em> возражение спорит о регистрации; претензия по авторскому праву на этикетку — отдельная линия (пример: Волк на дыне, 11.08.2026).</p>
    </div>
  </div>

  <p class="l24-boris-maugli-flow__total"><strong>Ключ для производителя:</strong> административный маршрут (возражение → ППС) может аннулировать ТЗ быстрее суда. После решения Роспатента проигравшая сторона идёт в <strong>СИП</strong>, но без согласия на персонаж шансы ограничены — как в деле «Маугли» и аналоге «Карлсон».</p>

  <div class="l24-boris-maugli-flow__foot">
    <span class="l24-boris-maugli-flow__tag l24-boris-maugli-flow__tag--case">ТЗ № 162034</span>
    <span class="l24-boris-maugli-flow__tag l24-boris-maugli-flow__tag--law">п. 9 ст. 1483</span>
    <span class="l24-boris-maugli-flow__tag l24-boris-maugli-flow__tag--sip">СИП-62/2023</span>
    <span class="l24-boris-maugli-flow__tag">класс 30</span>
    <span class="l24-boris-maugli-flow__tag">24.08.2026</span>
  </div>
</div>
</section>
```
