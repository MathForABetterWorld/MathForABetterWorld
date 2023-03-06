import urllib3

root = "http://???"
curPath = "/api"

http = urllib3.PoolManager()

def getUsers():
  r = http.request("GET", root + curPath + "/")
  return r.data

def postUser(email, name):
  f = {
    "email": email,
    "name": name
  }
  r = http.request("POST", root + curPath + "/signup", fields=f)
  return r.data

def updateUser(idField, email):
  f = {
    "id": idField,
    "email": email
  }
  r = http.request("POST", root + curPath + "/update", fields=f)
  return r.data