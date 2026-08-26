#!/usr/bin/env python3
"""Load kreditor blob append args for step N (0-3). Agent: CallDynamicTool with printed JSON."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor")
BLOB_STATE = Path("/workspace/.cursor/kreditor-publish-blob.json")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: kreditor_mcp_load_chunk.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    args = json.loads((BASE / f"kreditor-blob-payload-{step}.json").read_text(encoding="utf-8"))
    if step > 0:
        blob_id = sys.argv[2] if len(sys.argv) > 2 else None
        if not blob_id and BLOB_STATE.is_file():
            blob_id = json.loads(BLOB_STATE.read_text()).get("blob_id")
        if not blob_id:
            print("blob_id required for step > 0", file=sys.stderr)
            return 2
        args["blob_id"] = blob_id
        args.pop("reset", None)
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
