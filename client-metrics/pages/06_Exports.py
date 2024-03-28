
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

st.title('Cumulative Sum - Exports over Time')


exportItems = json.loads(exportConnectors.getExports())
Exports = pd.DataFrame(exportItems["exports"])
Exports['exportDate'] = pd.to_datetime(Exports['exportDate'])
result_df = Exports.groupby('exportDate')['weight'].sum().reset_index()

result_df['cumulative_sum'] = result_df['weight'].cumsum()

result_df['exportDate'] = pd.to_datetime(result_df['exportDate'])

result_df['exportDate'] = result_df['exportDate'].dt.date

dates = result_df['exportDate'].to_list()
cumulative_exports_weight = result_df['cumulative_sum'].to_list()

fig, ax = plt.subplots()

ax.plot(result_df['exportDate'], result_df['cumulative_sum'], label='Cumulative Sum of Exports (lb)')

plt.xlabel('Date')
plt.ylabel('Cumulative Sum of Exports (lb)')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()

st.pyplot(fig)

export_items = json.loads(exportConnectors.getExports())
Exports = pd.DataFrame(export_items["exports"])

grouped_df = Exports.groupby('donatedTo')['weight'].sum().reset_index()
grouped_df['donatedTo'] = grouped_df['donatedTo'].str.strip('"')
grouped_df = grouped_df[(grouped_df['weight'] >= 0.02 * grouped_df['weight'].sum())]

st.title('Distribution of Weights by Recipient')

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(grouped_df['weight'], labels=grouped_df['donatedTo'], autopct='%1.1f%%', startangle=140, counterclock=False)
ax.axis('equal')

st.pyplot(fig)

exportItems = json.loads(exportConnectors.getExports())
Exports = pd.DataFrame(exportItems["exports"])

pallet_weights = Exports["weight"].dropna().values.tolist()
cum_weights = []
for num_str in pallet_weights:
    #num_str = num_str.replace(",","")
    #if num_str.isnumeric():
    num = abs(int(num_str))
    prev = 0 if len(cum_weights) == 0 else cum_weights[-1]
    cum_weights.append(num + prev)

food_receiver = defaultdict(float)

for index, row in Exports.iterrows():
    food_receiver[row['category']["name"]] += np.absolute(row['weight'])

#print(food_provider)


receiver_labels = []
receiver_sizes = []

sorted_receiver_labels = []
sorted_receiver_sizes = []

for x,y in food_receiver.items():
    receiver_labels.append(x)
    receiver_sizes.append(y)

sorted_food_receiver = sorted(food_receiver.items(), key=lambda x:x[1])

for x,y in dict(sorted_food_receiver[-10:]).items():
    sorted_receiver_labels.append(x)
    sorted_receiver_sizes.append(y)

sorted_other_rec_labels = []
sorted_other_receivers = []

for x,y in dict(sorted_food_receiver[:-10]).items():
    sorted_other_rec_labels.append(x)
    sorted_other_receivers.append(y)

other_rec_total = sum(sorted_other_receivers)

sorted_receiver_sizes.append(other_rec_total)
sorted_receiver_labels.append("other")

ItemExpTot= sum(sorted_receiver_sizes)
receiverPercTot = []
for size in sorted_receiver_sizes:
    receiverPerc = size/ItemExpTot*100
    receiverPercTot.append(receiverPerc)

for i in range(len(sorted_receiver_labels)):
    sorted_receiver_labels[i] = f'{sorted_receiver_labels[i]}: {(float(receiverPercTot[i])):.1f}%'

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(sorted_receiver_sizes, labels=sorted_receiver_labels)
st.title('Distribution of Items (Type) Exported')

# Capture the Matplotlib figure
pie_chart = fig

Exports_df = pd.DataFrame(list(zip(sorted_receiver_sizes, sorted_receiver_labels)),
                            columns=['Quantity (lbs)', 'Item'])

# Display the pie chart in Streamlit
st.pyplot(pie_chart)

