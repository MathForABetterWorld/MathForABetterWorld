import urllib3
import rootName

root = rootName.root
curPath = "/api/distributor"

http = urllib3.PoolManager()

def getDistributors():
  r = http.request("GET", root + curPath + "/")
  return r.data

def postDistributor(name):
  f = {
    "name": name
  }
  r = http.request("POST", root + curPath + "/", fields=f)
  return r.data

def deleteDistributor(idField):
  r = http.request("DELETE", root + curPath + "/" + idField)
  return r.data

def updateDistributor(idField, name):
  f = {
    "name": name,
    "id": idField
  }
  r = http.request("POST", root + curPath + "/update", fields=f)
  return r.data


def getCountsPerDistributor():
  r = http.request("GET", root + curPath + "/counts")
  return r.data