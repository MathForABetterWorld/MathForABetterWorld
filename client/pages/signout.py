import streamlit as st

import requests
import urllib3
import json
import pandas as pd
from datetime import datetime
from routeConnectors import shiftConnector

# get list of users as json file?

active_shifts = shiftConnector.activeShifts()
# TODO figure out what json format is and how to get user ids to have as options in name dropdown
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
    foodAmt = float(food_input) if food_input.isnumeric() else st.write("Please input a number")
    if (foodAmt >= 0 and foodAmt <=20):

        current_user_id = user_input
        shift_id = row["id"]
        # TODO get shift id from corresponding user's last shift from active_shifts
        shiftConnector.signout(foodAmt, int(shift_id))
        st.write("Sign out successful!")
    else:
        st.write("Enter a value between 0 and 20.")
    

    # maybe just get all shifts that don't have end time then search for
    # the one that has that person's name