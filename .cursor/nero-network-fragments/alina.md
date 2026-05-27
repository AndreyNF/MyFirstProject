=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

<section id="l24-hero-ip-tz-reg-etapy" class="hero-ip-tz-reg-etapy" aria-label="Регистрация товарного знака: этапы и отказ Роспатента">
  <style>
    .hero-ip-tz-reg-etapy {
      position: relative;
      min-height: 85vh;
      min-height: 85dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(162deg, #fafbfc 0%, #f4f7fb 45%, #f0f4f8 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .hero-ip-tz-reg-etapy::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 58% 44% at 92% 14%, rgba(30, 64, 175, 0.07) 0%, transparent 55%),
        radial-gradient(ellipse 42% 38% at 6% 86%, rgba(163, 24, 48, 0.04) 0%, transparent 50%);
      pointer-events: none;
    }
    .hero-ip-tz-reg-etapy__inner {
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
    .hero-ip-tz-reg-etapy__badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 18px;
      padding: 8px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.92);
      border: 1px solid rgba(15, 23, 42, 0.1);
      font-size: 0.82rem;
      font-weight: 600;
      letter-spacing: 0.02em;
      color: #334155;
    }
    .hero-ip-tz-reg-etapy__badge-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #1e40af;
      flex-shrink: 0;
    }
    .hero-ip-tz-reg-etapy__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.55rem, 3.6vw, 2.4rem);
      line-height: 1.18;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .hero-ip-tz-reg-etapy__h1-accent {
      color: #1e40af;
    }
    .hero-ip-tz-reg-etapy__sub {
      margin: 0 0 28px;
      max-width: 38em;
      font-size: clamp(1rem, 1.6vw, 1.12rem);
      line-height: 1.55;
      color: #475569;
    }
    .hero-ip-tz-reg-etapy__letters {
      list-style: none;
      padding: 0;
      margin: 0 0 32px;
    }
    .hero-ip-tz-reg-etapy__letter {
      display: flex;
      gap: 14px;
      align-items: flex-start;
      margin-bottom: 14px;
      font-size: 0.94rem;
      line-height: 1.45;
      color: #334155;
    }
    .hero-ip-tz-reg-etapy__letter-tag {
      flex-shrink: 0;
      min-width: 88px;
      padding: 6px 10px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.68rem;
      letter-spacing: 0.04em;
      text-align: center;
      text-transform: uppercase;
      color: #fff;
    }
    .hero-ip-tz-reg-etapy__letter--req .hero-ip-tz-reg-etapy__letter-tag {
      background: #475569;
    }
    .hero-ip-tz-reg-etapy__letter--notif .hero-ip-tz-reg-etapy__letter-tag {
      background: #b45309;
    }
    .hero-ip-tz-reg-etapy__letter--ref .hero-ip-tz-reg-etapy__letter-tag {
      background: #a31830;
    }
    .hero-ip-tz-reg-etapy__cta {
      display: inline-block;
      background: #a31830;
      color: #fff !important;
      padding: 14px 28px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(163, 24, 48, 0.22);
      line-height: 1.35;
    }
    .hero-ip-tz-reg-etapy__cta:hover {
      background: #8b1528;
    }
    .hero-ip-tz-reg-etapy__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (prefers-reduced-motion: no-preference) {
      .hero-ip-tz-reg-etapy__env--1 {
        animation: hero-tz-reg-float 4.2s ease-in-out infinite;
      }
      .hero-ip-tz-reg-etapy__env--2 {
        animation: hero-tz-reg-float 4.2s ease-in-out 1.4s infinite;
      }
      .hero-ip-tz-reg-etapy__env--3 {
        animation: hero-tz-reg-float 4.2s ease-in-out 2.8s infinite;
      }
      .hero-ip-tz-reg-etapy__route-dash {
        stroke-dasharray: 8 6;
        animation: hero-tz-reg-dash 2.4s linear infinite;
      }
      .hero-ip-tz-reg-etapy__pulse {
        animation: hero-tz-reg-pulse 3.6s ease-in-out infinite;
      }
      .hero-ip-tz-reg-etapy__pulse--2 {
        animation-delay: 1.2s;
      }
      .hero-ip-tz-reg-etapy__pulse--3 {
        animation-delay: 2.4s;
      }
      .hero-ip-tz-reg-etapy__cert-glow {
        animation: hero-tz-reg-glow 3s ease-in-out infinite;
      }
    }
    @keyframes hero-tz-reg-float {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-6px); }
    }
    @keyframes hero-tz-reg-dash {
      to { stroke-dashoffset: -28; }
    }
    @keyframes hero-tz-reg-pulse {
      0%, 100% { opacity: 0.55; transform: scale(1); }
      50% { opacity: 1; transform: scale(1.06); }
    }
    @keyframes hero-tz-reg-glow {
      0%, 100% { opacity: 0.7; }
      50% { opacity: 1; }
    }
    @media (prefers-reduced-motion: reduce) {
      .hero-ip-tz-reg-etapy__env--1,
      .hero-ip-tz-reg-etapy__env--2,
      .hero-ip-tz-reg-etapy__env--3,
      .hero-ip-tz-reg-etapy__route-dash,
      .hero-ip-tz-reg-etapy__pulse,
      .hero-ip-tz-reg-etapy__cert-glow {
        animation: none !important;
      }
    }
    @media (max-width: 900px) {
      .hero-ip-tz-reg-etapy {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .hero-ip-tz-reg-etapy__inner {
        grid-template-columns: 1fr;
        gap: 32px;
      }
      .hero-ip-tz-reg-etapy__visual {
        order: -1;
        max-height: 300px;
      }
      .hero-ip-tz-reg-etapy__letter-tag {
        min-width: 76px;
        font-size: 0.64rem;
      }
    }
  </style>
  <div class="hero-ip-tz-reg-etapy__inner">
    <div class="hero-ip-tz-reg-etapy__content">
      <div class="hero-ip-tz-reg-etapy__badge">
        <span class="hero-ip-tz-reg-etapy__badge-dot" aria-hidden="true"></span>
        ИС · товарный знак · Роспатент · три письма · 2026
      </div>
      <h1 class="hero-ip-tz-reg-etapy__h1">
        <span class="hero-ip-tz-reg-etapy__h1-accent">Регистрация товарного знака:</span> этапы, отказ Роспатента и обжалование
      </h1>
      <p class="hero-ip-tz-reg-etapy__sub">
        От подачи заявки в Роспатент до обжалования отказа: пошаговый разбор процедуры, сроков и правовых инструментов защиты бренда
      </p>
      <ul class="hero-ip-tz-reg-etapy__letters">
        <li class="hero-ip-tz-reg-etapy__letter hero-ip-tz-reg-etapy__letter--req">
          <span class="hero-ip-tz-reg-etapy__letter-tag">Запрос</span>
          <span><strong>Первое письмо</strong> — уточнения экспертизы; срок можно продлить, иначе заявку отзовут</span>
        </li>
        <li class="hero-ip-tz-reg-etapy__letter hero-ip-tz-reg-etapy__letter--notif">
          <span class="hero-ip-tz-reg-etapy__letter-tag">6 мес.</span>
          <span><strong>Уведомление</strong> — предварительный отказ; срок со дня направления, без продления</span>
        </li>
        <li class="hero-ip-tz-reg-etapy__letter hero-ip-tz-reg-etapy__letter--ref">
          <span class="hero-ip-tz-reg-etapy__letter-tag">4 мес.</span>
          <span><strong>Отказ</strong> — финальное решение; возражение в ППС, затем оспаривание в СИП</span>
        </li>
      </ul>
      <a class="hero-ip-tz-reg-etapy__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по регистрации и защите товарного знака</a>
    </div>
    <div class="hero-ip-tz-reg-etapy__visual" aria-hidden="true">
      <svg viewBox="0 0 440 400" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:440px" role="img" aria-label="Три письма от Роспатента: запрос, уведомление и отказ на пути к свидетельству о регистрации товарного знака">
        <defs>
          <linearGradient id="hero-tzreg-sky" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f8fafc"/>
            <stop offset="100%" stop-color="#e8eef5"/>
          </linearGradient>
          <linearGradient id="hero-tzreg-rospatent" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1e3a8a"/>
            <stop offset="100%" stop-color="#0f2744"/>
          </linearGradient>
          <linearGradient id="hero-tzreg-paper" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#ffffff"/>
            <stop offset="100%" stop-color="#f1f5f9"/>
          </linearGradient>
          <linearGradient id="hero-tzreg-cert" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fef3c7"/>
            <stop offset="100%" stop-color="#fde68a"/>
          </linearGradient>
          <filter id="hero-tzreg-shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.13"/>
          </filter>
          <marker id="hero-tzreg-arrow" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7 Z" fill="#64748b"/>
          </marker>
        </defs>
        <rect x="8" y="10" width="424" height="380" rx="16" fill="url(#hero-tzreg-sky)" stroke="#cbd5e1" stroke-width="1.2"/>
        <!-- здание Роспатента / ФИПС -->
        <g transform="translate(148, 18)">
          <rect x="0" y="32" width="144" height="64" rx="4" fill="url(#hero-tzreg-rospatent)"/>
          <polygon points="72,0 144,32 0,32" fill="#1e40af"/>
          <rect x="18" y="50" width="22" height="32" rx="2" fill="rgba(255,255,255,0.18)"/>
          <rect x="61" y="50" width="22" height="32" rx="2" fill="rgba(255,255,255,0.18)"/>
          <rect x="104" y="50" width="22" height="32" rx="2" fill="rgba(255,255,255,0.18)"/>
          <text x="72" y="88" text-anchor="middle" fill="#e2e8f0" font-size="8" font-weight="700" letter-spacing="0.08em">РОСПАТЕНТ · ФИПС</text>
        </g>
        <!-- маршрутная линия -->
        <path class="hero-ip-tz-reg-etapy__route-dash" d="M220,108 C220,140 220,168 220,200" fill="none" stroke="#94a3b8" stroke-width="2" marker-end="url(#hero-tzreg-arrow)"/>
        <path class="hero-ip-tz-reg-etapy__route-dash" d="M220,248 C220,278 220,302 220,328" fill="none" stroke="#94a3b8" stroke-width="2" marker-end="url(#hero-tzreg-arrow)" style="animation-delay:0.8s"/>
        <!-- письмо 1: запрос -->
        <g class="hero-ip-tz-reg-etapy__env--1" filter="url(#hero-tzreg-shadow)">
          <g transform="translate(52, 118)">
            <rect width="108" height="76" rx="10" fill="url(#hero-tzreg-paper)" stroke="#94a3b8" stroke-width="1.2"/>
            <text x="54" y="20" text-anchor="middle" fill="#475569" font-size="9" font-weight="800">ЗАПРОС</text>
            <line x1="16" y1="30" x2="92" y2="30" stroke="#e2e8f0" stroke-width="3" stroke-linecap="round"/>
            <line x1="16" y1="42" x2="78" y2="42" stroke="#e2e8f0" stroke-width="3" stroke-linecap="round"/>
            <line x1="16" y1="54" x2="68" y2="54" stroke="#e2e8f0" stroke-width="3" stroke-linecap="round"/>
            <rect x="16" y="60" width="56" height="12" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
            <text x="44" y="69" text-anchor="middle" fill="#64748b" font-size="7" font-weight="700">+ продление</text>
            <circle class="hero-ip-tz-reg-etapy__pulse" cx="98" cy="14" r="7" fill="#475569" opacity="0.85"/>
            <text x="98" y="17" text-anchor="middle" fill="#fff" font-size="8" font-weight="800">1</text>
          </g>
        </g>
        <!-- письмо 2: уведомление -->
        <g class="hero-ip-tz-reg-etapy__env--2" filter="url(#hero-tzreg-shadow)">
          <g transform="translate(280, 168)">
            <rect width="116" height="82" rx="10" fill="url(#hero-tzreg-paper)" stroke="#d97706" stroke-width="1.4"/>
            <text x="58" y="20" text-anchor="middle" fill="#b45309" font-size="8" font-weight="800">УВЕДОМЛЕНИЕ</text>
            <line x1="14" y1="32" x2="102" y2="32" stroke="#fde68a" stroke-width="3" stroke-linecap="round"/>
            <line x1="14" y1="44" x2="88" y2="44" stroke="#fde68a" stroke-width="3" stroke-linecap="round"/>
            <line x1="14" y1="56" x2="72" y2="56" stroke="#fde68a" stroke-width="3" stroke-linecap="round"/>
            <rect x="14" y="62" width="88" height="14" rx="4" fill="#fffbeb" stroke="#fcd34d"/>
            <text x="58" y="72" text-anchor="middle" fill="#b45309" font-size="7" font-weight="800">6 мес. · без продления</text>
            <circle class="hero-ip-tz-reg-etapy__pulse hero-ip-tz-reg-etapy__pulse--2" cx="106" cy="14" r="7" fill="#b45309" opacity="0.85"/>
            <text x="106" y="17" text-anchor="middle" fill="#fff" font-size="8" font-weight="800">2</text>
          </g>
        </g>
        <!-- письмо 3: отказ -->
        <g class="hero-ip-tz-reg-etapy__env--3" filter="url(#hero-tzreg-shadow)">
          <g transform="translate(48, 248)">
            <rect width="120" height="84" rx="10" fill="url(#hero-tzreg-paper)" stroke="#a31830" stroke-width="1.4"/>
            <text x="60" y="20" text-anchor="middle" fill="#a31830" font-size="9" font-weight="800">ОТКАЗ</text>
            <line x1="14" y1="32" x2="106" y2="32" stroke="#fecaca" stroke-width="3" stroke-linecap="round"/>
            <line x1="14" y1="44" x2="92" y2="44" stroke="#fecaca" stroke-width="3" stroke-linecap="round"/>
            <line x1="14" y1="56" x2="76" y2="56" stroke="#fecaca" stroke-width="3" stroke-linecap="round"/>
            <rect x="14" y="62" width="92" height="14" rx="4" fill="#fef2f2" stroke="#fecaca"/>
            <text x="60" y="72" text-anchor="middle" fill="#a31830" font-size="7" font-weight="800">ППС 4 мес. · СИП</text>
            <circle class="hero-ip-tz-reg-etapy__pulse hero-ip-tz-reg-etapy__pulse--3" cx="110" cy="14" r="7" fill="#a31830" opacity="0.85"/>
            <text x="110" y="17" text-anchor="middle" fill="#fff" font-size="8" font-weight="800">3</text>
          </g>
        </g>
        <!-- заявка / знак -->
        <g filter="url(#hero-tzreg-shadow)" transform="translate(168, 108)">
          <rect width="104" height="56" rx="10" fill="#fff" stroke="#1e40af" stroke-width="1.2"/>
          <circle cx="36" cy="28" r="18" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.2"/>
          <text x="36" y="33" text-anchor="middle" fill="#1e40af" font-size="16" font-weight="800" font-family="Georgia, serif">®</text>
          <text x="72" y="24" fill="#64748b" font-size="7" font-weight="600">ЗАЯВКА</text>
          <text x="72" y="38" fill="#334155" font-size="8" font-weight="700">МКТУ</text>
        </g>
        <!-- свидетельство (цель) -->
        <g class="hero-ip-tz-reg-etapy__cert-glow" filter="url(#hero-tzreg-shadow)" transform="translate(268, 312)">
          <rect width="148" height="68" rx="10" fill="url(#hero-tzreg-cert)" stroke="#d97706" stroke-width="1.4"/>
          <rect x="12" y="12" width="124" height="44" rx="6" fill="#fff" stroke="#fcd34d" stroke-width="1"/>
          <text x="74" y="28" text-anchor="middle" fill="#92400e" font-size="8" font-weight="800">СВИДЕТЕЛЬСТВО</text>
          <text x="74" y="44" text-anchor="middle" fill="#1e40af" font-size="14" font-weight="800" font-family="Georgia, serif">®</text>
          <text x="74" y="58" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600">реестр · 10 лет</text>
        </g>
        <!-- стрелки между этапами -->
        <g fill="none" stroke="#64748b" stroke-width="1.6" stroke-linecap="round" marker-end="url(#hero-tzreg-arrow)">
          <path d="M160,152 C190,168 250,178 280,188"/>
          <path d="M168,290 C200,302 240,318 268,338"/>
        </g>
        <!-- подписи сроков -->
        <text x="220" y="132" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600">формальная · по существу</text>
        <text x="220" y="272" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600">ст. 1499 · 1500 ГК РФ</text>
      </svg>
    </div>
  </div>
</section>

## Передача Наташе
SLUG: registraciya-tovarnogo-znaka-etapy-otkaz
HERO_ID: l24-hero-ip-tz-reg-etapy
SVG: да (static SVG + CSS keyframes, без canvas и script)
H1: Регистрация товарного знака: этапы, отказ Роспатента и обжалование
ПОДЗАГОЛОВОК: От подачи заявки в Роспатент до обжалования отказа: пошаговый разбор процедуры, сроков и правовых инструментов защиты бренда
CTA: https://advokat-vsem.ru/ — «Консультация по регистрации и защите товарного знака»
