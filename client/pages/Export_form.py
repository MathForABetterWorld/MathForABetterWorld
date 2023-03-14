# import pdfkit
import streamlit as st
import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

st.set_page_config(layout="centered", page_icon="./assets/bmore_food_logo.png", page_title="Export Form")

title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    with col1:
        st.image('./assets/bmore_food_logo.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Food export form</h1>", unsafe_allow_html=True)


env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())

with st.form("template_form"):
    left, right = st.columns(2)
    donatedTo = left.text_input("Who is the food going to?", value="")
    category = left.selectbox("Category", ["Dairy", "Produce"])
    weight = right.text_input("Weight", value="")

    submit = st.form_submit_button()

if submit:
    st.balloons()
    st.success("🎉 Export recorded!")
