#!/usr/bin/env python3
"""Load MCP append args from JSON path and print metadata (agent calls CallDynamicTool)."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: kreditor_mcp_call_from_file.py ARGS_JSON", file=sys.stderr)
        return 2
    args = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out = Path("/workspace/.cursor/kreditor-mcp-active.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "args_path": str(out),
                "chunk_len": len(args["chunk"]),
                "blob_id": args.get("blob_id"),
                "reset": bool(args.get("reset")),
                "finalize": bool(args.get("finalize")),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
