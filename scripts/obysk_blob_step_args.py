#!/usr/bin/env python3
"""Print MCP append args for obysk blob step N (5k chunks, 18 total).

Usage:
  python3 scripts/obysk_blob_step_args.py STEP [BLOB_ID]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/obysk-mcp-5k")
BLOB = "G1EEm8tE38nr3noEJ7dPfndD"


def main() -> int:
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else BLOB
    d = json.loads((BASE / f"step_{step:02d}.json").read_text(encoding="utf-8"))
    args: dict = {"chunk": d["chunk"]}
    if d.get("reset"):
        args["reset"] = True
    elif step > 0:
        args["blob_id"] = blob_id
    if d.get("finalize"):
        args["finalize"] = True
    out = Path(f"/workspace/.cursor/obysk-active-step.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "chunk_len": len(args["chunk"]), "finalize": bool(args.get("finalize")), "path": str(out)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
