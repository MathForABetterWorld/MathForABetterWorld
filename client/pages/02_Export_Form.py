# import pdfkit
import streamlit as st
from PIL import Image
import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os 
from routeConnectors import categoryConnectors, locationConnectors, userConnector, exportConnectors
import json

path = os.path.dirname(__file__)
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Export Form")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')
st.image(image)
title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    # with col1:
    #     st.image(path + '/../assets/bmore_food_logo_dark_theme.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Food export form</h1>", unsafe_allow_html=True)
users = userConnector.getUsers()

locations = [{"id": -1, "name": "", "longitude":"", "latitude": ""}]  + locationConnectors.getLocations()['location']
allLocations = sorted(locations, key=lambda location: location["name"])

categories = [{"id": -1, "name": "", "description": ""}]  + categoryConnectors.getCategories()['category']
allCategories = sorted(categories, key=lambda cat: cat["name"])
users = json.loads(userConnector.getUsers())["users"]

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())


with st.form("template_form"):
    left, right = st.columns(2)
    donatedTo = left.text_input("Who is the food going to?", value="")
    category = left.selectbox("Category", allCategories, format_func=lambda cat: f'{cat["name"]}')

    weight = right.text_input("Weight", value="")
    location = right.selectbox("Location", allLocations, format_func=lambda loc: f'{loc["name"]}')
    exportedBy = left.selectbox("USer", users, format_func=lambda user: f'{user["name"]}')
    submit = st.form_submit_button()

### TODO:: update userID when sign in functionality is implemented
if submit:
    st.balloons()
    categoryIndex = category["id"]
    # if (categoryIndex != 0):
    #     categoryId = categories[categoryIndex - 1]['id']
    
    exportConnectors.postExport(exportedBy["id"], categoryIndex, donatedTo, int(weight), location["id"])
      
    st.success("🎉 Export recorded!")
