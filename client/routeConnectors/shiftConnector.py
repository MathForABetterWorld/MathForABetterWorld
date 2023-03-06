import urllib3
import rootName

root = rootName.root
curPath = "/api/shift"

http = urllib3.PoolManager()

def getShifts():
  r = http.request("GET", root + curPath + "/")
  return r.data

# times must be ISO 8601 times
def postShift(userId, startTime, endTime, foodWeightTaken):
  f = {
    "userId": userId,
    "start": startTime,
    "end": endTime,
    "foodTaken": foodWeightTaken
  }
  r = http.request("POST", root + curPath + "/", fields=f)
  return r.data

def deleteShift(idField):
  r = http.request("DELETE", root + curPath + "/" + idField)
  return r.data

def updateShift(idField, userId, startTime, endTime, foodWeightTaken):
  f = {
    "id": idField,
    "userId": userId,
    "start": startTime,
    "end": endTime,
    "foodTaken": foodWeightTaken
  }
  r = http.request("POST", root + curPath + "/update", fields=f)
  return r.data