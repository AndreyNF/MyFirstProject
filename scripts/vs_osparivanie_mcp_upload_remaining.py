#!/usr/bin/env python3
"""Emit MCP append args for vs-osparivanie steps 2-8 (agent calls mcp_call_tool per line)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor")


def main() -> int:
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    for i in range(start, end + 1):
        p = BASE / f"mcp-upload-step-{i}.json"
        if not p.exists():
            p = Path(f"/tmp/mcp-chunk-{i:02d}.json")
        args = json.loads(p.read_text(encoding="utf-8"))
        meta = {
            "step": i,
            "args_path": str(p),
            "chunk_len": len(args["chunk"]),
            "blob_id": args.get("blob_id"),
            "finalize": bool(args.get("finalize")),
        }
        print(json.dumps(meta, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
