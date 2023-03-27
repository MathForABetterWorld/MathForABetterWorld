# import pdfkit
import streamlit as st
import datetime
import numpy as np
from PIL import Image
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import pandas as pd
import random as random
from matplotlib import pyplot as plt, dates as mdates
import urllib3
from visualizations import tempImportVis, tempVolunteerVis
http = urllib3.PoolManager() # define http 
BASEURL = "http://????/api"


path = os.path.dirname(__file__)
st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo.png", page_title="Bmore Food")

image = Image.open(path + '/assets/bmore_food_logo.png')

def changeState(num):
    st.session_state.pageID = num

### defs for different screen visualizations
def mainDashboardVis():
    last_rows = np.random.randn(1, 1)
    # chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        last_rows = new_rows

    col1, col2 = st.columns(2)

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Imports/Exports")
    col2.write("Volunteers")
    tempImportVis(col1)
    tempVolunteerVis(col2)

    impButton = col1.button("See More", key="import", on_click=changeState, args=(1, ))
    volunteerButton = col2.button("See More", key="volunteer", on_click=changeState, args=(2, ))

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Clients")
    col2.write("Distributors")
    col2.line_chart(last_rows)
    col1.line_chart(last_rows)

    clientButton = col1.button("See More", key="client", on_click=changeState, args=(3, ))
    distButton = col2.button("See More", key="distributor", on_click=changeState, args=(4, ))


def importVis():
    ## TODO
    st.write("hi")

def volunteerVis():
    ## TODO
    st.write("hi")

def clientVis():
    ## TODO
    st.write("hi")

def distributorVis():
    ## TODO
    st.write("hi")




# streamlit runs from top to bottom on every iteraction
# use pageID variable to track current page
# 0 = main dashboard ; 1 = imports/exports ; 2 = voluneers ; 3 = clients ; 4 = distributors
if 'pageID' not in st.session_state:
	st.session_state.pageID = 0



### Header ###
col1, col2, col3 = st.columns(3)
with col1:
    st.write(st.session_state.pageID)

with col2:
    st.image(image)

with col3:
    st.write(' ')

pg = st.session_state.pageID
if pg == 0:
    mainDashboardVis()
elif pg == 1:
    importVis()
elif pg == 2:
    volunteerVis()
elif pg == 3:
    clientVis()
elif pg == 4:
    distributorVis()




# TODO: month by month progress / month this year vs same month last yr 

