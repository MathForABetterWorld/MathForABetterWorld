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
from image_slideshow import image_slideshow  # Import the image_slideshow function from the component script
import time
import json
from collections import defaultdict
from routeConnectors import pallet, exportConnectors, locationConnectors


path = os.path.dirname(__file__)
st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Bmore Food")
image = Image.open(path + '/assets/bmore_food_logo_dark_theme.png')

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
    st.write(' ')
with col2:
    st.image(image)
with col3:
    st.write(' ')


## display current dashboard view ##
pg = st.session_state.pageID
if pg == 0:
    #mainDashboardVis()

    # Main Dashboard View
    col1,col2,col3 = st.columns([0.02,0.96,0.02])
    
    with col1:
        st.write('')

    with col2:
        # Start the image slideshow automatically
        # Define the path to the folder containing your images
        image_folder_path = "assets/slideshow_images"  # Change this to the path of your image folder
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
    
elif pg == 1:

    # exports viz 

    
    #importVis()
    pallets = json.loads(pallet.getFood())
    exportItems = json.loads(exportConnectors.getExports())
    Exports = pd.DataFrame(exportItems["exports"])
    #Imports = pd.read_json(pallets["Pallet"])#pd.read_csv('Imports.csv')
    Imports = pd.DataFrame(pallets["Pallet"])
    pallet_weights = Exports["weight"].dropna().values.tolist()
    cum_weights = []
    for num_str in pallet_weights:
        #num_str = num_str.replace(",","")
        #if num_str.isnumeric():
        num = abs(int(num_str))
        prev = 0 if len(cum_weights) == 0 else cum_weights[-1]
        cum_weights.append(num + prev)

    food_provider = Imports["companyId"].dropna().tolist()
    food_provider = set(food_provider)
    food_provider = defaultdict(float)
    food_receiver = defaultdict(float)

    for index, row in Imports.iterrows():
        food_provider[row['company']["name"]] += row['weight']
    for index, row in Exports.iterrows():
        food_receiver[row['category']["name"]] += np.absolute(row['weight'])

    #print(food_provider)

    provider_labels = []
    provider_sizes = []

    sorted_provider_labels = []
    sorted_provider_sizes = []

    receiver_labels = []
    receiver_sizes = []

    sorted_receiver_labels = []
    sorted_receiver_sizes = []

    for x,y in food_provider.items():
        provider_labels.append(x)
        provider_sizes.append(y)

    for x,y in food_receiver.items():
        receiver_labels.append(x)
        receiver_sizes.append(y)


    sorted_food_provider = sorted(food_provider.items(), key=lambda x:x[1])
    sorted_food_receiver = sorted(food_receiver.items(), key=lambda x:x[1])


    for x,y in dict(sorted_food_provider[-10:]).items():
        sorted_provider_labels.append(x)
        sorted_provider_sizes.append(y)

    for x,y in dict(sorted_food_receiver[-10:]).items():
        sorted_receiver_labels.append(x)
        sorted_receiver_sizes.append(y)

    sorted_other_labels = []
    sorted_other_providers = []

    sorted_other_rec_labels = []
    sorted_other_receivers = []

    for x,y in dict(sorted_food_provider[:-10]).items():
        sorted_other_labels.append(x)
        sorted_other_providers.append(y)

    other_total = sum(sorted_other_providers)

    #print(other_total)
    sorted_provider_sizes.append(other_total)
    sorted_provider_labels.append("other")

    for x,y in dict(sorted_food_receiver[:-10]).items():
        sorted_other_rec_labels.append(x)
        sorted_other_receivers.append(y)

    other_rec_total = sum(sorted_other_receivers)

    sorted_receiver_sizes.append(other_rec_total)
    sorted_receiver_labels.append("other")

    ImpTot= sum(sorted_provider_sizes)
    percTot = []
    for size in sorted_provider_sizes:
        perc = size/ImpTot*100
        percTot.append(perc)

    ItemExpTot= sum(sorted_receiver_sizes)
    receiverPercTot = []
    for size in sorted_receiver_sizes:
        receiverPerc = size/ItemExpTot*100
        receiverPercTot.append(receiverPerc)

    for i in range(len(sorted_provider_labels)):
        sorted_provider_labels[i] = f'{sorted_provider_labels[i]}: {(float(percTot[i])):.1f}%'

    for i in range(len(sorted_receiver_labels)):
        sorted_receiver_labels[i] = f'{sorted_receiver_labels[i]}: {(float(receiverPercTot[i])):.1f}%'

    fig1, ax = plt.subplots()
    ax.pie(sorted_provider_sizes, labels=sorted_provider_labels)
    #plt.legend(provider_labels[-5:], bbox_to_anchor=(0,-2.7), loc="lower right")
    Imports_df = pd.DataFrame(list(zip(sorted_provider_sizes, sorted_provider_labels)),
                columns =['Provider Imports', 'Provider'])

    Exports_df = pd.DataFrame(list(zip(sorted_receiver_sizes, sorted_receiver_labels)),
                columns =['Quantity (lbs)', 'Item'])

    fig2, ax = plt.subplots()
    ax.pie(receiver_sizes, labels=receiver_labels)
    plt.legend(receiver_labels, bbox_to_anchor=(0,-2.7), loc="lower right")

    st.line_chart(cum_weights)



elif pg == 2:
    pass

elif pg == 3:
    clientVis()

    
elif pg == 4:
    distributorVis()





