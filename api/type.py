from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
  
  def do_GET(self):
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)
    print(dic)
    if 'type' in dic:
      url = 'https://www.gamerpower.com/api/giveaways'
      url = url + '?type=' + dic['type']
      r = requests.get(url) 
  
      data = r.json()
      games = []
      for n in range(len(data)):
        giveaways = {'type': data[n]['type'], 'title': data[n]['title'], 'url': data[n]['open_giveaway_url'], 'status': data[n]['status'] }
        games.append(giveaways)
        message = str(games)
        
    else:
      message = ('Please provide a valid game')
  
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())

    return