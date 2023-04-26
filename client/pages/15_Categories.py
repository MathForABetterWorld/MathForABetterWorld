
import streamlit as st
import numpy as np
import pandas as pd
import json
import os
from routeConnectors import categoryConnectors
from PIL import Image

path = os.path.dirname(__file__)
# This has to be the first streamlit command called
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="View Categories")

image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')
st.image(image)
print("getting categories....")
categories = categoryConnectors.getCategories()["category"]
categoryDF = pd.DataFrame(categories)
title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    # with col1:
    #     st.image(path + '/../assets/bmore_food_logo_dark_theme.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>View Categories</h1>", unsafe_allow_html=True)

st.dataframe(categoryDF)
if 'token' in st.session_state:
    editType = st.selectbox("Modification Type", ["", "New Category", "Update Category", "Delete Category"])
    if editType == "New Category":
        with st.form("template_form"):
            left, right = st.columns(2)
            name = left.text_input("Item", "")
            desc = right.text_input("Description", "")
            newSubmit = st.form_submit_button()
        if newSubmit:
            if name == "" or desc == "":
                st.error("Please fill in both form elements!")
            else:
                newCat = pd.DataFrame(json.loads(categoryConnectors.postCategory(name, desc))["category"], index=[0])
                st.experimental_rerun()
    elif editType == "Update Category":
        with st.form("template_form"):
            left, right = st.columns(2)
            idx = left.number_input("Id", min_value=1)
            name = left.text_input("Item", "")
            desc = right.text_input("Description", "")
            editSubmit = st.form_submit_button()
        if editSubmit:
            if name == "" or desc == "":
                st.error("Please fill in both form elements!")
            elif idx in categoryDF.id.unique():
                editedCat = categoryConnectors.updateCategory(idx, name, desc)
                st.experimental_rerun()
            else:
                st.error("Please input an id that is in the table!")
    elif editType == "Delete Category":
        with st.form("template_form"):
            idx = st.number_input("Id", min_value=1)
            deleteSubmit = st.form_submit_button()
        if deleteSubmit:
            if idx in categoryDF.id.unique():
                deletedCat = categoryConnectors.deleteCategory(idx)
                st.experimental_rerun()
            else:
                st.error("Please input an id that is in the table!")

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
