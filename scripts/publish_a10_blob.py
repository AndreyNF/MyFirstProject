#!/usr/bin/env python3
"""Build blob append argument files for A10 page 354."""
from __future__ import annotations

import json
from pathlib import Path

HTML = Path("/workspace/.cursor/page-content-natasha-A10.html")
OUT = Path("/workspace/.cursor/a10-blob-calls")
CHUNK = 18000
PAGE_ID = 354


def main() -> int:
    text = HTML.read_text(encoding="utf-8")
    if "<script" in text.lower():
        raise SystemExit("script tags in HTML")
    parts = [text[i : i + CHUNK] for i in range(0, len(text), CHUNK)]
    OUT.mkdir(parents=True, exist_ok=True)
    for i, part in enumerate(parts):
        args: dict = {"chunk": part}
        if i == 0:
            args["reset"] = True
        if i == len(parts) - 1:
            args["finalize"] = True
        (OUT / f"{i:02d}.json").write_text(
            json.dumps(args, ensure_ascii=False), encoding="utf-8"
        )
    meta = {
        "page_id": PAGE_ID,
        "parts": len(parts),
        "chars": len(text),
        "dir": str(OUT),
    }
    (OUT / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps(meta))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
