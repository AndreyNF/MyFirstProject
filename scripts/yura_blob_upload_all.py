#!/usr/bin/env python3
"""Upload page HTML via Kovcheg blob using 4x18k chunks.

Reads chunk files and prints MCP tool call instructions.
When CURSOR_MCP_BRIDGE is available, calls tools directly.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HTML = Path("/workspace/.cursor/page-content-natasha-A7.html")
CHUNK_SIZE = 18000
PAGE_ID = 341


def chunks() -> list[str]:
    text = HTML.read_text(encoding="utf-8")
    if "<script" in text.lower():
        raise SystemExit("script tags in HTML")
    return [text[i : i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]


def payloads() -> list[dict]:
    chs = chunks()
    out = []
    for i, ch in enumerate(chs):
        p: dict = {"chunk": ch}
        if i == 0:
            p["reset"] = True
        if i == len(chs) - 1:
            p["finalize"] = True
        out.append(p)
    return out


def main() -> int:
    pl = payloads()
    out_dir = Path("/workspace/.cursor/a7-18k-calls")
    out_dir.mkdir(exist_ok=True)
    for i, p in enumerate(pl):
        (out_dir / f"call-{i}.json").write_text(
            json.dumps(p, ensure_ascii=False), encoding="utf-8"
        )
    meta = {
        "chunks": len(pl),
        "total_chars": sum(len(x["chunk"]) for x in pl),
        "page_id": PAGE_ID,
        "dir": str(out_dir),
    }
    print(json.dumps(meta))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
