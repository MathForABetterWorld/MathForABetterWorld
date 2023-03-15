import streamlit as st


# on button click submit, check if valid user

# dropdown or text input for employee name
# text input for password
user_input = st.text_input("Name")
password_input = st.text_input("Password")
log_in_button = st.button("Log in")

if log_in_button:
    # check user_input and password_input match
    # go to employee page
    user_input