=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** vs-obysk-bez-upakovki-ekspertiza-dokazatelstva-zashchita-2026  
**Якорь:** `#boris-obysk-upakovka-flow`  
**Режим:** контраст к hero Алины — светлый hero с фактами дела → тёмный slate/navy блок двухконтурной стратегии в теле статьи  
**Техника:** static SVG + inline CSS · без `<canvas>` · без `<script>`

## Место вставки для Наташи

Вставить **после вводного абзаца H2 §7** «Защита по уголовному делу: тактика при спорных доказательствах обыска» (после абзаца про **двухконтурную** стратегию — контур A и контур B) и **перед** H3 §7.1 «Что фиксировать защитнику во время и сразу после обыска».

Якорь для Наташи: после H2 §7 (ввод), id `boris-obysk-upakovka-flow`

## Чеклист отличий от hero Алины

| | Hero Алины | Блок Бориса |
|---|---|---|
| Позиция | первый экран | тело статьи, после H2 §7 (ввод) |
| Фон | светлый (#fefefe / #f0f7ff) | тёмный slate/navy gradient |
| Смысл | факты: № 32-УД26-10-K1, ч. 10 ст. 182, КТЭ | **два контура** защиты: упаковка/КТЭ vs ст. 9 УК + Пленум 14 |
| id | `l24-hero-vs-obysk-upakovka` (Алина) | `boris-obysk-upakovka-flow` |
| canvas/script | нет (MCP-only SVG) | нет |

```html
<section id="boris-obysk-upakovka-flow" class="l24-boris-obysk-flow" aria-label="Двухконтурная защита по делу № 32-УД26-10-K1: процессуальный контур упаковки и КТЭ против уголовно-правового контура квалификации">
<style>
.l24-boris-obysk-flow {
  --ob-slate: #0f172a;
  --ob-slate-mid: #1e293b;
  --ob-slate-soft: #334155;
  --ob-proc: #38bdf8;
  --ob-proc-soft: #7dd3fc;
  --ob-qual: #34d399;
  --ob-qual-soft: #6ee7b7;
  --ob-warn: #fbbf24;
  --ob-warn-soft: #fde68a;
  --ob-fail: #f87171;
  --ob-muted: #94a3b8;
  --ob-txt: #e2e8f0;
  margin: 48px 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-obysk-flow__shell {
  background: linear-gradient(152deg, var(--ob-slate) 0%, var(--ob-slate-mid) 48%, #172554 100%);
  border: 1px solid rgba(56, 189, 248, 0.24);
  border-radius: 14px;
  padding: 32px 28px 24px;
  color: var(--ob-txt);
  box-shadow: 0 18px 48px rgba(15, 23, 42, 0.48);
}
.l24-boris-obysk-flow__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ob-proc-soft);
}
.l24-boris-obysk-flow__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-obysk-flow__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--ob-muted);
  max-width: 72ch;
}
.l24-boris-obysk-flow__lead strong { color: #fff; }
.l24-boris-obysk-flow__split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
  align-items: stretch;
  margin-bottom: 20px;
}
.l24-boris-obysk-flow__panel {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 18px 16px;
  display: flex;
  flex-direction: column;
}
.l24-boris-obysk-flow__panel--a { border-top: 3px solid var(--ob-proc); }
.l24-boris-obysk-flow__panel--b { border-top: 3px solid var(--ob-qual); }
.l24-boris-obysk-flow__panel-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  margin-bottom: 12px;
}
.l24-boris-obysk-flow__panel-title {
  margin: 0;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
.l24-boris-obysk-flow__panel--a .l24-boris-obysk-flow__panel-title { color: var(--ob-proc-soft); }
.l24-boris-obysk-flow__panel--b .l24-boris-obysk-flow__panel-title { color: var(--ob-qual-soft); }
.l24-boris-obysk-flow__badge {
  font-size: 0.62rem;
  font-weight: 800;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  padding: 4px 8px;
  border-radius: 999px;
  white-space: nowrap;
}
.l24-boris-obysk-flow__badge--fail {
  background: rgba(248, 113, 113, 0.14);
  border: 1px solid rgba(248, 113, 113, 0.45);
  color: #fca5a5;
}
.l24-boris-obysk-flow__badge--win {
  background: rgba(52, 211, 153, 0.14);
  border: 1px solid rgba(52, 211, 153, 0.45);
  color: var(--ob-qual-soft);
}
.l24-boris-obysk-flow__route-svg {
  display: block;
  width: 100%;
  height: auto;
  margin-bottom: 12px;
  flex: 1;
}
.l24-boris-obysk-flow__steps {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-obysk-flow__step {
  padding: 9px 10px;
  border-radius: 7px;
  background: rgba(0, 0, 0, 0.26);
  font-size: 0.7rem;
  line-height: 1.38;
  color: var(--ob-muted);
}
.l24-boris-obysk-flow__panel--a .l24-boris-obysk-flow__step { border-left: 2px solid var(--ob-proc); }
.l24-boris-obysk-flow__panel--b .l24-boris-obysk-flow__step { border-left: 2px solid var(--ob-qual); }
.l24-boris-obysk-flow__step strong {
  display: block;
  color: #fff;
  font-size: 0.74rem;
  margin-bottom: 3px;
}
.l24-boris-obysk-flow__step--weak { opacity: 0.72; }
.l24-boris-obysk-flow__caption {
  margin: 8px 0 0;
  font-size: 0.66rem;
  line-height: 1.4;
  color: rgba(148, 163, 184, 0.88);
  text-align: center;
}
.l24-boris-obysk-flow__merge {
  margin: 0 0 16px;
  padding: 16px 18px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px dashed rgba(251, 191, 36, 0.35);
}
.l24-boris-obysk-flow__merge-title {
  margin: 0 0 10px;
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--ob-warn-soft);
  text-align: center;
}
.l24-boris-obysk-flow__merge-svg {
  display: block;
  width: 100%;
  max-width: 520px;
  height: auto;
  margin: 0 auto;
}
.l24-boris-obysk-flow__total {
  margin: 0 0 16px;
  padding: 14px 16px;
  border-radius: 10px;
  background: rgba(52, 211, 153, 0.1);
  border: 1px solid rgba(52, 211, 153, 0.32);
  font-size: 0.84rem;
  line-height: 1.5;
  color: var(--ob-muted);
}
.l24-boris-obysk-flow__total strong { color: var(--ob-qual-soft); }
.l24-boris-obysk-flow__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-obysk-flow__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  color: var(--ob-txt);
  border: 1px solid rgba(255, 255, 255, 0.13);
}
.l24-boris-obysk-flow__tag--case { border-color: rgba(251, 191, 36, 0.45); color: var(--ob-warn-soft); }
.l24-boris-obysk-flow__tag--proc { border-color: rgba(56, 189, 248, 0.45); color: var(--ob-proc-soft); }
.l24-boris-obysk-flow__tag--qual { border-color: rgba(52, 211, 153, 0.45); color: var(--ob-qual-soft); }
@media (max-width: 860px) {
  .l24-boris-obysk-flow__split { grid-template-columns: 1fr; }
  .l24-boris-obysk-flow__shell { padding: 24px 18px 20px; }
}
</style>

<div class="l24-boris-obysk-flow__shell">
  <p class="l24-boris-obysk-flow__eyebrow">ВС РФ · дело № 32-УД26-10-K1 · 24.08.2026 · двухконтурная защита</p>
  <h3 class="l24-boris-obysk-flow__title">Два контура защиты: упаковка/КТЭ и квалификация по ст. 9 УК</h3>
  <p class="l24-boris-obysk-flow__lead">В кассации по делу № 32-УД26-10-K1 защита атаковала <strong>процессуально</strong> (неупакованные ноутбуки → недопустимость КТЭ) и <strong>уголовно-правово</strong> (проверочная закупка → покушение). ВС отклонил контур A, но <strong>снизил срок на 3 месяца</strong> по контуру B — с <strong>10 лет 6 мес.</strong> до <strong>10 лет 3 мес.</strong></p>

  <div class="l24-boris-obysk-flow__split">
    <!-- КОНТУР A -->
    <div class="l24-boris-obysk-flow__panel l24-boris-obysk-flow__panel--a">
      <div class="l24-boris-obysk-flow__panel-head">
        <p class="l24-boris-obysk-flow__panel-title">Контур A — процессуальный</p>
        <span class="l24-boris-obysk-flow__badge l24-boris-obysk-flow__badge--fail">частично провалился</span>
      </div>
      <svg class="l24-boris-obysk-flow__route-svg" viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="obFlowAT obFlowAD">
        <title id="obFlowAT">Контур A: цепочка упаковки и КТЭ при обыске</title>
        <desc id="obFlowAD">Обыск → протокол → упаковка/фото → КТЭ → ст. 75 УПК. В деле № 32-УД26-10-K1 КТЭ сохранена: голый довод «не упаковали» отклонён</desc>
        <defs>
          <linearGradient id="obProcLine" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#38bdf8"/>
            <stop offset="100%" stop-color="#7dd3fc"/>
          </linearGradient>
          <marker id="obProcArr" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
            <polygon points="0 0, 7 3, 0 6" fill="#7dd3fc"/>
          </marker>
          <filter id="obProcGlow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.35"/>
          </filter>
        </defs>

        <rect x="8" y="8" width="504" height="184" rx="10" fill="rgba(56,189,248,0.04)" stroke="rgba(56,189,248,0.18)" stroke-width="1.2"/>

        <!-- Цепочка звеньев -->
        <line x1="52" y1="88" x2="468" y2="88" stroke="rgba(56,189,248,0.15)" stroke-width="8" stroke-linecap="round"/>
        <line x1="52" y1="88" x2="468" y2="88" stroke="url(#obProcLine)" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="6,4" opacity="0.7"/>

        <!-- 1 Обыск -->
        <circle cx="52" cy="88" r="22" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" filter="url(#obProcGlow)"/>
        <text x="52" y="92" text-anchor="middle" fill="#fff" font-size="9" font-weight="800" font-family="system-ui,sans-serif">1</text>
        <text x="52" y="58" text-anchor="middle" fill="#7dd3fc" font-size="7" font-weight="700" font-family="system-ui,sans-serif">ОБЫСК</text>
        <text x="52" y="128" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">2 ноутбука</text>
        <text x="52" y="138" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">+ телефон</text>

        <!-- 2 Протокол -->
        <circle cx="156" cy="88" r="22" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" filter="url(#obProcGlow)"/>
        <text x="156" y="92" text-anchor="middle" fill="#fff" font-size="9" font-weight="800" font-family="system-ui,sans-serif">2</text>
        <text x="156" y="58" text-anchor="middle" fill="#7dd3fc" font-size="7" font-weight="700" font-family="system-ui,sans-serif">ПРОТОКОЛ</text>
        <text x="156" y="128" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">ст. 166–167</text>
        <text x="156" y="138" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">УПК</text>

        <!-- 3 Упаковка (перечёркнуто) -->
        <circle cx="260" cy="88" r="24" fill="#1e293b" stroke="#f87171" stroke-width="2.5" stroke-dasharray="4,3" filter="url(#obProcGlow)"/>
        <text x="260" y="92" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="800" font-family="system-ui,sans-serif">✕</text>
        <text x="260" y="58" text-anchor="middle" fill="#fca5a5" font-size="7" font-weight="700" font-family="system-ui,sans-serif">УПАКОВКА</text>
        <text x="260" y="128" text-anchor="middle" fill="#f87171" font-size="6" font-family="system-ui,sans-serif">не произведена</text>
        <text x="260" y="138" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">ч. 10 ст. 182</text>

        <!-- 4 КТЭ -->
        <circle cx="364" cy="88" r="22" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" filter="url(#obProcGlow)"/>
        <text x="364" y="92" text-anchor="middle" fill="#fff" font-size="9" font-weight="800" font-family="system-ui,sans-serif">4</text>
        <text x="364" y="58" text-anchor="middle" fill="#7dd3fc" font-size="7" font-weight="700" font-family="system-ui,sans-serif">КТЭ</text>
        <text x="364" y="128" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">заключение</text>
        <text x="364" y="138" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">2013 г.</text>

        <!-- 5 ст. 75 -->
        <circle cx="468" cy="88" r="22" fill="#1e293b" stroke="#fbbf24" stroke-width="2.5" filter="url(#obProcGlow)"/>
        <text x="468" y="92" text-anchor="middle" fill="#fde68a" font-size="8" font-weight="800" font-family="system-ui,sans-serif">75</text>
        <text x="468" y="58" text-anchor="middle" fill="#fde68a" font-size="7" font-weight="700" font-family="system-ui,sans-serif">ст. 75</text>
        <text x="468" y="128" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">ч. 2 п. 3</text>
        <text x="468" y="138" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">УПК</text>

        <path d="M74 88 L130 88" fill="none" stroke="#38bdf8" stroke-width="1.2" marker-end="url(#obProcArr)" opacity="0.8"/>
        <path d="M178 88 L234 88" fill="none" stroke="#38bdf8" stroke-width="1.2" marker-end="url(#obProcArr)" opacity="0.8"/>
        <path d="M286 88 L340 88" fill="none" stroke="#f87171" stroke-width="1.2" marker-end="url(#obProcArr)" opacity="0.6"/>
        <path d="M386 88 L444 88" fill="none" stroke="#fbbf24" stroke-width="1.2" marker-end="url(#obProcArr)" opacity="0.8"/>

        <!-- Итог контура A -->
        <rect x="120" y="158" width="280" height="28" rx="6" fill="rgba(248,113,113,0.12)" stroke="rgba(248,113,113,0.4)" stroke-width="1.2"/>
        <text x="260" y="176" text-anchor="middle" fill="#fca5a5" font-size="7.5" font-weight="700" font-family="system-ui,sans-serif">КТЭ сохранена · недопустимость не доказана</text>
      </svg>

      <ul class="l24-boris-obysk-flow__steps" aria-label="Шаги контура A">
        <li class="l24-boris-obysk-flow__step l24-boris-obysk-flow__step--weak">
          <strong>Слабый довод (отклонён)</strong>
          «Не упаковали → КТЭ недопустима» — ВС: ч. 10 ст. 182 не делает упаковку обязательной.
        </li>
        <li class="l24-boris-obysk-flow__step">
          <strong>Сильный довод (для иных дел)</strong>
          Разрыв цепочки: протокол ↔ бирка ↔ фото ↔ заключение; переупаковка; ст. 164.1 для ЭНИ.
        </li>
      </ul>
      <p class="l24-boris-obysk-flow__caption">Цепочка идентификации: протокол → упаковка/фото → постановление → заключение</p>
    </div>

    <!-- КОНТУР B -->
    <div class="l24-boris-obysk-flow__panel l24-boris-obysk-flow__panel--b">
      <div class="l24-boris-obysk-flow__panel-head">
        <p class="l24-boris-obysk-flow__panel-title">Контур B — уголовно-правовой</p>
        <span class="l24-boris-obysk-flow__badge l24-boris-obysk-flow__badge--win">сработал · −3 мес.</span>
      </div>
      <svg class="l24-boris-obysk-flow__route-svg" viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="obFlowBT obFlowBD">
        <title id="obFlowBT">Контур B: квалификация проверочной закупки по ст. 9 УК и Пленуму № 14</title>
        <desc id="obFlowBD">Проверочная закупка 20.06.2013 → ст. 9 УК → п. 13 Пленума № 14 (ред. 2010) → покушение → снижение срока на 3 месяца</desc>
        <defs>
          <linearGradient id="obQualLine" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#34d399"/>
            <stop offset="100%" stop-color="#6ee7b7"/>
          </linearGradient>
          <marker id="obQualArr" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
            <polygon points="0 0, 7 3, 0 6" fill="#6ee7b7"/>
          </marker>
          <filter id="obQualGlow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.35"/>
          </filter>
        </defs>

        <rect x="8" y="8" width="504" height="184" rx="10" fill="rgba(52,211,153,0.04)" stroke="rgba(52,211,153,0.18)" stroke-width="1.2"/>

        <line x1="52" y1="88" x2="468" y2="88" stroke="rgba(52,211,153,0.15)" stroke-width="8" stroke-linecap="round"/>
        <line x1="52" y1="88" x2="468" y2="88" stroke="url(#obQualLine)" stroke-width="2.5" stroke-linecap="round"/>

        <!-- 1 Проверочная закупка -->
        <circle cx="52" cy="88" r="22" fill="#1e293b" stroke="#34d399" stroke-width="2.5" filter="url(#obQualGlow)"/>
        <text x="52" y="92" text-anchor="middle" fill="#fff" font-size="9" font-weight="800" font-family="system-ui,sans-serif">1</text>
        <text x="52" y="54" text-anchor="middle" fill="#6ee7b7" font-size="6.5" font-weight="700" font-family="system-ui,sans-serif">ПРОВЕРОЧНАЯ</text>
        <text x="52" y="64" text-anchor="middle" fill="#6ee7b7" font-size="6.5" font-weight="700" font-family="system-ui,sans-serif">ЗАКУПКА</text>
        <text x="52" y="128" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">20.06.2013</text>
        <text x="52" y="138" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">марихуана</text>

        <!-- 2 ст. 9 УК -->
        <circle cx="182" cy="88" r="22" fill="#1e293b" stroke="#34d399" stroke-width="2.5" filter="url(#obQualGlow)"/>
        <text x="182" y="92" text-anchor="middle" fill="#fff" font-size="8" font-weight="800" font-family="system-ui,sans-serif">9</text>
        <text x="182" y="58" text-anchor="middle" fill="#6ee7b7" font-size="7" font-weight="700" font-family="system-ui,sans-serif">ст. 9 УК</text>
        <text x="182" y="128" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">закон на</text>
        <text x="182" y="138" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">момент деяния</text>

        <!-- 3 Пленум 14 -->
        <circle cx="312" cy="88" r="24" fill="#1e293b" stroke="#34d399" stroke-width="3" filter="url(#obQualGlow)"/>
        <text x="312" y="92" text-anchor="middle" fill="#fff" font-size="8" font-weight="800" font-family="system-ui,sans-serif">14</text>
        <text x="312" y="54" text-anchor="middle" fill="#6ee7b7" font-size="6.5" font-weight="700" font-family="system-ui,sans-serif">ПЛЕНУМ</text>
        <text x="312" y="64" text-anchor="middle" fill="#6ee7b7" font-size="6.5" font-weight="700" font-family="system-ui,sans-serif">ВС № 14</text>
        <text x="312" y="128" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">п. 13 · ред.</text>
        <text x="312" y="138" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">23.12.2010</text>

        <!-- 4 Покушение -->
        <circle cx="442" cy="88" r="22" fill="#14532d" stroke="#6ee7b7" stroke-width="2.5" filter="url(#obQualGlow)"/>
        <text x="442" y="86" text-anchor="middle" fill="#6ee7b7" font-size="6.5" font-weight="800" font-family="system-ui,sans-serif">ч.3</text>
        <text x="442" y="96" text-anchor="middle" fill="#6ee7b7" font-size="6.5" font-weight="800" font-family="system-ui,sans-serif">ст.30</text>
        <text x="442" y="58" text-anchor="middle" fill="#6ee7b7" font-size="7" font-weight="700" font-family="system-ui,sans-serif">ПОКУШЕНИЕ</text>
        <text x="442" y="128" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">вместо</text>
        <text x="442" y="138" text-anchor="middle" fill="#94a3b8" font-size="6" font-family="system-ui,sans-serif">оконч. сбыта</text>

        <path d="M74 88 L158 88" fill="none" stroke="#34d399" stroke-width="1.2" marker-end="url(#obQualArr)" opacity="0.9"/>
        <path d="M204 88 L286 88" fill="none" stroke="#34d399" stroke-width="1.2" marker-end="url(#obQualArr)" opacity="0.9"/>
        <path d="M336 88 L418 88" fill="none" stroke="#34d399" stroke-width="1.2" marker-end="url(#obQualArr)" opacity="0.9"/>

        <!-- Итог контура B -->
        <rect x="120" y="158" width="280" height="28" rx="6" fill="rgba(52,211,153,0.14)" stroke="rgba(52,211,153,0.45)" stroke-width="1.2"/>
        <text x="260" y="176" text-anchor="middle" fill="#6ee7b7" font-size="7.5" font-weight="700" font-family="system-ui,sans-serif">10 лет 6 мес. → 10 лет 3 мес. (−3 мес.)</text>
      </svg>

      <ul class="l24-boris-obysk-flow__steps" aria-label="Шаги контура B">
        <li class="l24-boris-obysk-flow__step">
          <strong>Переквалификация эпизода</strong>
          Суд I инстанции: оконченный сбыт → ВС: покушение (ч. 3 ст. 30 + ст. 228.1) по закону, действовавшему до 30.06.2015.
        </li>
        <li class="l24-boris-obysk-flow__step">
          <strong>Ретроспективность</strong>
          ст. 9 УК + п. 13 Пленума № 14 (ред. 23.12.2010): изъятие из оборота при проверочной закупке = покушение.
        </li>
      </ul>
      <p class="l24-boris-obysk-flow__caption">Пленум № 14 от 15.06.2006 · п. 13 в ред. 23.12.2010 · до изменений 30.06.2015</p>
    </div>
  </div>

  <!-- Сводка: оба контура → итог кассации -->
  <div class="l24-boris-obysk-flow__merge">
    <p class="l24-boris-obysk-flow__merge-title">Итог кассации · дело № 32-УД26-10-K1</p>
    <svg class="l24-boris-obysk-flow__merge-svg" viewBox="0 0 520 72" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Сводка: контур A провалился, контур B дал снижение наказания">
      <defs>
        <marker id="obMergeArr" markerWidth="6" markerHeight="5" refX="5" refY="2.5" orient="auto">
          <polygon points="0 0, 6 2.5, 0 5" fill="#fde68a"/>
        </marker>
      </defs>
      <rect x="16" y="20" width="140" height="32" rx="6" fill="rgba(56,189,248,0.1)" stroke="rgba(56,189,248,0.35)" stroke-width="1.2"/>
      <text x="86" y="34" text-anchor="middle" fill="#7dd3fc" font-size="7" font-weight="700" font-family="system-ui,sans-serif">КОНТУР A</text>
      <text x="86" y="46" text-anchor="middle" fill="#fca5a5" font-size="6.5" font-family="system-ui,sans-serif">КТЭ сохранена</text>

      <rect x="184" y="20" width="140" height="32" rx="6" fill="rgba(52,211,153,0.12)" stroke="rgba(52,211,153,0.4)" stroke-width="1.2"/>
      <text x="254" y="34" text-anchor="middle" fill="#6ee7b7" font-size="7" font-weight="700" font-family="system-ui,sans-serif">КОНТУР B</text>
      <text x="254" y="46" text-anchor="middle" fill="#6ee7b7" font-size="6.5" font-family="system-ui,sans-serif">покушение · −3 мес.</text>

      <line x1="156" y1="36" x2="178" y2="36" stroke="#475569" stroke-width="1" stroke-dasharray="3,2"/>
      <text x="167" y="30" text-anchor="middle" fill="#64748b" font-size="5.5" font-family="system-ui,sans-serif">+</text>

      <path d="M324 36 L368 36" fill="none" stroke="#fde68a" stroke-width="1.5" marker-end="url(#obMergeArr)"/>

      <rect x="372" y="14" width="132" height="44" rx="8" fill="rgba(251,191,36,0.12)" stroke="#fbbf24" stroke-width="1.4"/>
      <text x="438" y="32" text-anchor="middle" fill="#fde68a" font-size="7.5" font-weight="800" font-family="system-ui,sans-serif">10 лет 6 мес.</text>
      <text x="438" y="44" text-anchor="middle" fill="#fff" font-size="8" font-weight="800" font-family="system-ui,sans-serif">→ 10 лет 3 мес.</text>
      <text x="438" y="54" text-anchor="middle" fill="#94a3b8" font-size="5.5" font-family="system-ui,sans-serif">ИК строгого режима</text>
    </svg>
  </div>

  <p class="l24-boris-obysk-flow__total"><strong>Урок для защитника:</strong> не ставить всё на один довод. После определения ВС 24.08.2026 формула «не упаковали — недопустимо» <strong>сама по себе не работает</strong> — нужна цепочка идентификации и доказательство влияния на достоверность (ст. 75, 88 УПК). Параллельно проверяйте <strong>квалификацию каждого эпизода</strong> — ст. 9 УК и редакция Пленума № 14 на дату деяния могут дать снижение даже при сохранении КТЭ.</p>

  <div class="l24-boris-obysk-flow__foot">
    <span class="l24-boris-obysk-flow__tag l24-boris-obysk-flow__tag--case">№ 32-УД26-10-K1</span>
    <span class="l24-boris-obysk-flow__tag l24-boris-obysk-flow__tag--proc">ч. 10 ст. 182 УПК</span>
    <span class="l24-boris-obysk-flow__tag l24-boris-obysk-flow__tag--proc">ст. 75 · 88 УПК</span>
    <span class="l24-boris-obysk-flow__tag l24-boris-obysk-flow__tag--qual">ст. 9 УК</span>
    <span class="l24-boris-obysk-flow__tag l24-boris-obysk-flow__tag--qual">Пленум № 14</span>
    <span class="l24-boris-obysk-flow__tag">24.08.2026</span>
  </div>
</div>
</section>
```
