#!/usr/bin/env python3
"""Upload fns blob chunks 0-6 via Kovcheg MCP (agent must run mcp_call_tool per step).

Prints one line per step: STEP BLOB_ID_AFTER (agent updates BLOB_ID from MCP response).

Usage:
  python3 scripts/fns_mcp_upload_all.py prepare
  python3 scripts/fns_mcp_upload_all.py emit 0
  python3 scripts/fns_mcp_upload_all.py emit 1 <blob_id>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/fns-blob-mcp")
STATE = Path("/tmp/fns_upload_state.json")


def load_step(step: int, blob_id: str | None = None) -> dict:
    args = json.loads((BASE / f"{step}.json").read_text(encoding="utf-8"))
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    return args


def cmd_prepare() -> int:
    STATE.write_text(json.dumps({"index": 0, "blob_id": None}), encoding="utf-8")
    for i in range(7):
        load_step(i)
    print(json.dumps({"ok": True, "steps": 7}))
    return 0


def cmd_emit(step: int, blob_id: str | None) -> int:
    args = load_step(step, blob_id)
    out = Path(f"/tmp/fns_emit_step_{step}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "path": str(out), "chunk_len": len(args["chunk"]), "finalize": bool(args.get("finalize"))}))
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print("prepare | emit STEP [BLOB_ID]", file=sys.stderr)
        return 2
    if sys.argv[1] == "prepare":
        return cmd_prepare()
    if sys.argv[1] == "emit":
        step = int(sys.argv[2])
        bid = sys.argv[3] if len(sys.argv) > 3 else None
        return cmd_emit(step, bid)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
