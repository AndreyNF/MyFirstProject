#!/usr/bin/env python3
"""Load wordpress_content_blob_append arguments from JSON file; write MCP envelope."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: kovcheg_mcp_append_from_json.py ARGS_JSON [OUT_ENVELOPE]", file=sys.stderr)
        return 2
    args_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(f"/tmp/mcp-envelope-{args_path.stem}.json")
    args = json.loads(args_path.read_text(encoding="utf-8"))
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit("refusing placeholder chunk")
    envelope = {
        "server": "Kovcheg",
        "toolName": "wordpress_content_blob_append",
        "arguments": args,
    }
    out_path.write_text(json.dumps(envelope, ensure_ascii=False), encoding="utf-8")
    meta = {
        "envelope": str(out_path),
        "chunk_len": len(args["chunk"]),
        "blob_id": args.get("blob_id"),
        "reset": bool(args.get("reset")),
        "finalize": bool(args.get("finalize")),
    }
    print(json.dumps(meta, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
