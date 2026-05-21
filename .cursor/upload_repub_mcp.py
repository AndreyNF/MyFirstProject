#!/usr/bin/env python3
"""Prepare sequential MCP upload payloads for republish."""
import json
from pathlib import Path

REpub4k = Path('/workspace/.cursor/repub4k')
STATE = Path('/workspace/.cursor/repub_upload_state.json')

def main():
    state = json.loads(STATE.read_text()) if STATE.exists() else {'index': 1, 'blob_id': 'UnEXGC0MfNR1XTvHJKUgktb'}
    idx = state['index']
    chunk_file = REpub4k / f'chunk-{idx:02d}.json'
    if not chunk_file.exists():
        print('DONE')
        return
    meta = json.loads(chunk_file.read_text(encoding='utf-8'))
    args = {'chunk': meta['chunk'], 'blob_id': state['blob_id']}
    if meta.get('finalize'):
        args['finalize'] = True
    out = Path('/workspace/.cursor/NEXT_MCP_ARGS.json')
    out.write_text(json.dumps(args, ensure_ascii=False), encoding='utf-8')
    print(json.dumps({'index': idx, 'blob_id': state['blob_id'], 'finalize': bool(meta.get('finalize')), 'chunk_len': len(meta['chunk'])}))

if __name__ == '__main__':
    main()
