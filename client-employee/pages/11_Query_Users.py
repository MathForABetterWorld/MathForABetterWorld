import streamlit as st
import pandas as pd
from PIL import Image
import os
from routeConnectors import authConnectors, employeeConnectors
import json
from nav import nav_page

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Query Users")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')

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

title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    # with col1:
    #     st.image(path + '/../assets/bmore_food_logo_dark_theme.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Query Users</h1>", unsafe_allow_html=True)

# on button click submit, check if valid user

if 'token' in st.session_state:
    # check user_input and password_input match
    # go to employee page
    users = json.loads(employeeConnectors.getUsers())["users"]
    usersDF = pd.DataFrame.from_dict(users)
    filtered_usersDF = usersDF.drop(columns=['employee', 'employeeId'])
    st.dataframe(filtered_usersDF)
    st.write("Select a Volunteer to promote to Employee:")
    selectedIndex = st.selectbox('Volunteer Selection:', filtered_usersDF.name)


    user_input = st.text_input("Temporary Username")
    password_input = st.text_input("Temporary Password", type="password")
    promoteUser = st.button("Make User an Employee")
    
    if promoteUser:        
        idx = int(usersDF.loc[usersDF["name"]== selectedIndex].iloc[0].id)
        employeeConnectors.promoteUser(idx, user_input, password_input)

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