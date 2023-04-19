import urllib3
from .rootName import root
import json

#root = rootName.root
curPath = "/api"

http = urllib3.PoolManager()

def getUsers():
  r = http.request("GET", root + curPath + "/", headers={'Content-Type': 'application/json'})
  return r.data

def postUser(email, name, phoneNumber=None, address=None ):
  if (phoneNumber is None and address is None ):
    f = json.dumps({
      "email": email,
      "name": name
    })
  elif phoneNumber is None:
      f = json.dumps({
      "email": email,
      "name": name,
      "address": address
    })
  elif address is None:
    f = json.dumps({
      "email": email,
      "name": name,
      "phoneNumber": phoneNumber,
    })
  else:
    f = json.dumps({
      "email": email,
      "name": name,
      "phoneNumber": phoneNumber,
      "address": address
    })
  r = http.request("POST", root + curPath + "/signup", body=f, headers={'Content-Type': 'application/json'})
  return r.data.decode('utf-8')

def updateUser(idField, email):
  f = json.dumps({
    "id": idField,
    "email": email
  })
  r = http.request("POST", root + curPath + "/update", body=f, headers={'Content-Type': 'application/json'})
  return r.data.decode('utf-8')