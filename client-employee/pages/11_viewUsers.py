import streamlit as st
import pandas as pd
from PIL import Image
import os
from routeConnectors import authConnectors, employeeConnectors
import json
from nav import nav_page

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Bmore Food Volunteer Portal")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')

### Header ###
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(image)
with col3:
    st.write(' ')

# log in status

if 'token' in st.session_state :
    log_button = st.button("Employee Log-out", key=".my-button", use_container_width=True)
else:
    log_button = st.button("Employee Log-in", key=".my-button", use_container_width=True)


# on button click submit, check if valid user

if 'token' in st.session_state:
    # check user_input and password_input match
    # go to employee page
    users = json.loads(employeeConnectors.getUsers())["users"]
    usersDF = pd.DataFrame.from_dict(users)
    st.dataframe(usersDF)
    selectedIndex = st.selectbox('Select row:', usersDF.name)

    promoteUser = st.button("Make User an Employee")
    user_input = st.text_input("Temporary Username")
    password_input = st.text_input("Temporary Password", type="password")
    
    promoteToAdmin = st.button("Make User an Admin")

    if promoteUser:        
        idx = int(usersDF.loc[usersDF["name"]== selectedIndex].iloc[0].id)
        employeeConnectors.promoteUser(idx, user_input, password_input)
    if promoteToAdmin:
        idx = int(usersDF.loc[usersDF["name"] == selectedIndex].iloc[0].id)
        r = employeeConnectors.promoteToAdmin(idx)


if log_button :
    if "token" in st.session_state :
        del st.session_state.token
        st.experimental_rerun()
    else:
        nav_page("")