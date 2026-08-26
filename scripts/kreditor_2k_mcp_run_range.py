#!/usr/bin/env python3
"""Print MCP args for kreditor 2k chunks [start, end) with blob_id."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB = "LkSqYmdRz9YmYFNVNkFjre80"
CHUNKS = Path("/workspace/.cursor/kreditor-2k-chunks")


def main() -> int:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    blob = sys.argv[3] if len(sys.argv) > 3 else BLOB
    for i in range(start, end):
        args = json.loads((CHUNKS / f"{i:02d}.json").read_text(encoding="utf-8"))
        if i > 0:
            args["blob_id"] = blob
            args.pop("reset", None)
        out = Path(f"/tmp/kreditor-mcp-chunk-{i}.json")
        out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"step": i, "path": str(out), "len": len(args["chunk"]), "finalize": bool(args.get("finalize"))}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
