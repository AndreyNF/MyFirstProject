=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-vs-prodazha-kvartiry-moshenniki-st-159`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Развилка сделки» — обзор ВС РФ 01.07.2026: телефонный/«госуслуговый» обман третьих лиц → продажа квартиры → уголовное дело по ст. 159 и защита на проверке |
| **Центральная метафора** | Квартира на перекрёстке: слева — продавец с телефоном мошенника, справа — покупатель с риском соучастия; над домом — щит ст. 159 и весы ВС |
| **Пространство** | UG-градиент (#fefefe → #fff7f7 → #f0f4fa); SVG — жилой дом, телефон-ловушка, договор купли-продажи, щит защиты, бейдж ВС 01.07.2026 |
| **Движение** | Полностью static — без `<canvas>`, `<script>` и CSS-анимаций |
| **Палитра** | `#a31830` UG-red; `#1a365d` navy; `#4338ca` VS-blue; `#0f172a` текст; `#475569` подзаголовок |
| **Аудитория** | Продавец/покупатель квартиры после обмана, родственники, кому нужна защита по ст. 159 на доследственной проверке и в суде |

## Чеклист отличий от других hero

- [x] **Не municipalnyj-kontrakt**: не МУП/контракт — **продажа жилья под влиянием мошенников**
- [x] **Не osparivanie-bankrotstvo**: не банкротство/ст. 61.2 — **уголовный контур ст. 159**
- [x] **Не sip-nido**: не IP/товарный знак — **UG, недвижимость + мошенничество**
- [x] Уникальная сцена: **дом + телефон-обман + договор + щит ст. 159 + весы ВС**
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Badge **UG · ВС 01.07.2026 · ст. 159**; chips: ч. 3–4 ст. 159, обман третьих лиц, ст. 178–179 ГК, защита на проверке

