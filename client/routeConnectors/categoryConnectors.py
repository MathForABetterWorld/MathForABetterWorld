import urllib3

root = "http://???"
curPath = "/api/category"

http = urllib3.PoolManager()

def getCategories():
  r = http.request("GET", root + curPath + "/")
  return r.data

def postCategory(name, desc):
  r = http.request()
