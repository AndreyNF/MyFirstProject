#!/usr/bin/env python3
"""Print MCP wordpress_content_blob_append arguments for chunk index (0-5)."""
import json
import sys

def main() -> int:
    i = int(sys.argv[1])
    path = f"/workspace/.cursor/a16-blob-mcp/{i:02d}.json"
    d = json.load(open(path, encoding="utf-8"))
    args: dict = {"chunk": d["chunk"]}
    if d.get("reset"):
        args["reset"] = True
    if i > 0:
        args["blob_id"] = sys.argv[2] if len(sys.argv) > 2 else d.get("blob_id", "")
    if d.get("finalize"):
        args["finalize"] = True
    else:
        args["finalize"] = False
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
