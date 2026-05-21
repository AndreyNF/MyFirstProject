#!/usr/bin/env python3
"""Sequential blob upload helper — prints next MCP args JSON path and updates state."""
import json
import sys
from pathlib import Path

STATE = Path('/workspace/.cursor/blob_upload_state.json')
REpub4k = Path('/workspace/.cursor/repub4k')

def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding='utf-8'))
    return {'next_index': 1, 'blob_id': 'UnEXGC0MfNR1XTvHJKUgktb', 'done': False}

def save_state(state):
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')

def get_args(index: int, blob_id: str):
    if index == 0:
        meta = json.loads((REpub4k / 'chunk-00.json').read_text(encoding='utf-8'))
        args = {'chunk': meta['chunk'], 'reset': True}
    else:
        inv = json.loads((REpub4k / f'invoke-{index:02d}.json').read_text(encoding='utf-8'))
        args = inv
    return args

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'next'
    state = load_state()
    if cmd == 'advance':
        blob_id = sys.argv[2] if len(sys.argv) > 2 else state['blob_id']
        idx = int(sys.argv[3]) if len(sys.argv) > 3 else state['next_index']
        state['blob_id'] = blob_id
        state['next_index'] = idx + 1
        if state['next_index'] > 18:
            state['done'] = True
        save_state(state)
        print(json.dumps(state))
        return
    if state.get('done'):
        print('DONE')
        return
    idx = state['next_index']
    args = get_args(idx, state['blob_id'])
    out = Path('/workspace/.cursor/NEXT_MCP_ARGS.json')
    out.write_text(json.dumps(args, ensure_ascii=False), encoding='utf-8')
    print(json.dumps({'index': idx, 'blob_id': state['blob_id'], 'chunk_len': len(args['chunk']), 'finalize': args.get('finalize', False)}))

if __name__ == '__main__':
    main()
