#!/usr/bin/env python3
"""Upload remaining vs-uslovnyy sub-chunks via stdin/stdout MCP bridge file.

Writes next step args to /workspace/.cursor/vs-mcp-current.json
Agent calls mcp_call_tool, then: python3 scripts/vs_uslovnyy_mcp_record.py 'MCP_RESPONSE'
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SUB = Path("/workspace/.cursor/vs-uslovnyy-subchunks")
STATE = Path("/workspace/.cursor/vs-uslovnyy-upload-state.json")
CURRENT = Path("/workspace/.cursor/vs-mcp-current.json")


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"next": 0, "blob_id": ""}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2), encoding="utf-8")


def main() -> int:
    if len(sys.argv) < 2:
        print("next | record RESPONSE", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    s = load_state()
    meta = json.loads((SUB / "meta.json").read_text(encoding="utf-8"))
    if cmd == "next":
        step = s["next"]
        if step >= meta["parts"]:
            print(json.dumps({"done": True, "blob_id": s["blob_id"], "bytes": meta["total"]}))
            return 0
        args = json.loads((SUB / f"sub-{step:02d}.json").read_text(encoding="utf-8"))
        if step > 0:
            args["blob_id"] = s["blob_id"]
            args.pop("reset", None)
        CURRENT.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"step": step, "total": meta["parts"], "path": str(CURRENT), "finalize": bool(args.get("finalize"))}))
        return 0
    if cmd == "record":
        resp = sys.argv[2] if len(sys.argv) > 2 else sys.stdin.read()
        m = re.search(r"blob_id:\s*(\S+)", resp)
        if m:
            s["blob_id"] = m.group(1)
        s["next"] = s["next"] + 1
        save_state(s)
        print(json.dumps(s))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
