#!/usr/bin/env python3
"""Print MCP append args for step N (agent calls mcp_call_tool per step)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/fns-blob-mcp")
STATE = Path("/tmp/fns_blob_state.json")


def load_step(step: int, blob_id: str | None = None) -> dict:
    args = json.loads((BASE / f"{step}.json").read_text(encoding="utf-8"))
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: emit STEP [BLOB_ID] | save_blob BLOB_ID [bytes]", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "emit":
        step = int(sys.argv[2])
        bid = sys.argv[3] if len(sys.argv) > 3 else None
        args = load_step(step, bid)
        out = Path(f"/tmp/fns_emit_{step}.json")
        out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"step": step, "path": str(out), "len": len(args["chunk"])}))
        return 0
    if cmd == "save_blob":
        st = {"blob_id": sys.argv[2]}
        if len(sys.argv) > 3:
            st["bytes_total"] = int(sys.argv[3])
        STATE.write_text(json.dumps(st), encoding="utf-8")
        print(json.dumps(st))
        return 0
    if cmd == "get_blob":
        if STATE.is_file():
            print(STATE.read_text(encoding="utf-8"))
        else:
            print("{}")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
