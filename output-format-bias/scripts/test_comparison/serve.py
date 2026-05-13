"""Local server that adds register+rebuild endpoints to the comparison UI.

Run:
    python -m scripts.test_comparison.serve
    # default: http://localhost:5173/

The HTML's "Register new data + rebuild" button calls these endpoints. If you
open the HTML via file:// instead, the button shows the equivalent CLI commands
to paste into a terminal.

Endpoints:
    GET  /                            redirects to /<comparison_id>.html
    GET  /<file>.html                 serves a comparison HTML from data_tables/test_comparisons/
    GET  /api/health                  → {"ok": true}
    GET  /api/registry                → registry contents
    POST /api/upload      multipart   → saves a JSON file to data/raw_outputs/ (or genob_codes for manual_codes)
    POST /api/register/add-file       body {"config_id": str, "file": str (path relative to repo)}
    POST /api/register/add-config     body {"id","label","schema","files":[...]}
    POST /api/rebuild                 body {"comparison_id": str}  → runs build, returns output path
"""
from __future__ import annotations
import argparse
import http.server
import json
import socketserver
import threading
import traceback
import urllib.parse
import webbrowser
from pathlib import Path

from . import build, register

REPO_ROOT = Path(__file__).parent.parent.parent
RAW_OUTPUTS_DIR = REPO_ROOT / "data" / "raw_outputs"
GENOB_CODES_DIR = REPO_ROOT / "data_tables" / "genob_codes"
COMPARISONS_DIR = REPO_ROOT / "data_tables" / "test_comparisons"


