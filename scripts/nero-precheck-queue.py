#!/usr/bin/env python3
"""
Pre-check очереди Legis24 перед запуском пайплайна Nero Network.

Порядок проверок (жёсткий гейт):
  1. content-plan-legis24.md — первая строка без «✅»
  2. published-pages.md — код или slug (включая канон без «dnej»)
  3. Опционально: --wp-search через переменную PRECHECK_SKIP_WP=1 отключает подсказку WP

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
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "nero-network-office-page" / "shared"
PLAN = SHARED / "content-plan-legis24.md"
PUBLISHED = SHARED / "published-pages.md"
HANDOFF_SKIP = ROOT / ".cursor" / "nero-network-precheck-last.json"

QUEUE_ROW = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([A-Z]\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|"
)
SLUG_ALIASES: dict[str, list[str]] = {
    "srok-vozrazhenij-30-dnej-vs-15-mify": [
        "srok-vozrazhenij-30-dnej-vs-15-mify",
        "srok-vozrazhenij-30-vs-15-mify",
    ],
}


def _read(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def parse_queue(plan_text: str) -> list[dict]:
    rows = []
    for line in plan_text.splitlines():
        m = QUEUE_ROW.match(line.strip())
        if not m:
            continue
        num, code, h1, slug, status = (x.strip() for x in m.groups())
        rows.append(
            {
                "num": int(num),
                "code": code,
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


def next_topic(rows: list[dict]) -> dict | None:
    for r in sorted(rows, key=lambda x: x["num"]):
        if r["done"]:
            continue
        if r["slug"].upper() in ("TBD", "—", "-", ""):
            continue
        return r
    return None


def mark_plan_done(plan_text: str, code: str, page_id: str, canonical_slug: str) -> str:
    """Обновить строку очереди для code → ✅ page_id."""
    out = []
    for line in plan_text.splitlines():
        m = QUEUE_ROW.match(line.strip())
        if m and m.group(2).strip() == code:
            num, c, h1, slug, _status = (x.strip() for x in m.groups())
            note = f"✅ page_id {page_id}"
            if canonical_slug != slug.strip():
                note += f" (канон slug: {canonical_slug})"
            line = f"| {num} | {c} | {h1} | {slug} | {note} |"
        out.append(line)
    return "\n".join(out) + ("\n" if plan_text.endswith("\n") else "")


def run(mark_done: bool = False) -> dict:
    plan_text = _read(PLAN)
    pub_text = _read(PUBLISHED)
    if not plan_text:
        return {
            "action": "BLOCKER",
            "reason": f"Нет файла плана: {PLAN}",
            "exit_code": 2,
        }

    rows = parse_queue(plan_text)
    published = parse_published(pub_text)
    topic = next_topic(rows)

    if not topic:
        all_done = rows and all(r["done"] for r in rows)
        if all_done:
            return {
                "action": "KIRILL",
                "reason": "Все 16 строк очереди ✅ — следующий запуск: Кирилл (новость дня)",
                "exit_code": 0,
            }
        pending = [r for r in rows if not r["done"]]
        codes = ", ".join(f"#{r['num']} {r['code']}" for r in pending[:3])
        return {
            "action": "BLOCKER",
            "reason": (
                "Нет незавершённой строки с валидным SLUG (не TBD). "
                f"Заполните SLUG/H1 в плане для: {codes}…"
            ),
            "exit_code": 2,
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
        "reason": "Новая тема — запускать полный пайплайн",
        "queue_num": topic["num"],
        "code": topic["code"],
        "h1": topic["h1"],
        "slug": topic["slug"],
        "exit_code": 0,
    }


def write_handoff_skip(result: dict) -> None:
    handoff = ROOT / ".cursor" / "nero-network-handoff.md"
    handoff.parent.mkdir(parents=True, exist_ok=True)
    body = f"""# Nero Network — SKIP (уже опубликовано)

=== PRECHECK (ГЕЙТ) ===
Статус: ⏭️ SKIP
Причина: {result.get("reason", "")}

Очередь: #{result.get("queue_num")} **{result.get("code")}**
H1: {result.get("h1", "")}
SLUG (план): `{result.get("slug_plan", "")}`
SLUG (канон): `{result.get("slug_canon", "")}`
page_id: {result.get("page_id", "")}
URL: {result.get("url", "")}

**Пайплайн (Коля, Женя, Юра и др.) не запускался.**

Следующий cron: возьмите следующую строку очереди без ✅ после синхронизации плана.
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
    args = parser.parse_args()
    result = run(mark_done=args.mark_done)
    if args.write_handoff and result["action"] == "SKIP":
        write_handoff_skip(result)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        action = result["action"]
        print(f"=== Nero precheck: {action} ===")
        print(result.get("reason", ""))
        for k in ("queue_num", "code", "h1", "slug", "slug_plan", "slug_canon", "page_id", "url"):
            if k in result:
                print(f"  {k}: {result[k]}")
        if result.get("plan_updated"):
            print("  plan_updated: true")

    sys.exit(result["exit_code"])


if __name__ == "__main__":
    main()
