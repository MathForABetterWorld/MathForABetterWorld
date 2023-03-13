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

shifts = pd.read_json(active_shifts, orient='index')

active_users = shifts["userId"]

#user_names = users["Name"]
user_input = st.selectbox(label="Please enter your name", options = active_users)
food_input = st.text_input("Enter lbs of food")
submit_button = st.button("Submit")

if submit_button:
    foodAmt = float(food_input) if food_input.isnumeric() else st.write("Please input a number")
    if (foodAmt >= 0 & foodAmt <=20):

        current_user_id = user_input
        row = shifts[shifts["userId"] == current_user_id]
        shift_id = row["id"]
        # TODO get shift id from corresponding user's last shift from active_shifts
        shiftConnector.signout(foodAmt, shift_id)
        st.write("Sign out successful!")
    else:
        st.write("Enter a value between 0 and 20.")
    

    # maybe just get all shifts that don't have end time then search for
    # the one that has that person's name