#!/usr/bin/env python3
"""Upload page 341 HTML to WordPress via Kovcheg blob (chunk files on disk).

Run from repo root. Prints JSON lines for each blob step; agent must call MCP
wordpress_content_blob_append with each payload, then update_page_from_blob.

This script only prepares/validates chunks — MCP calls are done via mcp_call_tool.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HTML = Path("/workspace/.cursor/page-content-natasha-A7.html")
CHUNK_SIZE = 18000
OUT_DIR = Path("/workspace/.cursor")


def main() -> int:
    if not HTML.is_file():
        print(f"Missing {HTML}", file=sys.stderr)
        return 1
    text = HTML.read_text(encoding="utf-8")
    if "<script" in text.lower():
        print("ERROR: script tags found in HTML", file=sys.stderr)
        return 1
    chunks = [text[i : i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]
    for i, ch in enumerate(chunks):
        (OUT_DIR / f"a7-blob-chunk-{i}.txt").write_text(ch, encoding="utf-8")
        payload: dict = {"chunk": ch}
        if i == 0:
            payload["reset"] = True
        if i == len(chunks) - 1:
            payload["finalize"] = True
        (OUT_DIR / f"a7-blob-payload-{i}.json").write_text(
            json.dumps(payload, ensure_ascii=False), encoding="utf-8"
        )
    print(json.dumps({"ok": True, "chunks": len(chunks), "total_chars": len(text)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
