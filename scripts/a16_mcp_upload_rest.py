#!/usr/bin/env python3
"""Upload A16 blob chunks 01-05 via MCP args files. Prints one line per step for agent."""
import json
import sys

BLOB_ID = sys.argv[1] if len(sys.argv) > 1 else ""
for i in range(1, 6):
    d = json.load(open(f"/workspace/.cursor/a16-blob-mcp/{i:02d}.json", encoding="utf-8"))
    args = {"blob_id": BLOB_ID, "chunk": d["chunk"], "finalize": bool(d.get("finalize"))}
    print(json.dumps({"step": i, "tool": "wordpress_content_blob_append", "arguments": args}, ensure_ascii=False))
