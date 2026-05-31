#!/usr/bin/env python3
"""
Pre-check очереди Legis24 перед запуском пайплайна Nero Network.

Порядок проверок (жёсткий гейт):
  1. Определить cron-слот (1–3) → тип ARB / IP / UG
  2. content-plan-legis24.md — первая незавершённая строка **этого типа**
  3. published-pages.md — код или slug (включая канон без «dnej»)

Коды выхода:
  0 — PROCEED: можно запускать пайплайн
  1 — SKIP: тема уже в журнале (не запускать Коля/Женя/Юра)
  2 — BLOCKER: нет темы в очереди или битый план
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "nero-network-office-page" / "shared"
PLAN = SHARED / "content-plan-legis24.md"
PUBLISHED = SHARED / "published-pages.md"
HANDOFF_SKIP = ROOT / ".cursor" / "nero-network-precheck-last.json"

# 6 колонок: # | Код | Тип | H1 | SLUG | Статус
QUEUE_ROW = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([A-Z]\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|"
)
# 5 колонок (legacy без типа): # | Код | H1 | SLUG | Статус
QUEUE_ROW_LEGACY = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([A-Z]\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|"
)

SLUG_ALIASES: dict[str, list[str]] = {
    "srok-vozrazhenij-30-dnej-vs-15-mify": [
        "srok-vozrazhenij-30-dnej-vs-15-mify",
        "srok-vozrazhenij-30-vs-15-mify",
    ],
}

SLOT_CRON_UTC = {1: "03:00", 2: "09:00", 3: "15:00"}
SLOT_MSK = {1: "06:00", 2: "12:00", 3: "18:00"}
SLOT_TYPE = {1: "ARB", 2: "IP", 3: "UG"}
TYPE_ALIASES: dict[str, set[str]] = {
    "ARB": {"ARB", "АРБ", "АРБИТРАЖ", "арбитраж", "Арбитраж"},
    "IP": {
        "IP",
        "ИС",
        "ис",
        "ИС/ТЗ",
        "интеллектуальная собственность",
        "ИС",
    },
    "UG": {"UG", "УГ", "уголовное", "Уголовное", "уголовное право"},
}


def _read(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def normalize_type(raw: str) -> str | None:
    t = raw.strip()
    if t in ("—", "-", "", "TBD"):
        return None
    upper = t.upper()
    for canonical, aliases in TYPE_ALIASES.items():
        if t in aliases or upper in aliases:
            return canonical
    if upper in ("ARB", "IP", "UG"):
        return upper
    return None


def parse_queue(plan_text: str) -> list[dict]:
    rows = []
    for line in plan_text.splitlines():
        stripped = line.strip()
        m = QUEUE_ROW.match(stripped)
        if m:
            num, code, typ, h1, slug, status = (x.strip() for x in m.groups())
            rows.append(
                {
                    "num": int(num),
                    "code": code,
                    "type": normalize_type(typ),
                    "type_raw": typ,
                    "h1": h1,
                    "slug": slug,
                    "status": status,
                    "done": "✅" in status,
                }
            )
            continue
        m = QUEUE_ROW_LEGACY.match(stripped)
        if m:
            num, code, h1, slug, status = (x.strip() for x in m.groups())
            rows.append(
                {
                    "num": int(num),
                    "code": code,
                    "type": None,
                    "type_raw": "—",
                    "h1": h1,
                    "slug": slug,
                    "status": status,
                    "done": "✅" in status,
                }
            )
    return rows


def parse_published(text: str) -> list[dict]:
    entries = []
    for line in text.splitlines():
        if not line.startswith("|") or "---" in line or "Дата" in line:
            continue
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) < 5:
            continue
        entries.append(
            {
                "date": parts[0],
                "code": parts[1],
                "slug": parts[2],
                "page_id": parts[3],
                "url": parts[4],
            }
        )
    return entries


def slug_variants(slug: str) -> set[str]:
    slug = slug.strip().lower()
    if slug in SLUG_ALIASES:
        return set(SLUG_ALIASES[slug])
    variants = {slug}
    if "-30-dnej-" in slug:
        variants.add(slug.replace("-30-dnej-", "-30-"))
    if "-30-" in slug and "-dnej-" not in slug:
        variants.add(slug.replace("-30-", "-30-dnej-", 1))
    return variants


def find_in_published(
    code: str, slug: str, published: list[dict]
) -> dict | None:
    variants = slug_variants(slug)
    for e in published:
        if e["code"].upper() == code.upper():
            return e
        if e["slug"].lower() in variants:
            return e
    return None


def cron_slot_from_utc_hour(hour: int) -> int:
    """Слот по окну cron: 03–08 → 1, 09–14 → 2, 15–20 → 3."""
    if 3 <= hour < 9:
        return 1
    if 9 <= hour < 15:
        return 2
    if 15 <= hour < 21:
        return 3
    return 0


def next_topic(rows: list[dict], slot: int | None = None) -> dict | None:
    want = SLOT_TYPE.get(slot) if slot else None
    for r in sorted(rows, key=lambda x: x["num"]):
        if r["done"]:
            continue
        if r["slug"].upper() in ("TBD", "—", "-", ""):
            continue
        if want and r["type"] and r["type"] != want:
            continue
        if want and not r["type"]:
            continue
        return r
    if want:
        for r in sorted(rows, key=lambda x: x["num"]):
            if not r["done"] and r["slug"].upper() not in ("TBD", "—", "-", ""):
                if r["type"] == want:
                    return r
    for r in sorted(rows, key=lambda x: x["num"]):
        if r["done"]:
            continue
        if r["slug"].upper() in ("TBD", "—", "-", ""):
            continue
        return r
    return None


def mark_plan_done(plan_text: str, code: str, page_id: str, canonical_slug: str) -> str:
    out = []
    for line in plan_text.splitlines():
        m6 = QUEUE_ROW.match(line.strip())
        m5 = QUEUE_ROW_LEGACY.match(line.strip()) if not m6 else None
        if m6 and m6.group(2).strip() == code:
            num, c, typ, h1, slug, _status = (x.strip() for x in m6.groups())
            note = f"✅ page_id {page_id}"
            if canonical_slug != slug.strip():
                note += f" (канон slug: {canonical_slug})"
            line = f"| {num} | {c} | {typ} | {h1} | {slug} | {note} |"
        elif m5 and m5.group(2).strip() == code:
            num, c, h1, slug, _status = (x.strip() for x in m5.groups())
            note = f"✅ page_id {page_id}"
            if canonical_slug != slug.strip():
                note += f" (канон slug: {canonical_slug})"
            line = f"| {num} | {c} | {h1} | {slug} | {note} |"
        out.append(line)
    return "\n".join(out) + ("\n" if plan_text.endswith("\n") else "")


def slot_meta(slot: int) -> dict:
    t = SLOT_TYPE[slot]
    labels = {"ARB": "арбитраж", "IP": "защита ИС / товарный знак", "UG": "уголовное право"}
    return {
        "cron_slot": slot,
        "article_type": t,
        "article_type_label": labels.get(t, t),
        "cron_utc": SLOT_CRON_UTC[slot],
        "cron_msk": SLOT_MSK[slot],
    }


def run(mark_done: bool = False, slot: int | None = None) -> dict:
    plan_text = _read(PLAN)
    pub_text = _read(PUBLISHED)
    if not plan_text:
        return {
            "action": "BLOCKER",
            "reason": f"Нет файла плана: {PLAN}",
            "exit_code": 2,
        }

    now = datetime.now(timezone.utc)
    auto_slot = cron_slot_from_utc_hour(now.hour)
    use_slot = slot if slot in (1, 2, 3) else auto_slot

    if use_slot == 0:
        return {
            "action": "BLOCKER",
            "reason": (
                f"Вне окон публикации (UTC {now.hour:02d}:xx). "
                "Окна: 03–08 (ARB), 09–14 (IP), 15–20 (UG). "
                "Запустите с --slot 1|2|3 для ручного прогона."
            ),
            "exit_code": 2,
            "utc_hour": now.hour,
        }

    meta = slot_meta(use_slot)
    rows = parse_queue(plan_text)
    published = parse_published(pub_text)
    topic = next_topic(rows, use_slot)

    if not topic:
        all_done = rows and all(r["done"] for r in rows)
        if all_done:
            return {
                "action": "KIRILL",
                "reason": "Все 16 строк очереди ✅ — следующий запуск: Кирилл (новость дня)",
                "exit_code": 0,
                **meta,
            }
        pending = [
            r
            for r in rows
            if not r["done"] and r["slug"].upper() not in ("TBD", "—", "-", "")
        ]
        typed = [r for r in pending if r["type"] == meta["article_type"]]
        if not typed:
            codes = ", ".join(f"#{r['num']} {r['code']}" for r in pending[:3])
            return {
                "action": "BLOCKER",
                "reason": (
                    f"Нет незавершённой строки типа {meta['article_type']} "
                    f"({meta['article_type_label']}) для слота {use_slot}. "
                    f"Добавьте тему в план или заполните: {codes}…"
                ),
                "exit_code": 2,
                **meta,
            }
        codes = ", ".join(f"#{r['num']} {r['code']}" for r in pending[:3])
        return {
            "action": "BLOCKER",
            "reason": (
                "Нет незавершённой строки с валидным SLUG (не TBD). "
                f"Заполните SLUG/H1 в плане для: {codes}…"
            ),
            "exit_code": 2,
            **meta,
        }

    hit = find_in_published(topic["code"], topic["slug"], published)
    if hit:
        result = {
            "action": "SKIP",
            "reason": "Тема уже в published-pages.md — пайплайн не запускать",
            "queue_num": topic["num"],
            "code": topic["code"],
            "h1": topic["h1"],
            "slug_plan": topic["slug"],
            "slug_canon": hit["slug"],
            "page_id": hit["page_id"],
            "url": hit["url"],
            "exit_code": 1,
            **meta,
        }
        if mark_done and "✅" not in topic["status"]:
            new_plan = mark_plan_done(
                plan_text, topic["code"], hit["page_id"], hit["slug"]
            )
            PLAN.write_text(new_plan, encoding="utf-8")
            result["plan_updated"] = True
        return result

    return {
        "action": "PROCEED",
        "reason": (
            f"Новая тема слота {use_slot} ({meta['article_type_label']}) — "
            "запускать полный пайплайн. Угол: article-types-legis24.md"
        ),
        "queue_num": topic["num"],
        "code": topic["code"],
        "h1": topic["h1"],
        "slug": topic["slug"],
        "topic_type": topic.get("type") or meta["article_type"],
        "exit_code": 0,
        **meta,
    }


def write_handoff_skip(result: dict) -> None:
    handoff = ROOT / ".cursor" / "nero-network-handoff.md"
    handoff.parent.mkdir(parents=True, exist_ok=True)
    slot = result.get("cron_slot", "")
    atype = result.get("article_type", "")
    body = f"""# Nero Network — SKIP (уже опубликовано)

