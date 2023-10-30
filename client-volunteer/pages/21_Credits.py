import streamlit as st
from PIL import Image
import os

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Credits")
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
        st.markdown("<h1 style='text-align: center; '>Credits</h1>", unsafe_allow_html=True)

st.write("This dashboard was made in Spring 2023 by students of the class Math for a Better World in the Johns Hopkins University department of Applied Mathematics & Statistics.")
st.write()
st.write("Students: Chris Anto, Tim Chau, Jillayne Clarke, Matt Kleiman, Nolan Lombardo, Sofia LoVuolo, Gavin McElhennon, Nader Najjar, Joy Neuberger, Emi Ochoa, Krutal Patel, Kiana Soleiman, Jamie Stelnik, Sophia Stone, Kenny Testa, Isabel Thomas, Rishika Vadlamudi, Chris Wilhelm")
st.write()
st.write("Taught by JC Faulk and Fadil Santosa, with teaching assistant Kaleigh Rudge.")