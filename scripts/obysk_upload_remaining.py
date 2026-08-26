#!/usr/bin/env python3
"""Load remaining blob chunks and print step index for sequential MCP upload."""
from __future__ import annotations

import json
import sys
from pathlib import Path

HTML = Path("/workspace/.cursor/page-content-natasha-obysk-upakovka.html")
STATE = Path("/workspace/.cursor/obysk-upload-remaining-state.json")
BLOB = "6k97VtvlREclZgKuM9HLouz"
OFFSET = 55000
CHUNK = 5000


def prepare() -> None:
    html = HTML.read_text(encoding="utf-8")
    rem = html[OFFSET:]
    steps = []
    for i, start in enumerate(range(0, len(rem), CHUNK)):
        chunk = rem[start : start + CHUNK]
        args = {
            "blob_id": BLOB,
            "chunk": chunk,
            "finalize": start + len(chunk) >= len(rem),
        }
        p = Path(f"/workspace/.cursor/obysk-rem-step-{i:02d}.json")
        p.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        steps.append({"step": i, "len": len(chunk), "finalize": args["finalize"], "path": str(p)})
    STATE.write_text(json.dumps({"index": 0, "total": len(steps), "steps": steps}, indent=2), encoding="utf-8")
    print(json.dumps({"prepared": len(steps)}, ensure_ascii=False))


def next_args() -> None:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    idx = st["index"]
    if idx >= st["total"]:
        print(json.dumps({"done": True}))
        return
    step = st["steps"][idx]
    args = json.loads(Path(step["path"]).read_text(encoding="utf-8"))
    print(json.dumps({"step": idx, "total": st["total"], "args": args}, ensure_ascii=False))


def advance(resp: str) -> None:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    st["index"] = st.get("index", 0) + 1
    st["last_response"] = resp.strip()
    STATE.write_text(json.dumps(st, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"index": st["index"], "total": st["total"]}, ensure_ascii=False))


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: prepare|next|advance RESP", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "prepare":
        prepare()
        return 0
    if cmd == "next":
        next_args()
        return 0
    if cmd == "advance":
        advance(sys.argv[2] if len(sys.argv) > 2 else sys.stdin.read())
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
