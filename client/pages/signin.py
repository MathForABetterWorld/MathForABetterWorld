import streamlit as st
import requests
import json
import pandas as pd
from datetime import datetime
from routeConnectors import userConnector, shiftConnector


# get list of users as json file?

users = userConnector.getUsers()

users_df = pd.read_json(users)

# TODO understand json format and how we access
user_names = users_df["id"]
user_input = st.selectbox(label="Please enter your name", options = user_names)
check_in_button = st.button("Check in")

if check_in_button:

    startTime = datetime.now()
    shiftConnector.postShift(user_input, startTime.isoformat())

    st.write("Check in successful!")