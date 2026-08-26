#!/usr/bin/env python3
"""Load obysk-mcp-pending.json and print MCP envelope for agent CallDynamicTool."""
from __future__ import annotations

import json
import sys
from pathlib import Path

PENDING = Path("/workspace/.cursor/obysk-mcp-pending.json")


def main() -> int:
    args = json.loads(PENDING.read_text(encoding="utf-8"))
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit("refusing PLACEHOLDER")
    envelope = {
        "namespace": "Kovcheg",
        "toolName": "wordpress_content_blob_append",
        "arguments": args,
    }
    out = Path("/workspace/.cursor/obysk-mcp-envelope-active.json")
    out.write_text(json.dumps(envelope, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "envelope_path": str(out),
                "chunk_len": len(args["chunk"]),
                "reset": bool(args.get("reset")),
                "finalize": bool(args.get("finalize")),
                "blob_id": args.get("blob_id"),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
