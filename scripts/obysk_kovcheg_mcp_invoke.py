#!/usr/bin/env python3
"""Invoke Kovcheg wordpress_content_blob_append via Cursor agent socket experiments."""
from __future__ import annotations

import json
import socket
import sys
from pathlib import Path


def load_args(path: Path) -> dict:
    args = json.loads(path.read_text(encoding="utf-8"))
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit("refusing PLACEHOLDER chunk")
    return args


def try_socket_paths(args: dict) -> str | None:
    sock_path = "/run/cursor/api.sock"
    if not Path(sock_path).exists():
        return None
    body = json.dumps(
        {
            "namespace": "Kovcheg",
            "toolName": "wordpress_content_blob_append",
            "arguments": args,
        },
        ensure_ascii=False,
    ).encode()
    paths = [
        "/v1/dynamic-tool/call",
        "/v1/tools/dynamic/call",
        "/v1/agent/tools/call",
        "/v1/call-dynamic-tool",
    ]
    for path in paths:
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            s.connect(sock_path)
            req = (
                f"POST {path} HTTP/1.0\r\n"
                f"Host: localhost\r\n"
                f"Content-Type: application/json\r\n"
                f"Content-Length: {len(body)}\r\n"
                f"Connection: close\r\n\r\n"
            ).encode() + body
            s.sendall(req)
            data = b""
            while True:
                chunk = s.recv(65536)
                if not chunk:
                    break
                data += chunk
        finally:
            s.close()
        text = data.decode("utf-8", errors="replace")
        if "200 OK" in text and "404" not in text.split("\r\n", 1)[0]:
            return text
    return None


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: obysk_kovcheg_mcp_invoke.py ARGS_JSON", file=sys.stderr)
        return 2
    args = load_args(Path(sys.argv[1]))
    resp = try_socket_paths(args)
    if resp:
        print(resp)
        return 0
    print(
        json.dumps(
            {
                "needs_agent_call": True,
                "tool": "wordpress_content_blob_append",
                "chunk_len": len(args["chunk"]),
                "blob_id": args.get("blob_id"),
                "reset": bool(args.get("reset")),
                "finalize": bool(args.get("finalize")),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
