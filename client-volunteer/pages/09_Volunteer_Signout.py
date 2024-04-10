import streamlit as st
import json
import pandas as pd
import time
from datetime import datetime
from routeConnectors import shiftConnector, authConnectors, employeeConnectors
from nav import nav_page
from PIL import Image
import os

def is_non_neg_float(string):
    try:
        flt = float(string)
        if flt < 0:
            return False
        return True
    except ValueError:
        return False

path = os.path.dirname(__file__)
st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Volunteer Sign-Out")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(image)
with col3:
    st.write(' ')

title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    # with col1:
    #     st.image(path + '/../assets/bmore_food_logo_dark_theme.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Volunteer Sign-Out</h1>", unsafe_allow_html=True)


active_users = [{"id": -1, "name": ""}]
active_shifts = shiftConnector.activeShifts()
active_shifts2 = json.loads(active_shifts)
shifts = pd.json_normalize(active_shifts2["activateShifts"])
shifts = shifts[shifts["user.employeeId"].isnull()]
if shifts.empty:
    active_users = []
else:
    active_users = active_users + shifts.apply(lambda x: {'id': x['user.id'], 'name': x['user.name']}, axis=1).tolist()
#user_names = users["Name"]

user_input = st.selectbox("Please enter your name", active_users, format_func=lambda user: f'{user["name"]}' )
# food_input = st.text_input("Enter lbs of food")
food_input = st.text_input("Enter lbs of regular food taken")
damaged_food_input = st.text_input("Enter lbs of damaged food taken")
submit_button = st.button("Submit")


if st.session_state.get('button') != True:
    st.session_state['button'] = submit_button

if st.session_state['button'] == True:

    # username must be entered
    if not bool(user_input) :
        st.error("Please enter a user.")
        st.session_state['button'] = False
    else :
        rows = shifts[shifts["user.name"] == user_input["name"]]
        if not rows.empty:
            row = rows.iloc[0]

            # food_input must be a non-negative float
            if is_non_neg_float(food_input) and is_non_neg_float(damaged_food_input):
                foodAmt = float(food_input)
                damagedFoodAmt = float(damaged_food_input)
                
                # food amount more than 20lbs requires admin approval
                if foodAmt > 20:
                    st.write("Please get admin approval.")
                    admin_input = st.text_input("Admin Name")
                    password_input = st.text_input("Password", type="password")
                    if st.button("Login admin"):            
                        res = json.loads(authConnectors.signinEmployee(admin_input, password_input))
                        if res["status"]!=200:
                            st.error("Invalid admin login, volunteer not signed out")
                            time.sleep(2)
                            st.session_state['button'] = False
                            nav_page("Volunteer_Home")
                        else:
                            current_user_id = user_input
                            shift_id = row["id"]
                            shiftConnector.signout(foodAmt, int(shift_id), damagedFoodAmt)
                            st.write("Sign out successful!")
                            # wait 2 seconds
                            time.sleep(2)
                            st.session_state['button'] = False
                            nav_page("Volunteer_Home")
                else: 
                    current_user_id = user_input
                    shift_id = row["id"]
                    shiftConnector.signout(foodAmt, int(shift_id), damagedFoodAmt)
                    st.write("Sign out successful!")
                    st.session_state['button'] = False
            else:
                st.error("Please enter a number at least greater than or equal to 0.")
                st.session_state['button'] = False
        else:
            st.error("User does not have an active shift")
        
# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
