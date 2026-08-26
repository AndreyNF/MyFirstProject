#!/usr/bin/env python3
"""Print one mcp3 chunk payload per line for sequential upload (index as argv)."""
import json
import sys
from pathlib import Path

BLOB_ID = sys.argv[2] if len(sys.argv) > 2 else None
i = int(sys.argv[1])
f = Path(f"/workspace/.cursor/mcp3-{i:02d}.json")
d = json.loads(f.read_text(encoding="utf-8"))
if BLOB_ID:
    d["blob_id"] = BLOB_ID
    d.pop("reset", None)
print(json.dumps(d, ensure_ascii=False))
