#!/usr/bin/env python3
"""Load sub-chunk N with blob_id for MCP append (stdout = arguments JSON)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

SUB = Path("/workspace/.cursor/vs-uslovnyy-subchunks")


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: vs_uslovnyy_mcp_upload_loop.py STEP BLOB_ID", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2]
    args = json.loads((SUB / f"sub-{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
