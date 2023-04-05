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
st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo.png", page_title="Bmore Food")

image = Image.open(path + '/assets/bmore_food_logo.png')


## function definitions for visualizations are in visualizations.py
## function definitions for different dashboard views are in dashboardViews.py

# streamlit runs from top to bottom on every iteraction
# use pageID variable to track current page
# 0 = main dashboard ; 1 = imports/exports ; 2 = voluneers ; 3 = clients ; 4 = distributors



# default page
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
