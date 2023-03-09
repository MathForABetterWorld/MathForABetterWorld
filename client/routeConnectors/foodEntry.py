import urllib3
import rootName

root = rootName.root
curPath = "/api/food"

http = urllib3.PoolManager()

def getFood():
  r = http.request("GET", root + curPath + "/")
  return r.data

def postFood(entryUserId, inputDate, expirationDate, weight, companyId, rackId, inWarehouse, description, categoryId):
  f = {
    "entryUserId": entryUserId,
    "inputDate": inputDate,
    "expirationDate": expirationDate,
    "weight": weight,
    "companyId": companyId,
    "rackId": rackId,
    "inWarehouse": inWarehouse,
    "description": description,
    "categoryId": categoryId
  }
  r = http.request("POST", root + curPath + "/", fields=f)
  return r.data

def deleteFood(idField):
  r = http.request("DELETE", root + curPath + "/" + idField)
  return r.data

def updateFood(idField, entryUserId, inputDate, expirationDate, weight, companyId, rackId, inWarehouse, description, categoryId):
  f = {
    "entryUserId": entryUserId,
    "inputDate": inputDate,
    "expirationDate": expirationDate,
    "weight": weight,
    "companyId": companyId,
    "rackId": rackId,
    "inWarehouse": inWarehouse,
    "description": description,
    "categoryId": categoryId
  }
  r = http.request("POST", root + curPath + "/edit/" + idField, fields=f)
  return r.data