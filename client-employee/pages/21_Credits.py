import streamlit as st
from PIL import Image
import os

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Bmore Food Volunteer Portal")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')
st.image(image)

st.write("This dashboard was made in Spring 2023 by students of the class Math for a Better World in the Johns Hopkins University department of Applied Mathematics & Statistics.")
st.write()
st.write("Students: Chris Anto, Tim Chau, Jillayne Clarke, Matt Kleiman, Nolan Lombardo, Sofia LoVuolo, Gavin McElhennon, Nader Najjar, Joy Neuberger, Emi Ochoa, Krutal Patel, Kiana Soleiman, Jamie Stelnik, Sophia Stone, Kenny Testa, Isabel Thomas, Rishika Vadlamudi, Chris Wilhelm")
st.write()
st.write("Taught by JC Faulk and Fadil Santosa, with teaching assistant Kaleigh Rudge.")