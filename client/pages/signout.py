import streamlit as st
import json
import pandas as pd
import time
from datetime import datetime
from routeConnectors import shiftConnector
from nav import nav_page

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
            user_input = st.text_input("Admin Name")
            password_input = st.text_input("Password")
            # TODO search in employees to get employee with name Name, if password matches
                #"[foodAmt] is approved. Sign out successful!")
            
        
            
        current_user_id = user_input
        shift_id = row["id"]
        # TODO get shift id from corresponding user's last shift from active_shifts
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