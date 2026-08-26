#!/usr/bin/env python3
"""Emit next obysk blob append args with blob_id for agent CallDynamicTool."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB_ID = "G1EEm8tE38nr3noEJ7dPfndD"
CHUNK_DIR = Path("/workspace/.cursor/obysk-mcp-5k")
STATE = Path("/workspace/.cursor/obysk-blob-step.json")


def main() -> int:
    step = 1
    if STATE.is_file():
        step = json.loads(STATE.read_text(encoding="utf-8")).get("next", 1)
    if step > 17:
        print(json.dumps({"done": True}))
        return 0
    args = json.loads((CHUNK_DIR / f"step_{step:02d}.json").read_text(encoding="utf-8"))
    args["blob_id"] = BLOB_ID
    args.pop("reset", None)
    pending = Path("/workspace/.cursor/obysk-mcp-pending.json")
    pending.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "chunk_len": len(args["chunk"]), "finalize": bool(args.get("finalize")), "pending": str(pending)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
