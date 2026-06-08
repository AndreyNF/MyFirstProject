=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Карточка маркетплейса под процессуальным щитом» — ИП-продавец на площадке отражает волну иска о компенсации, пока суд (ВС) требует проверить цепочку иностранного права и Указ № 322 |
| **Центральная метафора** | Щит с символом ® перекрывает исковое требование (₽); за щитом — карточка товара; сбоку — абстрактный «паспорт иностранного правообладателя» (глобус + штриховка барьера, без флагов государств) |
| **Пространство** | Светлый градиентный фон; SVG-сцена в «витрине» маркетплейса (сетка ячеек); вертикаль ВС — колонна с датой 05.06.2026, не фасад СИП |
| **Движение** | Только CSS: пульс щита, мерцание барьера на глобусе, лёгкий дрейф цепочки «лицензия → цессия → иск»; `prefers-reduced-motion` отключает |
| **Палитра** | `#0f172a` текст, `#1e3a8a` акцент ВС/ТЗ, `#475569` подзаголовок, `#a31830` угроза иска, `#f8fafc`–`#f2f5f9` фон |
| **Аудитория** | ИП и селлеры на маркетплейсах, получившие претензию/иск от цессионария по иностранному ТЗ |

## Чеклист отличий от других hero

- [x] **Не POIZON** (`hero-ip-poizon-sip`): нет маршрута «Роспатент → СИП → аннулирование регистрации» и китайского бренда; фокус — **ответ на иск о компенсации**, не оспаривание регистрации
- [x] **Не Синергетик** (`hero-ip-sinergetik`): нет весов СИП, упаковки FMCG и штампа «766 млн отмена»; инстанция — **ВС 05.06.2026**, не постановление СИП
- [x] **Уникальная сцена**: маркетплейс-карточка + щит ® + абстрактный глобус-барьер (недружественность) + цепочка лицензия→цессия→иск + свиток Указа № 322
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Свой `id`/`class`: `l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany`

