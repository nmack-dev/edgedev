#!/usr/bin/env python3
import sys
import signal
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
from urllib.parse import parse_qs
import paho.mqtt.client as paho
from os.path import normpath
import json
from aws_get import get_table_data

# Capture SIGTERM signal to stop background process
def sigterm_handler(sig, frame):
    raise(SystemExit)
signal.signal(signal.SIGTERM, sigterm_handler)


class WebServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        prefix = 'freeboard'
        text = None
        binary_file = False

        if self.path == '/':
            self.path = '/index.html'

        if self.path == '/dashboard.json':
            self.path = self.path[1:]
            prefix = ''
            content_type = 'text/html'

        if self.path.endswith('.html'):
            content_type = 'text/html'
        elif self.path.endswith('.js'):
            content_type = 'application/javascript'
        elif self.path.endswith('.css'):
            content_type = 'text/css'
        elif self.path.endswith('.png'):
            content_type = 'image/png'
            binary_file = True
        
        if self.path == '/scan':
            content_type = 'application/json'
            text = json.dumps(get_table_data())
        else:
            try:
                with open(prefix + self.path, 'rb' if binary_file else 'r') as f:
                    text = f.read()
            except IOError:
                self.send_error(404, 'File Not Found: %s' % self.path[1:])
                return

        if not binary_file:
            text = bytes(text, 'utf-8')

        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
        self.wfile.write(text)
'''        
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
'''
if __name__ == "__main__":
  try:
    # Setup HTTP Server
    address = ('', 8081)
    server = HTTPServer(address, WebServer_RequestHandler)

    # Run the HTTP Server
    server.serve_forever()

  except (KeyboardInterrupt, SystemExit):
    print("Stopping Server")