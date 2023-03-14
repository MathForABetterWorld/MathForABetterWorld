# import pdfkit
import streamlit as st
import datetime
from PIL import Image
from jinja2 import Environment, FileSystemLoader, select_autoescape
from routeConnectors import pallet
import os

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon="./assets/bmore_food_logo.png", page_title="Import Form")
image = Image.open('./assets/bmore_food_logo.png')


title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    with col1:
        st.image('./assets/bmore_food_logo.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Food import form</h1>", unsafe_allow_html=True)


env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
# template = env.get_template("invoice_template.html")

todaysDate = datetime.date.today()
with st.form("template_form"):
    left, right = st.columns(2)
    expiration_date = left.date_input("Expiration date", value=datetime.date(2023, 1, 1))
    distributor_name = left.selectbox("Distributor name", ["Dole", "Amazon", ""])
    rack = right.text_input("Rack", value="12") # get more info on how racks are stored in the google form 
    pallet_weight = left.text_input("Weight", value="1000")
    category = right.selectbox("Category", ["Dairy", "Produce"])
    description = st.text_input("Description", value="")
    submit = st.form_submit_button()

if submit:
    st.balloons()
    st.write(expiration_date)

    ### TODO:: update userID when sign in functionality is implemented
    pallet.postFood(
        "userID",
        todaysDate, 
        expiration_date, 
        pallet_weight, 
        distributor_name,
        rack,
        True,
        description,
        category)

    
    st.success("🎉 Your import was generated!")
