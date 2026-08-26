#!/usr/bin/env python3
"""Load step N blob-append args and write to obysk-mcp-active-args.json."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def step_file(n: int) -> Path:
    p = Path(f"/workspace/.cursor/mcp-out-step-{n}.json")
    if not p.is_file():
        p = Path(f"/tmp/obysk-clean-{n:02d}.json")
    return p


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: obysk_mcp_upload_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    args = json.loads(step_file(step).read_text(encoding="utf-8"))
    if step == 0:
        args["reset"] = True
        args.pop("blob_id", None)
    else:
        blob_id = sys.argv[2] if len(sys.argv) > 2 else None
        if not blob_id:
            raise SystemExit("blob_id required for step >= 1")
        args["blob_id"] = blob_id
        args.pop("reset", None)
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit("refusing PLACEHOLDER chunk")
    out = Path("/workspace/.cursor/obysk-mcp-active-args.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
