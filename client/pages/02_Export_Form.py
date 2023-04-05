# import pdfkit
import streamlit as st
import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os 
from routeConnectors import categoryConnectors, locationConnectors, userConnector

path = os.path.dirname(__file__)
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Export Form")

title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    with col1:
        st.image(path + '/../assets/bmore_food_logo_dark_theme.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Food export form</h1>", unsafe_allow_html=True)
users = userConnector.getUsers()
locations = locationConnectors.getLocations()['location']
locationsName = [loc['name'] for loc in locations]
locationsName.insert(0, '')
locations.insert(0, None)
categories = categoryConnectors.getCategories()["category"]
categoryNames = [cat["name"] for cat in categories]
categories.insert(0, None)
categoryNames.insert(0, "")

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())

with st.form("template_form"):
    left, right = st.columns(2)
    donatedTo = left.text_input("Who is the food going to?", value="")
    category = left.selectbox("Category", categoryNames)
    weight = right.text_input("Weight", value="")
    location = right.selectbox("Location", locationsName)
    submit = st.form_submit_button()

if submit:
    st.balloons()
    st.success("🎉 Export recorded!")