```html
<section id="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany" class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany" aria-label="ВС 2026: защита от компенсации за товарный знак иностранца из недружественной страны">
  <style>
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(152deg, #fefefe 0%, #f7f9fc 38%, #f1f5f9 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 46% 40% at 92% 6%, rgba(30, 58, 138, 0.07) 0%, transparent 55%),
        radial-gradient(ellipse 34% 32% at 6% 88%, rgba(163, 24, 48, 0.04) 0%, transparent 50%);
      pointer-events: none;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__inner {
      position: relative;
      z-index: 1;
      max-width: 1200px;
      margin: 0 auto;
      width: 100%;
      display: grid;
      grid-template-columns: 1.04fr 0.96fr;
      gap: 44px;
      align-items: center;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 18px;
      padding: 8px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid rgba(15, 23, 42, 0.1);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #334155;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #1e3a8a;
      flex-shrink: 0;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.46rem, 3.3vw, 2.26rem);
      line-height: 1.22;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__h1-accent {
      color: #1e3a8a;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.48vw, 1.1rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0 0 26px;
      padding: 0;
      list-style: none;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__fact--accent {
      border-color: #bfdbfe;
      color: #1e3a8a;
      background: #eff6ff;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__fact--warn {
      border-color: #fecaca;
      color: #991b1b;
      background: #fef2f2;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__cta {
      display: inline-block;
      background: #a31830;
      color: #fff !important;
      padding: 14px 28px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(163, 24, 48, 0.2);
      line-height: 1.35;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__cta:hover {
      background: #8b1528;
    }
    .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (prefers-reduced-motion: no-preference) {
      .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__shield-pulse {
        animation: hero-vs322-shield 4.2s ease-in-out infinite;
      }
      .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__barrier-blink {
        animation: hero-vs322-barrier 3.6s ease-in-out infinite;
      }
      .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__chain-flow {
        animation: hero-vs322-chain 5s ease-in-out infinite;
      }
      .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__claim-wave {
        animation: hero-vs322-wave 3.8s ease-in-out infinite;
      }
    }
    @keyframes hero-vs322-shield {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.03); opacity: 0.94; }
    }
    @keyframes hero-vs322-barrier {
      0%, 100% { opacity: 0.55; }
      50% { opacity: 0.88; }
    }
    @keyframes hero-vs322-chain {
      0%, 100% { transform: translateX(0); }
      50% { transform: translateX(4px); }
    }
    @keyframes hero-vs322-wave {
      0%, 100% { opacity: 0.35; transform: translateX(0); }
      50% { opacity: 0.62; transform: translateX(-6px); }
    }
    @media (prefers-reduced-motion: reduce) {
      .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__shield-pulse,
      .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__barrier-blink,
      .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__chain-flow,
      .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__claim-wave {
        animation: none !important;
      }
    }
    @media (max-width: 900px) {
      .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__inner {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      .l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__visual {
        order: -1;
        max-height: 320px;
      }
    }
  </style>
  <div class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__inner">
    <div class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__content">
      <div class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__badge">
        <span class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__badge-mark" aria-hidden="true"></span>
        ВС · 05.06.2026 · Указ № 322 · маркетплейс
      </div>
      <h1 class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__h1">
        <span class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__h1-accent">ВС разъяснил защиту от компенсации</span> за товарный знак иностранца из недружественной страны
      </h1>
      <p class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__sub">
        ИП на маркетплейсе оспорил иск о «сходном» обозначении — коллегия ВС указала, что суды обязаны проверить недружественные действия правообладателя по Указу № 322
      </p>
      <ul class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__facts">
        <li class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__fact l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__fact--accent">пп. «в» п. 17 Указа № 322</li>
        <li class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__fact">лицензия → цессия → иск</li>
        <li class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__fact l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__fact--warn">сходное обозначение · ИП</li>
      </ul>
      <a class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация: ответ на иск по товарному знаку</a>
    </div>
    <div class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__visual" aria-hidden="true">
      <svg viewBox="0 0 480 430" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:480px" role="img" aria-label="Маркетплейс: карточка ИП под щитом товарного знака, иск о компенсации отражён, абстрактный символ недружественной юрисдикции и Указ № 322">
        <defs>
          <linearGradient id="hero-vs322-bg" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f8fafc"/>
            <stop offset="100%" stop-color="#e8edf4"/>
          </linearGradient>
          <linearGradient id="hero-vs322-mp" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#a855f7"/>
            <stop offset="50%" stop-color="#2563eb"/>
            <stop offset="100%" stop-color="#0ea5e9"/>
          </linearGradient>
          <linearGradient id="hero-vs322-shield" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#3b82f6"/>
            <stop offset="100%" stop-color="#1e3a8a"/>
          </linearGradient>
          <linearGradient id="hero-vs322-card" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#ffffff"/>
            <stop offset="100%" stop-color="#f1f5f9"/>
          </linearGradient>
          <linearGradient id="hero-vs322-paper" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#fffbeb"/>
            <stop offset="100%" stop-color="#fef3c7"/>
          </linearGradient>
          <linearGradient id="hero-vs322-vs" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1e40af"/>
            <stop offset="100%" stop-color="#0f2744"/>
          </linearGradient>
          <pattern id="hero-vs322-grid" width="20" height="20" patternUnits="userSpaceOnUse">
            <rect width="20" height="20" fill="#f1f5f9"/>
            <rect x="0" y="0" width="9" height="9" rx="2" fill="#e2e8f0" opacity="0.7"/>
            <rect x="11" y="11" width="9" height="9" rx="2" fill="#e2e8f0" opacity="0.5"/>
          </pattern>
          <pattern id="hero-vs322-barrier" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
            <rect width="8" height="8" fill="#fef2f2"/>
            <line x1="0" y1="0" x2="0" y2="8" stroke="#f87171" stroke-width="2.5"/>
          </pattern>
          <filter id="hero-vs322-shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="5" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.12"/>
          </filter>
        </defs>
        <rect x="8" y="10" width="464" height="410" rx="18" fill="url(#hero-vs322-bg)" stroke="#cbd5e1" stroke-width="1.2"/>
        <rect x="8" y="10" width="464" height="410" rx="18" fill="url(#hero-vs322-grid)" opacity="0.45"/>
        <rect x="24" y="26" width="168" height="28" rx="8" fill="#fff" stroke="#e2e8f0"/>
        <circle cx="42" cy="40" r="6" fill="url(#hero-vs322-mp)"/>
        <rect x="54" y="34" width="72" height="6" rx="3" fill="#cbd5e1"/>
        <rect x="54" y="44" width="48" height="4" rx="2" fill="#e2e8f0"/>
        <text x="148" y="44" text-anchor="end" fill="#64748b" font-size="7" font-weight="700">МАРКЕТПЛЕЙС</text>
        <g filter="url(#hero-vs322-shadow)" transform="translate(36, 68)">
          <rect width="132" height="168" rx="12" fill="url(#hero-vs322-card)" stroke="#cbd5e1" stroke-width="1.2"/>
          <rect x="10" y="10" width="112" height="72" rx="8" fill="#f8fafc" stroke="#e2e8f0"/>
          <rect x="18" y="22" width="56" height="8" rx="3" fill="#94a3b8" opacity="0.5"/>
          <rect x="18" y="36" width="88" height="6" rx="2" fill="#cbd5e1"/>
          <rect x="18" y="48" width="72" height="6" rx="2" fill="#e2e8f0"/>
          <rect x="10" y="90" width="36" height="14" rx="4" fill="#dbeafe" stroke="#93c5fd"/>
          <text x="28" y="100" text-anchor="middle" fill="#1e40af" font-size="7" font-weight="800">ИП</text>
          <text x="66" y="100" fill="#334155" font-size="7" font-weight="700">селлер</text>
          <text x="66" y="118" fill="#64748b" font-size="6.5" font-weight="600">«сходное» имя</text>
          <text x="66" y="132" fill="#94a3b8" font-size="6">карточка товара</text>
          <rect x="10" y="142" width="52" height="16" rx="4" fill="#1e3a8a"/>
          <text x="36" y="153" text-anchor="middle" fill="#fff" font-size="7.5" font-weight="800">1 290 ₽</text>
          <circle cx="118" cy="150" r="10" fill="#f1f5f9" stroke="#cbd5e1"/>
          <path d="M114 150 L117 153 L122 147" fill="none" stroke="#64748b" stroke-width="1.5"/>
        </g>
        <g class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__shield-pulse" filter="url(#hero-vs322-shadow)" transform="translate(148, 118)">
          <path d="M72 0 L144 28 L144 88 C144 128 108 158 72 172 C36 158 0 128 0 88 L0 28 Z" fill="url(#hero-vs322-shield)" stroke="#1e40af" stroke-width="2"/>
          <circle cx="72" cy="72" r="28" fill="rgba(255,255,255,0.18)"/>
          <text x="72" y="80" text-anchor="middle" fill="#fff" font-size="28" font-weight="800">®</text>
          <text x="72" y="108" text-anchor="middle" fill="#dbeafe" font-size="6.5" font-weight="700" letter-spacing="0.06em">ЗАЩИТА ТЗ</text>
        </g>
        <g class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__claim-wave" transform="translate(268, 96)">
          <rect width="108" height="130" rx="10" fill="#fff" stroke="#fca5a5" stroke-width="1.4" stroke-dasharray="6 4"/>
          <rect x="0" y="0" width="108" height="18" rx="10" fill="#991b1b"/>
          <text x="54" y="12" text-anchor="middle" fill="#fef2f2" font-size="6.5" font-weight="800">ИСК · КОМПЕНСАЦИЯ</text>
          <text x="54" y="38" text-anchor="middle" fill="#334155" font-size="7" font-weight="700">нарушение ТЗ</text>
          <text x="54" y="54" text-anchor="middle" fill="#64748b" font-size="6">сходное обозначение</text>
          <text x="54" y="78" text-anchor="middle" fill="#a31830" font-size="11" font-weight="800">до 10 млн ₽</text>
          <line x1="18" y1="88" x2="90" y2="88" stroke="#fecaca" stroke-width="2"/>
          <line x1="22" y1="100" x2="86" y2="116" stroke="#dc2626" stroke-width="2.5"/>
          <line x1="86" y1="100" x2="22" y2="116" stroke="#dc2626" stroke-width="2.5"/>
          <text x="54" y="128" text-anchor="middle" fill="#991b1b" font-size="6" font-weight="700">отражён щитом</text>
        </g>
        <g transform="translate(318, 248)">
          <rect width="88" height="112" rx="8" fill="#fff" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/>
          <rect x="0" y="0" width="88" height="22" rx="8" fill="#f1f5f9"/>
          <text x="44" y="14" text-anchor="middle" fill="#475569" font-size="5.5" font-weight="800" letter-spacing="0.08em">ИНОСТР. ПРАВО</text>
          <circle cx="44" cy="52" r="22" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.2"/>
          <ellipse cx="44" cy="52" rx="22" ry="14" fill="none" stroke="#64748b" stroke-width="1"/>
          <line x1="22" y1="52" x2="66" y2="52" stroke="#64748b" stroke-width="0.8"/>
          <path d="M44 30 Q58 52 44 74 Q30 52 44 30" fill="none" stroke="#64748b" stroke-width="0.8"/>
          <rect x="24" y="38" width="40" height="28" rx="4" fill="url(#hero-vs322-barrier)" class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__barrier-blink" opacity="0.75"/>
          <text x="44" y="88" text-anchor="middle" fill="#64748b" font-size="5.5" font-weight="600">недружеств.</text>
          <text x="44" y="98" text-anchor="middle" fill="#64748b" font-size="5.5" font-weight="600">юрисдикция</text>
          <rect x="14" y="104" width="60" height="3" rx="1.5" fill="#cbd5e1"/>
        </g>
        <g class="l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany__chain-flow" transform="translate(24, 262)">
          <rect x="0" y="0" width="56" height="40" rx="6" fill="url(#hero-vs322-paper)" stroke="#d97706" stroke-width="1"/>
          <text x="28" y="16" text-anchor="middle" fill="#92400e" font-size="5.5" font-weight="800">ЛИЦЕНЗИЯ</text>
          <text x="28" y="28" text-anchor="middle" fill="#78716c" font-size="5">исключит.</text>
          <path d="M58 20 H78" stroke="#64748b" stroke-width="1.5" marker-end="none"/>
          <polygon points="78,16 86,20 78,24" fill="#64748b"/>
          <rect x="88" y="0" width="56" height="40" rx="6" fill="url(#hero-vs322-paper)" stroke="#d97706" stroke-width="1"/>
          <text x="116" y="16" text-anchor="middle" fill="#92400e" font-size="5.5" font-weight="800">ЦЕССИЯ</text>
          <text x="116" y="28" text-anchor="middle" fill="#78716c" font-size="5">требование</text>
          <path d="M146 20 H166" stroke="#64748b" stroke-width="1.5"/>
          <polygon points="166,16 174,20 166,24" fill="#a31830"/>
          <rect x="176" y="0" width="56" height="40" rx="6" fill="#fef2f2" stroke="#f87171" stroke-width="1"/>
          <text x="204" y="16" text-anchor="middle" fill="#991b1b" font-size="5.5" font-weight="800">ИСК</text>
          <text x="204" y="28" text-anchor="middle" fill="#b91c1c" font-size="5">к ИП</text>
        </g>
        <g filter="url(#hero-vs322-shadow)" transform="translate(248, 28)">
          <rect x="0" y="34" width="96" height="44" rx="4" fill="url(#hero-vs322-vs)"/>
          <polygon points="48,0 96,34 0,34" fill="#1e40af"/>
          <rect x="14" y="46" width="16" height="22" rx="2" fill="rgba(255,255,255,0.12)"/>
          <rect x="40" y="46" width="16" height="22" rx="2" fill="rgba(255,255,255,0.12)"/>
          <rect x="66" y="46" width="16" height="22" rx="2" fill="rgba(255,255,255,0.12)"/>
          <text x="48" y="68" text-anchor="middle" fill="#e2e8f0" font-size="6" font-weight="800" letter-spacing="0.06em">ВЕРХОВНЫЙ СУД</text>
          <text x="48" y="92" text-anchor="middle" fill="#1e3a8a" font-size="7" font-weight="800">05.06.2026</text>
        </g>
        <g filter="url(#hero-vs322-shadow)" transform="translate(248, 358)">
          <rect width="148" height="52" rx="8" fill="#fff" stroke="#1e3a8a" stroke-width="1.2"/>
          <rect x="0" y="0" width="148" height="16" rx="8" fill="#1e3a8a"/>
          <text x="74" y="11" text-anchor="middle" fill="#fff" font-size="6" font-weight="800">УКАЗ ПРЕЗИДЕНТА № 322</text>
          <text x="74" y="30" text-anchor="middle" fill="#334155" font-size="6.5" font-weight="700">пп. «в» п. 17 — проверка</text>
          <text x="74" y="42" text-anchor="middle" fill="#64748b" font-size="6">недружественных действий правообладателя</text>
        </g>
        <text x="240" y="418" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600">маркетплейс · щит ТЗ · иностранное право · ответ на иск · не аннулирование регистрации</text>
      </svg>
    </div>
  </div>
</section>
```
