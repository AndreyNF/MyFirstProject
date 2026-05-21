=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

## Паспорт мира
- **Название:** Архив процессуальных сроков
- **Пространство:** Светлый зал арбитражного дела — стол с документами, таймлайн на стене, весы «30 vs 15»
- **Главный объект:** Весы правосудия с двумя чашами (30 дней — возражения, 15 — уведомление ФУ)
- **Транспорт/механика:** Бегущая линия таймлайна с маркерами процедур; «листающийся» календарь
- **Финал цикла:** Чаша «30 дней» опускается ниже — визуальный акцент на реальном сроке возражений
- **Уникальные объекты:** документ «Возражение», календарь ЕФРСБ, реестр требований, метка «127-ФЗ», штамп «миф»

## Сценарий сцены
Статичная SVG-композиция: слева — таймлайн процедуры банкротства физлица; в центре — весы с подписанными чашами; справа — календарь и стопка документов. CSS-анимации: покачивание весов, бегущий индикатор на таймлайне, пульсация даты «30», мягкое покачивание документов.

## Тексты hero
- **H1:** 30 или 15 дней? Разбираем мифы о сроке возражений
- **Подзаголовок:** Когда кредитор и должник могут возразить после введения процедур банкротства физлица — по 127-ФЗ и практике 2025–2026
- **Этапы:** 1) Определение суда → 2) 15 дн. уведомление ФУ → 3) 30 дн. на возражения
- **Pill:** 127-ФЗ · Реестр · Реструктуризация · Реализация

## HTML-фрагмент hero

