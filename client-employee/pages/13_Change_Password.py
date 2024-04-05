import streamlit as st

from PIL import Image
import os
from routeConnectors import authConnectors, employeeConnectors
import json
from nav import nav_page


path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Change Password")
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
        st.markdown("<h1 style='text-align: center; '>Change Password</h1>", unsafe_allow_html=True)


if 'token' in st.session_state:
    # dropdown or text input for employee name
    # text input for password
    user_input = st.text_input("Username")
    password_input = st.text_input("Password", type="password")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    log_in_button = st.button("Update Account")

    if log_in_button:
        if not user_input or not password_input or not new_password or not new_username:
            st.error("Fill out form.")
        else:
            try:
                # check user_input and password_input match
                # go to employee page
                employeeConnectors.changePassword(new_username, new_password, user_input, password_input)
                res = json.loads(authConnectors.signinEmployee(new_username, new_password))
                st.session_state.token = res["token"]
            except Exception as e:
                st.error("Login failed. Username or password incorrect.")

else:
    st.error("No access to change password. Please log in if employee.")

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")

if log_button :
    if "token" in st.session_state :
        if "role" in st.session_state :
            del st.session_state.role
        del st.session_state.token
        st.experimental_rerun()
    else:
        nav_page("")