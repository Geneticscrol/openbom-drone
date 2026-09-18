from __future__ import annotations
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs
from .engine import load_catalog, part_by_id, tally

STATIC = Path(__file__).resolve().parent / "static"

class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print("[openbom]", fmt % args)
    def _send(self, code, body, ctype="text/html; charset=utf-8"):
        data = body if isinstance(body, bytes) else body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send(200, (STATIC / "index.html").read_text(encoding="utf-8")); return
        if self.path == "/app.js":
            self._send(200, (STATIC / "app.js").read_text(encoding="utf-8"), "text/javascript"); return
        if self.path == "/style.css":
            self._send(200, (STATIC / "style.css").read_text(encoding="utf-8"), "text/css"); return
        if self.path == "/api/catalog":
            self._send(200, json.dumps(load_catalog()), "application/json"); return
        if self.path.startswith("/api/tally"):
            qs = parse_qs(self.path.split("?", 1)[-1] if "?" in self.path else "")
            cat = load_catalog()
            picks = []
            for raw in qs.get("p", []):
                if ":" not in raw: continue
                pid, qty = raw.rsplit(":", 1)
                try:
                    picks.append((part_by_id(cat, pid), int(qty)))
                except (KeyError, ValueError):
                    continue
            target = int(qs.get("target", [cat["target_g_default"]])[0])
            self._send(200, json.dumps(tally(picks, target_g=target)), "application/json"); return
        self._send(404, "not found")

def serve(host="127.0.0.1", port=8790):
    print(f"OpenBOM  http://{host}:{port}")
    ThreadingHTTPServer((host, port), Handler).serve_forever()
