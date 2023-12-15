
import streamlit as st
import numpy as np
import pandas as pd
import json
import os
from routeConnectors import userConnector
from PIL import Image
from nav import nav_page


path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Create New User")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(image)
with col3:
    st.write(' ')

if 'token' in st.session_state :
    log_button = st.button("Employee Log-out", key=".my-button", use_container_width=True)
else:
    log_button = st.button("Employee Log-in", key=".my-button", use_container_width=True)

title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    # with col1:
    #     st.image(path + '/../assets/bmore_food_logo_dark_theme.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Create New User</h1>", unsafe_allow_html=True)

if 'token' in st.session_state:
    with st.form("template_form"):
        left, right = st.columns(2)
        name = left.text_input("Name", "")
        email = right.text_input("Email", "")
        phoneNumber = left.text_input("Phone Number (Optional)", "")
        address = right.text_input("Address (Optional)", "")
        newSubmit = st.form_submit_button()
        if newSubmit:
            if name == "" or email == "":
                st.error("Please fill in required form elements!")
            else:
                jsonObj = json.loads(userConnector.postUser(email, name, None if phoneNumber == "" else phoneNumber, None if address == "" else address))
                newCat = pd.DataFrame(jsonObj["user"], index=[0])
                #print(newCat)
                st.experimental_rerun()
else:
    st.error("No access to create user. Please log in if employee.")

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")

if log_button :
    if "token" in st.session_state :
        del st.session_state.token
        st.experimental_rerun()
    else:
        nav_page("")