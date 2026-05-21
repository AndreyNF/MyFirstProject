#!/usr/bin/env python3
"""Prepare 4k chunk invoke args with current blob_id."""
import json
import sys
from pathlib import Path

BLOB = sys.argv[1] if len(sys.argv) > 1 else 'u7XGNrf9NTpzhEodN3uIDHu'
idx = int(sys.argv[2]) if len(sys.argv) > 2 else 1

data = json.loads(Path(f'/workspace/.cursor/repub4k/chunk-{idx:02d}.json').read_text(encoding='utf-8'))
args = {'chunk': data['chunk'], 'blob_id': BLOB}
if data.get('finalize'):
    args['finalize'] = True
Path('/workspace/.cursor/NEXT_MCP_ARGS.json').write_text(json.dumps(args, ensure_ascii=False), encoding='utf-8')
print(json.dumps({'idx': idx, 'len': len(args['chunk']), 'finalize': args.get('finalize')}, ensure_ascii=False))
