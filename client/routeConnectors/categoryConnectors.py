import urllib3

root = "http://???"
curPath = "/api/category"

http = urllib3.PoolManager()

def getCategories():
  r = http.request("GET", root + curPath + "/")
  return r.data

def postCategory(name, desc):
  f = {
    "name": name,
    "description": desc
  }
  r = http.request("POST", root + curPath + "/", fields=f)
  return r.data

def deleteCategory(idField):
  r = http.request("DELETE", root + curPath + "/" + idField)
  return r.data

def updateCategory(idField, name, desc):
  f = {
    "name": name,
    # "id": idField,
    "description": desc
  }
  r = http.request("POST", root + curPath + "/" + idField + "/" + "update", fields=f)
  return r.data
