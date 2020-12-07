#!/usr/bin/env python3
"""
Example Web Server Demo
"""
import sys
import signal
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
from urllib.parse import parse_qs
from os.path import normpath

# Capture SIGTERM signal to stop background process
def sigterm_handler(sig, frame):
    raise(SystemExit)
signal.signal(signal.SIGTERM, sigterm_handler)


class WebServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Try to eliminate possible exploits in the filename
        safe_path = sys.path[0] + '/' + normpath(self.path).lstrip('./\\')

        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()

        elif safe_path.endswith('.html'):
            self.sendFile(safe_path, 'text/html')

        elif safe_path.endswith('.js'):
            self.sendFile(safe_path, 'application/javascript')

        elif self.path.endswith('.css'):
            self.sendFile(safe_path, 'text/css')

        elif self.path.endswith('.png'):
            self.sendFile(safe_path, 'image/png', True)

        elif self.path.endswith('.ico'):
            self.sendFile(safe_path, 'image/x-icon', True)

        else:
            print(f'File Not Found: {safe_path}')
            self.send_error(404)
            self.end_headers()

    def do_POST(self):
        parsed_path = urlparse.urlparse(self.path)

        if parsed_path.path == '/send':
            query_params = parse_qs(parsed_path.query)
            ticker = query_params.get('ticker')
            interval = query_params.get('interval')

            if ticker and interval:
                file = open('placeholder.txt', 'w')
                file.write(ticker[0] + ', ' + interval[0])
                self.send_response(200)
            else:
                print(f'Bad Request: {self.path}')
                self.send_response(400)
            self.end_headers()
        else:
            self.send_error(404)
            self.end_headers()

    def sendFile(self, file_name, content_type='txt/html', is_binary=False):
        try:
            if is_binary:
                with open(file_name, 'rb') as f:
                    file_content = f.read()
            else:
                with open(file_name, 'r') as f:
                    file_content = f.read().encode('utf-8')

        except OSError:
            print(f'File Not Found: {file_name}')
            self.send_error(404)
            self.end_headers()

        else:
            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', len(file_content))
            self.end_headers()
            self.wfile.write(file_content)


if __name__ == "__main__":
  try:
    # Setup HTTP Server
    address = ('', 8000)
    server = HTTPServer(address, WebServer_RequestHandler)

    # Run the HTTP Server
    server.serve_forever()

  except (KeyboardInterrupt, SystemExit):
    print("Stopping Server")
