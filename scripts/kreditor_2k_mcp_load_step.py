#!/usr/bin/env python3
"""Load MCP args from /tmp/kreditor-mcp-chunk-N.json and print for agent."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    step = int(sys.argv[1])
    p = Path(f"/tmp/kreditor-mcp-chunk-{step}.json")
    if not p.is_file():
        p2 = Path(f"/workspace/.cursor/kreditor-2k-chunks/{step:02d}.json")
        args = json.loads(p2.read_text(encoding="utf-8"))
        if step > 0:
            args["blob_id"] = sys.argv[2] if len(sys.argv) > 2 else "LkSqYmdRz9YmYFNVNkFjre80"
            args.pop("reset", None)
    else:
        args = json.loads(p.read_text(encoding="utf-8"))
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
