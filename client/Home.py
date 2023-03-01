# import pdfkit
import streamlit as st
import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

import http.client

connection = http.client.HTTPConnection('www.python.org', 80, timeout=10)
print(connection)

st.set_page_config(layout="centered", page_icon="🍏", page_title="Bmore Food")
st.title("🍏 Bmore Food")

st.write(
    "Food import form!"
)


env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
# template = env.get_template("invoice_template.html")

with st.form("template_form"):
    left, right = st.columns(2)
    expiration_date = left.date_input("Expiration date", value=datetime.date(2023, 1, 1))
    distributer_name = left.selectbox("Distributor name", ["Dole", "Amazon", ""])
    rack = right.text_input("Rack", value="12") # get more info on how racks are stored in the google form 
    pallet_weight = left.text_input("Weight", value="1000")
    category = right.selectbox("Category", ["Dairy", "Produce"])
    description = st.text_input("Description", value="")
    submit = st.form_submit_button()

if submit:
    st.balloons()
    st.success("🎉 Your invoice was generated!")
