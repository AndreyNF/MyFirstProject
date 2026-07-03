#!/usr/bin/env python3
"""Emit one JSON line per blob step for sequential mcp_call_tool invocation."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/vpr-blob-calls")


def load_step(step: int, blob_id: str | None = None) -> dict:
    data = json.loads((BASE / f"{step:02d}.json").read_text(encoding="utf-8"))
    args: dict = {"chunk": data["chunk"]}
    if step == 0:
        args["reset"] = True
    else:
        if not blob_id:
            raise SystemExit(f"blob_id required for step {step}")
        args["blob_id"] = blob_id
    if data.get("finalize"):
        args["finalize"] = True
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vpr_mcp_upload_runner.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    args = load_step(step, blob_id)
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
