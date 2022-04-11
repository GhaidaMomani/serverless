from http.server import BaseHTTPRequestHandler
from typing import Dict
from urllib import parse 
import requests


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
  
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    stir = str(url_components)
    query_list = parse.parse_qsl(url_components.query)
    dic = dict(query_list)
    

    if "text" in dic:
      url = "https://artii.herokuapp.com/make?text="
      response = requests.get(url, params = dic)
      data = response.text
      print(data)



    self.send_response(300)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(data).encode())
    

    return