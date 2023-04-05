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

st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo.png", page_title="Bmore Food Volunteer Portal")
image = Image.open(path + '/../assets/bmore_food_logo.png')
st.image(image, caption="Bmore Food Logo")

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

if submit_button:
    row = shifts[shifts["user.name"] == user_input].iloc[0]
    # TODO deal with if user doesn't input anything for number
    foodAmt = float(food_input) if food_input.isnumeric() else st.write("Please input a number")
    if (foodAmt >= 0):
        if foodAmt > 20:
            st.write("Please get admin approval.")
            admin_input = st.text_input("Admin Name")
            password_input = st.text_input("Password", type="password")
            admin_login_button = st.button("Login admin")

            # this is currently causing errors we think?
            while not admin_login_button:
                time.sleep(1)
            
            res = json.loads(authConnectors.signinEmployee(admin_input, password_input))
        
            st.write(res)
            if res["status"]!=200:
                st.write("Invalid admin login, user not signed out")
                time.sleep(2)
                nav_page("UsersMain")
            
        current_user_id = user_input
        shift_id = row["id"]
        shiftConnector.signout(foodAmt, int(shift_id))
        st.write("Sign out successful!")
        # wait 2 seconds
        time.sleep(2)
        # redirect to UsersMain
        nav_page("UsersMain")
    else:
        st.write("Enter a value greater than or equal to 0.")
    

    # maybe just get all shifts that don't have end time then search for
    # the one that has that person's name