```html
<section id="hero" class="hero-bankrot-sroki" aria-label="Срок возражений при банкротстве физлица">
<style>
  .hero-bankrot-sroki {
    position: relative;
    min-height: 100vh;
    overflow: hidden;
    background: linear-gradient(165deg, #ffffff 0%, #f1f5f9 45%, #e8eef5 100%);
    color: #0f172a;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }
  .hero-bankrot-sroki::before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(15, 23, 42, 0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(15, 23, 42, 0.04) 1px, transparent 1px);
    background-size: 48px 48px;
    pointer-events: none;
    opacity: 0.55;
  }
  .hero-bankrot-sroki__inner {
    position: relative;
    z-index: 2;
    max-width: 1280px;
    margin: 0 auto;
    padding: clamp(2rem, 5vh, 4rem) clamp(1.25rem, 4vw, 3rem) clamp(5rem, 10vh, 7rem);
    display: grid;
    grid-template-columns: 1fr;
    gap: clamp(1.5rem, 3vw, 2.5rem);
    align-items: center;
  }
  @media (min-width: 960px) {
    .hero-bankrot-sroki__inner {
      grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr);
      gap: clamp(2rem, 4vw, 4rem);
    }
  }
  .hero-bankrot-sroki__badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.45rem 0.9rem;
    margin-bottom: 1rem;
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid #e2e8f0;
    border-radius: 999px;
    font-size: 0.8125rem;
    font-weight: 600;
    color: #475569;
    letter-spacing: 0.02em;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05);
  }
  .hero-bankrot-sroki__badge-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #2563eb;
    animation: hero-pulse-dot 2.4s ease-in-out infinite;
  }
  @keyframes hero-pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.55; transform: scale(0.85); }
  }
  .hero-bankrot-sroki__h1 {
    margin: 0 0 1.25rem;
    font-size: clamp(2rem, 4.8vw, 3.75rem);
    font-weight: 800;
    line-height: 1.08;
    letter-spacing: -0.03em;
    color: #0f172a;
  }
  .hero-bankrot-sroki__h1-accent {
    background: linear-gradient(135deg, #1d4ed8 0%, #0ea5e9 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .hero-bankrot-sroki__sub {
    margin: 0 0 1.75rem;
    max-width: 38rem;
    font-size: clamp(1rem, 1.6vw, 1.2rem);
    line-height: 1.65;
    color: rgba(15, 23, 42, 0.72);
  }
  .hero-bankrot-sroki__steps {
    display: flex;
    flex-direction: column;
    gap: 0.65rem;
    margin: 0 0 1.75rem;
    padding: 0;
    list-style: none;
  }
  .hero-bankrot-sroki__step {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    padding: 0.75rem 1rem;
    background: rgba(255, 255, 255, 0.88);
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    font-size: 0.9375rem;
    color: #334155;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
  }
  .hero-bankrot-sroki__step-num {
    flex-shrink: 0;
    width: 1.75rem;
    height: 1.75rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    background: #1e40af;
    color: #fff;
    font-size: 0.75rem;
    font-weight: 800;
  }
  .hero-bankrot-sroki__step:nth-child(2) .hero-bankrot-sroki__step-num { background: #64748b; }
  .hero-bankrot-sroki__step:nth-child(3) .hero-bankrot-sroki__step-num { background: #059669; }
  .hero-bankrot-sroki__step strong { color: #0f172a; }
  .hero-bankrot-sroki__cta {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.875rem 1.5rem;
    background: #1d4ed8;
    color: #fff;
    font-size: 0.9375rem;
    font-weight: 700;
    text-decoration: none;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(29, 78, 216, 0.28);
    transition: background 0.2s ease, transform 0.2s ease;
  }
  .hero-bankrot-sroki__cta:hover {
    background: #1e40af;
    transform: translateY(-1px);
  }
  .hero-bankrot-sroki__visual {
    position: relative;
    width: 100%;
    max-width: 560px;
    margin: 0 auto;
    aspect-ratio: 1 / 0.92;
  }
  .hero-bankrot-sroki__svg {
    width: 100%;
    height: 100%;
    display: block;
    filter: drop-shadow(0 12px 32px rgba(15, 23, 42, 0.08));
  }
  /* SVG CSS animations */
  .hero-scales-group {
    transform-origin: 280px 175px;
    animation: hero-scales-sway 5s ease-in-out infinite;
  }
  @keyframes hero-scales-sway {
    0%, 100% { transform: rotate(-3deg); }
    50% { transform: rotate(3deg); }
  }
  .hero-pan-left { animation: hero-pan-left 5s ease-in-out infinite; }
  .hero-pan-right { animation: hero-pan-right 5s ease-in-out infinite; }
  @keyframes hero-pan-left {
    0%, 100% { transform: translateY(8px); }
    50% { transform: translateY(-4px); }
  }
  @keyframes hero-pan-right {
    0%, 100% { transform: translateY(-4px); }
    50% { transform: translateY(8px); }
  }
  .hero-timeline-progress {
    stroke-dasharray: 320;
    stroke-dashoffset: 320;
    animation: hero-timeline-run 8s linear infinite;
  }
  @keyframes hero-timeline-run {
    0% { stroke-dashoffset: 320; }
    100% { stroke-dashoffset: 0; }
  }
  .hero-day-30 {
    animation: hero-day-pulse 2s ease-in-out infinite;
  }
  @keyframes hero-day-pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.55; }
  }
  .hero-doc-stack {
    animation: hero-doc-float 4s ease-in-out infinite;
  }
  @keyframes hero-doc-float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-6px); }
  }
  .hero-calendar-flip {
    transform-origin: 420px 310px;
    animation: hero-cal-tick 6s steps(1) infinite;
  }
  @keyframes hero-cal-tick {
    0%, 33% { transform: rotate(0deg); }
    34%, 66% { transform: rotate(-2deg); }
    67%, 100% { transform: rotate(2deg); }
  }
  .hero-myth-stamp {
    animation: hero-stamp-pop 4s ease-in-out infinite;
  }
  @keyframes hero-stamp-pop {
    0%, 85%, 100% { opacity: 0.35; transform: scale(0.92); }
    90% { opacity: 0.85; transform: scale(1); }
  }
  .hero-bankrot-sroki__pill {
    position: absolute;
    bottom: clamp(1.25rem, 3vh, 2.5rem);
    left: 50%;
    transform: translateX(-50%);
    z-index: 3;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.65rem;
    max-width: calc(100% - 2rem);
  }
  .hero-bankrot-sroki__pill span {
    padding: 0.55rem 1rem;
    background: rgba(255, 255, 255, 0.94);
    border: 1px solid #e2e8f0;
    border-radius: 999px;
    font-size: 0.8125rem;
    font-weight: 600;
    color: #475569;
    box-shadow: 0 2px 10px rgba(15, 23, 42, 0.05);
    white-space: nowrap;
  }
</style>

  <div class="hero-bankrot-sroki__inner">
    <div class="hero-bankrot-sroki__content">
      <div class="hero-bankrot-sroki__badge">
        <span class="hero-bankrot-sroki__badge-dot" aria-hidden="true"></span>
        Банкротство физлица · 127-ФЗ · 2025–2026
      </div>
      <h1 class="hero-bankrot-sroki__h1">
        <span class="hero-bankrot-sroki__h1-accent">30 или 15 дней?</span> Разбираем мифы о сроке возражений
      </h1>
      <p class="hero-bankrot-sroki__sub">
        Когда кредитор и должник могут возразить после введения процедур банкротства физлица — по 127-ФЗ и практике 2025–2026
      </p>
      <ol class="hero-bankrot-sroki__steps">
        <li class="hero-bankrot-sroki__step">
          <span class="hero-bankrot-sroki__step-num">1</span>
          <span><strong>Определение суда</strong> — введение реструктуризации или реализации имущества</span>
        </li>
        <li class="hero-bankrot-sroki__step">
          <span class="hero-bankrot-sroki__step-num">2</span>
          <span><strong>15 дней</strong> — финуправляющий уведомляет кредиторов (не срок ваших возражений)</span>
        </li>
        <li class="hero-bankrot-sroki__step">
          <span class="hero-bankrot-sroki__step-num">3</span>
          <span><strong>30 дней</strong> — окно на возражения против включения требования в реестр</span>
        </li>
      </ol>
      <a class="hero-bankrot-sroki__cta" href="https://advokat-vsem.ru/">Консультация по срокам возражений</a>
    </div>

    <div class="hero-bankrot-sroki__visual" aria-hidden="true">
      <svg class="hero-bankrot-sroki__svg" viewBox="0 0 560 520" xmlns="http://www.w3.org/2000/svg" role="img">
        <title>Весы 30 и 15 дней, таймлайн и документы возражений</title>
        <defs>
          <linearGradient id="hero-bg-panel" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#ffffff"/>
            <stop offset="100%" stop-color="#f8fafc"/>
          </linearGradient>
          <linearGradient id="hero-accent" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#1d4ed8"/>
            <stop offset="100%" stop-color="#0ea5e9"/>
          </linearGradient>
          <filter id="hero-soft-shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.08"/>
          </filter>
        </defs>

        <!-- Background panel -->
        <rect x="20" y="24" width="520" height="472" rx="24" fill="url(#hero-bg-panel)" stroke="#e2e8f0" stroke-width="1.5" filter="url(#hero-soft-shadow)"/>

        <!-- Timeline -->
        <g class="hero-timeline">
          <text x="48" y="68" fill="#64748b" font-size="11" font-weight="700" letter-spacing="0.08em">ТАЙМЛАЙН ПРОЦЕДУРЫ</text>
          <line x1="48" y1="200" x2="200" y2="200" stroke="#cbd5e1" stroke-width="4" stroke-linecap="round"/>
          <line class="hero-timeline-progress" x1="48" y1="200" x2="200" y2="200" stroke="url(#hero-accent)" stroke-width="4" stroke-linecap="round"/>
          <circle cx="48" cy="200" r="7" fill="#1d4ed8"/>
          <circle cx="108" cy="200" r="6" fill="#94a3b8"/>
          <circle cx="168" cy="200" r="6" fill="#059669"/>
          <text x="38" y="228" fill="#334155" font-size="10" font-weight="600">Суд</text>
          <text x="88" y="228" fill="#64748b" font-size="10" font-weight="600">15 дн.</text>
          <text x="148" y="228" fill="#059669" font-size="10" font-weight="700">30 дн.</text>
          <text x="48" y="98" fill="#475569" font-size="11">ЕФРСБ → требования → возражения</text>
        </g>

        <!-- Scales of justice -->
        <g class="hero-scales-group">
          <line x1="280" y1="100" x2="280" y2="175" stroke="#334155" stroke-width="3"/>
          <line x1="220" y1="120" x2="340" y2="120" stroke="#334155" stroke-width="3" stroke-linecap="round"/>
          <polygon points="280,175 260,195 300,195" fill="#475569"/>
          <!-- Left pan: 15 days (myth) -->
          <g class="hero-pan-left">
            <line x1="220" y1="120" x2="220" y2="155" stroke="#64748b" stroke-width="2"/>
            <ellipse cx="220" cy="168" rx="52" ry="10" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>
            <path d="M168 155 Q220 145 272 155 L272 175 Q220 185 168 175 Z" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5"/>
            <text x="220" y="162" text-anchor="middle" fill="#64748b" font-size="22" font-weight="800">15</text>
            <text x="220" y="178" text-anchor="middle" fill="#94a3b8" font-size="9" font-weight="600">уведомление ФУ</text>
            <g class="hero-myth-stamp">
              <rect x="188" y="188" width="64" height="22" rx="4" fill="none" stroke="#ef4444" stroke-width="2" transform="rotate(-12 220 199)"/>
              <text x="220" y="203" text-anchor="middle" fill="#ef4444" font-size="10" font-weight="800" transform="rotate(-12 220 199)">МИФ</text>
            </g>
          </g>
          <!-- Right pan: 30 days (real) -->
          <g class="hero-pan-right">
            <line x1="340" y1="120" x2="340" y2="155" stroke="#334155" stroke-width="2"/>
            <ellipse cx="340" cy="168" rx="52" ry="10" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
            <path d="M288 155 Q340 145 392 155 L392 175 Q340 185 288 175 Z" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
            <text class="hero-day-30" x="340" y="162" text-anchor="middle" fill="#1d4ed8" font-size="22" font-weight="800">30</text>
            <text x="340" y="178" text-anchor="middle" fill="#2563eb" font-size="9" font-weight="600">возражения в реестр</text>
          </g>
        </g>

        <!-- Calendar -->
        <g class="hero-calendar-flip">
          <rect x="400" y="250" width="120" height="110" rx="10" fill="#fff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#hero-soft-shadow)"/>
          <rect x="400" y="250" width="120" height="28" rx="10" fill="#1e293b"/>
          <rect x="400" y="266" width="120" height="12" fill="#1e293b"/>
          <text x="460" y="270" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">КАЛЕНДАРЬ</text>
          <text x="460" y="310" text-anchor="middle" fill="#0f172a" font-size="28" font-weight="800">30</text>
          <text x="460" y="332" text-anchor="middle" fill="#64748b" font-size="10">календарных дней</text>
          <rect x="418" y="345" width="18" height="14" rx="2" fill="#dbeafe" stroke="#93c5fd"/>
          <rect x="442" y="345" width="18" height="14" rx="2" fill="#f1f5f9" stroke="#cbd5e1"/>
          <rect x="466" y="345" width="18" height="14" rx="2" fill="#f1f5f9" stroke="#cbd5e1"/>
          <rect x="490" y="345" width="18" height="14" rx="2" fill="#f1f5f9" stroke="#cbd5e1"/>
        </g>

        <!-- Document stack -->
        <g class="hero-doc-stack">
          <rect x="48" y="280" width="130" height="168" rx="8" fill="#fff" stroke="#e2e8f0" stroke-width="1.5" transform="rotate(-4 113 364)"/>
          <rect x="58" y="272" width="130" height="168" rx="8" fill="#fff" stroke="#cbd5e1" stroke-width="1.5" transform="rotate(-2 123 356)"/>
          <rect x="68" y="264" width="130" height="168" rx="8" fill="#fff" stroke="#94a3b8" stroke-width="1.5" filter="url(#hero-soft-shadow)"/>
          <text x="133" y="300" text-anchor="middle" fill="#64748b" font-size="9" font-weight="700" letter-spacing="0.06em">127-ФЗ</text>
          <line x1="88" y1="312" x2="178" y2="312" stroke="#e2e8f0" stroke-width="1"/>
          <line x1="88" y1="328" x2="168" y2="328" stroke="#e2e8f0" stroke-width="1"/>
          <line x1="88" y1="344" x2="172" y2="344" stroke="#e2e8f0" stroke-width="1"/>
          <text x="133" y="378" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="800">Возражение</text>
          <text x="133" y="396" text-anchor="middle" fill="#475569" font-size="9">на требование кредитора</text>
          <rect x="98" y="408" width="70" height="3" rx="1.5" fill="#1d4ed8" opacity="0.35"/>
        </g>

        <!-- Registry label -->
        <rect x="230" y="420" width="180" height="36" rx="18" fill="#ecfdf5" stroke="#6ee7b7" stroke-width="1"/>
        <text x="320" y="443" text-anchor="middle" fill="#047857" font-size="11" font-weight="700">Реестр требований кредиторов</text>
      </svg>
    </div>
  </div>

  <div class="hero-bankrot-sroki__pill">
    <span>127-ФЗ</span>
    <span>Реестр</span>
    <span>Реструктуризация</span>
    <span>Реализация</span>
  </div>
</section>
```

## Передача Наташе
SLUG: srok-vozrazhenij-30-vs-15-mify
ВНИМАНИЕ: hero **без** `<canvas>` и **без** `<script>` — только статичный HTML, inline CSS и SVG-анимация (CSS). Не удалять секцию `#hero` и inline `<style>` внутри неё.
Файл фрагмента: `.cursor/nero-network-fragments/alina.md`

## Чеклист отличий от canvas-эталона vibecoding
| Элемент | Эталон vibecoding | Этот hero |
|---------|-------------------|-----------|
| Рендер | Canvas + JS engine | Статичный SVG + CSS `@keyframes` |
| Центральный объект | WebsiteTerminal | Весы «30 vs 15» с чашами |
| Транспорт | Conveyor belt | Таймлайн процедуры с бегущим индикатором |
| Персонажи Agent | 5 анимированных фигур | Документы, календарь, штамп «миф» |
| Финал цикла | Запуск/сборка | Чаша «30» ниже — акцент на реальном сроке |
| Композиция | Текст справа, canvas слева | Текст слева, SVG-метафора справа |
| Скрипты | `<script>` + RAF | Отсутствуют — MCP-safe |
