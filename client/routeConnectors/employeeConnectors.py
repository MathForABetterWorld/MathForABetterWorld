import urllib3
from .rootName import root
import json
import streamlit as st

#root = rootName.root
curPath = "/api/employee"

http = urllib3.PoolManager()

def getUsers():
  r = http.request("GET", root + curPath + "/users", headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {st.session_state.token}'})
  return r.data

def promoteUser(userId, userName, password):
  f = json.dumps({
    "userId": userId,
    "userName": userName,
    "password": password
  })
  r = http.request("POST", root + curPath + "/promoteUser", body=f, headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {st.session_state.token}'})
  return r.data.decode('utf-8')

def promoteToAdmin(userId):
  f = json.dumps({
    "userId": userId
  })
  r = http.request("POST", root + curPath + "/promoteToAdmin", body=f, headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {st.session_state.token}'})
  return r.data.decode('utf-8')

def changePassword(newUsername, newPassword, userName, password):
  f = json.dumps({
    "newUsername": newUsername,
    "newPassword": newPassword,
    "userName": userName,
    "password": password
  })
  r = http.request("POST", root + curPath + "/updateAccount", body=f, headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {st.session_state.token}'})
  return r.data.decode('utf-8')