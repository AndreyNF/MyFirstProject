#!/usr/bin/env python3
"""Print one line per parts3k file: index, json_path, chunk_len, finalize."""
from __future__ import annotations

import json
import sys
from pathlib import Path

PARTS = Path("/workspace/.cursor/sip-blob-mcp/parts3k")


def main() -> int:
    files = sorted(PARTS.glob("part-*.json"))
    for i, p in enumerate(files):
        d = json.loads(p.read_text(encoding="utf-8"))
        print(
            json.dumps(
                {
                    "i": i,
                    "path": str(p),
                    "chunk_len": len(d["chunk"]),
                    "finalize": bool(d.get("finalize")),
                    "json_bytes": p.stat().st_size,
                },
                ensure_ascii=False,
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
