from os import environ
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = '0.0.0.0'
PORT = int(environ.get('PORT', 8000))

MESSAGE = environ.get('MESSAGE', "Hello World!") + '\n'


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(MESSAGE.encode('utf-8'))


def main():
  server = HTTPServer((HOST, PORT), MyHandler)
  print('Started WebServer on port {}'.format(PORT))
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    pass
  server.server_close()
  print('Stopped WebServer')

if __name__ == '__main__':
  main()

