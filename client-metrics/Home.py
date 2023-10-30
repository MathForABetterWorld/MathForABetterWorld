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
from dashboardViews import mainDashboardVis, importVis, volunteerVis, clientVis, distributorVis
http = urllib3.PoolManager() # define http 
BASEURL = "http://????/api"

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Metrics Home")
image = Image.open(path + '/assets/bmore_food_logo_dark_theme.png')

### Header ###
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
        st.markdown("<h1 style='text-align: center; '>Metrics Home</h1>", unsafe_allow_html=True)

## function definitions for visualizations are in visualizations.py
## function definitions for different dashboard views are in dashboardViews.py

# streamlit runs from top to bottom on every iteraction
# use pageID variable to track current page
# 0 = main dashboard ; 1 = imports/exports ; 2 = voluneers ; 3 = clients ; 4 = distributors



# default page
if 'pageID' not in st.session_state:
	st.session_state.pageID = 0


## display current dashboard view ##
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





