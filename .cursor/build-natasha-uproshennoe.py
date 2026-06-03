#!/usr/bin/env python3
"""Assemble Natasha HTML for uproshennoe-bankrotstvo-fns article."""
import re
import json
from pathlib import Path

SLUG = "uproshennoe-bankrotstvo-fns-otsutstvuyushchij-dolzhnik-vs"
PAGE_CLASS = f"{SLUG}-page"
ROOT = Path("/workspace/.cursor")
MD = ROOT / "zhenya-longread-uproshennoe-bankrotstvo.md"
OUT = ROOT / "page-content-natasha-uproshennoe.html"

TITLE = "ВС: ФНС не может упрощённо банкротить работающее ООО"
DESC = (
    "ВС отказал ФНС в упрощённом банкротстве «Альфа-Тех» (дело № А65-23306/2023): "
    "блокировка счетов не равна закрытию ООО. Защита должника в арбитраже и наблюдение."
)
H1 = "Упрощённое банкротство отсутствующего должника: ВС остановил ФНС в деле «Альфа-Тех»"

H2_IDS = {
    "Позиция Верховного суда: дело № А65-23306/2023 и компания «Альфа-Тех»": "vs-alfa-teh-poziciya",
    "Упрощённая процедура банкротства отсутствующего должника: ст. 227 и 230": "uproshenka-st227-230",
    "Почему блокировка счетов ФНС не делает компанию «отсутствующей»": "blokirovka-schetov-fns",
    "Банкротство юридического лица кредитором: заявление налоговой и защита должника": "bankrotstvo-kreditorom-fns",
    "Наблюдение вместо упрощённой процедуры: что меняется для ООО": "nablyudenie-vmesto-uproshenki",
    "Налоговая и банкротство ООО: инициатива ФНС и последствия": "nalogovaya-bankrotstvo-ooo",
    "Арбитражный суд и банкротство юридических лиц: подсудность и доказательства": "arbitrazh-bankrotstvo-yurlic",
    "Оспаривание сделок при банкротстве — только контекст для управляющих": "osparivanie-kontekst",
    "Обзор Верховного суда № 5/2026 и требования ФНС (контекст)": "obzor-vs-5-2026-kontekst",
    "Стратегия ответа на заявление ФНС: чеклист для директора и юриста": "strategiya-otvet-fns",
    "FAQ": "l24-faq-uproshenka",
    "Итог": "itog-uproshenka",
}


def slugify_heading(title: str) -> str:
    return H2_IDS.get(title.strip(), re.sub(r"[^a-z0-9а-яё]+", "-", title.lower())[:48].strip("-"))


def inline_md(text: str) -> str:
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        text,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def md_link_to_cta(line: str) -> str:
    m = re.match(r"\[([^\]]+)\]\((https://advokat-vsem\.ru/[^)]*)\)", line.strip())
    if m:
        label, url = m.group(1), m.group(2)
        return f"""<aside class="ym-cta ym-cta--legis24" role="complementary">
<p class="ym-cta__text">{inline_md(label)}</p>
<p class="ym-cta__actions"><a class="ym-cta__btn" href="{url}">{inline_md(label)}</a></p>
</aside>"""
    return None


