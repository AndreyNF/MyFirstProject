#!/usr/bin/env python3
"""Emit MCP wordpress_content_blob_append args for page 341 (mcp3 2k chunks).

Agent: for each printed line N, call mcp_call_tool with
  server=Kovcheg, toolName=wordpress_content_blob_append,
  arguments=json.loads(line from /workspace/.cursor/blob-upload-queue.jsonl line N)

Or run upload via printed blob_id chain in blob-upload-state.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

CHUNK_DIR = Path("/workspace/.cursor")
QUEUE = CHUNK_DIR / "blob-upload-queue.jsonl"
STATE = CHUNK_DIR / "blob-upload-state.json"


def build_queue() -> int:
    files = sorted(CHUNK_DIR.glob("mcp3-*.json"))
    if not files:
        print("No mcp3-*.json", file=sys.stderr)
        return 1
    with QUEUE.open("w", encoding="utf-8") as q:
        for f in files:
            q.write(f.read_text(encoding="utf-8").strip() + "\n")
    STATE.write_text(json.dumps({"index": 0, "blob_id": None}), encoding="utf-8")
    print(json.dumps({"ok": True, "chunks": len(files), "queue": str(QUEUE)}))
    return 0


def show_next() -> int:
    if not QUEUE.is_file():
        return build_queue()
    lines = QUEUE.read_text(encoding="utf-8").splitlines()
    st = json.loads(STATE.read_text(encoding="utf-8"))
    i = st["index"]
    if i >= len(lines):
        print(json.dumps({"done": True, "blob_id": st.get("blob_id")}))
        return 0
    payload = json.loads(lines[i])
    if st.get("blob_id"):
        payload["blob_id"] = st["blob_id"]
        payload.pop("reset", None)
    print(json.dumps({"index": i, "total": len(lines), "arguments": payload}, ensure_ascii=False))
    return 0


def advance(blob_id: str, bytes_total: int | None = None) -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    st["blob_id"] = blob_id
    if bytes_total is not None:
        st["bytes_total"] = bytes_total
    st["index"] = st.get("index", 0) + 1
    STATE.write_text(json.dumps(st), encoding="utf-8")
    print(json.dumps({"advanced": st["index"], "blob_id": blob_id}))
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "build":
        raise SystemExit(build_queue())
    if cmd == "next":
        raise SystemExit(show_next())
    if cmd == "advance" and len(sys.argv) >= 3:
        bid = sys.argv[2]
        bt = int(sys.argv[3]) if len(sys.argv) > 3 else None
        raise SystemExit(advance(bid, bt))
    print("Usage: build | next | advance BLOB_ID [bytes]", file=sys.stderr)
    raise SystemExit(2)
