=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

<section id="l24-hero-arb-srok" class="hero-arb-srok" aria-label="Арбитражный процессуальный срок">
  <style>
    .hero-arb-srok {
      position: relative;
      min-height: 100vh;
      min-height: 100dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 120px 24px 80px;
      background: linear-gradient(168deg, #fcfcfd 0%, #f6f8fb 42%, #eef2f7 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .hero-arb-srok::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 50% 44% at 92% 12%, rgba(163, 24, 48, 0.06) 0%, transparent 55%),
        radial-gradient(ellipse 46% 42% at 6% 88%, rgba(30, 58, 138, 0.06) 0%, transparent 50%);
      pointer-events: none;
    }
    .hero-arb-srok__inner {
      position: relative;
      z-index: 1;
      max-width: 1200px;
      margin: 0 auto;
      width: 100%;
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 44px;
      align-items: center;
    }
    .hero-arb-srok__badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 18px;
      padding: 8px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid rgba(15, 23, 42, 0.1);
      font-size: 0.82rem;
      font-weight: 600;
      letter-spacing: 0.02em;
      color: #334155;
    }
    .hero-arb-srok__badge-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #a31830;
      flex-shrink: 0;
    }
    .hero-arb-srok__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.55rem, 3.5vw, 2.35rem);
      line-height: 1.2;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .hero-arb-srok__h1-accent {
      color: #a31830;
    }
    .hero-arb-srok__sub {
      margin: 0 0 26px;
      max-width: 38em;
      font-size: clamp(1rem, 1.55vw, 1.1rem);
      line-height: 1.55;
      color: #475569;
    }
    .hero-arb-srok__deadlines {
      list-style: none;
      padding: 0;
      margin: 0 0 30px;
    }
    .hero-arb-srok__deadline {
      display: flex;
      gap: 14px;
      align-items: flex-start;
      margin-bottom: 13px;
      font-size: 0.93rem;
      line-height: 1.45;
      color: #334155;
    }
    .hero-arb-srok__deadline-tag {
      flex-shrink: 0;
      min-width: 108px;
      padding: 6px 10px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.7rem;
      letter-spacing: 0.04em;
      text-align: center;
      text-transform: uppercase;
      color: #fff;
    }
    .hero-arb-srok__deadline--pret .hero-arb-srok__deadline-tag {
      background: #475569;
    }
    .hero-arb-srok__deadline--otz .hero-arb-srok__deadline-tag {
      background: #a31830;
    }
    .hero-arb-srok__deadline--app .hero-arb-srok__deadline-tag {
      background: #1e3a8a;
    }
    .hero-arb-srok__cta {
      display: inline-block;
      background: #a31830;
      color: #fff !important;
      padding: 14px 26px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.94rem;
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(163, 24, 48, 0.2);
    }
    .hero-arb-srok__cta:hover {
      background: #8b1528;
    }
    .hero-arb-srok__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (prefers-reduced-motion: no-preference) {
      .hero-b1-clock-hand {
        animation: hero-b1-clock-tick 4s ease-in-out infinite;
        transform-origin: 240px 118px;
      }
      .hero-b1-deadline-pulse {
        animation: hero-b1-deadline-pulse 2.2s ease-in-out infinite;
      }
      .hero-b1-flow-doc {
        animation: hero-b1-doc-flow 3.4s linear infinite;
      }
      .hero-b1-cal-day-active {
        animation: hero-b1-cal-flash 2.8s ease-in-out infinite;
      }
    }
    @keyframes hero-b1-clock-tick {
      0%, 100% { transform: rotate(0deg); }
      25% { transform: rotate(8deg); }
      50% { transform: rotate(0deg); }
      75% { transform: rotate(-4deg); }
    }
    @keyframes hero-b1-deadline-pulse {
      0%, 100% { opacity: 1; r: 6; }
      50% { opacity: 0.65; r: 8; }
    }
    @keyframes hero-b1-doc-flow {
      0% { offset-distance: 0%; opacity: 0; }
      8% { opacity: 1; }
      92% { opacity: 1; }
      100% { offset-distance: 100%; opacity: 0; }
    }
    @keyframes hero-b1-cal-flash {
      0%, 100% { fill: #fef2f2; stroke: #fca5a5; }
      50% { fill: #fee2e2; stroke: #a31830; }
    }
    @media (max-width: 900px) {
      .hero-arb-srok__inner {
        grid-template-columns: 1fr;
        gap: 28px;
      }
      .hero-arb-srok__visual {
        order: -1;
        max-height: 320px;
      }
      .hero-arb-srok__deadline-tag {
        min-width: 92px;
        font-size: 0.66rem;
      }
    }
    @media (prefers-reduced-motion: reduce) {
      .hero-b1-clock-hand,
      .hero-b1-deadline-pulse,
      .hero-b1-flow-doc,
      .hero-b1-cal-day-active {
        animation: none !important;
      }
    }
  </style>
  <div class="hero-arb-srok__inner">
    <div class="hero-arb-srok__content">
      <div class="hero-arb-srok__badge">
        <span class="hero-arb-srok__badge-dot" aria-hidden="true"></span>
        Legis24 ARB · B1 · АПК · ст. 113–117 · 2026
      </div>
      <h1 class="hero-arb-srok__h1">
        <span class="hero-arb-srok__h1-accent">Арбитражный процессуальный срок:</span> как не пропустить подачу и возражения
      </h1>
      <p class="hero-arb-srok__sub">
        Процессуальные сроки по АПК: иск, отзыв, апелляция и восстановление по ст. 117 — без пропусков для бизнеса
      </p>
      <ul class="hero-arb-srok__deadlines">
        <li class="hero-arb-srok__deadline hero-arb-srok__deadline--pret">
          <span class="hero-arb-srok__deadline-tag">30 к.д.</span>
          <span><strong>Претензия</strong> — досудебный ответ по ст. 4 АПК; не путать с отзывом на иск в суде</span>
        </li>
        <li class="hero-arb-srok__deadline hero-arb-srok__deadline--otz">
          <span class="hero-arb-srok__deadline-tag">15 / 30</span>
          <span><strong>Отзыв</strong> — ≥15 дней в УП (ст. 228) или срок из определения суда (ст. 131)</span>
        </li>
        <li class="hero-arb-srok__deadline hero-arb-srok__deadline--app">
          <span class="hero-arb-srok__deadline-tag">1 + 6 мес.</span>
          <span><strong>Апелляция</strong> — месяц со дня принятия решения; восстановление до 6 месяцев (ст. 117, 259)</span>
        </li>
      </ul>
      <a class="hero-arb-srok__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по соблюдению процессуальных сроков в арбитраже</a>
    </div>
    <div class="hero-arb-srok__visual" aria-hidden="true">
      <svg viewBox="0 0 480 420" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:480px" role="img" aria-label="Календарь арбитражных сроков: часы до 24:00, стрелки этапов и процессуальные документы">
        <defs>
          <linearGradient id="hero-b1-sky" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f8fafc"/>
            <stop offset="100%" stop-color="#e2e8f0"/>
          </linearGradient>
          <linearGradient id="hero-b1-court" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1e3a8a"/>
            <stop offset="100%" stop-color="#0f2744"/>
          </linearGradient>
          <linearGradient id="hero-b1-cal" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#ffffff"/>
            <stop offset="100%" stop-color="#f1f5f9"/>
          </linearGradient>
          <linearGradient id="hero-b1-arrow-line" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#94a3b8"/>
            <stop offset="50%" stop-color="#a31830"/>
            <stop offset="100%" stop-color="#1e3a8a"/>
          </linearGradient>
          <filter id="hero-b1-shadow" x="-8%" y="-8%" width="116%" height="116%">
            <feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="#0f172a" flood-opacity="0.12"/>
          </filter>
          <marker id="hero-b1-arrow" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7 Z" fill="#64748b"/>
          </marker>
          <marker id="hero-b1-arrow-red" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7 Z" fill="#a31830"/>
          </marker>
          <marker id="hero-b1-arrow-navy" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7 Z" fill="#1e3a8a"/>
          </marker>
          <path id="hero-b1-timeline" d="M48 318 Q120 280 240 268 T432 318" fill="none"/>
        </defs>
        <rect x="8" y="10" width="464" height="400" rx="16" fill="url(#hero-b1-sky)" stroke="#cbd5e1" stroke-width="1.2"/>
        <!-- арбитражный суд -->
        <g transform="translate(150, 14)">
          <rect x="0" y="20" width="180" height="48" rx="4" fill="url(#hero-b1-court)"/>
          <polygon points="90,0 180,20 0,20" fill="#1e40af"/>
          <text x="90" y="42" text-anchor="middle" fill="#e2e8f0" font-size="8" font-weight="700" letter-spacing="0.08em">АРБИТРАЖ · АПК</text>
          <text x="90" y="56" text-anchor="middle" fill="#93c5fd" font-size="7">процессуальные сроки · ст. 113–117</text>
        </g>
        <!-- часы: до 24:00 последнего дня -->
        <g filter="url(#hero-b1-shadow)" transform="translate(368, 28)">
          <circle cx="0" cy="0" r="34" fill="#fff" stroke="#1e3a8a" stroke-width="1.5"/>
          <circle cx="0" cy="0" r="28" fill="none" stroke="#e2e8f0" stroke-width="1"/>
          <line x1="0" y1="0" x2="0" y2="-18" stroke="#64748b" stroke-width="2"/>
          <g class="hero-b1-clock-hand">
            <line x1="0" y1="0" x2="14" y2="6" stroke="#a31830" stroke-width="2.5" stroke-linecap="round"/>
          </g>
          <circle cx="0" cy="0" r="3" fill="#a31830"/>
          <text x="0" y="-42" text-anchor="middle" fill="#334155" font-size="7" font-weight="700">до 24:00</text>
          <text x="0" y="-32" text-anchor="middle" fill="#64748b" font-size="6">Пленум № 99</text>
        </g>
        <!-- календарь — центр -->
        <g filter="url(#hero-b1-shadow)" transform="translate(118, 72)">
          <rect x="0" y="0" width="244" height="196" rx="10" fill="url(#hero-b1-cal)" stroke="#cbd5e1" stroke-width="1.2"/>
          <rect x="0" y="0" width="244" height="36" rx="10" fill="#a31830"/>
          <rect x="0" y="18" width="244" height="18" fill="#a31830"/>
          <text x="122" y="24" text-anchor="middle" fill="#fff" font-size="10" font-weight="800" letter-spacing="0.06em">КАЛЕНДАРЬ АРБИТРАЖНЫХ СРОКОВ</text>
          <!-- сетка дней -->
          <g fill="#f8fafc" stroke="#e2e8f0" stroke-width="0.6">
            <rect x="12" y="48" width="30" height="24" rx="3"/>
            <rect x="46" y="48" width="30" height="24" rx="3"/>
            <rect x="80" y="48" width="30" height="24" rx="3"/>
            <rect x="114" y="48" width="30" height="24" rx="3"/>
            <rect x="148" y="48" width="30" height="24" rx="3"/>
            <rect x="182" y="48" width="30" height="24" rx="3"/>
            <rect x="12" y="76" width="30" height="24" rx="3"/>
            <rect x="46" y="76" width="30" height="24" rx="3"/>
            <rect x="80" y="76" width="30" height="24" rx="3"/>
            <rect x="114" y="76" width="30" height="24" rx="3"/>
            <rect x="148" y="76" width="30" height="24" rx="3"/>
            <rect x="182" y="76" width="30" height="24" rx="3"/>
            <rect x="12" y="104" width="30" height="24" rx="3"/>
            <rect x="46" y="104" width="30" height="24" rx="3"/>
            <rect x="80" y="104" width="30" height="24" rx="3"/>
            <rect x="114" y="104" width="30" height="24" rx="3"/>
            <rect x="148" y="104" width="30" height="24" rx="3"/>
            <rect x="182" y="104" width="30" height="24" rx="3"/>
            <rect x="12" y="132" width="30" height="24" rx="3"/>
            <rect x="46" y="132" width="30" height="24" rx="3"/>
            <rect x="80" y="132" width="30" height="24" rx="3"/>
            <rect x="114" y="132" width="30" height="24" rx="3"/>
            <rect x="148" y="132" width="30" height="24" rx="3"/>
            <rect x="182" y="132" width="30" height="24" rx="3"/>
          </g>
          <!-- активный день — дедлайн -->
          <rect class="hero-b1-cal-day-active" x="148" y="104" width="30" height="24" rx="3" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
          <text x="163" y="120" text-anchor="middle" fill="#a31830" font-size="9" font-weight="800">!</text>
          <text x="12" y="168" fill="#64748b" font-size="6">30 к.д. · претензия</text>
          <text x="92" y="168" fill="#a31830" font-size="6" font-weight="700">15/30 · отзыв</text>
          <text x="168" y="168" fill="#1e3a8a" font-size="6" font-weight="700">1 мес. · апелляция</text>
          <circle class="hero-b1-deadline-pulse" cx="163" cy="116" r="6" fill="none" stroke="#a31830" stroke-width="1.5"/>
        </g>
        <!-- документы слева: претензия -->
        <g filter="url(#hero-b1-shadow)" transform="translate(24, 148)">
          <rect x="0" y="0" width="72" height="88" rx="6" fill="#fff" stroke="#475569" stroke-width="1"/>
          <rect x="10" y="12" width="52" height="6" rx="2" fill="#cbd5e1"/>
          <rect x="10" y="24" width="44" height="4" rx="1" fill="#e2e8f0"/>
          <rect x="10" y="32" width="48" height="4" rx="1" fill="#e2e8f0"/>
          <rect x="10" y="40" width="40" height="4" rx="1" fill="#e2e8f0"/>
          <rect x="10" y="56" width="36" height="14" rx="3" fill="#f1f5f9" stroke="#94a3b8"/>
          <text x="28" y="66" text-anchor="middle" fill="#475569" font-size="5" font-weight="700">ст. 4</text>
          <text x="36" y="82" text-anchor="middle" fill="#334155" font-size="6" font-weight="700">ПРЕТЕНЗИЯ</text>
        </g>
        <!-- документ: иск -->
        <g filter="url(#hero-b1-shadow)" transform="translate(24, 248)">
          <rect x="0" y="0" width="72" height="72" rx="6" fill="#fff" stroke="#a31830" stroke-width="1.2"/>
          <rect x="10" y="10" width="52" height="6" rx="2" fill="#fecaca"/>
          <rect x="10" y="22" width="44" height="4" rx="1" fill="#fee2e2"/>
          <rect x="10" y="30" width="48" height="4" rx="1" fill="#fee2e2"/>
          <text x="36" y="52" text-anchor="middle" fill="#a31830" font-size="6" font-weight="800">ИСК</text>
          <text x="36" y="64" text-anchor="middle" fill="#64748b" font-size="5">ст. 125–127</text>
        </g>
        <!-- документ: отзыв -->
        <g filter="url(#hero-b1-shadow)" transform="translate(384, 148)">
          <rect x="0" y="0" width="72" height="88" rx="6" fill="#fff" stroke="#a31830" stroke-width="1.2"/>
          <rect x="10" y="12" width="52" height="6" rx="2" fill="#fecaca"/>
          <rect x="10" y="24" width="44" height="4" rx="1" fill="#fee2e2"/>
          <rect x="10" y="32" width="48" height="4" rx="1" fill="#fee2e2"/>
          <rect x="10" y="48" width="52" height="18" rx="3" fill="#fef2f2" stroke="#fca5a5"/>
          <text x="36" y="60" text-anchor="middle" fill="#a31830" font-size="5" font-weight="800">ОТЗЫВ</text>
          <text x="36" y="82" text-anchor="middle" fill="#64748b" font-size="5">ст. 131 · 228</text>
        </g>
        <!-- документ: апелляция -->
        <g filter="url(#hero-b1-shadow)" transform="translate(384, 248)">
          <rect x="0" y="0" width="72" height="72" rx="6" fill="#fff" stroke="#1e3a8a" stroke-width="1.2"/>
          <rect x="10" y="10" width="52" height="6" rx="2" fill="#bfdbfe"/>
          <rect x="10" y="22" width="44" height="4" rx="1" fill="#dbeafe"/>
          <text x="36" y="44" text-anchor="middle" fill="#1e3a8a" font-size="6" font-weight="800">АПЕЛЛ.</text>
          <text x="36" y="56" text-anchor="middle" fill="#64748b" font-size="5">ст. 259</text>
          <text x="36" y="66" text-anchor="middle" fill="#a31830" font-size="5">+ ст. 117</text>
        </g>
        <!-- стрелки сроков между этапами -->
        <path d="M96 192 L118 168" stroke="#64748b" stroke-width="1.5" fill="none" marker-end="url(#hero-b1-arrow)"/>
        <path d="M96 284 L118 248" stroke="#a31830" stroke-width="1.5" fill="none" marker-end="url(#hero-b1-arrow-red)"/>
        <path d="M362 192 L342 168" stroke="#a31830" stroke-width="1.5" fill="none" marker-end="url(#hero-b1-arrow-red)"/>
        <path d="M362 284 L342 248" stroke="#1e3a8a" stroke-width="1.5" fill="none" marker-end="url(#hero-b1-arrow-navy)"/>
        <path d="M240 268 L240 248" stroke="#64748b" stroke-width="1.2" fill="none" stroke-dasharray="3 3"/>
        <!-- лента таймлайна -->
        <path d="M48 318 Q120 280 240 268 T432 318" stroke="url(#hero-b1-arrow-line)" stroke-width="3" fill="none" stroke-linecap="round"/>
        <circle class="hero-b1-flow-doc" r="5" fill="#a31830" stroke="#fff" stroke-width="1.5" style="offset-path: path('M48 318 Q120 280 240 268 T432 318'); offset-rotate: 0deg;"/>
        <text x="72" y="336" text-anchor="middle" fill="#475569" font-size="6" font-weight="700">претензия</text>
        <text x="168" y="328" text-anchor="middle" fill="#a31830" font-size="6" font-weight="700">иск · отзыв</text>
        <text x="300" y="336" text-anchor="middle" fill="#1e3a8a" font-size="6" font-weight="700">решение</text>
        <text x="408" y="328" text-anchor="middle" fill="#334155" font-size="6" font-weight="700">апелляция</text>
        <!-- зона пропуска -->
        <g transform="translate(188, 288)">
          <rect x="0" y="0" width="104" height="28" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1" stroke-dasharray="4 3"/>
          <text x="52" y="12" text-anchor="middle" fill="#a31830" font-size="6" font-weight="800">ПРОПУСК</text>
          <text x="52" y="22" text-anchor="middle" fill="#991b1b" font-size="5">ст. 115 · 117</text>
        </g>
        <!-- нижняя панель -->
        <g filter="url(#hero-b1-shadow)" transform="translate(28, 348)">
          <rect width="424" height="52" rx="10" fill="#fff" stroke="#cbd5e1" stroke-width="1"/>
          <rect x="0" y="0" width="106" height="52" rx="10" fill="#f1f5f9" stroke="none"/>
          <text x="53" y="22" text-anchor="middle" fill="#475569" font-size="7" font-weight="800">30 к.д.</text>
          <text x="53" y="36" text-anchor="middle" fill="#64748b" font-size="6">претензия · ст. 4</text>
          <line x1="106" y1="10" x2="106" y2="42" stroke="#e2e8f0"/>
          <text x="159" y="22" text-anchor="middle" fill="#a31830" font-size="7" font-weight="800">15 / 30</text>
          <text x="159" y="36" text-anchor="middle" fill="#64748b" font-size="6">отзыв · УП / обычное</text>
          <line x1="212" y1="10" x2="212" y2="42" stroke="#e2e8f0"/>
          <text x="265" y="22" text-anchor="middle" fill="#1e3a8a" font-size="7" font-weight="800">1 мес.</text>
          <text x="265" y="36" text-anchor="middle" fill="#64748b" font-size="6">апелляция · ст. 259</text>
          <line x1="318" y1="10" x2="318" y2="42" stroke="#e2e8f0"/>
          <rect x="318" y="0" width="106" height="52" rx="10" fill="#fef2f2" stroke="none"/>
          <text x="371" y="22" text-anchor="middle" fill="#a31830" font-size="7" font-weight="800">6 мес.</text>
          <text x="371" y="36" text-anchor="middle" fill="#64748b" font-size="6">предел · ст. 117</text>
        </g>
        <text x="240" y="412" text-anchor="middle" fill="#64748b" font-size="7">претензия → иск → отзыв → решение → апелляция · единый календарь по делу</text>
      </svg>
    </div>
  </div>
</section>

## Паспорт мира

| Поле | Значение |
|------|----------|
| **Код** | B1 (ARB) |
| **SLUG** | arbitrazhnyj-processualnyj-srok-podacha |
| **Метафора** | «Календарь арбитражных сроков» — настенный календарь в центре, часы до 24:00 (Пленум № 99), процессуальные документы по периметру, стрелки этапов и лента таймлайна |
| **Палитра** | Светлый фон `#fcfcfd`–`#eef2f7`, типографика `#0f172a` / `#475569`, акцент **#a31830**, арбитраж **#1e3a8a** |
| **Объекты SVG** | Календарь с подсветкой дедлайна, часы, претензия / иск / отзыв / апелляция, стрелки сроков, зона «ПРОПУСК», нижняя матрица 30·15/30·1·6 |
| **Анимации** | Только CSS `@keyframes` на стрелках часов, пульсе дня, точке по таймлайну |
| **MCP** | Только static SVG + inline CSS. **Без** `<canvas>` и **без** `<script>` |

## Чеклист отличий

- [x] Не A14 «мост соглашения» — другой мир: **календарь + часы + документы**, не handshake / весы / утверждение МС
- [x] Не A8 банкротный реестр / не A11 АУ и сделки — фокус на **процессуальных сроках АПК** (113–117, 131, 228, 259)
- [x] Акцент hero — **бордовый #a31830** (в A14 акцент H1 был navy)
- [x] Три тега в тексте: **30 к.д.** претензия · **15/30** отзыв · **1+6 мес.** апелляция (не плюсы/риски мира)
- [x] Hero id `l24-hero-arb-srok` — не пересекается с Boris-блоком в статье
- [x] Без `<canvas>` и `<script>` — совместимо с WordPress MCP publish

## Передача Наташе

**SLUG:** arbitrazhnyj-processualnyj-srok-podacha

**Hero ID:** `#l24-hero-arb-srok`

**Класс страницы:** `arbitrazhnyj-processualnyj-srok-podacha-page`

**MCP-only:** hero содержит только static SVG + inline CSS + `@keyframes`. Без `<canvas>` и без `<script>`. Не удалять анимации и SVG-разметку.

**Метафора:** «календарь арбитражных сроков» — единый календарь по делу, часы до 24:00, документы этапов и стрелки от претензии к апелляции (отличие от A14: не мировое соглашение, а контроль процессуальных дедлайнов).
