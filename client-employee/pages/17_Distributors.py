
import streamlit as st
import numpy as np
import pandas as pd
import json
import os
from routeConnectors import distributorConnectors
from PIL import Image
from nav import nav_page

path = os.path.dirname(__file__)
# This has to be the first streamlit command called
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="View Distributors")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')
st.image(image)

# log in status

if 'token' in st.session_state :
    log_button = st.button("Employee Log-out", key=".my-button", use_container_width=True)
else:
    log_button = st.button("Employee Log-in", key=".my-button", use_container_width=True)

print("getting distributors....")
distributors = distributorConnectors.getDistributors()["distributors"]
distributorDF = pd.DataFrame(distributors)
title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    # with col1:
    #     st.image(path + '/../assets/bmore_food_logo_dark_theme.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>View Distributors</h1>", unsafe_allow_html=True)

st.dataframe(distributorDF)
if 'token' in st.session_state:
    editType = st.selectbox("Modification Type", ["", "New Distributor", "Update Distributor", "Delete Distributor"])
    if editType == "New Distributor":
        with st.form("template_form"):
            name = st.text_input("Name", "")
            newSubmit = st.form_submit_button()
        if newSubmit:
            if name == "":
                st.error("Please fill in form elements!")
            else:
                newDist = pd.DataFrame(json.loads(distributorConnectors.postDistributor(name))["distributor"], index=[0])
                st.experimental_rerun()
    elif editType == "Update Distributor":
        with st.form("template_form"):
            left, right = st.columns(2)
            idx = left.number_input("Id", min_value=1)
            name = right.text_input("Name", "")
            editSubmit = st.form_submit_button()
        if editSubmit:
            if name == "":
                st.error("Please fill in both form elements!")
            elif idx in distributorDF.id.unique():
                editedCat = distributorConnectors.updateDistributor(idx, name)
                st.experimental_rerun()
            else:
                st.error("Please input an id that is in the table!")
    elif editType == "Delete Distributor":
        with st.form("template_form"):
            idx = st.number_input("Id", min_value=1)
            deleteSubmit = st.form_submit_button()
        if deleteSubmit:
            if idx in distributorDF.id.unique():
                deletedCat = distributorConnectors.deleteDistributor(idx)
                st.experimental_rerun()
            else:
                st.error("Please input an id that is in the table!")

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