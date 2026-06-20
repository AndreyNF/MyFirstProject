#!/usr/bin/env python3
"""Upload vs-uslovnyy sub-chunks START..END via agent MCP bridge file.

Writes request to /tmp/vs-mcp-req.json; agent calls mcp_call_tool, then:
  python3 scripts/vs_uslovnyy_mcp_runner.py done STEP 'MCP_RESPONSE'
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

READY = Path("/tmp")
STATE = Path("/workspace/.cursor/vs-uslovnyy-upload-state.json")


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"next": 1, "blob_id": "AdSUzgIZFipr56yMCytB2Kh"}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2), encoding="utf-8")


def parse_blob(resp: str) -> str:
    m = re.search(r"blob_id:\s*(\S+)", resp)
    return m.group(1) if m else ""


def main() -> int:
    if len(sys.argv) < 2:
        print("next | done STEP 'RESP'", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    s = load_state()
    if cmd == "next":
        step = s["next"]
        if step > 13:
            print(json.dumps({"done": True, "blob_id": s["blob_id"]}))
            return 0
        path = READY / f"mcp-ready-{step:02d}.json"
        args = json.loads(path.read_text(encoding="utf-8"))
        Path("/tmp/vs-mcp-req.json").write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"step": step, "args_path": "/tmp/vs-mcp-req.json", "chunk_len": len(args["chunk"]),
                          "finalize": bool(args.get("finalize"))}, ensure_ascii=False))
        return 0
    if cmd == "done":
        step = int(sys.argv[2])
        resp = sys.argv[3] if len(sys.argv) > 3 else ""
        bid = parse_blob(resp)
        if bid:
            s["blob_id"] = bid
        s["next"] = step + 1
        save_state(s)
        print(json.dumps(s, ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
