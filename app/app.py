from http.server import HTTPServer, BaseHTTPRequestHandler
import threading


class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        hello_world_string = 'Hello World!'

        # return string to test api is working
        self.wfile.write(hello_world_string.encode())


port = 5000
print('Listening on localhost:%s' % port)
server = HTTPServer(('0.0.0.0', port), Handler)
thread = threading.Thread(target=server.serve_forever)
thread.start()
