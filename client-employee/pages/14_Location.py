import streamlit as st
import datetime
import json
import urllib3
from PIL import Image
from jinja2 import Environment, FileSystemLoader, select_autoescape
from routeConnectors import locationConnectors
import os

def getCoordinates(address):
    http = urllib3.PoolManager()
    str(address)
    r = http.request("GET", 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=AIzaSyCnXWK-JgfzOK4wRYE1z8Zojx1_nLiEWGw', headers={'Content-Type': 'application/json'})
    jsonObj = json.loads(r.data.decode('utf-8'))
    lat = (jsonObj['results'][0]['geometry']['location']['lat'])
    lon = (jsonObj['results'][0]['geometry']['location']['lng'])
    return lat, lon

st.subheader("Every Time There is a New Delivery Location Input that Here")
with st.form("Location Form"):
    location_name = st.text_input(label = 'Location name (Where it is being donated: could be the name of a person, a neighborhood, etc)')
    address = st.text_input(label = 'Actual address')
    submit = st.form_submit_button()


if submit:
    st.balloons()

    ### TODO:: update location with coordinates 
    latitude, longitude = getCoordinates(address)
    r = locationConnectors.postLocation(location_name, str(longitude), str(latitude))
    st.success("🎉 Your new location was generated!")


   