from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        hello_world_string = 'Hello World!'
        
        # return string to test api is working
        self.wfile.write(actionResult.encode())

port = 5000
print('Listening on localhost:%s' % port)
server = HTTPServer(('0.0.0.0', port), Handler)
thread = threading.Thread(target=server.serve_forever)
thread.start()
