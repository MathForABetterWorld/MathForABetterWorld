import streamlit as st

from PIL import Image
import os
from routeConnectors import authConnectors, employeeConnectors
import json

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo.png", page_title="Bmore Food Volunteer Portal")
image = Image.open(path + '/../assets/bmore_food_logo.png')
st.image(image, caption="Bmore Food Logo")
# on button click submit, check if valid user

# dropdown or text input for employee name
# text input for password
user_input = st.text_input("Username")
password_input = st.text_input("Password", type="password")
log_in_button = st.button("Log in")

if log_in_button:
    # check user_input and password_input match
    # go to employee page
    res = json.loads(authConnectors.signinEmployee(user_input, password_input))
    st.session_state.token = res["token"]