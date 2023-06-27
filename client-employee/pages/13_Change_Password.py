import streamlit as st

from PIL import Image
import os
from routeConnectors import authConnectors, employeeConnectors
import json

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Bmore Food Volunteer Portal")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')
st.image(image, caption="Bmore Food Logo")

if 'token' in st.session_state:
    # dropdown or text input for employee name
    # text input for password
    user_input = st.text_input("Username")
    password_input = st.text_input("Password", type="password")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    log_in_button = st.button("Update Account")

    if log_in_button:
        # check user_input and password_input match
        # go to employee page
        employeeConnectors.changePassword(new_username, new_password, user_input, password_input)
        res = json.loads(authConnectors.signinEmployee(new_username, new_password))
        st.session_state.token = res["token"]