
import streamlit as st
import numpy as np
import pandas as pd
import json
import os
from routeConnectors import rackConnector
from PIL import Image
from nav import nav_page

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Racks")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(image)
with col3:
    st.write(' ')
# log in status

if 'token' in st.session_state :
    log_button = st.button("Employee Log-out", key=".my-button", use_container_width=True)
else:
    log_button = st.button("Employee Log-in", key=".my-button", use_container_width=True)


print("getting racks....")
racks = rackConnector.getRacks()["rack"]
rackDF = pd.DataFrame(racks)

title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    # with col1:
    #     st.image(path + '/../assets/bmore_food_logo_dark_theme.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Racks Page</h1>", unsafe_allow_html=True)

if 'token' in st.session_state:
    editType = st.selectbox("Modification Type (Add, Edit) (Select Below)", ["", "New Rack", "Update Rack"])
    if editType == "New Rack":
        with st.form("template_form"):
            left, right = st.columns(2)
            location = left.text_input("Location", "")
            desc = right.text_input("Description", "")
            weightLimit = left.number_input("Weight Limit (Optional)", min_value=0.0, format="%.2f")
            newSubmit = st.form_submit_button()
        if newSubmit:
            if location == "" or weightLimit == 0 or desc == "":
                st.error("Please fill in form elements!")
            else:
                rackConnector.postRack(location, desc, weightLimit)
                st.experimental_rerun()
    elif editType == "Update Rack":
        with st.form("template_form"):
            left, right = st.columns(2)
            location = left.text_input("Location", "")
            desc = right.text_input("Description", "")
            weightLimit = left.number_input("Weight Limit", min_value=0.0, format="%.2f")
            idx = right.number_input("Id", min_value=1)
            editSubmit = st.form_submit_button()
        if editSubmit:
            if location == "" or weightLimit == 0 or desc == "":
                st.error("Please fill in form elements!")
            elif idx in rackDF.id.unique():
                editedCat = rackConnector.updateRack(idx, location, desc, weightLimit)
                st.experimental_rerun()
            else:
                st.error("Please input an id that is in the table!")


st.dataframe(rackDF)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")


if log_button :
    if "token" in st.session_state :
        del st.session_state.token
        st.experimental_rerun()
    else:
        nav_page("")