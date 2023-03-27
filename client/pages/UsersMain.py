import streamlit as st
import numpy as np
import pandas as pd
from nav import nav_page
from PIL import Image
import os

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo.png", page_title="Bmore Food Volunteer Portal")
image = Image.open(path + '/../assets/bmore_food_logo.png')
st.image(image, caption="Bmore Food Logo")

st.markdown("<h1 style='text-align: center; color: cyan;'>Bmore Food Volunteer Portal</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Welcome!</h2>", unsafe_allow_html=True)
unsafe_allow_html = True



col1,col2,col3=st.columns([0.45,1.2,0.45])
with col1:
    placeholder = st.empty()
with col2:
    m = st.markdown("""
        <style>
        div.stButton > button:first-child {
            box-shadow: 0px 1px 0px 0px #f0f7fa;
            background:linear-gradient(to bottom, #33bdef 5%, #019ad2 100%);
            background-color:#33bdef;
            border-radius:6px;
            border:1px solid #057fd0;
            display:inline-block;
            cursor:pointer;
            color:#ffffff;
            font-size:25px;
            font-weight:bold;
            padding:6px 24px;
            text-decoration:none;
            text-shadow:0px -1px 0px #5b6178;
            height: 5em;
            width: 15em;
            }
            </style>""", unsafe_allow_html=True)
    sign_in_button = st.button("Volunteer Sign In", key="signInButton")
    if sign_in_button:
        nav_page("signin")

    m = st.markdown("""
        <style>
        div.stButton > button:first-child {
             box-shadow: 0px 1px 0px 0px #f0f7fa;
            background:linear-gradient(to bottom, #33bdef 5%, #019ad2 100%);
            background-color:#33bdef;
            border-radius:6px;
            border:1px solid #057fd0;
            display:inline-block;
            cursor:pointer;
            color:#ffffff;
            font-size:25px;
            font-weight:bold;
            padding:6px 24px;
            text-decoration:none;
            text-shadow:0px -1px 0px #5b6178;
            height: 5em;
            width: 15em;
            }
            </style>""", unsafe_allow_html=True)
    sign_out_button = st.button("Volunteer Sign Out", key="signOutButton")
    if sign_out_button:
        nav_page("signout")

    m = st.markdown("""
        <style>
        div.stButton > button:first-child {
             box-shadow: 0px 1px 0px 0px #f0f7fa;
            background:linear-gradient(to bottom, #33bdef 5%, #019ad2 100%);
            background-color:#33bdef;
            border-radius:6px;
            border:1px solid #057fd0;
            display:inline-block;
            cursor:pointer;
            color:#ffffff;
            font-size:25px;
            font-weight:bold;
            padding:6px 24px;
            text-decoration:none;
            text-shadow:0px -1px 0px #5b6178;
            height: 5em;
            width: 15em;
            }
            </style>""", unsafe_allow_html=True)
    employee_button = st.button("Employee Access", key="employeeButton")
    if employee_button:
        nav_page("employee")

with col3:
    placeholder2 = st.empty()