class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        # less noise
        print("[serve]", fmt % args)

    def _json(self, status: int, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _file(self, path: Path, content_type: str):
        body = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        # Prevent caching so a rebuild shows up on refresh
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.end_headers()
        self.wfile.write(body)

    def _read_json_body(self):
        n = int(self.headers.get("Content-Length", 0))
        if n == 0:
            return {}
        return json.loads(self.rfile.read(n).decode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Filename, X-Schema, X-Overwrite")
        self.send_header("Access-Control-Max-Age", "3600")
        self.end_headers()

    def do_GET(self):
        try:
            parsed = urllib.parse.urlparse(self.path)
            path = parsed.path
            if path == "/api/health":
                return self._json(200, {"ok": True})
            if path == "/api/registry":
                return self._json(200, register._load())
            if path == "/":
                # redirect to the most-recent comparison HTML if exists
                comps = sorted(COMPARISONS_DIR.glob("*.html"))
                if comps:
                    self.send_response(302)
                    self.send_header("Location", f"/{comps[-1].name}")
                    self.end_headers()
                    return
                return self._json(404, {"error": "no comparison HTMLs found"})
            if path.endswith(".html"):
                target = COMPARISONS_DIR / path.lstrip("/")
                if not target.exists():
                    return self._json(404, {"error": f"no such HTML: {path}"})
                return self._file(target, "text/html; charset=utf-8")
            return self._json(404, {"error": f"unknown path {path}"})
        except Exception as e:
            traceback.print_exc()
            return self._json(500, {"error": str(e)})

    def do_POST(self):
        try:
            parsed = urllib.parse.urlparse(self.path)
            path = parsed.path
            if path == "/api/upload":
                return self._handle_upload()
            if path == "/api/register/add-file":
                body = self._read_json_body()
                return self._add_file(body["config_id"], body["file"])
            if path == "/api/register/add-config":
                body = self._read_json_body()
                return self._add_config(body)
            if path == "/api/register/add-comparison":
                body = self._read_json_body()
                return self._add_comparison(body)
            if path == "/api/register/relabel-config":
                body = self._read_json_body()
                return self._relabel_config(body)
            if path == "/api/rebuild":
                body = self._read_json_body()
                return self._rebuild(body["comparison_id"])
            return self._json(404, {"error": f"unknown POST path {path}"})
        except Exception as e:
            traceback.print_exc()
            return self._json(500, {"error": str(e)})

    def _handle_upload(self):
        """Upload a JSON file. Body = raw file bytes; metadata via headers.

        Headers expected:
            X-Filename:  the filename (basename only is kept)
            X-Schema:    one of 'binary_concern' | '4axis' | 'manual_codes'
        """
        filename = self.headers.get("X-Filename")
        schema = self.headers.get("X-Schema", "binary_concern")
        if not filename:
            return self._json(400, {"error": "missing X-Filename header"})
        filename = Path(filename).name  # strip any path components
        n = int(self.headers.get("Content-Length", 0))
        if n <= 0:
            return self._json(400, {"error": "empty body"})
        data_bytes = self.rfile.read(n)
        # Validate it's parseable JSON
        try:
            json.loads(data_bytes.decode("utf-8"))
        except Exception as e:
            return self._json(400, {"error": f"uploaded file is not valid JSON: {e}"})

        dest_dir = GENOB_CODES_DIR if schema == "manual_codes" else RAW_OUTPUTS_DIR
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / filename
        if dest.exists():
            # If the existing file's content matches what's being uploaded, treat as success.
            existing_bytes = dest.read_bytes()
            if existing_bytes == data_bytes:
                rel = dest.relative_to(REPO_ROOT).as_posix()
                return self._json(200, {"path": rel, "absolute": str(dest), "already_present": True})
            # Allow overwrite only when client explicitly opts in via X-Overwrite: yes
            if self.headers.get("X-Overwrite", "").lower() != "yes":
                return self._json(409, {
                    "error": f"file already exists at {dest.relative_to(REPO_ROOT)} with different contents",
                    "existing_size": len(existing_bytes),
                    "uploaded_size": len(data_bytes),
                    "hint": "retry with X-Overwrite: yes to replace, or rename the file",
                })
            dest.write_bytes(data_bytes)
            rel = dest.relative_to(REPO_ROOT).as_posix()
            return self._json(200, {"path": rel, "absolute": str(dest), "overwrote": True})
        dest.write_bytes(data_bytes)
        rel = dest.relative_to(REPO_ROOT).as_posix()
        return self._json(200, {"path": rel, "absolute": str(dest)})

    def _add_file(self, config_id: str, file_path: str):
        reg = register._load()
        for c in reg.get("test_configs", []):
            if c["id"] == config_id:
                if file_path in c.get("files", []):
                    return self._json(200, {"ok": True, "message": "already present", "config": c})
                c.setdefault("files", []).append(file_path)
                register._save(reg)
                return self._json(200, {"ok": True, "config": c})
        return self._json(404, {"error": f"no config with id {config_id!r}"})

    def _add_config(self, body):
        reg = register._load()
        cid = body["id"]
        if any(c["id"] == cid for c in reg.get("test_configs", [])):
            return self._json(409, {"error": f"config id {cid!r} already exists"})
        reg.setdefault("test_configs", []).append({
            "id": cid,
            "label": body.get("label", cid),
            "schema": body["schema"],
            "files": list(body["files"]),
        })
        # Optionally also add to a comparison's configs list (so it shows up as a column).
        added_to = None
        target_comparison = body.get("add_to_comparison")
        if target_comparison:
            for c in reg.get("comparisons", []):
                if c["id"] == target_comparison:
                    if cid not in c.get("configs", []):
                        c.setdefault("configs", []).append(cid)
                        added_to = target_comparison
                    break
        register._save(reg)
        return self._json(200, {"ok": True, "id": cid, "added_to_comparison": added_to})

    def _add_comparison(self, body):
        reg = register._load()
        cid = body["id"]
        if any(c["id"] == cid for c in reg.get("comparisons", [])):
            return self._json(409, {"error": f"comparison id {cid!r} already exists"})
        reg.setdefault("comparisons", []).append({
            "id": cid,
            "label": body.get("label", cid),
            "configs": list(body["configs"]),
            "output": body["output"],
            "flag_threshold": body.get("flag_threshold", 0.5),
        })
        register._save(reg)
        return self._json(200, {"ok": True, "id": cid})

    def _relabel_config(self, body):
        cid = body["id"]
        reg = register._load()
        for c in reg.get("test_configs", []):
            if c["id"] == cid:
                # display_label: empty / null clears the field
                if body.get("display_label"):
                    c["display_label"] = body["display_label"]
                elif "display_label" in c:
                    del c["display_label"]
                if body.get("label"):
                    c["label"] = body["label"]
                register._save(reg)
                return self._json(200, {"ok": True, "config": c})
        return self._json(404, {"error": f"no config with id {cid!r}"})

    def _rebuild(self, comparison_id: str):
        try:
            out_path = build.build(comparison_id)
        except Exception as e:
            return self._json(500, {"error": str(e)})
        rel = out_path.relative_to(REPO_ROOT).as_posix()
        return self._json(200, {"ok": True, "output": rel, "url": "/" + out_path.name})


class ReuseAddrServer(socketserver.TCPServer):
    allow_reuse_address = True


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=5173)
    p.add_argument("--no-open", action="store_true", help="don't auto-open the browser")
    p.add_argument("--comparison", help="open this comparison id; default = most recent in data_tables/test_comparisons/")
    args = p.parse_args()

    # Build the comparison once on startup if --comparison is passed, so the link works
    if args.comparison:
        try:
            build.build(args.comparison)
        except Exception as e:
            print(f"[serve] could not pre-build {args.comparison}: {e}")

    server = ReuseAddrServer(("127.0.0.1", args.port), Handler)
    url = f"http://127.0.0.1:{args.port}/"
    if args.comparison:
        url += f"{args.comparison}.html"
    print(f"[serve] listening on {url}")
    print(f"[serve] press Ctrl+C to stop")
    if not args.no_open:
        threading.Timer(0.3, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[serve] shutting down")
        server.shutdown()


if __name__ == "__main__":
    main()
