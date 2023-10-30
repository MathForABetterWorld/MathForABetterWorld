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


users = userConnector.getUsers()

users2 = json.loads(users)
users_df = pd.json_normalize(users2["users"])

users_df.insert(0,"Blank_Column", " ")

user_names = users_df["name"]
user_input = st.selectbox(label="Please enter your name", options = user_names.sort_values())
check_in_button = st.button("Check in")

if check_in_button:
    if users_df["name"].iloc[0]  in shiftConnector.activeShifts():
        st.error("ERROR: User is currently signed in. Please sign out.")
    else:
        startTime = datetime.now()
        id = users_df[users_df["name"] == user_input]["id"]
        shiftConnector.postShift(int(id.iloc[0]), startTime.isoformat())

        st.write("Check in successful!")

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
