# import pdfkit
import streamlit as st
import datetime
import numpy as np
from PIL import Image
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import urllib3
http = urllib3.PoolManager() # define http 
BASEURL = "http://????/api"

path = os.path.dirname(__file__)
st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo.png", page_title="Bmore Food")

image = Image.open(path + '/assets/bmore_food_logo.png')
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(image)

with col3:
    st.write(' ')



def importLineGraph():
    last_rows = np.random.randn(1, 1)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        last_rows = new_rows

    return st.line_chart(last_rows)

def distributorsBarGraph(key):
    last_rows = np.random.randn(1, 1)
    # chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        last_rows = new_rows

    return st.bar_chart(last_rows)


last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    last_rows = new_rows

col1, col2 = st.columns(2)

col1.line_chart(last_rows)
col2.line_chart(last_rows)
col1.line_chart(last_rows)
col2.line_chart(last_rows)

# TODO: month by month progress / month this year vs same month last yr 

