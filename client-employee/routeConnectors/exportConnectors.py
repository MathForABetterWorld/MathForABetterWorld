import urllib3
from .rootName import root
import json

#root = rootName.root
curPath = "/api/exports"

http = urllib3.PoolManager()

def getExports():
  r = http.request("GET", root + curPath + "/", headers={'Content-Type': 'application/json'})
  return r.data

def postExport(userId, categoryId, donatedTo, weight, location, exportType, rackId):
  jsonDict = {
    "userId": userId,
    "categoryId": categoryId,
    "donatedTo": donatedTo,
    "weight": weight,
    "exportType": exportType,
  }
  if rackId > 0:
    jsonDict["rackId"] = rackId
  if location > 0:
    jsonDict["locationId"] = location
  f = json.dumps(jsonDict)
  r = http.request("POST", root + curPath + "/", body=f, headers={'Content-Type': 'application/json'})
  return r.data.decode('utf-8')

def deleteExport(idField):
  r = http.request("DELETE", root + curPath + "/" + idField, headers={'Content-Type': 'application/json'})
  return r.data

def updateExport(idField, userId, categoryId, donatedTo, weight, exportType, rackId):
  f = json.dumps({
    "userId": userId,
    "categoryId": categoryId,
    "donatedTo": donatedTo,
    "weight": weight,
    "exportType": exportType,
    "rackId": rackId,
  })
  r = http.request("POST", root + curPath + "/edit/" + idField, body=f, headers={'Content-Type': 'application/json'})
  return r.data.decode('utf-8')

def getExportsInDuration(duration):
  r = http.require("GET", root + curPath + "/inPast/" + duration, headers={'Content-Type': 'application/json'})
  return r.data.encode('utf-8')