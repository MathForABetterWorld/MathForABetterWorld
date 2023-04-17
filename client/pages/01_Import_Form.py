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

path = os.path.dirname(__file__)
print(path + "/../assets/bmore_food_logo_dark_theme.png" )
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Import Form")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')
st.image(image)
# Get rack, distributor and category info 
print("getting racks....")
allRacks = [1, 2, 3, 4, 5, 6]
rackRes = rackConnector.getRacks()
if rackRes: 
    allRacks = allRacks + rackRes["rack"]

print("getting distributors....")
allDistributors = [{"id": -1, "name": ""}]
distRes = distributorConnectors.getDistributors()
if distRes: 
    allDistributors = allDistributors + distRes["distributors"]

print("getting categories....")
allCategories = [{"id": -1, "name": "", "description":""}] 
catRes = categoryConnectors.getCategories()
if catRes: 
    allCategories = allCategories + catRes["category"]


allUsers = [{"id": -1, "name": ""}]
dbUsers = json.loads(userConnector.getUsers().decode("utf-8"))
if dbUsers:
    allUsers = allUsers + dbUsers["users"]
# print("all cats", allCategories)

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
    expiration_date = left.date_input("Expiration date", value=datetime.date(2023, 1, 1))
    distributor_name = left.selectbox("Distributor name", allDistributors, format_func=lambda dist: f'{dist["name"]}')
    rack = right.selectbox("Rack", allRacks) # get more info on how racks are stored in the google form 
    pallet_weight = left.text_input("Weight", value="1000")
    category = right.selectbox("Category", allCategories, format_func=lambda cat: f'{cat["name"]}')
    inputUser = right.selectbox("User", allUsers, format_func=lambda user: f'{user["name"]}' )
    description = st.text_input("Description", value="")
    submit = st.form_submit_button()

if submit:
    st.balloons()
    st.write(type(expiration_date))

    ### TODO:: update userID when sign in functionality is implemented
    pallet.postFood(
        "userID",
        todaysDate, 
        expiration_date, 
        pallet_weight, 
        distributor_name,
        rack,
        True,
        (description if description != "" else category["description"]),
        category)

    st.success("🎉 Your import was generated!")
