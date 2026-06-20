#!/usr/bin/env python3
"""Sequential Kovcheg blob upload for vs-uslovnyy via agent mcp_call_tool loop.

Prints one line per step: MCP_ARGS_JSON
Agent must call mcp_call_tool Kovcheg wordpress_content_blob_append with each line,
then run: python3 scripts/vs_uslovnyy_blob_loop.py record STEP 'MCP_RESPONSE'
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SUB = Path("/workspace/.cursor/vs-uslovnyy-subchunks")
STATE = Path("/workspace/.cursor/vs-uslovnyy-upload-state.json")


def state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"next": 0, "blob_id": ""}


def save(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2), encoding="utf-8")


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "next"
    s = state()
    meta = json.loads((SUB / "meta.json").read_text(encoding="utf-8"))
    if cmd == "next":
        step = s["next"]
        if step >= meta["parts"]:
            print(json.dumps({"done": True, "blob_id": s["blob_id"]}))
            return 0
        args = json.loads((SUB / f"sub-{step:02d}.json").read_text(encoding="utf-8"))
        if step > 0:
            args["blob_id"] = s["blob_id"]
            args.pop("reset", None)
        print(json.dumps({"step": step, "arguments": args}, ensure_ascii=False))
        return 0
    if cmd == "record":
        step = int(sys.argv[2])
        resp = sys.argv[3] if len(sys.argv) > 3 else sys.stdin.read()
        m = re.search(r"blob_id:\s*(\S+)", resp)
        if m:
            s["blob_id"] = m.group(1)
        s["next"] = step + 1
        save(s)
        print(json.dumps(s))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
