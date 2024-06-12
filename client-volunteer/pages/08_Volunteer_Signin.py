import streamlit as st
import json
import pandas as pd
import time
from datetime import datetime
from routeConnectors import userConnector, shiftConnector, rootName
from nav import nav_page
from PIL import Image
import os

path = os.path.dirname(__file__)
st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Volunteer Sign-In")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(image)
with col3:
    st.write(' ')

title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    # with col1:
    #     st.image(path + '/../assets/bmore_food_logo_dark_theme.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Volunteer Sign-In</h1>", unsafe_allow_html=True)

allUsers = [{"id": -1, "name": ""}]
dbUsers = json.loads(userConnector.getUsers().decode("utf-8"))
if dbUsers:
    allUsers = allUsers + dbUsers["users"]

user_input = st.selectbox("Please enter your name", allUsers, format_func=lambda user: f'{user["name"]}' )
check_in_button = st.button("Check in")


if check_in_button:
    if user_input["name"] in shiftConnector.activeShifts():
        st.error("ERROR: User is currently signed in. Please sign out.")
    else:
        startTime = datetime.now()
        shiftConnector.postShift(user_input["id"], startTime.isoformat())
        st.write("Check in successful!")
        time.sleep(2)
        nav_page("")

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
