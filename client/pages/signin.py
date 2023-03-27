import streamlit as st
import json
import pandas as pd
import time
from datetime import datetime
from routeConnectors import userConnector, shiftConnector, rootName
from nav import nav_page
users = userConnector.getUsers()

users2 = json.loads(users)
users_df = pd.json_normalize(users2["users"])

users_df.insert(0,"Blank_Column", " ")

user_names = users_df["name"]
user_input = st.selectbox(label="Please enter your name", options = user_names.sort_values())
check_in_button = st.button("Check in")

if check_in_button:

    startTime = datetime.now()
    id = users_df[users_df["name"] == user_input]["id"]
    shiftConnector.postShift(int(id.iloc[0]), startTime.isoformat())

    st.write("Check in successful!")
    # wait 2 seconds
    time.sleep(2)
    # redirect to UsersMain
    nav_page("UsersMain")