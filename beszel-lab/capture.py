import http.server, sys
class H(http.server.BaseHTTPRequestHandler):
    def _cap(self):
        n = int(self.headers.get('Content-Length') or 0)
        body = self.rfile.read(n).decode('utf-8', 'replace')
        with open('/home/hatch/workspace/beszel-lab-work/notification-capture.txt', 'a') as f:
            f.write(f"{self.command} {self.path}\n{dict(self.headers)}\n{body}\n---\n")
        self.send_response(200); self.end_headers(); self.wfile.write(b'ok')
    do_POST = _cap
    do_GET = _cap
    def log_message(self, *a): pass
http.server.HTTPServer(('127.0.0.1', 9999), H).serve_forever()
