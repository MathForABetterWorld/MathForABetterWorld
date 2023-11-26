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
import json
from routeConnectors import pallet, exportConnectors, locationConnectors
from matplotlib import pyplot as plt, dates as mdates
from routeConnectors import pallet
from collections import defaultdict
from dashboardViews import mainDashboardVis, importVis, volunteerVis, clientVis, distributorVis

# Get the directory of the current script
script_path = os.path.dirname(__file__)
assets_path = os.path.join(script_path, '..', 'assets')
image_path = os.path.join(assets_path, 'bmore_food_logo_dark_theme.png')

# Set page configuration with the image
st.set_page_config(layout="centered", page_icon=image_path, page_title="Bmore Food")  
# Open the image using Pillow
image = Image.open(image_path)


### Header ###
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(image)
with col3:
    st.write(' ')



st.title('Cumulative Sum - Imports over Time')

pallets = json.loads(pallet.getFood())
Imports = pd.DataFrame(pallets["Pallet"])

result_df = Imports.groupby('inputDate')['weight'].sum().reset_index()

result_df['cumulative_sum'] = result_df['weight'].cumsum()

# Convert 'inputDate' to datetime format
result_df['inputDate'] = pd.to_datetime(result_df['inputDate'])

# Extract only the date part
result_df['inputDate'] = result_df['inputDate'].dt.date

dates = result_df['inputDate'].to_list()
cumulative_imports_weight = result_df['cumulative_sum'].to_list()
# Create Matplotlib plot
plt.xlabel('Date')
plt.ylabel('Cumulative Sum of Imports (lb)')
plt.xticks(rotation=45, ha='right')  # Adjust the rotation angle as needed
plt.plot(dates, cumulative_imports_weight)
plt.xticks(dates[::20], rotation=45, ha='right')
# Capture the Matplotlib figure
fig = plt.gcf()
# Display the plot in Streamlit
st.pyplot(fig)

Imports['company_name'] = Imports['company'].apply(lambda x: x['name'])
new_df = Imports.groupby('company_name')['weight'].sum().reset_index()
new_df = new_df[new_df['weight'] >= 0.02 * new_df['weight'].sum()]

# Streamlit app
st.title('Distribution of Import Weights by Company')

# Plotting a pie chart using Matplotlib in Streamlit
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(new_df['weight'], labels=new_df['company_name'], autopct='', startangle=140,
        counterclock=False)
ax.axis('equal')

# Show the plot in Streamlit
st.pyplot(fig)