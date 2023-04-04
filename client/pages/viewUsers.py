import streamlit as st
import pandas as pd
from PIL import Image
import os
from routeConnectors import authConnectors, employeeConnectors
import json

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo.png", page_title="Bmore Food Volunteer Portal")
image = Image.open(path + '/../assets/bmore_food_logo.png')
st.image(image, caption="Bmore Food Logo")
# on button click submit, check if valid user
print('token' in st.session_state)

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
