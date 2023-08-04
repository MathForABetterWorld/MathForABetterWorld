
import streamlit as st
import numpy as np
import pandas as pd
import json
import os 
from routeConnectors import categoryConnectors, exportConnectors, locationConnectors, userConnector, rackConnector
from PIL import Image
from nav import nav_page


path = os.path.dirname(__file__)


# This has to be the first streamlit command called
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Query exports")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')
st.image(image)

# log in status

if 'token' in st.session_state :
    log_button = st.button("Employee Log-out", key=".my-button", use_container_width=True)
else:
    log_button = st.button("Employee Log-in", key=".my-button", use_container_width=True)


title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    # with col1:
    #     st.image(path + '/../assets/bmore_food_logo_dark_theme.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Query exports</h1>", unsafe_allow_html=True)

# Opening JSON file
catFile = open(path + '/../assets/fakeCategories.json')
sortFile = open(path + '/../assets/sortBy.json')
#recFile = open(path + '/../assets/recipients.json')
  

# load categories and sortBy map 
#categories = json.load(catFile)["categories"]
sortByMap = json.load(sortFile)["sortBy"]
#recList = json.load(recFile)["recipients"]

locations = [{"id": -1, "name": "", "longitude":"", "latitude": ""}]  + locationConnectors.getLocations()['location']
sortedLocations = sorted(locations, key=lambda location: location["name"])

categories = [{"id": -1, "name": "", "description": ""}]  + categoryConnectors.getCategories()['category']
sortedCategories = sorted(categories, key=lambda cat: cat["name"])

# allRacks = ["", 1, 2, 3, 4, 5, 6]
# rackRes = rackConnector.getRacks()
# if rackRes: 
#     allRacks = allRacks + rackRes["rack"]

racks = [{"id": -1, "location": "", "description": "", "weightLimit": ""}]  + rackConnector.getRacks()['rack']
sortedRacks = sorted(racks, key=lambda rack: rack["location"])

categorySelect = st.selectbox("Show all food of type", categories, format_func=lambda cat: f'{cat["name"]}')
recSelect = st.selectbox("Show all food going to", sortedLocations, format_func=lambda loc: f'{loc["name"]}')

sortBySelect = st.selectbox("Sort food imports by", sortByMap)

df = pd.DataFrame(json.loads(exportConnectors.getExports().decode('utf-8'))["exports"])
categoryDF = pd.DataFrame(categories)
def getCategories(category):
    return categoryDF.loc[categoryDF.id == category["id"], "name"].values[0]

def getLocation(location):
    if location is None:
        return "N/A"
    return location["name"]

def getRack(rack):
    if rack is None:
        return "N/A"
    return rack["location"]

df["category"] = df.category.apply(getCategories)
df["location"] = df.location.apply(getLocation)
df["rack"] = df.rack.apply(getRack)
# # Uncomment this when connected to backend 
# df = df.sort_values(by=[sortByMap[sortBySelect]])
# # Filter by distributor 
# df = df[df['distributor'] == distributorSelect] #this maybe should sort by distributor ID 
# # Filter by selected category
# df = df[df['category'] == categorySelect] 

if categorySelect['id'] != -1:
    categoryIndices = []
    for index, row in df.iterrows():
        if categorySelect['name'] == row["category"]:
            categoryIndices.append(index)
    df = df.iloc[categoryIndices]
    df = df.reset_index()

if recSelect['id'] != -1:
    locIndices = []
    for index, row in df.iterrows():
        if recSelect['name'] == row["location"]:
            locIndices.append(index)
    df = df.iloc[locIndices]
    df = df.reset_index()

st.dataframe(df)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")

### TODO: Add totals / summary to bottom of table to see how much 
# food one person / place has taken
# Filter by time -- how much we've exported in the past month vs year
# 
###


if log_button :
    if "token" in st.session_state :
        del st.session_state.token
        st.experimental_rerun()
    else:
        nav_page("")