def md_to_html(md: str, boris_html: str) -> str:
    lines = md.split("\n")
    out = []
    i = 0
    skip_until = {"SLUG:", "Title:", "Description:", "H1:"}
    while i < len(lines):
        line = lines[i]
        if any(line.startswith(p) for p in skip_until) or line.startswith("# ") and i < 8:
            i += 1
            continue
        if line.strip() == "BORIS_PLACEHOLDER":
            out.append(boris_html)
            i += 1
            continue
        cta = md_link_to_cta(line)
        if cta and line.strip().startswith("["):
            out.append(cta)
            i += 1
            continue
        if line.startswith("## "):
            title = line[3:].strip()
            if title == "FAQ":
                i += 1
                while i < len(lines) and not lines[i].startswith("## "):
                    i += 1
                continue
            hid = slugify_heading(title)
            out.append(f'<h2 id="{hid}">{inline_md(title)}</h2>')
            i += 1
            continue
        if line.startswith("### "):
            out.append(f"<h3>{inline_md(line[4:].strip())}</h3>")
            i += 1
            continue
        if line.strip() == "---":
            i += 1
            continue
        if line.strip().startswith("**") and "?" in line and i + 1 < len(lines) and lines[i + 1].strip():
            q = line.strip().rstrip("**").lstrip("*").strip()
            if q.endswith("**"):
                q = q[:-2].strip()
            i += 1
            a_lines = []
            while i < len(lines) and lines[i].strip() and not lines[i].startswith("**") and not lines[i].startswith("##"):
                a_lines.append(lines[i])
                i += 1
            out.append(f'<div class="l24-faq__item"><p class="l24-faq__q">{inline_md(q)}</p><p class="l24-faq__a">{inline_md(" ".join(a_lines))}</p></div>')
            continue
        if re.match(r"^\d+\.\s", line.strip()):
            out.append("<ol>")
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i].strip()):
                item = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                out.append(f"<li>{inline_md(item)}</li>")
                i += 1
            out.append("</ol>")
            continue
        if line.strip():
            para = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith("#") and lines[i].strip() != "---" and not lines[i].strip().startswith("**") and not re.match(r"^\d+\.\s", lines[i].strip()) and lines[i].strip() != "BORIS_PLACEHOLDER":
                if lines[i].strip().startswith("[") and "advokat-vsem.ru" in lines[i]:
                    break
                para.append(lines[i])
                i += 1
            out.append(f"<p>{inline_md(' '.join(para))}</p>")
            continue
        i += 1
    return "\n".join(out)


