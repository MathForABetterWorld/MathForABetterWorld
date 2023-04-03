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
from visualizations import *

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
    col1, col2 = st.columns(2)

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Graph 1")
    col2.write("Graph 2")
    importGraph1(col1)
    importGraph2(col2)

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Graph 3")
    col2.write("Graph 4")
    importGraph3(col1)
    importGraph4(col2)

    back = col1.button("Back", key="bck", on_click=changeState, args=(0, ))

def volunteerVis():
    col1, col2 = st.columns(2)

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Graph 1")
    col2.write("Graph 2")
    volunteerGraph1(col1)
    volunteerGraph2(col2)

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Graph 3")
    col2.write("Graph 4")
    volunteerGraph3(col1)
    volunteerGraph4(col2)

    back = col1.button("Back", key="bck", on_click=changeState, args=(0, ))

def clientVis():
    col1, col2 = st.columns(2)

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Graph 1")
    col2.write("Graph 2")
    clientGraph1(col1)
    clientGraph2(col2)

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Graph 3")
    col2.write("Graph 4")
    clientGraph3(col1)
    clientGraph4(col2)

    back = col1.button("Back", key="bck", on_click=changeState, args=(0, ))

def distributorVis():
    col1, col2 = st.columns(2)

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Graph 1")
    col2.write("Graph 2")
    distributorGraph1(col1)
    distributorGraph2(col2)

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Graph 3")
    col2.write("Graph 4")
    distributorGraph3(col1)
    distributorGraph4(col2)

    back = col1.button("Back", key="bck", on_click=changeState, args=(0, ))