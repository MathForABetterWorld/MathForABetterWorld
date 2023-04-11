import streamlit as st

from PIL import Image
import os
from routeConnectors import authConnectors, employeeConnectors, shiftConnector
import json
from datetime import datetime
import pandas as pd
import time
from nav import nav_page

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Employee Login")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')

### Header ###
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(image)
with col3:
    st.write(' ')

# on button click submit, check if valid user

user_input = st.text_input("Username")
password_input = st.text_input("Password", type="password")
log_in_button = st.button("Log in")
logout_button = st.button("Logout")

if log_in_button:
    res = json.loads(authConnectors.signinEmployee(user_input, password_input))
    st.session_state.token = res["token"]

    # test successfuly login
    st.write('successful login')

    
    # connect to the employee data table
    employee = employeeConnectors.getUsers()
    # get the employee table as a pandas df via json file
    users2 = json.loads(employee)
    users_df = pd.json_normalize(users2["users"])

    # new column in the dataframe
    users_df.insert(0,"Blank_Column", " ")
    # create column for the names of each user in the employee table
    user_names = users_df["name"]



    # set the current time of shirt login
    startTime = datetime.now()

    id = users_df[users_df["name"] == user_input]["id"]  # get id of the input username
    st.write(id)
    shiftConnector.postShift(int(id.iloc[0]), startTime.isoformat())

    st.write("Check in successful!")
    # wait 2 seconds
    time.sleep(2)

    # redirect to UsersMain
    # nav_page("UsersMain")

if logout_button: 
    # record checkout time
    endTime = datetime.now()
    # 
    food_input = st.text_input("Enter lbs of food")
    # set variable foodamt with datatype object
    foodAmt = float(food_input) if food_input.isnumeric() else st.write("Please input a number")
    submit_button = st.button("Submit")

    if submit_button:
        st.write('Thank you')
        time.sleep(2)
        current_user_id = user_input
        #shift_id = row["id"]
        #shiftConnector.signout(foodAmt, int(shift_id))
        st.write("Sign out successful!")
        # wait 2 seconds
        time.sleep(5)
        # redirect to UsersMain
        nav_page("UsersMain")


    # add shirt duration time AND amoutn taken into the respective tables

    del st.session_state.token
