import urllib3
from .rootName import root
import json

#root = rootName.root
curPath = "/api/rack"

http = urllib3.PoolManager()

def getRacks():
  r = http.request("GET", root + curPath + "/", headers={'Content-Type': 'application/json'})
  return r.data

def postRack(location, desc, weightLimit):
  f = json.dumps({
    "location": location,
    "desc": desc,
    "weightLimit": weightLimit
  })
  r = http.request("POST", root + curPath + "/", body=f, headers={'Content-Type': 'application/json'})
  return r.data.decode('utf-8')

def deleteRack(idField):
  r = http.request("DELETE", root + curPath + "/" + idField, headers={'Content-Type': 'application/json'})
  return r.data

def updateRack(idField, location, desc, weightLimit):
  f = json.dumps({
    "location": location,
    "desc": desc,
    "weightLimit": weightLimit
  })
  r = http.request("POST", root + curPath + "/update/" + idField, body=f, headers={'Content-Type': 'application/json'})
  return r.data.decode('utf-8')