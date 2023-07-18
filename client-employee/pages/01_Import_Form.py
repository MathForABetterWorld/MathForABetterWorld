# import pdfkit
import streamlit as st
import datetime
from PIL import Image
from jinja2 import Environment, FileSystemLoader, select_autoescape
from routeConnectors import pallet
from routeConnectors import distributorConnectors
from routeConnectors import rackConnector
from routeConnectors import categoryConnectors
from routeConnectors import userConnector
import json
import os
from nav import nav_page

path = os.path.dirname(__file__)
print(path + "/../assets/bmore_food_logo_dark_theme.png" )
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Import Form")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')
st.image(image)

# log in status

if 'token' in st.session_state :
    log_button = st.button("Employee Log-out", key=".my-button", use_container_width=True)
else:
    log_button = st.button("Employee Log-in", key=".my-button", use_container_width=True)

# Get rack, distributor and category info 
print("getting racks....")
allRacks = [{"id": -1, "location": "", "description": "", "weightLimit": 0}]
rackRes = rackConnector.getRacks()
if rackRes: 
    allRacks = allRacks + rackRes["rack"]

distributors = [{"id": -1, "name": "", "description": ""}]  + distributorConnectors.getDistributors()['distributors']
allDistributors = sorted(distributors, key=lambda cat: cat["name"])

categories = [{"id": -1, "name": "", "description": ""}]  + categoryConnectors.getCategories()['category']
allCategories = sorted(categories, key=lambda cat: cat["name"])


allUsers = [{"id": -1, "name": ""}]
dbUsers = json.loads(userConnector.getUsers().decode("utf-8"))
if dbUsers:
    allUsers = allUsers + dbUsers["users"]


title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    # with col1:
    #     st.image(image, width=200)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Food import form</h1>", unsafe_allow_html=True)


env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
# template = env.get_template("invoice_template.html")

todaysDate = datetime.date.today()
with st.form("template_form"):
    left, right = st.columns(2)
    expiration_date = left.date_input("Expiration date", value=datetime.date(1970, 1, 1))
    category = right.selectbox("Category", allCategories, format_func=lambda cat: f'{cat["name"]}')
    rack = left.selectbox("Rack", allRacks, format_func=lambda rack: f'{rack["location"]}') # get more info on how racks are stored in the google form 
    distributor= right.selectbox("Distributor name", allDistributors, format_func=lambda dis: f'{dis["name"]}')
    pallet_weight = left.text_input("Weight", value="1000")
    inputUser = right.selectbox("User", allUsers, format_func=lambda user: f'{user["name"]}' )
    description = st.text_input("Description (OPTIONAL)", value="")
    submit = st.form_submit_button()

if submit:
    ### TODO:: update userID when sign in functionality is implemented
    r = json.loads(pallet.postFood(
        inputUser["id"],
        todaysDate, 
        expiration_date, 
        pallet_weight, 
        distributor['id'],
        rack["id"],
        (description if description != "" else category["description"]),
        category['id']
       ))

  
    if "msg" not in r:
        st.balloons()
        st.success("🎉 Your import was generated!")
    else:
        st.error(r["msg"])

if log_button :
    if "token" in st.session_state :
        del st.session_state.token
        st.experimental_rerun()
    else:
        nav_page("")