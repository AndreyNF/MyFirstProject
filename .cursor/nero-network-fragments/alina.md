=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

<section id="l24-hero-arb-mir-settle" class="hero-arb-mir-settle" aria-label="Мировое соглашение в арбитраже">
  <style>
    .hero-arb-mir-settle {
      position: relative;
      min-height: 100vh;
      min-height: 100dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 120px 24px 80px;
      background: linear-gradient(168deg, #fcfcfd 0%, #f6f8fb 40%, #eef2f7 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .hero-arb-mir-settle::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 52% 46% at 90% 10%, rgba(30, 58, 138, 0.07) 0%, transparent 55%),
        radial-gradient(ellipse 44% 40% at 8% 92%, rgba(163, 24, 48, 0.05) 0%, transparent 50%);
      pointer-events: none;
    }
    .hero-arb-mir-settle__inner {
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
    .hero-arb-mir-settle__badge {
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
    .hero-arb-mir-settle__badge-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #1e3a8a;
      flex-shrink: 0;
    }
    .hero-arb-mir-settle__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.55rem, 3.5vw, 2.35rem);
      line-height: 1.2;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .hero-arb-mir-settle__h1-accent {
      color: #1e3a8a;
    }
    .hero-arb-mir-settle__sub {
      margin: 0 0 26px;
      max-width: 38em;
      font-size: clamp(1rem, 1.55vw, 1.1rem);
      line-height: 1.55;
      color: #475569;
    }
    .hero-arb-mir-settle__forks {
      list-style: none;
      padding: 0;
      margin: 0 0 30px;
    }
    .hero-arb-mir-settle__fork {
      display: flex;
      gap: 14px;
      align-items: flex-start;
      margin-bottom: 13px;
      font-size: 0.93rem;
      line-height: 1.45;
      color: #334155;
    }
    .hero-arb-mir-settle__fork-tag {
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
    .hero-arb-mir-settle__fork--plus .hero-arb-mir-settle__fork-tag {
      background: #1e3a8a;
    }
    .hero-arb-mir-settle__fork--risk .hero-arb-mir-settle__fork-tag {
      background: #a31830;
    }
    .hero-arb-mir-settle__fork--apk .hero-arb-mir-settle__fork-tag {
      background: #475569;
    }
    .hero-arb-mir-settle__cta {
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
    .hero-arb-mir-settle__cta:hover {
      background: #8b1528;
    }
    .hero-arb-mir-settle__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (prefers-reduced-motion: no-preference) {
      .hero-a14-bridge-deck {
        animation: hero-a14-bridge-glow 3.2s ease-in-out infinite;
      }
      .hero-a14-handshake {
        animation: hero-a14-handshake-pulse 2.4s ease-in-out infinite;
      }
      .hero-a14-scales-beam {
        animation: hero-a14-scales-sway 4s ease-in-out infinite;
        transform-origin: 240px 198px;
      }
      .hero-a14-flow-dot {
        animation: hero-a14-flow-dot 2.8s linear infinite;
      }
      .hero-a14-stamp-ring {
        animation: hero-a14-stamp 2.6s ease-out infinite;
      }
    }
    @keyframes hero-a14-bridge-glow {
      0%, 100% { filter: drop-shadow(0 0 0 rgba(30, 58, 138, 0)); }
      50% { filter: drop-shadow(0 0 10px rgba(30, 58, 138, 0.35)); }
    }
    @keyframes hero-a14-handshake-pulse {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.04); opacity: 0.92; }
    }
    @keyframes hero-a14-scales-sway {
      0%, 100% { transform: rotate(0deg); }
      25% { transform: rotate(-2.5deg); }
      75% { transform: rotate(2.5deg); }
    }
    @keyframes hero-a14-flow-dot {
      0% { offset-distance: 0%; opacity: 0; }
      10% { opacity: 1; }
      90% { opacity: 1; }
      100% { offset-distance: 100%; opacity: 0; }
    }
    @keyframes hero-a14-stamp {
      0%, 70%, 100% { opacity: 0; transform: scale(0.85); }
      78% { opacity: 0.85; transform: scale(1); }
      88% { opacity: 0.4; transform: scale(1.02); }
    }
    @media (max-width: 900px) {
      .hero-arb-mir-settle__inner {
        grid-template-columns: 1fr;
        gap: 28px;
      }
      .hero-arb-mir-settle__visual {
        order: -1;
        max-height: 320px;
      }
      .hero-arb-mir-settle__fork-tag {
        min-width: 92px;
        font-size: 0.66rem;
      }
    }
    @media (prefers-reduced-motion: reduce) {
      .hero-a14-bridge-deck,
      .hero-a14-handshake,
      .hero-a14-scales-beam,
      .hero-a14-flow-dot,
      .hero-a14-stamp-ring {
        animation: none !important;
      }
    }
  </style>
  <div class="hero-arb-mir-settle__inner">
    <div class="hero-arb-mir-settle__content">
      <div class="hero-arb-mir-settle__badge">
        <span class="hero-arb-mir-settle__badge-dot" aria-hidden="true"></span>
        Legis24 ARB · A14 · АПК · ст. 139–142 · 2026
      </div>
      <h1 class="hero-arb-mir-settle__h1">
        <span class="hero-arb-mir-settle__h1-accent">Мировое соглашение</span> в арбитраже
      </h1>
      <p class="hero-arb-mir-settle__sub">
        Стратегия для экономических споров: когда мир с контрагентом снижает издержки, а когда — создаёт новые риски в арбитражном суде
      </p>
      <ul class="hero-arb-mir-settle__forks">
        <li class="hero-arb-mir-settle__fork hero-arb-mir-settle__fork--plus">
          <span class="hero-arb-mir-settle__fork-tag">Плюсы</span>
          <span><strong>Экономия процесса</strong> — прекращение спора, возврат госпошлины, исполнительный лист без полного доказывания</span>
        </li>
        <li class="hero-arb-mir-settle__fork hero-arb-mir-settle__fork--risk">
          <span class="hero-arb-mir-settle__fork-tag">Риски</span>
          <span><strong>Отказ в утверждении</strong> — налоги на прощение, санкции за просрочку, res judicata только после определения суда</span>
        </li>
        <li class="hero-arb-mir-settle__fork hero-arb-mir-settle__fork--apk">
          <span class="hero-arb-mir-settle__fork-tag">ст. 139–142</span>
          <span><strong>На любой стадии</strong> — от первого заседания до исполнения; суд проверяет законность условий перед утверждением</span>
        </li>
      </ul>
      <a class="hero-arb-mir-settle__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по стратегии мирового соглашения в арбитраже</a>
    </div>
    <div class="hero-arb-mir-settle__visual" aria-hidden="true">
      <svg viewBox="0 0 480 420" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:480px" role="img" aria-label="Мост соглашения: стороны спора, handshake и весы на мосту, утверждение арбитражным судом">
        <defs>
          <linearGradient id="hero-a14-sky" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f8fafc"/>
            <stop offset="100%" stop-color="#e2e8f0"/>
          </linearGradient>
          <linearGradient id="hero-a14-court" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1e3a8a"/>
            <stop offset="100%" stop-color="#0f2744"/>
          </linearGradient>
          <linearGradient id="hero-a14-bridge" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#93c5fd"/>
            <stop offset="50%" stop-color="#1e3a8a"/>
            <stop offset="100%" stop-color="#93c5fd"/>
          </linearGradient>
          <linearGradient id="hero-a14-gap" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#fef2f2"/>
            <stop offset="100%" stop-color="#fee2e2"/>
          </linearGradient>
          <linearGradient id="hero-a14-save" x1="0%" y1="100%" x2="0%" y2="0%">
            <stop offset="0%" stop-color="#dbeafe"/>
            <stop offset="100%" stop-color="#eff6ff"/>
          </linearGradient>
          <filter id="hero-a14-shadow" x="-8%" y="-8%" width="116%" height="116%">
            <feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="#0f172a" flood-opacity="0.12"/>
          </filter>
          <marker id="hero-a14-arrow" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7 Z" fill="#64748b"/>
          </marker>
          <marker id="hero-a14-arrow-navy" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7 Z" fill="#1e3a8a"/>
          </marker>
          <path id="hero-a14-bridge-path" d="M72 248 Q240 168 408 248" fill="none"/>
        </defs>
        <rect x="8" y="10" width="464" height="400" rx="16" fill="url(#hero-a14-sky)" stroke="#cbd5e1" stroke-width="1.2"/>
        <!-- арбитражный суд — утверждение -->
        <g transform="translate(140, 16)">
          <rect x="0" y="22" width="200" height="54" rx="4" fill="url(#hero-a14-court)"/>
          <polygon points="100,0 200,22 0,22" fill="#1e40af"/>
          <text x="100" y="48" text-anchor="middle" fill="#e2e8f0" font-size="8" font-weight="700" letter-spacing="0.08em">АРБИТРАЖ · УТВЕРЖДЕНИЕ</text>
          <text x="100" y="62" text-anchor="middle" fill="#93c5fd" font-size="7">ст. 141 АПК · определение суда</text>
        </g>
        <!-- штамп утверждения -->
        <g class="hero-a14-stamp-ring" transform="translate(340, 52)">
          <circle cx="0" cy="0" r="22" fill="none" stroke="#1e3a8a" stroke-width="2" stroke-dasharray="4 3" opacity="0.7"/>
          <text x="0" y="-4" text-anchor="middle" fill="#1e3a8a" font-size="6" font-weight="800">УТВЕРЖДЕНО</text>
          <text x="0" y="6" text-anchor="middle" fill="#64748b" font-size="5">ст. 141</text>
        </g>
        <!-- левый берег: спор -->
        <g filter="url(#hero-a14-shadow)">
          <rect x="24" y="248" width="96" height="14" rx="3" fill="#94a3b8"/>
          <rect x="28" y="220" width="88" height="28" rx="8" fill="#fff" stroke="#a31830" stroke-width="1.2"/>
          <text x="72" y="234" text-anchor="middle" fill="#a31830" font-size="7" font-weight="800">СТОРОНА А</text>
          <text x="72" y="244" text-anchor="middle" fill="#64748b" font-size="6">иск · спор</text>
          <!-- растущие издержки -->
          <rect x="36" y="196" width="12" height="20" rx="2" fill="#fecaca"/>
          <rect x="52" y="188" width="12" height="28" rx="2" fill="#fca5a5"/>
          <rect x="68" y="178" width="12" height="38" rx="2" fill="#f87171"/>
          <rect x="84" y="170" width="12" height="46" rx="2" fill="#a31830" opacity="0.85"/>
          <text x="72" y="164" text-anchor="middle" fill="#a31830" font-size="6" font-weight="700">издержки ↑</text>
        </g>
        <!-- правый берег: мир -->
        <g filter="url(#hero-a14-shadow)">
          <rect x="360" y="248" width="96" height="14" rx="3" fill="#94a3b8"/>
          <rect x="364" y="220" width="88" height="28" rx="8" fill="#fff" stroke="#1e3a8a" stroke-width="1.2"/>
          <text x="408" y="234" text-anchor="middle" fill="#1e3a8a" font-size="7" font-weight="800">СТОРОНА B</text>
          <text x="408" y="244" text-anchor="middle" fill="#64748b" font-size="6">контрагент</text>
          <!-- сниженные издержки -->
          <rect x="372" y="206" width="12" height="10" rx="2" fill="#93c5fd"/>
          <rect x="388" y="200" width="12" height="16" rx="2" fill="#60a5fa"/>
          <rect x="404" y="194" width="12" height="22" rx="2" fill="#3b82f6"/>
          <rect x="420" y="188" width="12" height="28" rx="2" fill="#1e3a8a" opacity="0.75"/>
          <text x="408" y="182" text-anchor="middle" fill="#1e3a8a" font-size="6" font-weight="700">экономия ↓</text>
        </g>
        <!-- пропасть спора -->
        <rect x="120" y="262" width="240" height="48" rx="6" fill="url(#hero-a14-gap)" stroke="#fecaca" stroke-width="1" stroke-dasharray="5 4"/>
        <text x="240" y="282" text-anchor="middle" fill="#a31830" font-size="7" font-weight="700">РИСК · отказ в утверждении</text>
        <text x="240" y="296" text-anchor="middle" fill="#991b1b" font-size="6">нарушение закона · налоги · санкции</text>
        <!-- мост соглашения -->
        <g class="hero-a14-bridge-deck">
          <path d="M68 252 Q240 162 412 252" stroke="url(#hero-a14-bridge)" stroke-width="10" fill="none" stroke-linecap="round"/>
          <path d="M68 252 Q240 162 412 252" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.35"/>
          <!-- опоры -->
          <rect x="108" y="248" width="8" height="36" rx="2" fill="#64748b"/>
          <rect x="364" y="248" width="8" height="36" rx="2" fill="#64748b"/>
          <text x="240" y="152" text-anchor="middle" fill="#1e3a8a" font-size="8" font-weight="800" letter-spacing="0.06em">МОСТ СОГЛАШЕНИЯ</text>
        </g>
        <!-- точка движения по мосту -->
        <circle class="hero-a14-flow-dot" r="5" fill="#a31830" stroke="#fff" stroke-width="1.5" style="offset-path: path('M72 248 Q240 168 408 248'); offset-rotate: 0deg;"/>
        <!-- весы на центре моста -->
        <g class="hero-a14-scales-beam">
          <line x1="240" y1="198" x2="240" y2="218" stroke="#64748b" stroke-width="2"/>
          <line x1="188" y1="198" x2="292" y2="198" stroke="#475569" stroke-width="2.5"/>
          <circle cx="240" cy="198" r="5" fill="#f59e0b" stroke="#fff" stroke-width="1.5"/>
          <!-- чаша: процесс -->
          <line x1="188" y1="198" x2="176" y2="214" stroke="#64748b" stroke-width="1.5"/>
          <path d="M160 214 Q188 228 216 214" fill="none" stroke="#a31830" stroke-width="1.5"/>
          <rect x="168" y="216" width="40" height="22" rx="4" fill="#fef2f2" stroke="#fca5a5"/>
          <text x="188" y="230" text-anchor="middle" fill="#a31830" font-size="6" font-weight="700">процесс</text>
          <!-- чаша: мир -->
          <line x1="292" y1="198" x2="304" y2="214" stroke="#64748b" stroke-width="1.5"/>
          <path d="M288 214 Q316 228 344 214" fill="none" stroke="#1e3a8a" stroke-width="1.5"/>
          <rect x="296" y="216" width="40" height="22" rx="4" fill="url(#hero-a14-save)" stroke="#93c5fd"/>
          <text x="316" y="230" text-anchor="middle" fill="#1e3a8a" font-size="6" font-weight="700">мир</text>
        </g>
        <!-- handshake -->
        <g class="hero-a14-handshake" transform="translate(240, 248)">
          <circle cx="0" cy="0" r="28" fill="#fff" stroke="#1e3a8a" stroke-width="1.5" filter="url(#hero-a14-shadow)"/>
          <!-- левая рука -->
          <path d="M-18 4 L-8 -6 L-2 0 L-6 8 L-14 10 Z" fill="#fde68a" stroke="#d97706" stroke-width="0.8"/>
          <rect x="-20" y="6" width="14" height="8" rx="3" fill="#1e3a8a" opacity="0.85"/>
          <!-- правая рука -->
          <path d="M18 4 L8 -6 L2 0 L6 8 L14 10 Z" fill="#fde68a" stroke="#d97706" stroke-width="0.8"/>
          <rect x="6" y="6" width="14" height="8" rx="3" fill="#a31830" opacity="0.85"/>
          <!-- сжатие -->
          <ellipse cx="0" cy="2" rx="10" ry="6" fill="#fcd34d" stroke="#b45309" stroke-width="0.6"/>
          <text x="0" y="-38" text-anchor="middle" fill="#334155" font-size="7" font-weight="700">согласие сторон</text>
        </g>
        <!-- стрелки к суду -->
        <path d="M240 88 L240 118" stroke="#1e3a8a" stroke-width="1.5" fill="none" marker-end="url(#hero-a14-arrow-navy)"/>
        <path d="M240 276 L240 318" stroke="#64748b" stroke-width="1.2" fill="none" stroke-dasharray="3 3"/>
        <!-- итоговая панель -->
        <g filter="url(#hero-a14-shadow)" transform="translate(28, 328)">
          <rect width="424" height="68" rx="10" fill="#fff" stroke="#cbd5e1" stroke-width="1"/>
          <rect x="0" y="0" width="140" height="68" rx="10" fill="#eff6ff" stroke="none"/>
          <text x="70" y="24" text-anchor="middle" fill="#1e3a8a" font-size="7" font-weight="800">ПЛЮС</text>
          <text x="70" y="38" text-anchor="middle" fill="#475569" font-size="6">прекращение спора</text>
          <text x="70" y="50" text-anchor="middle" fill="#475569" font-size="6">возврат пошлины</text>
          <line x1="140" y1="12" x2="140" y2="56" stroke="#e2e8f0"/>
          <rect x="140" y="0" width="144" height="68" fill="#fff" stroke="none"/>
          <text x="212" y="24" text-anchor="middle" fill="#334155" font-size="7" font-weight="800">СТРАТЕГИЯ</text>
          <text x="212" y="38" text-anchor="middle" fill="#64748b" font-size="6">оценка до подписания</text>
          <text x="212" y="50" text-anchor="middle" fill="#64748b" font-size="6">ст. 139–142 АПК</text>
          <line x1="284" y1="12" x2="284" y2="56" stroke="#e2e8f0"/>
          <rect x="284" y="0" width="140" height="68" rx="10" fill="#fef2f2" stroke="none"/>
          <text x="354" y="24" text-anchor="middle" fill="#a31830" font-size="7" font-weight="800">РИСК</text>
          <text x="354" y="38" text-anchor="middle" fill="#64748b" font-size="6">отказ суда</text>
          <text x="354" y="50" text-anchor="middle" fill="#64748b" font-size="6">налоги · санкции</text>
        </g>
        <text x="240" y="408" text-anchor="middle" fill="#64748b" font-size="7">спор → мост соглашения → утверждение арбитражным судом</text>
      </svg>
    </div>
  </div>
</section>

## Передача Наташе

**SLUG:** mirovoe-soglashenie-v-arbitrazhe-plyusy-riski

**Hero ID:** `#l24-hero-arb-mir-settle`

**Класс страницы:** `mirovoe-soglashenie-v-arbitrazhe-plyusy-riski-page`

**MCP-only:** hero содержит только static SVG + inline CSS + `@keyframes`. Без `<canvas>` и без `<script>`. Не удалять анимации и SVG-разметку.

**Метафора:** «мост соглашения» — два берега спора, handshake и весы на мосту, утверждение арбитражным судом (отличие от A11: не АУ/оспаривание сделок, а мировое соглашение сторон).
