#!/usr/bin/env python3
"""Upload remaining vs-uslovnyy sub-chunks via Kovcheg MCP (steps 3-13).

Prints one line per step with args_path; agent must call mcp_call_tool for each,
then run: python3 scripts/vs_uslovnyy_mcp_upload_all.py record STEP 'RESPONSE'
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/vs-uslovnyy-upload-state.json")
READY = Path("/tmp")


def state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"next": 3, "blob_id": "AdSUzgIZFipr56yMCytB2Kh"}


def save(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2), encoding="utf-8")


def parse_blob(resp: str) -> str:
    m = re.search(r"blob_id:\s*(\S+)", resp)
    return m.group(1) if m else ""


def main() -> int:
    if len(sys.argv) < 2:
        print("next | record STEP 'RESP' | list", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    s = state()
    if cmd == "list":
        for i in range(s["next"], 14):
            p = READY / f"mcp-ready-{i:02d}.json"
            d = json.loads(p.read_text(encoding="utf-8"))
            print(json.dumps({"step": i, "path": str(p), "utf8": len(d["chunk"].encode("utf-8")),
                              "finalize": bool(d.get("finalize"))}))
        return 0
    if cmd == "next":
        step = s["next"]
        if step > 13:
            print(json.dumps({"done": True, "blob_id": s["blob_id"]}))
            return 0
        p = READY / f"mcp-ready-{step:02d}.json"
        args = json.loads(p.read_text(encoding="utf-8"))
        print(json.dumps({"step": step, "arguments": args}, ensure_ascii=False))
        return 0
    if cmd == "record":
        step = int(sys.argv[2])
        resp = sys.argv[3] if len(sys.argv) > 3 else ""
        bid = parse_blob(resp)
        if bid:
            s["blob_id"] = bid
        s["next"] = step + 1
        save(s)
        print(json.dumps(s, ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
