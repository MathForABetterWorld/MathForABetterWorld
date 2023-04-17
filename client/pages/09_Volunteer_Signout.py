import streamlit as st
import json
import pandas as pd
import time
from datetime import datetime
from routeConnectors import shiftConnector, authConnectors, employeeConnectors
from nav import nav_page
from PIL import Image
import os

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

# get list of users as json file?

active_shifts = shiftConnector.activeShifts()
active_shifts2 = json.loads(active_shifts)
#st.write(active_shifts2)
shifts = pd.json_normalize(active_shifts2["activateShifts"])
if shifts.empty:
    active_users = []
else:
    active_users = shifts["user.name"]
#user_names = users["Name"]

user_input = st.selectbox(label="Please enter your name", options = active_users)
food_input = st.text_input("Enter lbs of food")
submit_button = st.button("Submit")
#st.session_state['button'] = False
if st.session_state.get('button') != True:
    st.session_state['button'] = submit_button

if st.session_state['button'] == True:
    row = shifts[shifts["user.name"] == user_input].iloc[0]
    # TODO deal with if user doesn't input anything for number

    foodAmt = float(food_input) if (food_input.isnumeric()) else st.write("Please input a number")
    # if food_input isn't a number, foodAmt = None so the next bit has issues
    if (foodAmt >= 0):
        if foodAmt > 20:
            st.write("Please get admin approval.")
            admin_input = st.text_input("Admin Name")
            password_input = st.text_input("Password", type="password")
            if st.button("Login admin"):            
                res = json.loads(authConnectors.signinEmployee(admin_input, password_input))
                if res["status"]!=200:
                    st.write("Invalid admin login, volunteer not signed out")
                    time.sleep(2)
                    st.session_state['button'] = False
                    nav_page("UsersMain")
                else:
                    current_user_id = user_input
                    shift_id = row["id"]
                    shiftConnector.signout(foodAmt, int(shift_id))
                    st.write("Sign out successful!")
                    # wait 2 seconds
                    time.sleep(2)
                    st.session_state['button'] = False
                    # redirect to UsersMain
                    nav_page("UsersMain")
        else: 
            current_user_id = user_input
            shift_id = row["id"]
            shiftConnector.signout(foodAmt, int(shift_id))
            st.write("Sign out successful!")
            # wait 2 seconds
            time.sleep(2)
            st.session_state['button'] = False
            # redirect to UsersMain
            nav_page("UsersMain")
    else:
        st.write("Enter a value greater than or equal to 0.")
    

    # maybe just get all shifts that don't have end time then search for
    # the one that has that person's name