def hero() -> str:
    return f"""
<section id="l24-hero-{SLUG}" class="hero-arb-uproshenka" aria-label="{H1}">
<style>
.hero-arb-uproshenka{{position:relative;min-height:88vh;min-height:88dvh;box-sizing:border-box;display:flex;align-items:center;padding:112px 24px 72px;background:linear-gradient(158deg,#fcfcfd 0%,#f4f7fb 45%,#eef2f7 100%);color:#0f172a;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;overflow:hidden}}
.hero-arb-uproshenka::before{{content:"";position:absolute;inset:0;background:radial-gradient(ellipse 50% 42% at 88% 8%,rgba(163,24,48,.08) 0%,transparent 55%),radial-gradient(ellipse 40% 38% at 8% 92%,rgba(30,58,138,.07) 0%,transparent 52%);pointer-events:none}}
.hero-arb-uproshenka__inner{{position:relative;z-index:1;max-width:1200px;margin:0 auto;width:100%;display:grid;grid-template-columns:1.05fr .95fr;gap:40px;align-items:center}}
.hero-arb-uproshenka__badge{{display:inline-flex;align-items:center;gap:10px;margin:0 0 16px;padding:8px 14px;border-radius:999px;background:#fff;border:1px solid rgba(15,23,42,.1);font-size:.78rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:#475569}}
.hero-arb-uproshenka__dot{{width:8px;height:8px;border-radius:50%;background:#a31830}}
.hero-arb-uproshenka__h1{{margin:0 0 16px;font-size:clamp(1.45rem,3.2vw,2.2rem);line-height:1.22;font-weight:800;color:#0f172a}}
.hero-arb-uproshenka__h1 em{{font-style:normal;color:#a31830}}
.hero-arb-uproshenka__sub{{margin:0 0 22px;max-width:40em;font-size:clamp(.98rem,1.4vw,1.08rem);line-height:1.58;color:#475569}}
.hero-arb-uproshenka__facts{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 22px;padding:0;list-style:none}}
.hero-arb-uproshenka__fact{{font-size:.76rem;font-weight:700;padding:7px 11px;border-radius:8px;background:#fff;border:1px solid #e2e8f0;color:#334155}}
.hero-arb-uproshenka__fact--warn{{border-color:#fecaca;color:#a31830;background:#fef2f2}}
.hero-arb-uproshenka__cta{{display:inline-block;background:#a31830;color:#fff!important;padding:14px 26px;border-radius:8px;font-weight:700;text-decoration:none;box-shadow:0 4px 14px rgba(163,24,48,.22)}}
.hero-arb-uproshenka__cta:hover{{background:#8b1528}}
@media(max-width:900px){{.hero-arb-uproshenka__inner{{grid-template-columns:1fr}}}}
</style>
<div class="hero-arb-uproshenka__inner">
<div>
<p class="hero-arb-uproshenka__badge"><span class="hero-arb-uproshenka__dot"></span> ARB · ВС 18.05.2026 · дело А65-23306/2023</p>
<h1 class="hero-arb-uproshenka__h1">Упрощённое банкротство: <em>ВС остановил ФНС</em> в деле «Альфа-Тех»</h1>
<p class="hero-arb-uproshenka__sub">Когда блокировка счетов не равна «мёртвой» компании и как защититься в арбитражном суде от упрощёнки «отсутствующего» должника.</p>
<ul class="hero-arb-uproshenka__facts">
<li class="hero-arb-uproshenka__fact hero-arb-uproshenka__fact--warn">22,3 млн ₽ · ФНС</li>
<li class="hero-arb-uproshenka__fact">ст. 227–230</li>
<li class="hero-arb-uproshenka__fact">наблюдение</li>
<li class="hero-arb-uproshenka__fact">блокировка счетов</li>
</ul>
<a class="hero-arb-uproshenka__cta" href="https://advokat-vsem.ru/">Получить консультацию</a>
</div>
<div aria-hidden="true">
<svg viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:420px;height:auto">
<rect width="400" height="280" rx="14" fill="#fff" stroke="#e2e8f0"/>
<text x="24" y="36" fill="#64748b" font-size="11" font-weight="700">УПРОЩЁНКА vs НАБЛЮДЕНИЕ</text>
<rect x="24" y="52" width="150" height="56" rx="8" fill="#fee2e2" stroke="#fca5a5"/>
<text x="99" y="78" text-anchor="middle" fill="#a31830" font-size="11" font-weight="700">ФНС: упрощёнка</text>
<text x="99" y="94" text-anchor="middle" fill="#64748b" font-size="9">отсутствующий</text>
<path d="M174 80 H226" stroke="#94a3b8" stroke-width="2" marker-end="url(#arr-u)"/>
<defs><marker id="arr-u" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#a31830"/></marker></defs>
<rect x="226" y="52" width="150" height="56" rx="8" fill="#fef2f2" stroke="#a31830" stroke-width="1.5"/>
<text x="301" y="78" text-anchor="middle" fill="#a31830" font-size="11" font-weight="700">ВС: отмена</text>
<text x="301" y="94" text-anchor="middle" fill="#64748b" font-size="9">→ наблюдение</text>
<rect x="24" y="130" width="352" height="48" rx="8" fill="#eff6ff" stroke="#93c5fd"/>
<text x="200" y="158" text-anchor="middle" fill="#1e40af" font-size="10" font-weight="700">блокировка счетов ≠ 12 мес. без операций</text>
<rect x="24" y="196" width="168" height="64" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
<text x="108" y="224" text-anchor="middle" fill="#334155" font-size="9" font-weight="700">активы 6 000 ₽</text>
<text x="108" y="240" text-anchor="middle" fill="#64748b" font-size="8">vs 18,6 млн ₽</text>
<rect x="208" y="196" width="168" height="64" rx="8" fill="#f8fafc" stroke="#a31830"/>
<text x="292" y="224" text-anchor="middle" fill="#a31830" font-size="9" font-weight="700">отчётность · платежи</text>
<text x="292" y="240" text-anchor="middle" fill="#64748b" font-size="8">через 3-их лиц</text>
</svg>
</div>
</div>
</section>
"""


