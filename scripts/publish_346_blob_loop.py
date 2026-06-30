#!/usr/bin/env python3
"""Emit one blob-append JSON line per chunk for agent mcp_call_tool loop.

Usage:
  python3 scripts/publish_346_blob_loop.py init
  python3 scripts/publish_346_blob_loop.py emit 0   # prints JSON args for chunk 0
  python3 scripts/publish_346_blob_loop.py advance BLOB_ID
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HTML = Path("/workspace/.cursor/page-content-natasha-A9-upload.html")
STATE = Path("/tmp/p346_blob_state.json")
CHUNK = 3000


def init() -> int:
    text = HTML.read_text(encoding="utf-8")
    if "<script" in text.lower():
        print("script in html", file=sys.stderr)
        return 1
    parts = [text[i : i + CHUNK] for i in range(0, len(text), CHUNK)]
    STATE.write_text(
        json.dumps({"index": 0, "total": len(parts), "blob_id": None, "chars": len(text)}),
        encoding="utf-8",
    )
    print(json.dumps({"ok": True, "parts": len(parts), "chars": len(text)}))
    return 0


def emit(i: int) -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    text = HTML.read_text(encoding="utf-8")
    parts = [text[j : j + CHUNK] for j in range(0, len(text), CHUNK)]
    if i < 0 or i >= len(parts):
        print(json.dumps({"error": "bad index", "total": len(parts)}), file=sys.stderr)
        return 1
    args: dict = {"chunk": parts[i]}
    if i == 0:
        args["reset"] = True
    if i == len(parts) - 1:
        args["finalize"] = True
    if st.get("blob_id") and i > 0:
        args["blob_id"] = st["blob_id"]
    print(json.dumps(args, ensure_ascii=False))
    return 0


def advance(blob_id: str) -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    st["blob_id"] = blob_id
    st["index"] = st.get("index", 0) + 1
    STATE.write_text(json.dumps(st), encoding="utf-8")
    print(json.dumps({"index": st["index"], "blob_id": blob_id}))
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print("init | emit N | advance BLOB_ID", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "init":
        return init()
    if cmd == "emit" and len(sys.argv) >= 3:
        return emit(int(sys.argv[2]))
    if cmd == "advance" and len(sys.argv) >= 3:
        return advance(sys.argv[2])
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
