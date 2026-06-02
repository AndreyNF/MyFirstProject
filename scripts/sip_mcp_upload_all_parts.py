#!/usr/bin/env python3
"""Upload all parts3k via stdin lines for agent mcp_call_tool loop.

Prints: INDEX BLOB_ID CHUNK_LEN FINALIZE
Agent: for each line, mcp_call_tool wordpress_content_blob_append with json from parts3k/part-NN.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

PARTS = Path("/workspace/.cursor/sip-blob-mcp/parts3k")
BLOB = sys.argv[1] if len(sys.argv) > 1 else "txtpcRCC3ps3jqBnuVcLzTZ7"
START = int(sys.argv[2]) if len(sys.argv) > 2 else 0


def main() -> int:
    files = sorted(PARTS.glob("part-*.json"))
    for i, p in enumerate(files):
        if i < START:
            continue
        d = json.loads(p.read_text(encoding="utf-8"))
        d["blob_id"] = BLOB
        out = Path(f"/tmp/sip_mcp_part_{i:02d}.json")
        out.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
        print(
            json.dumps(
                {
                    "i": i,
                    "path": str(out),
                    "chunk_len": len(d["chunk"]),
                    "finalize": bool(d.get("finalize")),
                    "json_bytes": out.stat().st_size,
                },
                ensure_ascii=False,
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
