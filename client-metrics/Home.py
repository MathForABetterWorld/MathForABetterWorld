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
from routeConnectors import exportConnectors, pallet

http = urllib3.PoolManager()
BASEURL = "http://????/api"
import time
import json
from collections import defaultdict
from routeConnectors import pallet, exportConnectors, locationConnectors


path = os.path.dirname(__file__)
st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Bmore Food")
image = Image.open(path + '/assets/bmore_food_logo_dark_theme.png')

### Header ###
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(image)
with col3:
    st.write(' ')

pallets = json.loads(pallet.getFood())
imports = pd.DataFrame(pallets["Pallet"])
total_imports = imports["weight"].sum()
imports

exports = json.loads(exportConnectors.getExports())
exports = pd.DataFrame(exports["exports"])
total_exports = exports["weight"].sum()
exports

formatted_total_imports = "{:,.2f}".format(total_imports)
formatted_total_exports = "{:,.2f}".format(total_exports)

 
st.markdown("# TOTAL IMPORTS: " + formatted_total_imports + " lbs!")
st.markdown("# TOTAL EXPORTS: " + formatted_total_exports + " lbs!")

# Main Dashboard View
col1,col2,col3 = st.columns([0.02,0.96,0.02])

with col1:
    st.write('')

with col2:
    # Start the image slideshow automatically
    image_folder_path = os.path.join(path, 'assets', 'slideshow_images')
    # Get a list of image files in the specified folder
    image_files = [f for f in os.listdir(image_folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    # Set the delay (in seconds) between images
    delay_between_images = 6  # Adjust as needed
    default_caption = ""

    # Initialize the index to track the current image
    current_image_index = 0
    # Run the slideshow
    while True:
        image_file = image_files[current_image_index]
        image_path = os.path.join(image_folder_path, image_file)
        image = Image.open(image_path)
        placeholder = st.image(image, caption=default_caption, use_column_width=True)
        # Add a delay between images
        time.sleep(delay_between_images)
        # Clear the previous image
        placeholder.empty()
        # Increment the current image index and loop back to the first image if necessary
        current_image_index = (current_image_index + 1) % len(image_files)

with col3:
    st.write('')
