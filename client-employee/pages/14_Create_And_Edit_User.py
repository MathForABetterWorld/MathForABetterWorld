
import streamlit as st
import numpy as np
import pandas as pd
import json
import os
from routeConnectors import userConnector, employeeConnectors
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
        st.markdown("<h1 style='text-align: center; '>Create & Edit Users</h1>", unsafe_allow_html=True)

if 'token' in st.session_state:
    editType = st.selectbox("Modification Type (Add, Edit) (Select Below)", ["", "New User", "Update User"])
    if editType == 'New User':
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
                    r = json.loads(userConnector.postUser(email, name, None if phoneNumber == "" else phoneNumber, None if address == "" else address))
                    if "msg" not in r:
                        st.balloons()
                        st.success("🎉 Your user was created!")
                    else:
                        st.error(r["msg"])
    elif editType == 'Update User':
        # Input field for User ID
        users = json.loads(employeeConnectors.getUsers())["users"]
        usersDF = pd.DataFrame.from_dict(users)
        filtered_usersDF = usersDF[pd.isna(usersDF['employeeId'])]
        filtered_usersDF = filtered_usersDF.drop(columns=['employee', 'employeeId'])

        user_id_to_update = st.selectbox("Select User ID to Update:", filtered_usersDF['id'].values, index=0)
        find_user = st.button("Find User")
        
        if find_user:
            if user_id_to_update in filtered_usersDF['id'].values:
                selected_user = filtered_usersDF.loc[filtered_usersDF['id'] == user_id_to_update]

                with st.form("template_form"):
                    left, right = st.columns(2)
                    name = left.text_input("Name", selected_user['name'].values[0])
                    email = right.text_input("Email", selected_user['email'].values[0])
                    phoneNumber = left.text_input("Phone Number (Optional)", selected_user['phoneNumber'].values[0])
                    address = right.text_input("Address (Optional)", selected_user['address'].values[0])
                    isActive = left.checkbox("Is Active Volunteer?", selected_user['isActive'].values[0])
                    update_submit = st.form_submit_button("Update User")

                    if update_submit:
                        jsonObj = json.loads(userConnector.postUser(email, name, None if phoneNumber == "" else phoneNumber, None if address == "" else address, isActive))
                        newCat = pd.DataFrame(jsonObj["user"], index=[0])
                        st.experimental_rerun()
            else:
                st.warning("User ID not found. Please enter a valid User ID.")
        st.dataframe(filtered_usersDF)
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