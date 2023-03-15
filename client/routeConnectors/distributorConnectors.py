import urllib3
from .rootName import root
import json
import ast

#root = rootName.root
curPath = "/api/distributor"

http = urllib3.PoolManager()

def getDistributors():
  r = http.request("GET", root + curPath + "/", headers={'Content-Type': 'application/json'})
  return ast.literal_eval(r.data.decode('utf-8'))

def postDistributor(name):
  f = json.dumps({
    "name": name
  })
  r = http.request("POST", root + curPath + "/", body=f, headers={'Content-Type': 'application/json'})
  return r.data.decode('utf-8')

def deleteDistributor(idField):
  r = http.request("DELETE", root + curPath + "/" + idField, headers={'Content-Type': 'application/json'})
  return r.data

def updateDistributor(idField, name):
  f = json.dumps({
    "name": name,
    "id": idField
  })
  r = http.request("POST", root + curPath + "/update", body=f, headers={'Content-Type': 'application/json'})
  return r.data.decode('utf-8')


def getCountsPerDistributor():
  r = http.request("GET", root + curPath + "/counts", headers={'Content-Type': 'application/json'})
  return r.data