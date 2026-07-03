#!/usr/bin/env python3
"""Split publish HTML into JSON chunk files for MCP blob upload (manual/agent step)."""
import json
from pathlib import Path

text = Path("/workspace/.cursor/page-content-natasha-A13-publish.html").read_text(encoding="utf-8")
chunk_size = 18000
chunks = [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]
meta = {"page_id": 370, "slug": "statya-159-177-uk-pri-dolgah-granica", "num_chunks": len(chunks)}
out = Path("/workspace/.cursor/blob-upload-a13.json")
out.write_text(
    json.dumps({"meta": meta, "chunks": chunks}, ensure_ascii=False),
    encoding="utf-8",
)
print(f"Wrote {out} ({len(chunks)} chunks, {len(text)} chars)")
