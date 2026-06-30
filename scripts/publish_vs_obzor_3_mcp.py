#!/usr/bin/env python3
"""Publish vs-obzor-3 page via MCP Kovcheg blob flow (chunk prep only)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

HTML_PATH = Path("/workspace/.cursor/page-content-natasha-vs-obzor-3.html")
OUT_DIR = Path("/workspace/.cursor/vs3-blob-calls")
CHUNK = 18000

SLUG = "vs-obzor-3-2026-nalogovye-spory-ens-fns"
TITLE = "Обзор ВС № 3/2026: налоговые споры с ФНС — ЕНС, безнадёжная задолженность и защита"
EXCERPT = (
    "28 позиций обзора ВС о налоговых спорах: ЕНС, одно требование, "
    "безнадёжная задолженность, пени, НДФЛ. Как оспорить ФНС — сроки и стратегия."
)


def main() -> int:
    text = HTML_PATH.read_text(encoding="utf-8")
    low = text.lower()
    if "<script" in low:
        print("ERROR: script tags found", file=sys.stderr)
        return 1
    parts = [text[i : i + CHUNK] for i in range(0, len(text), CHUNK)]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i, part in enumerate(parts):
        args: dict = {"chunk": part}
        if i == 0:
            args["reset"] = True
        if i == len(parts) - 1:
            args["finalize"] = True
        (OUT_DIR / f"{i:02d}.json").write_text(
            json.dumps(args, ensure_ascii=False), encoding="utf-8"
        )
    meta = {
        "slug": SLUG,
        "title": TITLE,
        "excerpt": EXCERPT,
        "parts": len(parts),
        "chars": len(text),
    }
    (OUT_DIR / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(meta, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
