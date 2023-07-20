import streamlit as st
import numpy as np
import pandas as pd
import json
import os 
from routeConnectors import categoryConnectors, exportConnectors, locationConnectors, userConnector, importConnectors
from PIL import Image
from nav import nav_page

path = os.path.dirname(__file__)
# This has to be the first streamlit command called
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Query inventory")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')
st.image(image)

# log in status

if 'token' in st.session_state :
    log_button = st.button("Employee Log-out", key=".my-button", use_container_width=True)
else:
    log_button = st.button("Employee Log-in", key=".my-button", use_container_width=True)

categories = [{"id": -1, "name": "", "description": ""}]  + categoryConnectors.getCategories()['category']
sortedCategories = sorted(categories, key=lambda cat: cat["name"])



categoryDF = pd.DataFrame(categories)
categorySelect = st.selectbox("Show all food of type", sortedCategories, format_func=lambda cat: f'{cat["name"]}')
st.dataframe(df)

sum = df["weight"].sum()

s = pd.Series([sum], name='Total import weight')

st.dataframe(s, use_container_width=True)

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