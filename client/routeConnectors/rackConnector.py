import urllib3

root = "http://???"
curPath = "/api/rack"

http = urllib3.PoolManager()

def getRacks():
  r = http.request("GET", root + curPath + "/")
  return r.data

def postRack(location, desc, weightLimit):
  f = {
    "location": location,
    "desc": desc,
    "weightLimit": weightLimit
  }
  r = http.request("POST", root + curPath + "/", fields=f)
  return r.data

def deleteRack(idField):
  r = http.request("DELETE", root + curPath + "/" + idField)
  return r.data

def updateRack(idField, location, desc, weightLimit):
  f = {
    "location": location,
    "desc": desc,
    "weightLimit": weightLimit
  }
  r = http.request("POST", root + curPath + "/update/" + idField, fields=f)
  return r.data