#!/usr/bin/env python3
"""Load blob append args and invoke Kovcheg MCP via subprocess (agent bridge).

Usage:
  python3 plenum19_mcp_invoke_step.py STEP [BLOB_ID]

Prints MCP response JSON to stdout. Requires agent to wire MCP; falls back to
emitting args path for manual mcp_call_tool.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path("/workspace/scripts/publish_plenum19_mcp_step.py")


def load_args(step: int, blob_id: str | None) -> dict:
    cmd = ["python3", str(SCRIPT), str(step)]
    if blob_id:
        cmd.append(blob_id)
    return json.loads(subprocess.check_output(cmd, text=True))


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: plenum19_mcp_invoke_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    args = load_args(step, blob_id)
    out = Path(f"/tmp/plenum19_mcp_args_step{step}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    meta = {
        "step": step,
        "args_path": str(out),
        "chunk_len": len(args["chunk"]),
        "reset": bool(args.get("reset")),
        "finalize": bool(args.get("finalize")),
        "blob_id": args.get("blob_id"),
        "latin_st158": args["chunk"].count("st. 158"),
        "cyr_st158": args["chunk"].count("ст. 158"),
    }
    print(json.dumps(meta, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
