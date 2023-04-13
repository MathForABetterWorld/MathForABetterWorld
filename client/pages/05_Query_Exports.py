
import streamlit as st
import numpy as np
import pandas as pd
import json
import os 
from routeConnectors import categoryConnectors, exportConnectors, locationConnectors

path = os.path.dirname(__file__)


# This has to be the first streamlit command called
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Query exports")

title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    with col1:
        st.image(path + '/../assets/bmore_food_logo_dark_theme.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Query exports</h1>", unsafe_allow_html=True)

# Opening JSON file
catFile = open(path + '/../assets/fakeCategories.json')
sortFile = open(path + '/../assets/sortBy.json')
recFile = open(path + '/../assets/recipients.json')
  
# load categories and sortBy mapc
print("getting categories....")
allCategories = [{"id": -1, "name": "", "description":""}] 
catRes = categoryConnectors.getCategories()
if catRes: 
    allCategories = allCategories + catRes["category"]
sortByMap = json.load(sortFile)["sortBy"]
recList = json.load(recFile)["recipients"]
locationsList = [{"id": -1, "name": ""}]
locationRes = locationConnectors.getLocations()
if locationRes:
    locationsList = locationsList + locationRes["location"]

categorySelect = st.selectbox("Show all food of type", allCategories, format_func=lambda cat: f'{cat["name"]}')
locSelect = st.selectbox("Show all food going to", locationsList, format_func=lambda loc: f'{loc["name"]}')
sortBySelect = st.selectbox("Sort food imports by", sortByMap)

df = pd.DataFrame(json.loads(exportConnectors.getExports().decode('utf-8'))["exports"])
categoryDF = pd.DataFrame(allCategories)
def getCategories(category):
    return categoryDF.loc[categoryDF.id == category["id"], "name"].values[0]

def getLocation(location):
    if location is None:
        return "N/A"
    return location["name"]

df["category"] = df.category.apply(getCategories)
df["location"] = df.location.apply(getLocation)
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

if locSelect['id'] != -1:
    locIndices = []
    for index, row in df.iterrows():
        if locSelect['name'] == row["location"]:
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