=== PRECHECK (ГЕЙТ) ===
Статус: ⏭️ SKIP
Причина: {result.get("reason", "")}
Слот: {slot} ({result.get("cron_utc", "")} UTC / {result.get("cron_msk", "")} МСК)
Тип статьи: {atype} — {result.get("article_type_label", "")}

Очередь: #{result.get("queue_num")} **{result.get("code")}**
H1: {result.get("h1", "")}
SLUG (план): `{result.get("slug_plan", "")}`
SLUG (канон): `{result.get("slug_canon", "")}`
page_id: {result.get("page_id", "")}
URL: {result.get("url", "")}

**Пайплайн (Коля, Женя, Юра и др.) не запускался.**

Следующий слот: см. content-plan-legis24.md (3 публикации/сутки, +6 ч).
"""
    handoff.write_text(body, encoding="utf-8")
    HANDOFF_SKIP.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")


def write_handoff_gate(result: dict) -> None:
    """Минимальный гейт в handoff + актуальный JSON (KIRILL / PROCEED)."""
    handoff = ROOT / ".cursor" / "nero-network-handoff.md"
    handoff.parent.mkdir(parents=True, exist_ok=True)
    action = result.get("action", "")
    slot = result.get("cron_slot", "")
    atype = result.get("article_type", "")
    label = result.get("article_type_label", "")
    status = "✅ KIRILL" if action == "KIRILL" else "✅ PROCEED"
    body = f"""# Legis24 — precheck {action} (слот {atype})

