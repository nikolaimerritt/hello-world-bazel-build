import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello world')

port_num = 30001
httpd = socketserver.TCPServer(('', port_num), Handler)
httpd.serve_forever()
