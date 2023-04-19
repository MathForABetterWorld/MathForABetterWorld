import streamlit as st
import numpy as np
import pandas as pd
from nav import nav_page
from PIL import Image
import os
#from streamlit_extras.switch_page_button import switch_page

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Bmore Food Volunteer Portal")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')
st.image(image)

st.markdown("<h1 style='text-align: center; color: cyan;'>Bmore Food Volunteer Portal</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Welcome!</h2>", unsafe_allow_html=True)
unsafe_allow_html = True

m = st.markdown("""
        <style>
        div.stButton > button:first-child {
            text-align: center;
            box-shadow: 0px 1px 0px 0px #f0f7fa;
            background: linear-gradient(to bottom, #33bdef 5%, #1ad1f5 100%);
            background-color: #1ad1f5;
            border-radius:10px;
            border:1px solid #057fd0;
            display:inline-block;
            cursor:pointer;
            color:#ffffff;
            font-size:18px;
            font-weight:bold;
            padding:6px 24px;
            text-decoration:none;
            text-shadow:0px -1px 0px #5b6178;
            height: 5em;
            width: 19em;
            }
            </style>""", unsafe_allow_html=True)

col1,col2=st.columns([1,1])
with col1:
    sign_in_button = st.button("Volunteer Sign In", key="signInButton")
    if sign_in_button:
        nav_page("Volunteer_Signin")
    import_button = st.button("Food Import")
    if import_button:
        nav_page("Import_Form")

with col2:
    sign_out_button = st.button("Volunteer Sign Out", key="signOutButton")
    if sign_out_button:
        nav_page("Volunteer_Signout")
    export_button = st.button("Food Export")
    if export_button:
        nav_page("Export_Form")

col1a, col2a, col3a = st.columns([0.5,1,0.5])
with col1a:
    st.empty()
with col2a:
    employee_button = st.button("Employee Access", key="employeeButton")
    if employee_button:
        nav_page("Employee_SignIn")
with col3a:
    st.empty()
