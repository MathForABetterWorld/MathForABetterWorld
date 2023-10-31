import streamlit as st

from PIL import Image
import os
from routeConnectors import authConnectors, employeeConnectors, shiftConnector
import json
from datetime import datetime
import pandas as pd
import time
from nav import nav_page

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Employee Login")
image = Image.open(path + '/assets/bmore_food_logo_dark_theme.png')

### Header ###
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
        st.markdown("<h1 style='text-align: center; '>Employee Log-In</h1>", unsafe_allow_html=True)

# on button click submit, check if valid user

user_input = st.text_input("Username")
password_input = st.text_input("Password", type="password")
log_in_button = st.button("Log in")
logout_button = st.button("Logout")

if log_in_button:
    try:
        if not user_input or not password_input:
            st.error("fill out form")
        else:
            res = json.loads(authConnectors.signinEmployee(user_input, password_input))
            st.session_state.token = res["token"]

            # test successfuly login
            st.write('successful login')

            
            # connect to the employee data table
            employee = employeeConnectors.getEmployees()
            # get the employee table as a pandas df via json file
            users2 = json.loads(employee)
            users_df = pd.json_normalize(users2["employees"])

            # new column in the dataframe
            #users_df.insert(0,"Blank_Column", " ")
            # create column for the names of each user in the employee table
            #user_names = users_df["userName"]


            #print(users_df)
            # set the current time of shirt login
            idx = users_df[users_df["userName"] == user_input].iloc[0]["user.id"]  # get id of the input username
            st.write(idx)
            st.session_state["idx"] = idx

            st.write("Check in successful!")
            # wait 2 seconds
            #time.sleep(2)
            st.experimental_rerun()
            # redirect to UsersMain
            # nav_page("UsersMain")
    except Exception as e:
        st.error("Login failed. Username or password incorrect")


if logout_button: 
    # record checkout time

    # add shirt duration time AND amount taken into the respective tables
    if 'token' in st.session_state:
        del st.session_state.token
    else:
        st.error("Already logged out")

if 'token' in st.session_state:
    shift = json.loads(employeeConnectors.getMyActiveShift())["shift"]
    if len(shift) == 0:
        sign_in_for_shift = st.button("Start Shift")
        if sign_in_for_shift:
            startTime = datetime.now()
            r = json.loads(shiftConnector.postShift(int(st.session_state.idx), startTime.isoformat()))["shift"]
            st.session_state["shift_active"] = r["id"]
            st.experimental_rerun()

    else:
        st.session_state["shift_active"] = shift[0]["id"]
        food_input = st.number_input("Enter lbs of regular food taken", min_value=0.0, format="%.2f")
        damaged_food_input = st.number_input("Enter lbs of damaged food taken", min_value=0.0, format="%.2f")
        foodAmt = food_input
        sign_out_for_shift = st.button("End Shift (Optional)")
        if sign_out_for_shift:
            if "shift_active" in st.session_state:
                endTime = datetime.now()
                st.write('Thank you')
                time.sleep(2)
                current_user_id = user_input
                #shift_id = row["id"]
                print('calling shift connector')
                r = shiftConnector.signout(foodAmt, int(st.session_state.shift_active), damaged_food_input)
                st.write("Sign out successful!")
                # wait 2 seconds
                del st.session_state.token
                del st.session_state.shift_active
                if "idx" in st.session_state:
                    del st.session_state.idx
                st.experimental_rerun()
            else:
                st.error("Not currently logged in")

            