def boris() -> str:
    return """
<section id="l24-boris-uproshenka-route" class="l24-boris-uproshenka" aria-label="Маршрут: от заявления ФНС к наблюдению">
<style>
.l24-boris-uproshenka{margin:44px 0;font-family:system-ui,sans-serif}
.l24-boris-uproshenka__shell{background:linear-gradient(145deg,#0f2744,#1a365d);border-radius:14px;padding:28px 24px;color:#e2e8f0;border:1px solid rgba(236,201,75,.2)}
.l24-boris-uproshenka__eyebrow{margin:0 0 6px;font-size:.7rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#ecc94b}
.l24-boris-uproshenka__title{margin:0 0 20px;font-size:1.2rem;color:#fff;font-weight:700}
.l24-boris-uproshenka__steps{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.l24-boris-uproshenka__step{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:12px;text-align:center}
.l24-boris-uproshenka__n{display:block;font-size:.68rem;font-weight:700;color:#ecc94b;margin-bottom:6px}
.l24-boris-uproshenka__t{font-size:.78rem;line-height:1.35;color:#cbd5e1}
@media(max-width:720px){.l24-boris-uproshenka__steps{grid-template-columns:1fr 1fr}}
</style>
<div class="l24-boris-uproshenka__shell">
<p class="l24-boris-uproshenka__eyebrow">ARB · защита должника</p>
<h3 class="l24-boris-uproshenka__title">Маршрут после позиции ВС (май 2026)</h3>
<div class="l24-boris-uproshenka__steps">
<div class="l24-boris-uproshenka__step"><span class="l24-boris-uproshenka__n">1</span><span class="l24-boris-uproshenka__t">Заявление ФНС · ст. 230</span></div>
<div class="l24-boris-uproshenka__step"><span class="l24-boris-uproshenka__n">2</span><span class="l24-boris-uproshenka__t">Возражения · блокировка</span></div>
<div class="l24-boris-uproshenka__step"><span class="l24-boris-uproshenka__n">3</span><span class="l24-boris-uproshenka__t">ВС · отмена упрощёнки</span></div>
<div class="l24-boris-uproshenka__step"><span class="l24-boris-uproshenka__n">4</span><span class="l24-boris-uproshenka__t">Наблюдение · п. 64 Пленума № 40</span></div>
</div>
</div>
</section>
"""


def faq_section() -> str:
    return """
<section id="l24-faq-uproshenka" class="l24-faq" aria-label="Частые вопросы">
<h2>Частые вопросы</h2>
<div class="l24-faq__item"><p class="l24-faq__q">Может ли ФНС банкротить ООО по упрощённой процедуре, если компания продолжает сдавать отчётность?</p><p class="l24-faq__a">Сама по себе задолженность не равна «отсутствующему» должнику. По делу «Альфа-Тех» ВС указал: отчётность, текущие платежи и частичное погашение долга указывают на продолжение деятельности.</p></div>
<div class="l24-faq__item"><p class="l24-faq__q">Достаточно ли 12 месяцев без операций по счёту для ст. 230?</p><p class="l24-faq__a">Только если отсутствие движения не объясняется блокировкой счетов ФНС. В «Альфа-Тех» критерий не был соблюдён: пустой счёт — следствие блокировки.</p></div>
<div class="l24-faq__item"><p class="l24-faq__q">Что делать при противоречии по активам (6 000 ₽ vs 18,6 млн ₽)?</p><p class="l24-faq__a">Фиксировать обе позиции в процессуальных документах, требовать судебной оценки и экспертизы — это прямой аргумент ВС.</p></div>
<div class="l24-faq__item"><p class="l24-faq__q">Чем наблюдение лучше упрощёнки для работающего ООО?</p><p class="l24-faq__a">Наблюдение — реабилитационная стадия с шансом на мировое соглашение; упрощёнка ведёт к ускоренному конкурсному производству.</p></div>
<div class="l24-faq__item"><p class="l24-faq__q">Нужно ли разбирать оспаривание сделок на стадии заявления ФНС?</p><p class="l24-faq__a">В первую очередь — процедура (упрощёнка vs наблюдение). Оспаривание критично после введения конкурсного производства.</p></div>
</section>
"""


