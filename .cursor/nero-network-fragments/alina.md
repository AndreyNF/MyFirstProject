=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

<section id="l24-hero-dosudeb-zashchita" class="hero-ug-dosudeb" aria-label="Досудебная защита по уголовному делу: права подозреваемого и допрос">
  <style>
    .hero-ug-dosudeb {
      position: relative;
      min-height: 100vh;
      min-height: 100dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 120px 24px 80px;
      background: linear-gradient(165deg, #f9f8f6 0%, #f2f0eb 42%, #eae8e2 100%);
      color: #18181b;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .hero-ug-dosudeb::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 52% 44% at 88% 8%, rgba(30, 58, 95, 0.08) 0%, transparent 58%),
        radial-gradient(ellipse 48% 40% at 8% 92%, rgba(120, 53, 15, 0.05) 0%, transparent 52%);
      pointer-events: none;
    }
    .hero-ug-dosudeb::after {
      content: "";
      position: absolute;
      inset: 0;
      opacity: 0.035;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80' viewBox='0 0 80 80'%3E%3Cpath d='M8 8h20v4H12v28H8z' fill='%2318181b'/%3E%3C/svg%3E");
      background-size: 80px 80px;
      pointer-events: none;
    }
    .hero-ug-dosudeb__inner {
      position: relative;
      z-index: 1;
      max-width: 1200px;
      margin: 0 auto;
      width: 100%;
      display: grid;
      grid-template-columns: 1.06fr 0.94fr;
      gap: 46px;
      align-items: center;
    }
    .hero-ug-dosudeb__badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 18px;
      padding: 8px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.93);
      border: 1px solid rgba(24, 24, 27, 0.12);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #3f3f46;
    }
    .hero-ug-dosudeb__badge-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #1e3a5f;
      flex-shrink: 0;
      animation: hero-dosudeb-pulse 2.4s ease-in-out infinite;
    }
    @keyframes hero-dosudeb-pulse {
      0%, 100% { box-shadow: 0 0 0 0 rgba(30, 58, 95, 0.35); }
      50% { box-shadow: 0 0 0 5px rgba(30, 58, 95, 0); }
    }
    .hero-ug-dosudeb__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.6rem, 3.6vw, 2.38rem);
      line-height: 1.18;
      font-weight: 800;
      color: #09090b;
      letter-spacing: -0.024em;
    }
    .hero-ug-dosudeb__h1-accent {
      color: #1e3a5f;
      display: block;
    }
    .hero-ug-dosudeb__sub {
      margin: 0 0 26px;
      max-width: 40em;
      font-size: clamp(1rem, 1.55vw, 1.1rem);
      line-height: 1.58;
      color: #52525b;
    }
    .hero-ug-dosudeb__rights {
      list-style: none;
      padding: 0;
      margin: 0 0 30px;
    }
    .hero-ug-dosudeb__right {
      display: flex;
      gap: 14px;
      align-items: flex-start;
      margin-bottom: 13px;
      font-size: 0.93rem;
      line-height: 1.48;
      color: #3f3f46;
    }
    .hero-ug-dosudeb__right-tag {
      flex-shrink: 0;
      min-width: 58px;
      padding: 5px 8px;
      border-radius: 6px;
      background: #1e3a5f;
      color: #f8fafc;
      font-weight: 700;
      font-size: 0.7rem;
      letter-spacing: 0.03em;
      text-align: center;
    }
    .hero-ug-dosudeb__right-tag--warn {
      background: #78350f;
    }
    .hero-ug-dosudeb__right-tag--law {
      background: #27272a;
    }
    .hero-ug-dosudeb__cta {
      display: inline-block;
      background: #1e3a5f;
      color: #fff !important;
      padding: 14px 26px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.94rem;
      text-decoration: none;
      box-shadow: 0 4px 16px rgba(30, 58, 95, 0.28);
    }
    .hero-ug-dosudeb__cta:hover {
      background: #172554;
    }
    .hero-ug-dosudeb__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .hero-ug-dosudeb__balance-arm {
      transform-origin: 220px 168px;
      animation: hero-dosudeb-balance 5s ease-in-out infinite;
    }
    @keyframes hero-dosudeb-balance {
      0%, 100% { transform: rotate(-2deg); }
      50% { transform: rotate(2deg); }
    }
    .hero-ug-dosudeb__shield-glow {
      animation: hero-dosudeb-shield 3.2s ease-in-out infinite;
    }
    @keyframes hero-dosudeb-shield {
      0%, 100% { opacity: 0.92; }
      50% { opacity: 1; filter: drop-shadow(0 0 8px rgba(30, 58, 95, 0.25)); }
    }
    .hero-ug-dosudeb__corridor-light {
      animation: hero-dosudeb-light 4s ease-in-out infinite;
    }
    @keyframes hero-dosudeb-light {
      0%, 100% { opacity: 0.55; }
      50% { opacity: 0.85; }
    }
    @media (max-width: 900px) {
      .hero-ug-dosudeb__inner {
        grid-template-columns: 1fr;
        gap: 28px;
      }
      .hero-ug-dosudeb__visual {
        order: -1;
        max-height: 310px;
      }
    }
    @media (prefers-reduced-motion: reduce) {
      .hero-ug-dosudeb__badge-dot,
      .hero-ug-dosudeb__balance-arm,
      .hero-ug-dosudeb__shield-glow,
      .hero-ug-dosudeb__corridor-light {
        animation: none;
      }
    }
  </style>
  <div class="hero-ug-dosudeb__inner">
    <div class="hero-ug-dosudeb__content">
      <div class="hero-ug-dosudeb__badge">
        <span class="hero-ug-dosudeb__badge-dot" aria-hidden="true"></span>
        УПК · досудебная стадия · ст. 46–47 · 159 / 177 · 2026
      </div>
      <h1 class="hero-ug-dosudeb__h1">
        <span class="hero-ug-dosudeb__h1-accent">Досудебная защита по уголовному делу</span>
      </h1>
      <p class="hero-ug-dosudeb__sub">
        Что говорить следователю на допросе, какие права у подозреваемого до суда и когда подключать адвоката — в том числе по ст. 159 и 177 УК
      </p>
      <ul class="hero-ug-dosudeb__rights">
        <li class="hero-ug-dosudeb__right">
          <span class="hero-ug-dosudeb__right-tag">144</span>
          <span><strong>Проверка 3 / 10 / 30 суток</strong> — объяснения ≠ допрос; оценить риск статуса подозреваемого</span>
        </li>
        <li class="hero-ug-dosudeb__right">
          <span class="hero-ug-dosudeb__right-tag hero-ug-dosudeb__right-tag--warn">24 ч</span>
          <span><strong>После задержания</strong> — свидание с защитником до допроса (ст. 92); не подписывать протокол без адвоката</span>
        </li>
        <li class="hero-ug-dosudeb__right">
          <span class="hero-ug-dosudeb__right-tag hero-ug-dosudeb__right-tag--law">46</span>
          <span><strong>Отказ от показаний</strong> — п. 2 ч. 4 ст. 46 / п. 3 ч. 4 ст. 47 УПК; замечания к протоколу до подписи</span>
        </li>
      </ul>
      <a class="hero-ug-dosudeb__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по досудебной защите</a>
    </div>
    <div class="hero-ug-dosudeb__visual" aria-hidden="true">
      <svg viewBox="0 0 440 400" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:440px" role="img" aria-label="Весы прав подозреваемого: давление следствия и защита до суда, коридор досудебной стадии">
        <defs>
          <linearGradient id="hero-dosudeb-corridor" x1="50%" y1="100%" x2="50%" y2="0%">
            <stop offset="0%" stop-color="#d4d4d8"/>
            <stop offset="55%" stop-color="#e4e4e7"/>
            <stop offset="100%" stop-color="#fafafa"/>
          </linearGradient>
          <linearGradient id="hero-dosudeb-wall" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#a1a1aa"/>
            <stop offset="50%" stop-color="#d4d4d8"/>
            <stop offset="100%" stop-color="#a1a1aa"/>
          </linearGradient>
          <linearGradient id="hero-dosudeb-shield-fill" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#e0e7ff"/>
            <stop offset="100%" stop-color="#1e3a5f"/>
          </linearGradient>
          <linearGradient id="hero-dosudeb-scale" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#78716c"/>
            <stop offset="100%" stop-color="#27272a"/>
          </linearGradient>
          <filter id="hero-dosudeb-shadow" x="-12%" y="-12%" width="124%" height="124%">
            <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#18181b" flood-opacity="0.14"/>
          </filter>
        </defs>
        <!-- коридор к залу суда (перспектива) -->
        <g class="hero-ug-dosudeb__corridor-light">
          <path d="M0,120 L220,72 L440,120 L440,400 L0,400 Z" fill="url(#hero-dosudeb-corridor)"/>
          <path d="M60,140 L220,100 L380,140 L340,400 L100,400 Z" fill="#f4f4f5" opacity="0.9"/>
          <rect x="188" y="48" width="64" height="88" rx="4" fill="#fafafa" stroke="#a1a1aa" stroke-width="2"/>
          <path d="M196,56 L220,72 L244,56" fill="none" stroke="#71717a" stroke-width="1.5"/>
          <text x="220" y="118" text-anchor="middle" fill="#52525b" font-size="8" font-weight="700" letter-spacing="0.08em">ДОСУДЕБНЫЙ КОРИДОР</text>
          <line x1="0" y1="120" x2="440" y2="120" stroke="#d4d4d8" stroke-width="1"/>
        </g>
        <!-- кабинет допроса слева -->
        <g filter="url(#hero-dosudeb-shadow)" transform="translate(20, 148)">
          <rect width="118" height="108" rx="10" fill="#fff" stroke="#d4d4d8" stroke-width="1.2"/>
          <rect x="10" y="12" width="98" height="14" rx="4" fill="#fef2f2" stroke="#fecaca"/>
          <text x="59" y="22" text-anchor="middle" fill="#991b1b" font-size="8" font-weight="800">ДОПРОС</text>
          <rect x="14" y="34" width="90" height="6" rx="3" fill="#e4e4e7"/>
          <rect x="14" y="46" width="72" height="6" rx="3" fill="#e4e4e7"/>
          <rect x="14" y="58" width="80" height="6" rx="3" fill="#e4e4e7"/>
          <circle cx="32" cy="82" r="10" fill="#f4f4f5" stroke="#a1a1aa"/>
          <text x="32" y="86" text-anchor="middle" fill="#52525b" font-size="7" font-weight="700">?</text>
          <rect x="52" y="74" width="48" height="22" rx="5" fill="#fff7ed" stroke="#fdba74"/>
          <text x="76" y="88" text-anchor="middle" fill="#9a3412" font-size="7" font-weight="700">давление</text>
        </g>
        <!-- весы прав (центр) -->
        <g filter="url(#hero-dosudeb-shadow)">
          <rect x="196" y="148" width="48" height="92" rx="6" fill="url(#hero-dosudeb-scale)"/>
          <circle cx="220" cy="148" r="10" fill="#27272a"/>
          <g class="hero-ug-dosudeb__balance-arm">
            <line x1="220" y1="158" x2="148" y2="198" stroke="#3f3f46" stroke-width="3" stroke-linecap="round"/>
            <line x1="220" y1="158" x2="292" y2="198" stroke="#3f3f46" stroke-width="3" stroke-linecap="round"/>
            <!-- левая чаша: вопросы следователя -->
            <g transform="translate(108, 188)">
              <line x1="40" y1="0" x2="40" y2="14" stroke="#71717a" stroke-width="2"/>
              <ellipse cx="40" cy="34" rx="44" ry="10" fill="#e7e5e4" stroke="#a8a29e"/>
              <path d="M8,34 Q40,18 72,34 L68,52 Q40,62 12,52 Z" fill="#fafaf9" stroke="#d6d3d1"/>
              <text x="40" y="44" text-anchor="middle" fill="#57534e" font-size="7" font-weight="700">показания</text>
            </g>
            <!-- правая чаша: отказ ст. 46 -->
            <g transform="translate(252, 188)">
              <line x1="40" y1="0" x2="40" y2="14" stroke="#71717a" stroke-width="2"/>
              <ellipse cx="40" cy="34" rx="44" ry="10" fill="#dbeafe" stroke="#93c5fd"/>
              <path d="M8,34 Q40,18 72,34 L68,52 Q40,62 12,52 Z" fill="#eff6ff" stroke="#bfdbfe"/>
              <text x="40" y="44" text-anchor="middle" fill="#1e3a5f" font-size="7" font-weight="800">ст. 46 · отказ</text>
            </g>
          </g>
          <text x="220" y="252" text-anchor="middle" fill="#3f3f46" font-size="8" font-weight="700" letter-spacing="0.06em">БАЛАНС ПРАВ</text>
        </g>
        <!-- щит + адвокат справа -->
        <g class="hero-ug-dosudeb__shield-glow" filter="url(#hero-dosudeb-shadow)" transform="translate(302, 142)">
          <path d="M58,8 L88,22 L88,58 C88,82 72,96 58,104 C44,96 28,82 28,58 L28,22 Z" fill="url(#hero-dosudeb-shield-fill)" stroke="#1e3a5f" stroke-width="1.8"/>
          <path d="M46,52 L54,62 L72,40" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
          <rect x="18" y="112" width="80" height="52" rx="8" fill="#fff" stroke="#d4d4d8"/>
          <text x="58" y="130" text-anchor="middle" fill="#1e3a5f" font-size="8" font-weight="800">ЗАЩИТНИК</text>
          <text x="58" y="146" text-anchor="middle" fill="#52525b" font-size="7" font-weight="600">до допроса · ст. 92</text>
          <rect x="26" y="152" width="64" height="6" rx="3" fill="#e0e7ff"/>
        </g>
        <!-- ст. 159 / 177 -->
        <g transform="translate(36, 292)">
          <rect width="88" height="56" rx="8" fill="#fff" stroke="#d4d4d8" stroke-width="1"/>
          <text x="44" y="22" text-anchor="middle" fill="#78350f" font-size="9" font-weight="800">ст. 159</text>
          <text x="44" y="38" text-anchor="middle" fill="#71717a" font-size="7" font-weight="600">мошенничество</text>
          <text x="44" y="50" text-anchor="middle" fill="#a1a1aa" font-size="6" font-weight="600">бизнес-риск</text>
        </g>
        <g transform="translate(136, 292)">
          <rect width="88" height="56" rx="8" fill="#fff" stroke="#d4d4d8" stroke-width="1"/>
          <text x="44" y="22" text-anchor="middle" fill="#78350f" font-size="9" font-weight="800">ст. 177</text>
          <text x="44" y="38" text-anchor="middle" fill="#71717a" font-size="7" font-weight="600">злостное уклонение</text>
          <text x="44" y="50" text-anchor="middle" fill="#a1a1aa" font-size="6" font-weight="600">долги · ФССП</text>
        </g>
        <!-- протокол внизу -->
        <g filter="url(#hero-dosudeb-shadow)" transform="translate(248, 278)">
          <rect width="172" height="78" rx="10" fill="#fff" stroke="#d4d4d8" stroke-width="1.2"/>
          <text x="86" y="20" text-anchor="middle" fill="#27272a" font-size="9" font-weight="800">ПРОТОКОЛ ДОПРОСА</text>
          <line x1="18" y1="30" x2="154" y2="30" stroke="#e4e4e7" stroke-width="4" stroke-linecap="round"/>
          <line x1="18" y1="42" x2="130" y2="42" stroke="#e4e4e7" stroke-width="4" stroke-linecap="round"/>
          <rect x="18" y="52" width="136" height="16" rx="5" fill="#f4f4f5" stroke="#a1a1aa"/>
          <text x="86" y="64" text-anchor="middle" fill="#52525b" font-size="7" font-weight="700">замечания до подписи</text>
        </g>
        <!-- стрелка: коридор → суд -->
        <g fill="none" stroke="#71717a" stroke-width="1.4" stroke-dasharray="5 4" opacity="0.7">
          <path d="M220,136 L220,148"/>
          <path d="M220,240 L220,268"/>
        </g>
        <g transform="translate(168, 362)">
          <rect width="104" height="26" rx="13" fill="#18181b"/>
          <text x="52" y="17" text-anchor="middle" fill="#fafafa" font-size="8" font-weight="700" letter-spacing="0.05em">до суда · УПК</text>
        </g>
      </svg>
    </div>
  </div>
</section>
