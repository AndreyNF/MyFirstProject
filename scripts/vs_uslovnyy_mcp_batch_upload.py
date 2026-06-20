#!/usr/bin/env python3
"""Batch upload vs-uslovnyy sub-chunks via Kovcheg MCP (agent runs mcp_call_tool per step).

Usage:
  python3 scripts/vs_uslovnyy_mcp_batch_upload.py emit STEP   # print args JSON path
  python3 scripts/vs_uslovnyy_mcp_batch_upload.py record STEP 'MCP_RESPONSE'
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SUB = Path("/workspace/.cursor/vs-uslovnyy-subchunks")
STATE = Path("/workspace/.cursor/vs-uslovnyy-upload-state.json")
ARGS_DIR = Path("/workspace/.cursor")


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"next": 0, "blob_id": ""}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2), encoding="utf-8")


def parse_blob(resp: str) -> str:
    m = re.search(r"blob_id:\s*(\S+)", resp)
    return m.group(1) if m else ""


def emit(step: int) -> dict:
    s = load_state()
    args = json.loads((SUB / f"sub-{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0:
        args["blob_id"] = s["blob_id"]
        args.pop("reset", None)
    out = ARGS_DIR / f"vs-sub-mcp-{step:02d}.json"
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    return {
        "step": step,
        "args_path": str(out),
        "chunk_len": len(args["chunk"]),
        "finalize": bool(args.get("finalize")),
        "blob_id": args.get("blob_id"),
    }


def record(step: int, resp: str) -> dict:
    s = load_state()
    bid = parse_blob(resp)
    if bid:
        s["blob_id"] = bid
    s["next"] = step + 1
    save_state(s)
    return s


def main() -> int:
    if len(sys.argv) < 2:
        print("emit STEP | record STEP 'RESP'", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "emit":
        print(json.dumps(emit(int(sys.argv[2])), ensure_ascii=False))
        return 0
    if cmd == "record":
        print(json.dumps(record(int(sys.argv[2]), sys.argv[3]), ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
