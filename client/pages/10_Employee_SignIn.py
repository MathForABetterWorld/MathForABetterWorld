import streamlit as st

from PIL import Image
import os
from routeConnectors import authConnectors, employeeConnectors
import json

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo.png", page_title="Employee Login")
image = Image.open(path + '/../assets/bmore_food_logo.png')
st.image(image, caption="Bmore Food Logo")

user_input = st.text_input("Username")
password_input = st.text_input("Password", type="password")
log_in_button = st.button("Log in")
logout_button = st.button("Logout")
if log_in_button:
    res = json.loads(authConnectors.signinEmployee(user_input, password_input))
    st.session_state.token = res["token"]
if logout_button: 
    del st.session_state.token