=== PRECHECK (ГЕЙТ) ===
Статус: {status}
Причина: {result.get("reason", "")}
Слот: {slot} ({result.get("cron_utc", "")} UTC / {result.get("cron_msk", "")} МСК)
Тип статьи: {atype} — {label}
Угол: см. nero-network-office-page/shared/article-types-legis24.md (тип {atype})

**Полный пайплайн (Коля, Женя, Юра) в этом запуске не запускался.**
"""
    if action == "PROCEED":
        body += f"""
Очередь: #{result.get("queue_num")} **{result.get("code")}**
H1: {result.get("h1", "")}
SLUG: `{result.get("slug", "")}`

Следующий шаг: сброс handoff → Коля||Артём.
"""
    elif action == "KIRILL":
        body += """
Следующий шаг: Task(kirill) — новость дня по типу слота.
"""
    handoff.write_text(body, encoding="utf-8")
    HANDOFF_SKIP.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Pre-check очереди Legis24")
    parser.add_argument("--json", action="store_true", help="JSON на stdout")
    parser.add_argument(
        "--mark-done",
        action="store_true",
        help="Проставить ✅ в content-plan для SKIP-строки",
    )
    parser.add_argument(
        "--write-handoff",
        action="store_true",
        help="Записать handoff SKIP (для automation)",
    )
    parser.add_argument(
        "--slot",
        type=int,
        choices=[1, 2, 3],
        help="Принудительный слот (1=ARB 03:00, 2=IP 09:00, 3=UG 15:00 UTC)",
    )
    args = parser.parse_args()
    result = run(mark_done=args.mark_done, slot=args.slot)
    if args.write_handoff:
        if result["action"] == "SKIP":
            write_handoff_skip(result)
        elif result["action"] in ("KIRILL", "PROCEED"):
            write_handoff_gate(result)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        action = result["action"]
        print(f"=== Nero precheck: {action} ===")
        print(result.get("reason", ""))
        extra_keys = (
            "cron_slot",
            "article_type",
            "article_type_label",
            "cron_utc",
            "cron_msk",
            "queue_num",
            "code",
            "h1",
            "slug",
            "slug_plan",
            "slug_canon",
            "page_id",
            "url",
            "topic_type",
        )
        for k in extra_keys:
            if k in result:
                print(f"  {k}: {result[k]}")
        if result.get("plan_updated"):
            print("  plan_updated: true")

    sys.exit(result["exit_code"])


if __name__ == "__main__":
    main()
