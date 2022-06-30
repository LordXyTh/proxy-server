import http.server
import socketserver
import urllib.request

class MyProxy(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        url = self.path
        self.send_response(200)
        self.end_headers()
        self.copyfile(urllib.request.urlopen(url), self.wfile)

# --- main ---

PORT = 7777

httpd = None

try:
    socketserver.TCPServer.allow_reuse_address = True   # solution for `OSError: [Errno 98] Address already in use`
    httpd = socketserver.TCPServer(('localhost', PORT), MyProxy)
    print(f"Proxy at: http://localhost:{PORT}")
    httpd.serve_forever()
except KeyboardInterrupt:
    print("Pressed Ctrl+C")
finally:
    if httpd:
        httpd.shutdown()