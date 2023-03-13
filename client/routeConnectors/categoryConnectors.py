import urllib3
from .rootName import root
import json

#root = rootName.root
curPath = "/api/category"

http = urllib3.PoolManager()

def getCategories():
  r = http.request("GET", root + curPath + "/", headers={'Content-Type': 'application/json'})
  return r.data

def postCategory(name, desc):
  f = json.dumps( {
    "name": name,
    "description": desc
  })
  r = http.request("POST", root + curPath + "/", body=f, headers={'Content-Type': 'application/json'})
  return r.data.decode('utf-8')

def deleteCategory(idField):
  r = http.request("DELETE", root + curPath + "/" + idField, headers={'Content-Type': 'application/json'})
  return r.data

def updateCategory(idField, name, desc):
  f = json.dumps({
    "name": name,
    # "id": idField,
    "description": desc
  })
  r = http.request("POST", root + curPath + "/" + idField + "/" + "update", body=f, headers={'Content-Type': 'application/json'})
  return r.data
