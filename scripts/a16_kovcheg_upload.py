#!/usr/bin/env python3
"""Upload A16 page 412 HTML via Kovcheg blob (6 chunks from a16-blob-mcp/).

Prints one JSON object per line: {"tool": "...", "arguments": {...}}
Agent calls mcp_call_tool for each line, passing blob_id from prior response.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/a16-blob-mcp")
PAGE_ID = 412
EXCERPT = (
    "Что говорить следователю на допросе и чего избегать на досудебной стадии: "
    "права подозреваемого, дознание и следствие, защита по ст. 159 и 177 УК."
)


def chunk_args(i: int, blob_id: str = "") -> dict:
    d = json.loads((BASE / f"{i:02d}.json").read_text(encoding="utf-8"))
    args: dict = {"chunk": d["chunk"]}
    if d.get("reset"):
        args["reset"] = True
    if i > 0 and blob_id:
        args["blob_id"] = blob_id
    args["finalize"] = bool(d.get("finalize"))
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: a16_kovcheg_upload.py <step 0-5> [blob_id]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    if step < 0 or step > 5:
        return 2
    args = chunk_args(step, blob_id)
    print(
        json.dumps(
            {"tool": "wordpress_content_blob_append", "arguments": args},
            ensure_ascii=False,
        )
    )
    if step == 5:
        print(
            json.dumps(
                {
                    "tool": "wordpress_update_page_from_blob",
                    "arguments": {"page_id": PAGE_ID, "blob_id": "<BLOB_ID>"},
                },
                ensure_ascii=False,
            ),
            file=sys.stderr,
        )
        print(
            json.dumps(
                {
                    "tool": "wordpress_update_page",
                    "arguments": {
                        "page_id": PAGE_ID,
                        "status": "publish",
                        "excerpt": EXCERPT,
                    },
                },
                ensure_ascii=False,
            ),
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
