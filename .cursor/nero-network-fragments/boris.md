=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** `sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie`  
**Якорь:** `boris-vpr-process`  
**Размещение для Наташи:** сразу **после H2 «Оспаривание товарного знака: возражение в Роспатенте и иск в СИП»** (после таблицы «Полное прекращение охраны vs частичное исключение»), **перед primary CTA** «Роспатент частично удовлетворил возражение…».  
**Режим:** тёмная панель в теле статьи (**контраст** со светлым hero Алины по ТЗ «ВПР» / СИП-844/2025) — **карта процесса (возражение → Роспатент → СИП → Президиум)** слева + **SVG-таймлайн** справа.  
**Legis24 MCP-only:** static SVG + inline CSS, без `<canvas>` и `<script>`.

## Паспорт блока

| Параметр | Значение |
|----------|----------|
| **Метафора** | «Двухинстанционный маршрут с ловушкой» — административное возражение не снимает монополию; отказ СИП — не финал; Президиум переворачивает исход |
| **Цифры-крючки** | 17.12.2024 → 16.06.2025 (частично) → 16.01.2026 (отказ) → 01.06.2026 (полное аннулирование); свидетельство № 652761; 100 000 ₽ госпошлины |
| **Палитра** | Тёмный plum-navy `#1a1225`–`#2d1f3d` (контраст hero); ВПР-красный `#dc2626`; Роспатент `#f59e0b`; СИП `#8b5cf6`; победа `#34d399`; ловушка `#fbbf24` |
| **Композиция** | Сплит: SVG-карта 4 инстанций \| вертикальный SVG-таймлайн 2018–2026 |

**Чеклист отличий от hero Алины**
- [x] Не полноэкранный блок; в теле статьи после H2 об оспаривании
- [x] Свой `id`: `boris-vpr-process` (не `l24-hero-…`)
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Тёмная панель — контраст со светлым IP-hero Алины (красные квадраты «ВПР», светлый градиент)
- [x] Сплит «карта процесса 4 стадии» \| «таймлайн дела СИП-844/2025»

