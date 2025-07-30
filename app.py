from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Docker app on ECS!")

if __name__ == "__main__":
    server = HTTPServer(("", 8080), Handler)
    print("Serving on port 8080")
    server.serve_forever()
