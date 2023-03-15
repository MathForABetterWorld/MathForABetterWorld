import streamlit as st
import requests
import json
import pandas as pd
from datetime import datetime
from routeConnectors import userConnector, shiftConnector, rootName

users = userConnector.getUsers()

users2 = json.loads(users)
users_df = pd.json_normalize(users2["users"])

user_names = users_df["name"]
user_input = st.selectbox(label="Please enter your name", options = user_names)
check_in_button = st.button("Check in")

if check_in_button:

    startTime = datetime.now()
    id = users_df[users_df["name"] == user_input]["id"]
    shiftConnector.postShift(str(id.iloc[0]), startTime.isoformat())

    st.write("Check in successful!")