def page_css() -> str:
    return f"""
.breadcrumbs,.breadcrumb,.woocommerce-breadcrumb,.rank-math-breadcrumb,.yoast-breadcrumb,
.entry-header,.page-title-section,.entry-title,.main_title,h1.entry-title{{display:none!important}}
#primary,.site-main,.site-content,#content,.content-area{{padding-top:0!important;margin-top:0!important}}
#sidebar,.sidebar,#secondary{{display:none!important}}
.{PAGE_CLASS} .entry-content{{max-width:none!important;width:100%!important;padding:0!important}}
.{PAGE_CLASS} .l24-longread-wrap{{max-width:820px;margin:0 auto;padding:48px 24px 80px;font-size:1.05rem;line-height:1.65;color:#1a202c}}
.{PAGE_CLASS} h2{{margin-top:2.5em;color:#1a365d;font-size:1.45rem}}
.{PAGE_CLASS} h3{{margin-top:1.5em;color:#2c5282;font-size:1.15rem}}
.{PAGE_CLASS} a{{color:#1e40af}}
.ym-toc{{max-width:820px;margin:24px auto 0;padding:0 24px 32px;text-align:center;font-family:system-ui,sans-serif}}
.ym-toc__title{{font-size:.8rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#64748b;margin:0 0 12px}}
.ym-toc__list{{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;justify-content:center;gap:8px}}
.ym-toc__list a{{display:inline-block;padding:8px 12px;border-radius:8px;background:#f1f5f9;color:#1e40af;text-decoration:none;font-size:.88rem;font-weight:600}}
.ym-cta{{margin:28px 0;padding:22px 24px;border-radius:10px;background:linear-gradient(135deg,#f8fafc,#edf2f7);border:1px solid #cbd5e1;border-left:4px solid #a31830}}
.ym-cta--legis24{{border-left-color:#1e3a8a}}
.ym-cta__text{{margin:0 0 14px;line-height:1.55;color:#334155}}
.ym-cta__btn{{display:inline-block;background:#a31830;color:#fff!important;padding:12px 22px;border-radius:8px;font-weight:700;text-decoration:none}}
.l24-faq{{margin-top:2.5em;padding:28px 24px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px}}
.l24-faq__q{{margin:0 0 8px;font-size:1.05rem;color:#1a365d;font-weight:700}}
.l24-faq__a{{margin:0 0 18px;color:#334155}}
.l24-faq__item:last-child .l24-faq__a{{margin-bottom:0}}
"""


def main():
    raw = MD.read_text(encoding="utf-8")
    # strip meta header lines for body
    body_start = raw.find("\n\n# ")
    md_body = raw[body_start + 2 :] if body_start > 0 else raw
    md_body = md_body.replace("## FAQ", "BORIS_PLACEHOLDER\n\n## FAQ", 1)
    md_body = re.sub(r"^# .+\n\n", "", md_body, count=1)
    md_body = md_body.replace("## FAQ\n\n", "BORIS_PLACEHOLDER\n\n", 1)
    md_body = re.sub(r"## FAQ[\s\S]*?## Итог", "BORIS_PLACEHOLDER\n\n## Итог", md_body, count=1)

    content = md_to_html(md_body, boris())
    toc_items = [(v, k.split("-")[0].title()) for k, v in list(H2_IDS.items())[:8]]
    toc = '<nav class="ym-toc" aria-label="Содержание"><p class="ym-toc__title">Содержание</p><ul class="ym-toc__list">' + "".join(
        f'<li><a href="#{a}">{t[:40]}</a></li>' for a, t in [
            ("vs-alfa-teh-poziciya", "Позиция ВС"),
            ("uproshenka-st227-230", "Ст. 227–230"),
            ("blokirovka-schetov-fns", "Блокировка счетов"),
            ("bankrotstvo-kreditorom-fns", "Заявление ФНС"),
            ("nablyudenie-vmesto-uproshenki", "Наблюдение"),
            ("strategiya-otvet-fns", "Чеклист"),
            ("l24-faq-uproshenka", "FAQ"),
            ("itog-uproshenka", "Итог"),
        ]
    ) + "</ul></nav>"

    html = f"""<!-- wp:html -->
<style>
{page_css()}
</style>
<main id="primary" class="site-main {PAGE_CLASS}" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
<meta itemprop="headline" content="{H1}">
<meta itemprop="description" content="{DESC}">
<meta itemprop="inLanguage" content="ru-RU">
{hero()}
{toc}
<div class="l24-longread-wrap" itemprop="articleBody">
{content}
{faq_section()}
</div>
</main>
<!-- /wp:html -->
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
