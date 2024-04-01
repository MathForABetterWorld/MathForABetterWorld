# This should allow you to look up an employee and get their 
# personal info (phone, address etc) as well as info on how 
# many hours they've worked etc. 

import streamlit as st
import pandas as pd
from PIL import Image
import os
from routeConnectors import authConnectors, employeeConnectors
import json
from nav import nav_page

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Query Employees")
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
        st.markdown("<h1 style='text-align: center; '>Query Employees</h1>", unsafe_allow_html=True)

if 'token' in st.session_state:
    # check user_input and password_input match
    # go to employee page
    users = json.loads(employeeConnectors.getUsers())["users"]
    usersDF = pd.DataFrame.from_dict(users)
    filtered_usersDF = usersDF.dropna(subset=['employeeId'])
    filtered_usersDF['userName'] = filtered_usersDF['employee'].apply(lambda x: x['userName'] if x else None)
    filtered_usersDF['role'] = filtered_usersDF['employee'].apply(lambda x: x['role'] if x else None)
    filtered_usersDF = filtered_usersDF.drop(columns=['employee', 'employeeId'])
    st.dataframe(filtered_usersDF)
    selectedIndex = st.selectbox('Select row:', filtered_usersDF.name)

    promoteToAdmin = st.button("Make User an Admin")

    if promoteToAdmin:
        idx = int(usersDF.loc[usersDF["name"] == selectedIndex].iloc[0].id)
        r = employeeConnectors.promoteToAdmin(idx)

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