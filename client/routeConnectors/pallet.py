import urllib3
from .rootName import root
import json
import ast

#root = rootName.root
curPath = "/api/pallet"

http = urllib3.PoolManager()

def getFood():
  r = http.request("GET", root + curPath + "/", headers={'Content-Type': 'application/json'})
  # print("r.data: ", ast.parse(r.data.decode('utf-8'), mode='eval'))
  print("r.data type: ", type(r.data))
  print("datastring", str(r.data, 'UTF-8')[:100])
  res_dict = json.loads(r.data.decode('utf-8'))
  print("res_dict: ", (res_dict)["Pallet"])
  return res_dict

def postFood(entryUserId, inputDate, expirationDate, weight, companyId, rackId, inWarehouse, description, categoryId):
  f = json.dumps({
    "entryUserId": entryUserId,
    "inputDate": inputDate.isoformat(),
    "expirationDate": expirationDate.isoformat(),
    "weight": weight,
    "companyId": companyId,
    "rackId": rackId,
    "inWarehouse": inWarehouse,
    "description": description,
    "categoryId": categoryId
  })
  r = http.request("POST", root + curPath + "/", body=f, headers={'Content-Type': 'application/json'})
  return r.data.decode('utf-8')

def deleteFood(idField):
  r = http.request("DELETE", root + curPath + "/" + idField, headers={'Content-Type': 'application/json'})
  return r.data

def updateFood(idField, entryUserId, inputDate, expirationDate, weight, companyId, rackId, inWarehouse, description, categoryId):
  f = json.dumps({
    "entryUserId": entryUserId,
    "inputDate": inputDate,
    "expirationDate": expirationDate,
    "weight": weight,
    "companyId": companyId,
    "rackId": rackId,
    "inWarehouse": inWarehouse,
    "description": description,
    "categoryId": categoryId
  })
  r = http.request("POST", root + curPath + "/edit/" + idField, body=f, headers={'Content-Type': 'application/json'})
  return r.data.decode('utf-8')