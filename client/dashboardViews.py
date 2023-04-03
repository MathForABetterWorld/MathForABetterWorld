## defs for different dashboard views
## function definitions for graphs/visualizations are in visualizations.py

import streamlit as st
import datetime
import numpy as np
from PIL import Image
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import pandas as pd
import random as random
from matplotlib import pyplot as plt, dates as mdates
from visualizations import tempImportVis, tempVolunteerVis

def changeState(num):
    st.session_state.pageID = num

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
    col1, col2 = st.columns(2)
    
    col1.markdown("##")
    col2.markdown("##")

def volunteerVis():
    ## TODO
    st.write("hi")

def clientVis():
    ## TODO
    st.write("hi")

def distributorVis():
    ## TODO
    st.write("hi")