#!/usr/bin/env python3
"""Load vpr blob append args for step N; merge blob_id if provided."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/vpr-blob-calls")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vpr_mcp_invoke_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    args = json.loads((BASE / f"{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0 and len(sys.argv) > 2:
        args["blob_id"] = sys.argv[2]
        args.pop("reset", None)
    out = Path(f"/tmp/vpr-mcp-step-{step:02d}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({
        "step": step,
        "path": str(out),
        "chunk_len": len(args["chunk"]),
        "finalize": bool(args.get("finalize")),
        "has_blob_id": "blob_id" in args,
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
