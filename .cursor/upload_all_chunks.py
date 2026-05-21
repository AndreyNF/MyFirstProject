#!/usr/bin/env python3
"""Upload all blob chunks via subprocess curl to MCP if available, else print args."""
import json
import sys
from pathlib import Path

BLOB_ID = sys.argv[1] if len(sys.argv) > 1 else None
START = int(sys.argv[2]) if len(sys.argv) > 2 else 1
END = int(sys.argv[3]) if len(sys.argv) > 3 else 20

chunks_dir = Path("/workspace/.cursor/payload4k")
for i in range(START, END + 1):
    data = json.loads((chunks_dir / f"chunk-{i}.json").read_text(encoding="utf-8"))
    args = {"chunk": data["chunk"], "blob_id": BLOB_ID}
    if data.get("finalize"):
        args["finalize"] = True
    out = Path(f"/workspace/.cursor/upload_chunk_{i}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(f"prepared chunk {i} -> {out} ({len(args['chunk'])} chars)")
