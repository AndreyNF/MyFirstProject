#!/usr/bin/env python3
"""Orchestrate sequential MCP blob uploads by writing next args and reading results."""
import json
import re
import sys
from pathlib import Path

STATE = Path('/workspace/.cursor/seq_upload_state.json')
REpub4k = Path('/workspace/.cursor/repub4k')
RESULT = Path('/workspace/.cursor/last_mcp_result.txt')

def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding='utf-8'))
    return {'index': 1, 'blob_id': 'UnEXGC0MfNR1XTvHJKUgktb', 'done': False}

def save_state(state):
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')

def get_next_args():
    state = load_state()
    if state.get('done') or state['index'] > 18:
        return None, state
    idx = state['index']
    inv = json.loads((REpub4k / f'invoke-{idx:02d}.json').read_text(encoding='utf-8'))
    return inv, state

def parse_blob_id(text: str):
    m = re.search(r'blob_id:\s*(\S+)', text)
    return m.group(1) if m else None

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'next'
    if cmd == 'next':
        args, state = get_next_args()
        if args is None:
            print('DONE')
            return
        Path('/workspace/.cursor/NEXT_MCP_ARGS.json').write_text(json.dumps(args, ensure_ascii=False), encoding='utf-8')
        print(json.dumps({'index': state['index'], 'blob_id': state['blob_id'], 'chunk_len': len(args['chunk']), 'finalize': bool(args.get('finalize'))}))
        return
    if cmd == 'result':
        text = RESULT.read_text(encoding='utf-8') if RESULT.exists() else sys.stdin.read()
        blob_id = parse_blob_id(text) or load_state()['blob_id']
        state = load_state()
        idx = state['index']
        state['blob_id'] = blob_id
        if 'finalize' in text.lower() or 'sha256' in text.lower():
            m = re.search(r'sha256:\s*([a-f0-9]+)', text)
            if m:
                state['sha256'] = m.group(1)
        state['index'] = idx + 1
        if state['index'] > 18:
            state['done'] = True
        save_state(state)
        print(json.dumps(state, ensure_ascii=False))
        return
    if cmd == 'status':
        print(json.dumps(load_state(), ensure_ascii=False))
        return
    print('unknown', cmd, file=sys.stderr)
    sys.exit(1)

if __name__ == '__main__':
    main()
