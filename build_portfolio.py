"""
Shubham Pal - Portfolio build script (no dependencies).

  python build_portfolio.py           build into ./public and preview at http://localhost:3000
  python build_portfolio.py --build   build only (used by Vercel, see vercel.json)

Source files:  src/index.html  (page, styles and scripts)   assets/  (avatar.jpg, resume PDF)
"""
import http.server, os, shutil, socketserver, sys, threading, webbrowser

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")

if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)
shutil.copy(os.path.join(ROOT, "src", "index.html"), os.path.join(OUT, "index.html"))
shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))
print("[OK] public/ built")

if "--build" in sys.argv:
    sys.exit(0)

PORT = 3000

class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

os.chdir(OUT)
threading.Timer(1.2, lambda: webbrowser.open(f"http://localhost:{PORT}")).start()
print(f"[>>] http://localhost:{PORT}  (Ctrl+C to stop)")
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Quiet) as server:
    server.serve_forever()
