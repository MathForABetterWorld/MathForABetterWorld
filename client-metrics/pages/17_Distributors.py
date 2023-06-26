
import streamlit as st
import numpy as np
import pandas as pd
import json
import os
from routeConnectors import distributorConnectors
from PIL import Image
path = os.path.dirname(__file__)
# This has to be the first streamlit command called
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="View Distributors")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')
st.image(image)
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

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