```html
<section id="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159" class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159" aria-label="ВС разъяснил продажу квартиры под влиянием мошенников: уголовные риски по ст. 159 и защита на проверке и в суде">
  <style>
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159 {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(152deg, #fefefe 0%, #fff7f7 36%, #f0f4fa 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 42% 38% at 90% 12%, rgba(163, 24, 48, 0.08) 0%, transparent 55%),
        radial-gradient(ellipse 36% 34% at 4% 88%, rgba(67, 56, 202, 0.06) 0%, transparent 52%);
      pointer-events: none;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__inner {
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
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 18px;
      padding: 8px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid rgba(163, 24, 48, 0.16);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #334155;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #a31830;
      flex-shrink: 0;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.32rem, 2.85vw, 2.08rem);
      line-height: 1.22;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__h1-accent {
      color: #a31830;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.45vw, 1.08rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0 0 26px;
      padding: 0;
      list-style: none;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__fact--red {
      border-color: #fecaca;
      color: #a31830;
      background: #fff7f7;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__fact--blue {
      border-color: #c4b5fd;
      color: #4338ca;
      background: #f5f3ff;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__fact--navy {
      border-color: #93c5fd;
      color: #1a365d;
      background: #eff6ff;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__fact--warn {
      border-color: #fde68a;
      color: #92400e;
      background: #fffbeb;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__cta {
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
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__cta:hover {
      background: #8b1528;
    }
    .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (max-width: 900px) {
      .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159 {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__inner {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      .l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__visual {
        order: -1;
        max-height: 320px;
        overflow: hidden;
      }
    }
  </style>

  <div class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__inner">
    <div class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__content">
      <div class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__badge">
        <span class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__badge-mark" aria-hidden="true"></span>
        UG · ВС 01.07.2026 · ст. 159
      </div>
      <h1 class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__h1">
        <span class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__h1-accent">ВС разъяснил продажу квартиры под влиянием мошенников:</span> уголовные риски по ст. 159 и защита на проверке и в суде
      </h1>
      <p class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__sub">
        Когда заблуждение продавца перерастает в уголовное дело, а покупатель рискует обвинением в соучастии — разбор обзора ВС РФ от 01.07.2026
      </p>
      <ul class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__facts">
        <li class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__fact l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__fact--red">ч. 3–4 ст. 159 УК РФ</li>
        <li class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__fact l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__fact--blue">ВС · 01.07.2026 · 20 позиций</li>
        <li class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__fact l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__fact--navy">ст. 178–179 ГК · оспаривание</li>
        <li class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__fact l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__fact--warn">обман третьих лиц</li>
      </ul>
      <a class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация адвоката по мошенничеству</a>
    </div>

    <div class="l24-hero-vs-prodazha-kvartiry-moshenniki-st-159__visual" aria-hidden="true">
      <svg viewBox="0 0 520 440" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:520px" role="img" aria-label="Продажа квартиры под влиянием мошенников: телефонный обман, сделка с жильём, щит ст. 159 УК РФ и весы ВС РФ — обзор 01.07.2026">
        <defs>
          <linearGradient id="hvs159-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fafafa"/>
            <stop offset="55%" stop-color="#fff7f7"/>
            <stop offset="100%" stop-color="#eff6ff"/>
          </linearGradient>
          <linearGradient id="hvs159-red" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#dc2626"/>
            <stop offset="100%" stop-color="#a31830"/>
          </linearGradient>
          <linearGradient id="hvs159-blue" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#6366f1"/>
            <stop offset="100%" stop-color="#4338ca"/>
          </linearGradient>
          <linearGradient id="hvs159-shield" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#fff7f7"/>
            <stop offset="55%" stop-color="#fff"/>
            <stop offset="100%" stop-color="#eff6ff"/>
          </linearGradient>
          <linearGradient id="hvs159-building" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#e2e8f0"/>
            <stop offset="100%" stop-color="#cbd5e1"/>
          </linearGradient>
          <pattern id="hvs159-grid" width="20" height="20" patternUnits="userSpaceOnUse">
            <rect width="20" height="20" fill="#f8fafc"/>
            <path d="M20 0 L0 0 0 20" fill="none" stroke="#fecaca" stroke-width="0.4"/>
          </pattern>
          <filter id="hvs159-sh" x="-8%" y="-8%" width="116%" height="116%">
            <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#1a365d" flood-opacity="0.12"/>
          </filter>
        </defs>

        <rect x="10" y="12" width="500" height="416" rx="16" fill="url(#hvs159-bg)" stroke="#fecaca" stroke-width="1.2"/>
        <rect x="10" y="12" width="500" height="416" rx="16" fill="url(#hvs159-grid)" opacity="0.35"/>

        <!-- VS badge -->
        <g filter="url(#hvs159-sh)" transform="translate(138,14)">
          <rect x="0" y="26" width="244" height="48" rx="6" fill="url(#hvs159-blue)"/>
          <polygon points="122,4 238,26 6,26" fill="#4338ca"/>
          <text x="122" y="44" text-anchor="middle" fill="#e0e7ff" font-size="6.5" font-weight="800" letter-spacing="0.04em">ВС РФ · 01.07.2026</text>
          <text x="122" y="58" text-anchor="middle" fill="#a5b4fc" font-size="5.5">обзор · сделки с жильём · 20 позиций</text>
        </g>

        <!-- Scammer phone (left) -->
        <g filter="url(#hvs159-sh)" transform="translate(22,96)">
          <ellipse cx="58" cy="108" rx="52" ry="7" fill="#fecaca" opacity="0.5"/>
          <rect x="28" y="18" width="60" height="88" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1.2"/>
          <rect x="34" y="26" width="48" height="68" rx="4" fill="#0f172a"/>
          <circle cx="58" cy="100" r="5" fill="#475569"/>
          <text x="58" y="42" text-anchor="middle" fill="#ef4444" font-size="5" font-weight="800">!</text>
          <text x="58" y="52" text-anchor="middle" fill="#fca5a5" font-size="4.5">«сотрудник»</text>
          <text x="58" y="60" text-anchor="middle" fill="#fca5a5" font-size="4">ЦБ / ФСБ</text>
          <path d="M58 8 Q72 0 86 8" fill="none" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="3 2"/>
          <path d="M58 8 Q44 0 30 8" fill="none" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="3 2"/>
          <text x="58" y="122" text-anchor="middle" fill="#a31830" font-size="5" font-weight="700">обман третьих лиц</text>
          <text x="58" y="132" text-anchor="middle" fill="#64748b" font-size="4.5">телефон · госуслуги</text>
        </g>

        <!-- Seller silhouette -->
        <g filter="url(#hvs159-sh)" transform="translate(88,148)">
          <ellipse cx="36" cy="72" rx="34" ry="6" fill="#e2e8f0" opacity="0.7"/>
          <circle cx="36" cy="18" r="12" fill="#94a3b8"/>
          <path d="M20 36 Q36 28 52 36 L48 68 Q36 62 24 68 Z" fill="#cbd5e1" stroke="#64748b" stroke-width="0.8"/>
          <rect x="48" y="32" width="14" height="22" rx="3" fill="#1e293b"/>
          <line x1="88" y1="42" x2="62" y2="42" stroke="#ef4444" stroke-width="1" stroke-dasharray="3 2"/>
          <text x="36" y="86" text-anchor="middle" fill="#475569" font-size="5" font-weight="700">продавец</text>
          <text x="36" y="96" text-anchor="middle" fill="#64748b" font-size="4.5">потерпевший</text>
        </g>

        <!-- Central apartment building -->
        <g filter="url(#hvs159-sh)" transform="translate(168,72)">
          <rect x="24" y="48" width="136" height="148" rx="4" fill="url(#hvs159-building)" stroke="#64748b" stroke-width="1.2"/>
          <polygon points="92,20 168,48 16,48" fill="#94a3b8" stroke="#64748b" stroke-width="1"/>
          <rect x="40" y="68" width="22" height="18" rx="2" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.8"/>
          <rect x="70" y="68" width="22" height="18" rx="2" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.8"/>
          <rect x="100" y="68" width="22" height="18" rx="2" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.8"/>
          <rect x="130" y="68" width="22" height="18" rx="2" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.8"/>
          <rect x="40" y="96" width="22" height="18" rx="2" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.8"/>
          <rect x="70" y="96" width="22" height="18" rx="2" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.8"/>
          <rect x="100" y="96" width="22" height="18" rx="2" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.8"/>
          <rect x="130" y="96" width="22" height="18" rx="2" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.8"/>
          <rect x="40" y="124" width="22" height="18" rx="2" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.8"/>
          <rect x="70" y="124" width="22" height="18" rx="2" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.8"/>
          <rect x="100" y="124" width="22" height="18" rx="2" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.8"/>
          <rect x="130" y="124" width="22" height="18" rx="2" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.8"/>
          <rect x="72" y="156" width="40" height="40" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
          <circle cx="104" cy="176" r="3" fill="#d97706"/>
          <text x="92" y="210" text-anchor="middle" fill="#1a365d" font-size="5.5" font-weight="800">КВАРТИРА</text>
          <text x="92" y="222" text-anchor="middle" fill="#64748b" font-size="4.5">сделка под влиянием</text>
        </g>

        <!-- Article 159 shield over building -->
        <g filter="url(#hvs159-sh)" transform="translate(196,38)">
          <path d="M92 6 C92 6 156 28 156 72 C156 118 92 142 92 142 C92 142 28 118 28 72 C28 28 92 6 92 6 Z" fill="url(#hvs159-shield)" stroke="url(#hvs159-red)" stroke-width="2"/>
          <text x="92" y="52" text-anchor="middle" fill="#a31830" font-size="5" font-weight="800" letter-spacing="0.05em">УК РФ</text>
          <text x="92" y="78" text-anchor="middle" fill="#991b1b" font-size="14" font-weight="900">ст. 159</text>
          <text x="92" y="96" text-anchor="middle" fill="#64748b" font-size="4.8" font-weight="600">мошенничество</text>
          <rect x="36" y="104" width="112" height="14" rx="4" fill="url(#hvs159-red)"/>
          <text x="92" y="114" text-anchor="middle" fill="#fff" font-size="5" font-weight="800">ЗАЩИТА НА ПРОВЕРКЕ</text>
        </g>

        <!-- Buyer silhouette (right) -->
        <g filter="url(#hvs159-sh)" transform="translate(388,148)">
          <ellipse cx="52" cy="72" rx="40" ry="6" fill="#fef3c7" opacity="0.6"/>
          <circle cx="52" cy="18" r="12" fill="#fbbf24"/>
          <path d="M34 36 Q52 28 70 36 L66 68 Q52 62 38 68 Z" fill="#fde68a" stroke="#d97706" stroke-width="0.8"/>
          <text x="68" y="48" text-anchor="middle" fill="#d97706" font-size="8" font-weight="900">?</text>
          <text x="52" y="86" text-anchor="middle" fill="#92400e" font-size="5" font-weight="700">покупатель</text>
          <text x="52" y="96" text-anchor="middle" fill="#b45309" font-size="4.5">риск соучастия</text>
        </g>

        <!-- Contract document -->
        <g filter="url(#hvs159-sh)" transform="translate(148,228)">
          <rect width="108" height="72" rx="6" fill="#fff" stroke="#4338ca" stroke-width="1.2"/>
          <text x="54" y="16" text-anchor="middle" fill="#4338ca" font-size="5.5" font-weight="800">ДКП</text>
          <line x1="14" y1="24" x2="94" y2="24" stroke="#e2e8f0" stroke-width="1"/>
          <line x1="14" y1="34" x2="80" y2="34" stroke="#cbd5e1" stroke-width="0.8"/>
          <line x1="14" y1="42" x2="88" y2="42" stroke="#cbd5e1" stroke-width="0.8"/>
          <line x1="14" y1="50" x2="72" y2="50" stroke="#cbd5e1" stroke-width="0.8"/>
          <rect x="14" y="56" width="80" height="12" rx="3" fill="#f5f3ff"/>
          <text x="54" y="65" text-anchor="middle" fill="#4338ca" font-size="4.8" font-weight="600">продажа квартиры</text>
        </g>

        <!-- Arrow chain: phone → sale → criminal -->
        <path d="M80 200 Q130 218 168 210" fill="none" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="4 3" marker-end="none"/>
        <path d="M304 210 Q340 218 380 200" fill="none" stroke="#d97706" stroke-width="1.2" stroke-dasharray="4 3"/>
        <text x="260" y="232" text-anchor="middle" fill="#64748b" font-size="5" font-weight="700">заблуждение → сделка → уголовное дело</text>

        <!-- st. 178-179 GK chip -->
        <g filter="url(#hvs159-sh)" transform="translate(268,228)">
          <rect width="128" height="58" rx="8" fill="#fff" stroke="#1a365d" stroke-width="1.2"/>
          <text x="64" y="16" text-anchor="middle" fill="#1a365d" font-size="6" font-weight="800">ГК РФ</text>
          <text x="64" y="32" text-anchor="middle" fill="#334155" font-size="8" font-weight="800">ст. 178–179</text>
          <text x="64" y="44" text-anchor="middle" fill="#64748b" font-size="5">оспаривание сделки</text>
          <text x="64" y="54" text-anchor="middle" fill="#475569" font-size="4.5">обман · заблуждение</text>
        </g>

        <!-- Criminal case chip -->
        <g filter="url(#hvs159-sh)" transform="translate(408,228)">
          <rect width="94" height="58" rx="8" fill="url(#hvs159-red)"/>
          <text x="47" y="16" text-anchor="middle" fill="#fecaca" font-size="5.5" font-weight="700">УГОЛОВНОЕ</text>
          <text x="47" y="32" text-anchor="middle" fill="#fff" font-size="7" font-weight="800">ч. 3–4</text>
          <text x="47" y="44" text-anchor="middle" fill="#fecaca" font-size="5">особо крупный</text>
          <text x="47" y="54" text-anchor="middle" fill="#fca5a5" font-size="4.5">размер</text>
        </g>

        <!-- Scales of justice -->
        <g filter="url(#hvs159-sh)" transform="translate(18,228)">
          <line x1="54" y1="8" x2="54" y2="48" stroke="#4338ca" stroke-width="2"/>
          <line x1="20" y1="20" x2="88" y2="20" stroke="#4338ca" stroke-width="1.5"/>
          <path d="M20 20 L12 36 L28 36 Z" fill="#eef2ff" stroke="#6366f1" stroke-width="1"/>
          <path d="M88 20 L80 36 L96 36 Z" fill="#fff7f7" stroke="#a31830" stroke-width="1"/>
          <text x="20" y="44" text-anchor="middle" fill="#4338ca" font-size="4">ГК</text>
          <text x="88" y="44" text-anchor="middle" fill="#a31830" font-size="4">УК</text>
          <rect x="24" y="50" width="60" height="10" rx="3" fill="#f5f3ff"/>
          <text x="54" y="58" text-anchor="middle" fill="#4338ca" font-size="4.5" font-weight="600">разграничение</text>
        </g>

        <!-- Bottom info row -->
        <g filter="url(#hvs159-sh)" transform="translate(18,308)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#a31830" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#a31830" font-size="6" font-weight="800">ПРОДАВЕЦ</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">обманут мошенниками</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">может быть потерпевшим</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">психиатрическая экспертиза</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#fff7f7"/>
          <text x="77" y="63" text-anchor="middle" fill="#a31830" font-size="5" font-weight="600">защита на проверке</text>
        </g>
        <g filter="url(#hvs159-sh)" transform="translate(183,308)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#4338ca" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#4338ca" font-size="6" font-weight="800">ОБЗОР ВС</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">01.07.2026 · 20 позиций</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">сделки с жильём</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">дело Долиной — контекст</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#f5f3ff"/>
          <text x="77" y="63" text-anchor="middle" fill="#4338ca" font-size="5" font-weight="600">Краснов · Президиум</text>
        </g>
        <g filter="url(#hvs159-sh)" transform="translate(348,308)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#d97706" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#b45309" font-size="6" font-weight="800">ПОКУПАТЕЛЬ</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">«знал / должен был знать»</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">риск соучастия</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">риелторское посредничество</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#fffbeb"/>
          <text x="77" y="63" text-anchor="middle" fill="#d97706" font-size="5" font-weight="600">ст. 159 · покушение</text>
        </g>

        <text x="260" y="432" text-anchor="middle" fill="#94a3b8" font-size="6.5" font-weight="600">UG · ст. 159 · мошенничество с недвижимостью · ВС 2026 · защита</text>
      </svg>
    </div>
  </div>
</section>
```

## Передача Наташе

SLUG: vs-prodazha-kvartiry-moshenniki-st-159-zashchita-2026
H1_для_hero: ВС разъяснил продажу квартиры под влиянием мошенников: уголовные риски по ст. 159 и защита на проверке и в суде
ПОДЗАГОЛОВОК_HERO: Когда заблуждение продавца перерастает в уголовное дело, а покупатель рискует обвинением в соучастии — разбор обзора ВС РФ от 01.07.2026
ТИП_СТАТЬИ: UG — уголовное право
СЛЕДУЮЩИЙ_ШАГ: Наташа (сборка + публикация)
ВНИМАНИЕ: hero — static SVG + inline CSS, без `<canvas>`, `<script>`.
