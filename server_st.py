from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)

class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, max-age=0')
        super().end_headers()

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8001
    print(f'Serving S_T on http://127.0.0.1:{port}')
    httpd = ThreadingHTTPServer((host, port), NoCacheHandler)
    httpd.serve_forever()
