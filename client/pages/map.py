"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from routeConnectors import exportConnectors


st.title('Map Example')

lat = []
long = []
place_names= []
size = []


for i in range (20):
    lat.append(39.304150)
    long.append(-76.643036)
    place_names.append("Sandtown")


for i in range (40):
    lat.append(39.316390)
    long.append(-76.620630)
    place_names.append("BMORE Community Food")
    
for i in range (10):
    lat.append(39.311310)
    long.append(-76.612430)
    place_names.append("Greenmount West")

for i in range (5):
    lat.append(39.340460)
    long.append(-76.587720)
    place_names.append("Morgan State University")

    
df = pd.DataFrame({
    "lat": lat,
    "lon": long,
    "Location": place_names
    
})

# Create a Plotly scatter mapbox object with the center on Baltimore
fig = px.scatter_mapbox(lat=lat, lon=long, zoom=12, hover_name = place_names)
# Update the mapbox style
fig.update_layout(mapbox_style="open-street-map")
# Show the plot
fig.show()

