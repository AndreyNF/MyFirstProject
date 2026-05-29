#!/usr/bin/env python3
"""Rebuild ordered chunk files from HTML (6000-char chunks, correct order)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

HTML = Path("/workspace/.cursor/page-content-natasha-B1.html")
OUT = Path("/workspace/.cursor/b1-blob-ordered")
CHUNK = 6000


def main() -> int:
    text = HTML.read_text(encoding="utf-8")
    if "<script" in text.lower():
        print("ERROR: script in HTML", file=sys.stderr)
        return 1
    chunks = [text[i : i + CHUNK] for i in range(0, len(text), CHUNK)]
    OUT.mkdir(parents=True, exist_ok=True)
    for i, ch in enumerate(chunks):
        args: dict = {"chunk": ch}
        if i == 0:
            args["reset"] = True
        if i == len(chunks) - 1:
            args["finalize"] = True
        (OUT / f"{i:02d}.json").write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"ok": True, "chunks": len(chunks), "bytes": len(text)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