```html
<section id="boris-vpr-process" class="boris-vpr-process" aria-label="Дело СИП-844/2025: маршрут оспаривания ТЗ «ВПР» — возражение, Роспатент, СИП, Президиум">
<style>
.boris-vpr-process {
  --vpr-ink: #1a1225;
  --vpr-plum: #2d1f3d;
  --vpr-plum-soft: #3d2d52;
  --vpr-red: #dc2626;
  --vpr-red-soft: #fca5a5;
  --vpr-gold: #fbbf24;
  --vpr-gold-soft: #fde68a;
  --vpr-sip: #8b5cf6;
  --vpr-sip-soft: #c4b5fd;
  --vpr-win: #34d399;
  --vpr-win-soft: #a7f3d0;
  --vpr-muted: #a8a3b3;
  --vpr-text: #e8e4ef;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.boris-vpr-process__shell {
  background: linear-gradient(152deg, var(--vpr-ink) 0%, var(--vpr-plum) 48%, var(--vpr-plum-soft) 100%);
  border: 1px solid rgba(220, 38, 38, 0.28);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: 0 18px 48px rgba(26, 18, 37, 0.42);
  color: var(--vpr-text);
}
.boris-vpr-process__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--vpr-gold);
}
.boris-vpr-process__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.boris-vpr-process__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--vpr-muted);
  max-width: 72ch;
}
.boris-vpr-process__lead strong { color: #fff; }
.boris-vpr-process__split {
  display: grid;
  grid-template-columns: minmax(0, 1.08fr) minmax(0, 1fr);
  gap: 24px;
  align-items: stretch;
}
.boris-vpr-process__panel {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.boris-vpr-process__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--vpr-gold);
}
.boris-vpr-process__map-svg,
.boris-vpr-process__timeline-svg {
  display: block;
  width: 100%;
  height: auto;
}
.boris-vpr-process__map-svg { max-height: 300px; margin-bottom: 12px; }
.boris-vpr-process__timeline-svg { max-height: 380px; }
.boris-vpr-process__stages {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  margin: 0 0 12px;
  padding: 0;
  list-style: none;
}
.boris-vpr-process__stage {
  padding: 10px 6px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border-top: 3px solid var(--vpr-gold);
  font-size: 0.68rem;
  line-height: 1.38;
  text-align: center;
  color: var(--vpr-muted);
}
.boris-vpr-process__stage:nth-child(1) { border-top-color: var(--vpr-gold); }
.boris-vpr-process__stage:nth-child(2) { border-top-color: var(--vpr-gold); }
.boris-vpr-process__stage:nth-child(3) { border-top-color: var(--vpr-sip); }
.boris-vpr-process__stage:nth-child(4) { border-top-color: var(--vpr-win); }
.boris-vpr-process__stage strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.boris-vpr-process__verdict {
  margin: 0;
  padding: 12px 14px;
  border-radius: 8px;
  background: rgba(251, 191, 36, 0.1);
  border: 1px solid rgba(251, 191, 36, 0.35);
  font-size: 0.78rem;
  line-height: 1.45;
  color: var(--vpr-text);
}
.boris-vpr-process__verdict strong { color: var(--vpr-gold); }
.boris-vpr-process__caption {
  margin: 10px 0 0;
  font-size: 0.7rem;
  line-height: 1.4;
  color: rgba(168, 163, 179, 0.88);
  text-align: center;
}
.boris-vpr-process__events {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 14px 0 0;
  padding: 0;
  list-style: none;
}
.boris-vpr-process__event {
  margin: 0;
  padding: 10px 12px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.24);
  border-left: 3px solid var(--vpr-muted);
  font-size: 0.74rem;
  line-height: 1.42;
  color: #cbd5e1;
}
.boris-vpr-process__event--trap { border-left-color: var(--vpr-gold); }
.boris-vpr-process__event--loss { border-left-color: var(--vpr-red); }
.boris-vpr-process__event--win { border-left-color: var(--vpr-win); }
.boris-vpr-process__event-date {
  display: inline-block;
  margin-right: 6px;
  font-weight: 700;
  color: #fff;
  font-size: 0.7rem;
}
.boris-vpr-process__event em {
  font-style: normal;
  font-weight: 600;
  color: var(--vpr-gold-soft);
}
.boris-vpr-process__event--loss em { color: var(--vpr-red-soft); }
.boris-vpr-process__event--win em { color: var(--vpr-win-soft); }
.boris-vpr-process__note {
  margin: 12px 0 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--vpr-muted);
}
.boris-vpr-process__note em {
  font-style: normal;
  color: var(--vpr-sip-soft);
  font-weight: 600;
}
.boris-vpr-process__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.boris-vpr-process__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--vpr-text);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.boris-vpr-process__tag--case {
  border-color: rgba(220, 38, 38, 0.5);
  color: var(--vpr-red-soft);
}
.boris-vpr-process__tag--law { border-color: rgba(139, 92, 246, 0.45); color: var(--vpr-sip-soft); }
.boris-vpr-process__tag--norm { border-color: rgba(52, 211, 153, 0.45); color: var(--vpr-win-soft); }
@media (max-width: 900px) {
  .boris-vpr-process__split { grid-template-columns: 1fr; }
  .boris-vpr-process__stages { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 520px) {
  .boris-vpr-process__stages { grid-template-columns: 1fr; }
}
</style>

  <div class="boris-vpr-process__shell">
    <p class="boris-vpr-process__eyebrow">IP · СИП-844/2025 · ТЗ «ВПР» № 652761 · ФИОКО vs Роспатент</p>
    <h3 class="boris-vpr-process__title">Маршрут оспаривания: возражение → Роспатент → СИП → Президиум</h3>
    <p class="boris-vpr-process__lead">Дело «ВПР» — не линейная победа: <strong>частичное</strong> решение Роспатента от 16.06.2025 оставило монополию через родовые позиции МКТУ; СИП отказал 16.01.2026. Президиум 01.06.2026 признал <strong>злоупотребление правом</strong> (ст. 10 ГК) и обязал <strong>полностью</strong> прекратить охрану — ст. 1483 + подп. 6 п. 2 ст. 1512.</p>

    <div class="boris-vpr-process__split">
      <div class="boris-vpr-process__panel">
        <p class="boris-vpr-process__panel-title">Карта процесса: 4 инстанции</p>
        <svg class="boris-vpr-process__map-svg" viewBox="0 0 560 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="vpr-map-title vpr-map-desc">
          <title id="vpr-map-title">Карта оспаривания ТЗ «ВПР»: возражение ФИОКО, Роспатент, СИП, Президиум</title>
          <desc id="vpr-map-desc">Горизонтальный маршрут от возражения в Роспатенте через частичное решение и отказ СИП к полному аннулированию в Президиуме СИП 01.06.2026</desc>
          <defs>
            <linearGradient id="vpr-route" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#f59e0b"/>
              <stop offset="45%" stop-color="#8b5cf6"/>
              <stop offset="100%" stop-color="#34d399"/>
            </linearGradient>
            <marker id="vpr-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0 0 L8 4 L0 8 Z" fill="#c4b5fd"/>
            </marker>
            <marker id="vpr-arr-win" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0 0 L8 4 L0 8 Z" fill="#34d399"/>
            </marker>
          </defs>

          <rect x="4" y="4" width="552" height="272" rx="14" fill="rgba(0,0,0,0.22)" stroke="#4a3d5c" stroke-width="1"/>

          <!-- Route line -->
          <path d="M72 118 L488 118" stroke="url(#vpr-route)" stroke-width="3" fill="none" stroke-dasharray="6 3" opacity="0.7"/>
          <path d="M400 118 L488 118" stroke="#34d399" stroke-width="3.5" fill="none" marker-end="url(#vpr-arr-win)"/>

          <!-- Stage 1: Возражение -->
          <g>
            <rect x="16" y="72" width="112" height="92" rx="10" fill="rgba(245,158,11,0.12)" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="72" y="94" text-anchor="middle" fill="#fde68a" font-size="7" font-weight="800">1 · ВОЗРАЖЕНИЕ</text>
            <text x="72" y="108" text-anchor="middle" fill="#fff" font-size="6.5" font-weight="600">ФИОКО → Роспатент</text>
            <text x="72" y="122" text-anchor="middle" fill="#a8a3b3" font-size="6">17.12.2024</text>
            <text x="72" y="136" text-anchor="middle" fill="#a8a3b3" font-size="5.8">ст. 1512–1513 ГК</text>
            <text x="72" y="150" text-anchor="middle" fill="#fde68a" font-size="5.8" font-weight="600">ст. 1483 · ст. 10</text>
          </g>
          <path d="M128 118 L168 118" stroke="#f59e0b" stroke-width="2" fill="none" marker-end="url(#vpr-arr)"/>

          <!-- Stage 2: Роспатент -->
          <g>
            <rect x="168" y="62" width="112" height="112" rx="10" fill="rgba(251,191,36,0.14)" stroke="#fbbf24" stroke-width="2"/>
            <text x="224" y="84" text-anchor="middle" fill="#fbbf24" font-size="7" font-weight="800">2 · РОСПАТЕНТ</text>
            <text x="224" y="98" text-anchor="middle" fill="#fff" font-size="6.5" font-weight="600">Палата по спорам</text>
            <text x="224" y="112" text-anchor="middle" fill="#a8a3b3" font-size="6">16.06.2025</text>
            <rect x="184" y="120" width="80" height="18" rx="4" fill="rgba(251,191,36,0.2)" stroke="#fbbf24" stroke-width="1"/>
            <text x="224" y="132" text-anchor="middle" fill="#fde68a" font-size="5.8" font-weight="700">ЧАСТИЧНО ⚠</text>
            <text x="224" y="152" text-anchor="middle" fill="#a8a3b3" font-size="5.5">«книги» · «издания»</text>
            <text x="224" y="164" text-anchor="middle" fill="#fca5a5" font-size="5.5">монополия осталась</text>
          </g>
          <path d="M280 118 L320 118" stroke="#8b5cf6" stroke-width="2" fill="none" marker-end="url(#vpr-arr)"/>

          <!-- Stage 3: СИП -->
          <g>
            <rect x="320" y="72" width="96" height="92" rx="10" fill="rgba(139,92,246,0.12)" stroke="#8b5cf6" stroke-width="1.8"/>
            <text x="368" y="94" text-anchor="middle" fill="#c4b5fd" font-size="7" font-weight="800">3 · СИП</text>
            <text x="368" y="108" text-anchor="middle" fill="#fff" font-size="6.5" font-weight="600">1-я инстанция</text>
            <text x="368" y="122" text-anchor="middle" fill="#a8a3b3" font-size="6">16.01.2026</text>
            <rect x="332" y="130" width="72" height="18" rx="4" fill="rgba(220,38,38,0.18)" stroke="#dc2626" stroke-width="1"/>
            <text x="368" y="142" text-anchor="middle" fill="#fca5a5" font-size="5.8" font-weight="700">ОТКАЗ ✗</text>
            <text x="368" y="156" text-anchor="middle" fill="#a8a3b3" font-size="5.5">23.12.2025 — РИА</text>
          </g>
          <path d="M416 118 L456 118" stroke="#34d399" stroke-width="2.5" fill="none" marker-end="url(#vpr-arr-win)"/>

          <!-- Stage 4: Президиум -->
          <g>
            <rect x="456" y="58" width="96" height="120" rx="10" fill="rgba(52,211,153,0.14)" stroke="#34d399" stroke-width="2.2"/>
            <text x="504" y="80" text-anchor="middle" fill="#a7f3d0" font-size="7" font-weight="800">4 · ПРЕЗИДИУМ</text>
            <text x="504" y="94" text-anchor="middle" fill="#fff" font-size="6.5" font-weight="600">кассация СИП</text>
            <text x="504" y="108" text-anchor="middle" fill="#a8a3b3" font-size="6">01.06.2026</text>
            <rect x="468" y="116" width="72" height="20" rx="4" fill="rgba(52,211,153,0.22)" stroke="#34d399" stroke-width="1.2"/>
            <text x="504" y="130" text-anchor="middle" fill="#a7f3d0" font-size="5.8" font-weight="800">ПОЛНОЕ ✓</text>
            <text x="504" y="148" text-anchor="middle" fill="#a8a3b3" font-size="5.5">аннулирование</text>
            <text x="504" y="162" text-anchor="middle" fill="#a8a3b3" font-size="5.5">Госреестр ТЗ</text>
          </g>

          <!-- Parties row -->
          <rect x="16" y="188" width="168" height="44" rx="8" fill="rgba(0,0,0,0.3)" stroke="#64748b" stroke-width="1"/>
          <text x="100" y="206" text-anchor="middle" fill="#e8e4ef" font-size="6" font-weight="700">ИСТЕЦ: ФИОКО</text>
          <text x="100" y="220" text-anchor="middle" fill="#a8a3b3" font-size="5.5">Рособрнадзор · госаббревиатура ВПР</text>

          <rect x="196" y="188" width="168" height="44" rx="8" fill="rgba(0,0,0,0.3)" stroke="#f59e0b" stroke-width="1"/>
          <text x="280" y="206" text-anchor="middle" fill="#fde68a" font-size="6" font-weight="700">ОТВЕТЧИК: Роспатент</text>
          <text x="280" y="220" text-anchor="middle" fill="#a8a3b3" font-size="5.5">решение 16.06.2025 отменено</text>

          <rect x="376" y="188" width="168" height="44" rx="8" fill="rgba(220,38,38,0.12)" stroke="#dc2626" stroke-width="1"/>
          <text x="460" y="206" text-anchor="middle" fill="#fca5a5" font-size="6" font-weight="700">3-е ЛИЦО: «Просвещение»</text>
          <text x="460" y="220" text-anchor="middle" fill="#a8a3b3" font-size="5.5">лицензии · 100 000 ₽ госпошлины</text>

          <!-- VPR mark hint -->
          <g transform="translate(16, 244)">
            <rect width="20" height="20" rx="3" fill="#dc2626"/>
            <rect x="24" width="20" height="20" rx="3" fill="#dc2626"/>
            <rect x="48" width="20" height="20" rx="3" fill="#dc2626"/>
            <text x="80" y="14" fill="#a8a3b3" font-size="6">комбинированный знак «ВПР» · заявка № 2017709530 · классы 09, 16, 35, 41</text>
          </g>
        </svg>

        <ul class="boris-vpr-process__stages" aria-label="Краткие итоги по стадиям">
          <li class="boris-vpr-process__stage">
            <strong>Возражение</strong>
            17.12.2024 · ФИОКО · ст. 10 bis
          </li>
          <li class="boris-vpr-process__stage">
            <strong>Роспатент</strong>
            16.06.2025 · частично · ловушка МКТУ
          </li>
          <li class="boris-vpr-process__stage">
            <strong>СИП</strong>
            16.01.2026 · отказ · не финал
          </li>
          <li class="boris-vpr-process__stage">
            <strong>Президиум</strong>
            01.06.2026 · полное аннулирование
          </li>
        </ul>
        <p class="boris-vpr-process__verdict"><strong>Урок ВПР:</strong> компромисс Роспатента <em>не снимает монополию</em> — при родовых формулировках («книги», «издания печатные») правообладатель сохраняет рычаги. Имеет смысл идти в СИП за <strong>полным</strong> прекращением охраны и готовить кассацию (определение С01-405/2026).</p>
        <p class="boris-vpr-process__caption">Схема по делу № СИП-844/2025 · постановление Президиума СИП от 01.06.2026</p>
      </div>

      <div class="boris-vpr-process__panel">
        <p class="boris-vpr-process__panel-title">Таймлайн дела: от регистрации до аннулирования</p>
        <svg class="boris-vpr-process__timeline-svg" viewBox="0 0 320 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="vpr-tl-title vpr-tl-desc">
          <title id="vpr-tl-title">Хронология дела СИП-844/2025: товарный знак «ВПР»</title>
          <desc id="vpr-tl-desc">Вертикальный таймлайн от регистрации ТЗ в 2018 году до полного прекращения охраны Президиумом СИП 1 июня 2026 года</desc>
          <defs>
            <linearGradient id="vpr-tl-axis" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#64748b"/>
              <stop offset="35%" stop-color="#fbbf24"/>
              <stop offset="65%" stop-color="#dc2626"/>
              <stop offset="100%" stop-color="#34d399"/>
            </linearGradient>
          </defs>

          <!-- Axis -->
          <line x1="56" y1="28" x2="56" y2="372" stroke="url(#vpr-tl-axis)" stroke-width="3" stroke-linecap="round"/>

          <!-- 2018 -->
          <circle cx="56" cy="40" r="10" fill="#64748b" stroke="#fff" stroke-width="2"/>
          <text x="76" y="36" fill="#a8a3b3" font-size="7" font-weight="700">2018</text>
          <text x="76" y="48" fill="#e8e4ef" font-size="6.5" font-weight="600">Регистрация ТЗ «ВПР»</text>
          <text x="76" y="60" fill="#a8a3b3" font-size="5.8">«Просвещение» · свид. № 652761</text>

          <!-- 17.12.2024 -->
          <circle cx="56" cy="88" r="10" fill="#f59e0b" stroke="#fff" stroke-width="2"/>
          <text x="76" y="84" fill="#fde68a" font-size="7" font-weight="700">17.12.2024</text>
          <text x="76" y="96" fill="#e8e4ef" font-size="6.5" font-weight="600">Возражение ФИОКО</text>
          <text x="76" y="108" fill="#a8a3b3" font-size="5.8">Палата: заседание 22.04.2025</text>

          <!-- 16.06.2025 -->
          <circle cx="56" cy="148" r="12" fill="#fbbf24" stroke="#fff" stroke-width="2"/>
          <text x="76" y="142" fill="#fbbf24" font-size="7" font-weight="800">16.06.2025</text>
          <text x="76" y="154" fill="#e8e4ef" font-size="6.5" font-weight="600">Роспатент: частично ⚠</text>
          <text x="76" y="166" fill="#fca5a5" font-size="5.8">родовые позиции МКТУ сохранены</text>
          <rect x="76" y="172" width="220" height="16" rx="4" fill="rgba(251,191,36,0.15)" stroke="#fbbf24" stroke-width="0.8"/>
          <text x="186" y="183" text-anchor="middle" fill="#fde68a" font-size="5.5" font-weight="600">ловушка частичного аннулирования</text>

          <!-- Sep 2025 -->
          <circle cx="56" cy="218" r="9" fill="#8b5cf6" stroke="#fff" stroke-width="2"/>
          <text x="76" y="214" fill="#c4b5fd" font-size="7" font-weight="700">сент. 2025</text>
          <text x="76" y="226" fill="#e8e4ef" font-size="6.5" font-weight="600">Иск ФИОКО в СИП</text>
          <text x="76" y="238" fill="#a8a3b3" font-size="5.8">оспаривание решения Роспатента</text>

          <!-- 23.12.2025 -->
          <circle cx="56" cy="268" r="10" fill="#dc2626" stroke="#fff" stroke-width="2"/>
          <text x="76" y="264" fill="#fca5a5" font-size="7" font-weight="700">23.12.2025</text>
          <text x="76" y="276" fill="#e8e4ef" font-size="6.5" font-weight="600">СИП отказал ФИОКО</text>
          <text x="76" y="288" fill="#a8a3b3" font-size="5.8">нет ассоциации «ВПР» у потребителей (РИА)</text>

          <!-- 16.01.2026 -->
          <circle cx="56" cy="308" r="10" fill="#dc2626" stroke="#fff" stroke-width="2"/>
          <text x="76" y="304" fill="#fca5a5" font-size="7" font-weight="700">16.01.2026</text>
          <text x="76" y="316" fill="#e8e4ef" font-size="6.5" font-weight="600">Решение СИП-844/2025</text>
          <text x="76" y="328" fill="#a8a3b3" font-size="5.8">отказ в иске · 1-я инстанция</text>

          <!-- 20.03.2026 -->
          <circle cx="56" cy="340" r="8" fill="#8b5cf6" stroke="#fff" stroke-width="1.5"/>
          <text x="76" y="338" fill="#c4b5fd" font-size="6.5" font-weight="600">20.03.2026 · С01-405/2026</text>
          <text x="76" y="350" fill="#a8a3b3" font-size="5.8">кассация принята · срок восстановлен</text>

          <!-- 01.06.2026 -->
          <circle cx="56" cy="378" r="14" fill="#34d399" stroke="#fff" stroke-width="2.5"/>
          <text x="76" y="372" fill="#a7f3d0" font-size="8" font-weight="800">01.06.2026</text>
          <text x="76" y="386" fill="#fff" font-size="7" font-weight="700">Президиум: полное аннулирование ✓</text>
          <text x="76" y="398" fill="#a8a3b3" font-size="5.8">ст. 10 ГК · ст. 1483 · подп. 6 п. 2 ст. 1512</text>
        </svg>

        <ul class="boris-vpr-process__events" aria-label="Ключевые повороты хронологии">
          <li class="boris-vpr-process__event boris-vpr-process__event--trap">
            <span class="boris-vpr-process__event-date">16.06.2025</span>
            Роспатент исключил «ВПР» для части классов 16 и 41, но оставил <em>«книги»</em> и <em>«издания печатные»</em> — монополия сохранилась.
          </li>
          <li class="boris-vpr-process__event boris-vpr-process__event--loss">
            <span class="boris-vpr-process__event-date">16.01.2026</span>
            СИП отказал: по 1-й инстанции <em>не дожали</em> описательность — нужна линия злоупотребления правом и лицензирования.
          </li>
          <li class="boris-vpr-process__event boris-vpr-process__event--win">
            <span class="boris-vpr-process__event-date">01.06.2026</span>
            Кассация <em>полностью</em> прекратила охрану; ст. 1515 не применялась — только <em>100 000 ₽</em> госпошлины.
          </li>
        </ul>
        <p class="boris-vpr-process__note"><em>Ориентир сроков:</em> от возражения (12.2024) до итога кассации (06.2026) — ~18 месяцев; проигрыш в декабре–январе не финал при правильной кассационной стратегии.</p>
      </div>
    </div>

    <div class="boris-vpr-process__foot" aria-label="Контекст дела СИП-844/2025">
      <span class="boris-vpr-process__tag boris-vpr-process__tag--case">СИП-844/2025 · № 652761 · ВПР</span>
      <span class="boris-vpr-process__tag boris-vpr-process__tag--law">ст. 10 ГК · злоупотребление правом</span>
      <span class="boris-vpr-process__tag boris-vpr-process__tag--norm">ст. 1483 · подп. 6 п. 2 ст. 1512</span>
    </div>
  </div>
</section>
```

## Передача Наташе

- **Якорь вставки:** `#boris-vpr-process`
- **После H2:** «Оспаривание товарного знака: возражение в Роспатенте и иск в СИП»
- **Перед:** primary CTA «Роспатент частично удовлетворил возражение…»
- **MCP-only:** без `<canvas>` и `<script>`
