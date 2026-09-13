#!/usr/bin/env python3
"""Run ADHD Mode Playground on an available port."""

import http.server
import socket
import socketserver
import sys
from pathlib import Path

DIR = Path(__file__).resolve().parent

def find_free_port(start_port=8080):
    for port in range(start_port, start_port + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
    return 8080

def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else find_free_port(8080)
    handler = lambda *args, **kwargs: http.server.SimpleHTTPRequestHandler(*args, directory=str(DIR), **kwargs)
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"ADHD Mode Playground running at: http://localhost:{port}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
