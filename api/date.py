from http.server import BaseHTTPRequestHandler
from typing import Dict
from datetime import datetime
from urllib import parse 
import platform
import requests


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
   

    s= self.path
    url_components = parse.urlparse(s)
    query_string = parse.parse_qsl(url_components.query)
    dic=dict(query_string)
    name= dic.get('name')
    if name:
      message = f'Hello, {name}!'
    else:
      message = 'Hello, Stranger!' 
    #message += f"\n Greetings from {self.server.server_address[1]} at {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}  \n"
    message += f"\n Greetings from {platform.python_version} at {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}  \n"
    self.wfile.write(message.encode())



  def do_GET(self):
    # self.send_response(200)
    # self.send_header('Content-type', 'text/plain')
    # self.end_headers()
    # self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return
 