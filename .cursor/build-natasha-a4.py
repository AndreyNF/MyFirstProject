#!/usr/bin/env python3
"""Сборка page-content-natasha-A4.html для MCP publish."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LONG = ROOT / ".cursor/nero-network-fragments/zhenya-longread.html"
OUT = ROOT / ".cursor/page-content-natasha-A4.html"
SLUG = "plan-restrukturizacii-dolgov-grazhdanina-sroki"

BORIS = """
<section id="l24-boris-plan-restr" class="l24-boris-block" aria-label="Сроки: собрание и суд">
  <div class="l24-boris-block__inner">
    <p class="l24-boris-block__eyebrow">127-ФЗ · план реструктуризации</p>
    <h3 class="l24-boris-block__title">10 дней на проект ≠ 5 лет реализации: два контура сроков</h3>
    <p class="l24-boris-block__lead">Путаница «сроки плана» чаще всего смешивает <strong>процессуальный календарь до собрания</strong> и <strong>срок выплат после утверждения</strong> — это разные этапы по ст. 213.12–213.14.</p>
    <div class="l24-boris-block__grid">
      <div class="l24-boris-card l24-boris-card--navy">
        <strong>До утверждения</strong>
        <ul>
          <li>2 мес. — требования в реестр</li>
          <li>10 дн. — проект плана управляющему</li>
          <li>20–60 дн. — первое собрание</li>
        </ul>
      </div>
      <div class="l24-boris-card l24-boris-card--accent">
        <strong>После утверждения судом</strong>
        <ul>
          <li>до 5 лет — реализация плана</li>
          <li>до 3 лет — если без одобрения собрания (п. 4 ст. 213.17)</li>
          <li>2 мес. — доработка при отказе собрания</li>
        </ul>
      </div>
    </div>
    <table class="l24-boris-table">
      <thead><tr><th>Этап</th><th>Кто решает</th><th>Что при провале</th></tr></thead>
      <tbody>
        <tr><td>Одобрение проекта</td><td>Собрание кредиторов (ст. 213.16)</td><td>Доработка или переход к реализации</td></tr>
        <tr><td>Утверждение плана</td><td>Арбитражный суд (ст. 213.17)</td><td>Реализация имущества</td></tr>
        <tr><td>Возражения</td><td>Должник / ФУ на собрании</td><td>Голосование «против» + суд</td></tr>
      </tbody>
    </table>
  </div>
