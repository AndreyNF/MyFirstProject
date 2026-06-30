#!/usr/bin/env python3
"""Emit blob append args for steps 2-6 (step 0-1 done by agent)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB = sys.argv[1] if len(sys.argv) > 1 else None
BASE = Path("/workspace/.cursor/vpr-blob-calls")


def main() -> int:
    if not BLOB:
        print("usage: vpr_blob_mcp_upload_all.py BLOB_ID [STEP]", file=sys.stderr)
        return 2
    steps = [int(sys.argv[2])] if len(sys.argv) > 2 else list(range(2, 7))
    for step in steps:
        args = json.loads((BASE / f"{step:02d}.json").read_text(encoding="utf-8"))
        args["blob_id"] = BLOB
        args.pop("reset", None)
        out = Path(f"/tmp/vpr-mcp-step-{step:02d}.json")
        out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"step": step, "path": str(out), "finalize": bool(args.get("finalize"))}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
