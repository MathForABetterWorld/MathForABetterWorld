# import pdfkit
import streamlit as st
import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

st.set_page_config(layout="centered", page_icon="🍏", page_title="Bmore Food")
st.title("🍏 Bmore Food")

st.write(
    "Food export form!"
)


env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())

# export schema 
#   id         Int      @id @default(autoincrement())
#   weight     Float    @default(0)
#   exportDate DateTime @default(now()) @db.Date
#   category   Category @relation(fields: [categoryId], references: [id])
#   categoryId Int
#   donatedTo  String
#   user       User     @relation(fields: [userId], references: [id])
#   userId     Int
with st.form("template_form"):
    # rackFrom = right.text_input("Which rack is the food from?", value="")
    # description = st.text_input("Description", value="")

    left, right = st.columns(2)
    donatedTo = left.text_input("Who is the food going to?", value="")
    category = left.selectbox("Category", ["Dairy", "Produce"])
    weight = right.text_input("Weight", value="")

    submit = st.form_submit_button()

if submit:
    st.balloons()
    st.success("🎉 Export recorded!")
