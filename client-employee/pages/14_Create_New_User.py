
import streamlit as st
import numpy as np
import pandas as pd
import json
import os
from routeConnectors import userConnector
from PIL import Image

path = os.path.dirname(__file__)
# This has to be the first streamlit command called
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Create New User")

image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')
st.image(image)
if 'token' in st.session_state:
    users = json.loads(userConnector.getUsers())["users"]
    df = pd.DataFrame(users)
    st.write(df)
    with st.form("template_form"):
        left, right = st.columns(2)
        name = left.text_input("Name", "")
        email = right.text_input("Email", "")
        phoneNumber = left.text_input("Phone Number (Optional)", "")
        address = right.text_input("Address (Optional)", "")
        newSubmit = st.form_submit_button()
        isActive = True
        if newSubmit:
            if name == "" or email == "":
                st.error("Please fill in required form elements!")
            else:
                jsonObj = json.loads(userConnector.postUser(email, name, None if phoneNumber == "" else phoneNumber, None if address == "" else address, isActive))
                newCat = pd.DataFrame(jsonObj["user"], index=[0])
                #print(newCat)
                st.experimental_rerun()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
