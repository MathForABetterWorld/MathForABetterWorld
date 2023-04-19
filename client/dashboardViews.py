## defs for different dashboard views
## function definitions for graphs/visualizations are in visualizations.py

import streamlit as st
import datetime
import numpy as np
from PIL import Image
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import json
import pandas as pd
import random as random

from visualizations import *

from collections import defaultdict

from data import imports, exports
import seaborn as sb
from routeConnectors import pallet, exportConnectors


def changeState(num):
    st.session_state.pageID = num

def mainDashboardVis():
    col1, col2 = st.columns(2)

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Imports/Exports")
    col2.write("Volunteers")
    importGraph1(col1)
    volunteerGraph1(col2)


    impButton = col1.button("See More", key="import", on_click=changeState, args=(1, ))
    volunteerButton = col2.button("See More", key="volunteer", on_click=changeState, args=(2, ))

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Clients")
    col2.write("Distributors")
    clientGraph1(col1)
    distributorGraph1(col2)

    clientButton = col1.button("See More", key="client", on_click=changeState, args=(3, ))
    distButton = col2.button("See More", key="distributor", on_click=changeState, args=(4, ))


def importVis():
    tab1, tab2, tab3, tab4 = st.tabs(["Daily Food Imports", "Total Cumulative Imports", "Provider Imports", "Item Exports"])
    with tab1:
        importGraph1(tab1)
    with tab2:
        importGraph2(tab2)
    with tab3:
        importGraph3(tab3)
    with tab4:
        importGraph4(tab4)
    col1, col2 = st.columns(2)

    col1, col2 = st.columns(2)
    back = col1.button("Back", key="bck", on_click=changeState, args=(0, ))


    #back = col1.button("Back", key="bck", on_click=changeState, args=(0,))

    # col1.button("Back", key="bck", on_click=changeState, args=(0, ))

def volunteerVis():
    tab1, tab2, tab3 = st.tabs(["Last 7 Days", "Last 12 Months", "G3"])
    with tab1:
        volunteerGraph1(tab1)
    with tab2:
        volunteerGraph2(tab2)
    with tab3:
        volunteerGraph3(tab3)

    col1, col2 = st.columns(2)

    back = col1.button("Back", key="bck", on_click=changeState, args=(0, ))

def clientVis():
    tab1, tab2, tab3 = st.tabs(["G1", "G2", "G3"])
    with tab1:
        clientGraph1(tab1)
    with tab2:
        clientGraph2(tab2)
    with tab3:
        clientGraph3(tab3)

    col1, col2 = st.columns(2)

    back = col1.button("Back", key="bck", on_click=changeState, args=(0, ))

def distributorVis():
    tab1, tab2, tab3 = st.tabs(["G1", "G2", "G3"])
    with tab1:
        distributorGraph1(tab1)
    with tab2:
        distributorGraph2(tab2)
    with tab3:
        distributorGraph3(tab3)

    col1, col2 = st.columns(2)

    back = col1.button("Back", key="bck", on_click=changeState, args=(0, ))