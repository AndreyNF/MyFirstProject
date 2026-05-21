#!/usr/bin/env python3
"""Load next blob chunk args for MCP relay. Usage: mcp_blob_uploader.py [step] [blob_id]"""
import json
import sys
from pathlib import Path

BLOB_ID = sys.argv[2] if len(sys.argv) > 2 else None
step = int(sys.argv[1]) if len(sys.argv) > 1 else 0

args = json.loads(Path(f'/workspace/.cursor/mcp20k_{step}.json').read_text(encoding='utf-8'))
if BLOB_ID and step > 0:
    args['blob_id'] = BLOB_ID

out = Path('/workspace/.cursor/NEXT_MCP_ARGS.json')
out.write_text(json.dumps(args, ensure_ascii=False), encoding='utf-8')
print(json.dumps({
    'step': step,
    'chunk_len': len(args['chunk']),
    'reset': args.get('reset'),
    'finalize': args.get('finalize'),
    'blob_id': args.get('blob_id'),
}, ensure_ascii=False))
