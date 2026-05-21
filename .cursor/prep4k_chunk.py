#!/usr/bin/env python3
"""Prepare next 4k chunk MCP args with blob_id."""
import json
import sys
from pathlib import Path

BLOB = sys.argv[1]
IDX = int(sys.argv[2])
repub = Path('/workspace/.cursor/repub4k')
data = json.loads((repub / f'chunk-{IDX:02d}.json').read_text(encoding='utf-8'))
args = {'chunk': data['chunk'], 'blob_id': BLOB}
if data.get('finalize'):
    args['finalize'] = True
out = Path('/workspace/.cursor/MCP_ARGS_NOW.json')
out.write_text(json.dumps(args, ensure_ascii=False), encoding='utf-8')
print(json.dumps({'idx': IDX, 'len': len(args['chunk']), 'finalize': bool(args.get('finalize'))}))