</section>
"""

HERO_CSS = """
.hero-plan-restr {
  min-height: 100vh;
  min-height: 100dvh;
  position: relative;
  background: linear-gradient(135deg, #1a365d 0%, #2c5282 45%, #1a365d 100%);
  color: #fff;
  display: flex;
  align-items: center;
  padding: 120px 24px 80px;
  box-sizing: border-box;
}
.hero-plan-restr__inner {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: center;
  width: 100%;
}
.hero-plan-restr__badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  opacity: 0.9;
  margin-bottom: 16px;
}
.hero-plan-restr__badge-dot {
  width: 8px; height: 8px;
  background: #a31830;
  border-radius: 50%;
}
.hero-plan-restr__h1 {
  font-size: clamp(1.75rem, 4vw, 2.5rem);
  line-height: 1.2;
  margin: 0 0 16px;
  font-weight: 800;
}
.hero-plan-restr__h1-accent { color: #fbd38d; }
.hero-plan-restr__sub { font-size: 1.1rem; opacity: 0.92; margin: 0 0 24px; max-width: 36em; }
.hero-plan-restr__steps { list-style: none; padding: 0; margin: 0 0 28px; }
.hero-plan-restr__step {
  display: flex; gap: 12px; align-items: flex-start;
  margin-bottom: 12px; font-size: 0.95rem;
}
.hero-plan-restr__step-num {
  flex-shrink: 0;
  width: 28px; height: 28px;
  background: #a31830;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-weight: 700; font-size: 0.8rem;
}
.hero-plan-restr__cta {
  display: inline-block;
  background: #a31830;
  color: #fff !important;
  padding: 14px 28px;
  border-radius: 8px;
  font-weight: 700;
  text-decoration: none;
}
.hero-plan-restr__cta:hover { background: #8b1528; }
@media (max-width: 900px) {
  .hero-plan-restr__inner { grid-template-columns: 1fr; }
  .hero-plan-restr__visual { display: none; }
}
"""

PAGE_CSS = """
.breadcrumbs, .breadcrumb, .woocommerce-breadcrumb, .rank-math-breadcrumb, .yoast-breadcrumb,
.entry-header, .page-title-section { display: none !important; }
#primary, .site-main, .site-content, #content, .content-area {
  padding-top: 0 !important; margin-top: 0 !important;
}
#sidebar, .sidebar, #secondary, .et_pb_column_1_4 { display: none !important; }
.plan-restrukturizacii-dolgov-grazhdanina-sroki-page .entry-content {
  max-width: none !important;
  width: 100% !important;
  padding: 0 !important;
}
.plan-restrukturizacii-dolgov-grazhdanina-sroki-page .l24-longread-wrap {
  max-width: 820px;
  margin: 0 auto;
  padding: 48px 24px 80px;
  font-size: 1.05rem;
  line-height: 1.65;
  color: #1a202c;
}
.plan-restrukturizacii-dolgov-grazhdanina-sroki-page h2 { margin-top: 2.5em; color: #1a365d; }
.plan-restrukturizacii-dolgov-grazhdanina-sroki-page table {
  width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.95rem;
}
.plan-restrukturizacii-dolgov-grazhdanina-sroki-page th,
.plan-restrukturizacii-dolgov-grazhdanina-sroki-page td {
  border: 1px solid #e2e8f0; padding: 10px 12px; text-align: left;
}
.plan-restrukturizacii-dolgov-grazhdanina-sroki-page th { background: #edf2f7; }
.answer-first { background: #f7fafc; border-left: 4px solid #a31830; padding: 20px 24px; margin-bottom: 2em; }
.l24-boris-block {
  margin: 48px 0;
  padding: 40px 32px;
  background: linear-gradient(180deg, #f8fafc 0%, #fff 100%);
  border: 1px solid #e2e8f0;
  border-radius: 12px;
}
.l24-boris-block__eyebrow { font-size: 0.75rem; font-weight: 700; letter-spacing: 0.06em; color: #a31830; margin: 0 0 8px; }
.l24-boris-block__title { margin: 0 0 12px; color: #1a365d; font-size: 1.35rem; }
.l24-boris-block__grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0; }
.l24-boris-card { padding: 20px; border-radius: 8px; color: #fff; }
.l24-boris-card--navy { background: #1a365d; }
.l24-boris-card--accent { background: #a31830; }
.l24-boris-card ul { margin: 8px 0 0; padding-left: 18px; }
.l24-boris-table { width: 100%; }
@media (max-width: 900px) {
  .l24-boris-block__grid { grid-template-columns: 1fr; }
  #sidebar, .sidebar { display: none !important; }
}
"""

HERO_HTML = """
<section id="l24-hero-plan-restr" class="hero-plan-restr" aria-label="План реструктуризации долгов гражданина">
  <div class="hero-plan-restr__inner">
    <div class="hero-plan-restr__content">
      <div class="hero-plan-restr__badge">
        <span class="hero-plan-restr__badge-dot" aria-hidden="true"></span>
        Банкротство физлица · 127-ФЗ · 2025–2026
      </div>
      <h1 class="hero-plan-restr__h1">
        <span class="hero-plan-restr__h1-accent">План реструктуризации:</span> сроки, собрание и утверждение судом
      </h1>
      <p class="hero-plan-restr__sub">
        От 10 дней на проект плана до 5 лет реализации — разбираем календарь по ст. 213.12–213.17 и возражения на собрании
      </p>
      <ol class="hero-plan-restr__steps">
        <li class="hero-plan-restr__step">
          <span class="hero-plan-restr__step-num">1</span>
          <span><strong>2 месяца</strong> — кредиторы заявляют требования в реестр</span>
        </li>
        <li class="hero-plan-restr__step">
          <span class="hero-plan-restr__step-num">2</span>
          <span><strong>10 дней</strong> — направление проекта плана финуправляющему</span>
        </li>
        <li class="hero-plan-restr__step">
          <span class="hero-plan-restr__step-num">3</span>
          <span><strong>Собрание + суд</strong> — одобрение и утверждение плана</span>
        </li>
      </ol>
      <a class="hero-plan-restr__cta" href="https://advokat-vsem.ru/">Консультация по плану реструктуризации</a>
    </div>
    <div class="hero-plan-restr__visual" aria-hidden="true">
      <svg viewBox="0 0 400 360" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:400px">
        <rect x="20" y="20" width="360" height="320" rx="16" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.2)"/>
        <text x="40" y="60" fill="#fbd38d" font-size="12" font-weight="700">КАЛЕНДАРЬ ПЛАНА</text>
        <rect x="40" y="90" width="120" height="40" rx="6" fill="#a31830"/>
        <text x="55" y="115" fill="#fff" font-size="11">10 дн. → проект</text>
        <rect x="180" y="90" width="120" height="40" rx="6" fill="rgba(255,255,255,0.25)"/>
        <text x="195" y="115" fill="#fff" font-size="11">20–60 дн. → собрание</text>
        <rect x="40" y="160" width="260" height="50" rx="6" fill="rgba(255,255,255,0.15)"/>
        <text x="55" y="190" fill="#fff" font-size="11">до 5 лет — реализация утверждённого плана</text>
        <circle cx="200" cy="280" r="50" fill="none" stroke="#fbd38d" stroke-width="3"/>
        <text x="168" y="285" fill="#fff" font-size="14" font-weight="700">213.17</text>
      </svg>
    </div>
  </div>
</section>
"""


def main():
    raw = LONG.read_text(encoding="utf-8")
    if "LONGREAD_BODY_START" in raw:
        body = raw.split("LONGREAD_BODY_START", 1)[1]
        body = body.split("=== ЖЕНЯ", 1)[0].strip()
    else:
        body = raw

    # Insert Boris after 2nd </h2> block (end of second h2 section)
    parts = body.split("</h2>")
    if len(parts) >= 3:
        body = "</h2>".join(parts[:2]) + "</h2>" + BORIS + "</h2>".join(parts[2:])
    else:
        body = BORIS + body

    html = f"""<!-- wp:html -->
<style>
{HERO_CSS}
{PAGE_CSS}
</style>
<main id="primary" class="site-main plan-restrukturizacii-dolgov-grazhdanina-sroki-page" role="main" tabindex="-1">
{HERO_HTML}
<div class="l24-longread-wrap">
{body}
</div>
</main>
<!-- /wp:html -->
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
