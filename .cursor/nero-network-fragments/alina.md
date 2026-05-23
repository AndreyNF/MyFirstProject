=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

<section id="l24-hero-arb-kred" class="hero-arb-kred" aria-label="Арбитражный спор с кредитором">
  <style>
    .hero-arb-kred {
      position: relative;
      min-height: 100vh;
      min-height: 100dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 120px 24px 80px;
      background: linear-gradient(168deg, #f8fafc 0%, #eef2f7 42%, #e8eef6 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .hero-arb-kred::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 60% 50% at 92% 12%, rgba(30, 58, 138, 0.09) 0%, transparent 55%),
        radial-gradient(ellipse 50% 45% at 6% 88%, rgba(15, 39, 68, 0.07) 0%, transparent 50%);
      pointer-events: none;
    }
    .hero-arb-kred__inner {
      position: relative;
      z-index: 1;
      max-width: 1200px;
      margin: 0 auto;
      width: 100%;
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 48px;
      align-items: center;
    }
    .hero-arb-kred__badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 18px;
      padding: 8px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.92);
      border: 1px solid rgba(15, 23, 42, 0.12);
      font-size: 0.82rem;
      font-weight: 600;
      letter-spacing: 0.02em;
      color: #334155;
    }
    .hero-arb-kred__badge-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #1e3a8a;
      flex-shrink: 0;
    }
    .hero-arb-kred__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.6rem, 3.6vw, 2.4rem);
      line-height: 1.2;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .hero-arb-kred__h1-accent {
      color: #1e3a8a;
    }
    .hero-arb-kred__sub {
      margin: 0 0 28px;
      max-width: 38em;
      font-size: clamp(1rem, 1.6vw, 1.12rem);
      line-height: 1.55;
      color: #475569;
    }
    .hero-arb-kred__tracks {
      list-style: none;
      padding: 0;
      margin: 0 0 32px;
    }
    .hero-arb-kred__track {
      display: flex;
      gap: 14px;
      align-items: flex-start;
      margin-bottom: 14px;
      font-size: 0.94rem;
      line-height: 1.45;
      color: #334155;
    }
    .hero-arb-kred__track-label {
      flex-shrink: 0;
      min-width: 118px;
      padding: 6px 10px;
      border-radius: 6px;
      background: #0f2744;
      color: #fff;
      font-weight: 700;
      font-size: 0.72rem;
      letter-spacing: 0.04em;
      text-align: center;
      text-transform: uppercase;
    }
    .hero-arb-kred__track--bank .hero-arb-kred__track-label {
      background: #1e3a8a;
    }
    .hero-arb-kred__track--dual .hero-arb-kred__track-label {
      background: #a31830;
    }
    .hero-arb-kred__cta {
      display: inline-block;
      background: #a31830;
      color: #fff !important;
      padding: 14px 28px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(163, 24, 48, 0.22);
    }
    .hero-arb-kred__cta:hover {
      background: #8b1528;
    }
    .hero-arb-kred__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (max-width: 900px) {
      .hero-arb-kred__inner {
        grid-template-columns: 1fr;
        gap: 32px;
      }
      .hero-arb-kred__visual {
        order: -1;
        max-height: 320px;
      }
      .hero-arb-kred__track-label {
        min-width: 96px;
        font-size: 0.68rem;
      }
    }
  </style>
  <div class="hero-arb-kred__inner">
    <div class="hero-arb-kred__content">
      <div class="hero-arb-kred__badge">
        <span class="hero-arb-kred__badge-dot" aria-hidden="true"></span>
        АПК · 127-ФЗ · защита ответчика · три трека · 2026
      </div>
      <h1 class="hero-arb-kred__h1">
        <span class="hero-arb-kred__h1-accent">Арбитражный спор с кредитором:</span> сроки, подсудность и первая стратегия ответа
      </h1>
      <p class="hero-arb-kred__sub">
        Иск в арбитраж или требование в банкротстве — разберём подсудность, сроки и план защиты ответчика до первого заседания.
      </p>
      <ul class="hero-arb-kred__tracks">
        <li class="hero-arb-kred__track hero-arb-kred__track--isk">
          <span class="hero-arb-kred__track-label">Иск в АС</span>
          <span><strong>Подсудность и сроки</strong> — отзыв, возражения, ходатайства до первого заседания по АПК</span>
        </li>
        <li class="hero-arb-kred__track hero-arb-kred__track--bank">
          <span class="hero-arb-kred__track-label">Банкротство</span>
          <span><strong>Требование в реестр</strong> — возражения, оспаривание, связка с арбитражным иском кредитора</span>
        </li>
        <li class="hero-arb-kred__track hero-arb-kred__track--dual">
          <span class="hero-arb-kred__track-label">Двойной фронт</span>
          <span><strong>Иск + дело о банкротстве</strong> — единая стратегия ответчика, чтобы не проиграть на одном треке</span>
        </li>
      </ul>
      <a class="hero-arb-kred__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Получить консультацию по арбитражному спору с кредитором — стратегия ответа и представительство в суде</a>
    </div>
    <div class="hero-arb-kred__visual" aria-hidden="true">
      <svg viewBox="0 0 440 400" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:440px" role="img" aria-label="Три трека защиты ответчика: арбитражный иск, банкротство кредитора, двойной фронт">
        <defs>
          <linearGradient id="hero-arb-scene" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0f2744"/>
            <stop offset="50%" stop-color="#1e3a8a"/>
            <stop offset="100%" stop-color="#172554"/>
          </linearGradient>
          <linearGradient id="hero-arb-panel" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1e40af"/>
            <stop offset="100%" stop-color="#0f2744"/>
          </linearGradient>
          <linearGradient id="hero-arb-card" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#ffffff"/>
            <stop offset="100%" stop-color="#f1f5f9"/>
          </linearGradient>
          <linearGradient id="hero-arb-fork" x1="0%" y1="50%" x2="100%" y2="50%">
            <stop offset="0%" stop-color="#93c5fd"/>
            <stop offset="45%" stop-color="#60a5fa"/>
            <stop offset="100%" stop-color="#f87171"/>
          </linearGradient>
          <filter id="hero-arb-shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#020617" flood-opacity="0.26"/>
          </filter>
          <filter id="hero-arb-shadow-soft" x="-8%" y="-8%" width="116%" height="116%">
            <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#1e293b" flood-opacity="0.12"/>
          </filter>
          <marker id="hero-arb-arrow" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7 Z" fill="#93c5fd"/>
          </marker>
        </defs>
        <rect x="14" y="18" width="412" height="364" rx="18" fill="url(#hero-arb-scene)" stroke="#0c1a33" stroke-width="1.5" filter="url(#hero-arb-shadow)"/>
        <text x="220" y="48" text-anchor="middle" fill="#e2e8f0" font-size="10" font-weight="700" letter-spacing="0.12em">СТРАТЕГИЯ ОТВЕТЧИКА</text>
        <line x1="44" y1="58" x2="396" y2="58" stroke="rgba(148,163,184,0.35)" stroke-width="1"/>
        <!-- центр: ответчик -->
        <circle cx="220" cy="118" r="34" fill="url(#hero-arb-card)" stroke="#93c5fd" stroke-width="2" filter="url(#hero-arb-shadow-soft)"/>
        <text x="220" y="114" text-anchor="middle" fill="#0f2744" font-size="9" font-weight="700">ОТВЕТЧИК</text>
        <text x="220" y="128" text-anchor="middle" fill="#475569" font-size="8">защита</text>
        <!-- развилка -->
        <path d="M220 152 L220 178" stroke="url(#hero-arb-fork)" stroke-width="3" fill="none"/>
        <path d="M220 178 L92 210" stroke="#60a5fa" stroke-width="2.5" fill="none" marker-end="url(#hero-arb-arrow)"/>
        <path d="M220 178 L220 210" stroke="#93c5fd" stroke-width="2.5" fill="none"/>
        <path d="M220 178 L348 210" stroke="#f87171" stroke-width="2.5" fill="none"/>
        <!-- трек 1: арбитраж -->
        <g transform="translate(28, 218)">
          <rect width="128" height="148" rx="10" fill="url(#hero-arb-panel)" opacity="0.95"/>
          <text x="64" y="22" text-anchor="middle" fill="#bfdbfe" font-size="8" font-weight="700" letter-spacing="0.08em">ИСК В АС</text>
          <rect x="14" y="34" width="100" height="36" rx="6" fill="rgba(255,255,255,0.12)"/>
          <text x="22" y="52" fill="#fff" font-size="8">ст. 35–37 АПК</text>
          <text x="22" y="64" fill="#cbd5e1" font-size="7">подсудность</text>
          <rect x="14" y="78" width="100" height="28" rx="5" fill="rgba(255,255,255,0.08)"/>
          <text x="22" y="96" fill="#e2e8f0" font-size="7">отзыв · возражения</text>
          <rect x="14" y="114" width="100" height="22" rx="5" fill="#a31830"/>
          <text x="64" y="129" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">1-е заседание</text>
        </g>
        <!-- трек 2: банкротство -->
        <g transform="translate(156, 218)">
          <rect width="128" height="148" rx="10" fill="url(#hero-arb-card)" stroke="#1e3a8a" stroke-width="1.2" filter="url(#hero-arb-shadow-soft)"/>
          <text x="64" y="22" text-anchor="middle" fill="#1e3a8a" font-size="8" font-weight="700" letter-spacing="0.08em">БАНКРОТСТВО</text>
          <rect x="14" y="34" width="100" height="36" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>
          <text x="22" y="52" fill="#1e3a8a" font-size="8">127-ФЗ</text>
          <text x="22" y="64" fill="#64748b" font-size="7">требование в реестр</text>
          <rect x="14" y="78" width="100" height="28" rx="5" fill="#f8fafc" stroke="#e2e8f0"/>
          <text x="22" y="96" fill="#334155" font-size="7">возражения · оспаривание</text>
          <rect x="14" y="114" width="100" height="22" rx="5" fill="#1e3a8a"/>
          <text x="64" y="129" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">реестр</text>
        </g>
        <!-- трек 3: двойной фронт -->
        <g transform="translate(284, 218)">
          <rect width="128" height="148" rx="10" fill="#7f1d1d" opacity="0.92"/>
          <text x="64" y="22" text-anchor="middle" fill="#fecaca" font-size="8" font-weight="700" letter-spacing="0.06em">ДВОЙНОЙ ФРОНТ</text>
          <line x1="20" y1="50" x2="108" y2="50" stroke="rgba(255,255,255,0.35)" stroke-width="1"/>
          <text x="64" y="72" text-anchor="middle" fill="#fff" font-size="8">иск + банкротство</text>
          <text x="64" y="88" text-anchor="middle" fill="#fecaca" font-size="7">синхрон сроков</text>
          <rect x="14" y="98" width="100" height="38" rx="6" fill="rgba(0,0,0,0.2)" stroke="#fca5a5"/>
          <text x="64" y="116" text-anchor="middle" fill="#fff" font-size="7">единый план</text>
          <text x="64" y="128" text-anchor="middle" fill="#fecaca" font-size="7">ответчика</text>
        </g>
        <!-- сроки внизу -->
        <rect x="44" y="372" width="352" height="2" rx="1" fill="rgba(148,163,184,0.4)"/>
        <text x="72" y="390" fill="#94a3b8" font-size="7">сроки АПК</text>
        <text x="200" y="390" text-anchor="middle" fill="#94a3b8" font-size="7">2 мес. требования</text>
        <text x="368" y="390" text-anchor="end" fill="#fca5a5" font-size="7">до 1-го заседания</text>
      </svg>
    </div>
  </div>
</section>

## Передача Наташе
SLUG: arbitrazhnyj-spor-s-kreditorom-sroki-strategiya
ВНИМАНИЕ: hero — только static SVG + inline CSS; без `<canvas>` и `<script>` (MCP publish удаляет scripts).
