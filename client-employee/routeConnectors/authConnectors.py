import urllib3
from .rootName import root
import json

#root = rootName.root
curPath = "/"

http = urllib3.PoolManager()

def signinEmployee(username, password):
  f = json.dumps({
    "username": username,
    "password": password
  })
  r = http.request("POST", root + curPath + "authenticate", body=f, headers={'Content-Type': 'application/json'})
  return r.data.decode('utf-8')