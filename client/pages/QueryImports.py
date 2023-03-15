
import streamlit as st
import numpy as np
import pandas as pd
import json
import os
from routeConnectors import pallet
from routeConnectors import distributorConnectors
from routeConnectors import rackConnector
from routeConnectors import categoryConnectors

path = os.path.dirname(__file__)
# This has to be the first streamlit command called
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo.png", page_title="Query imports")

# Get rack, distributor and category info 
print("getting racks....")
allRacks = [1, 2, 3, 4, 5, 6]
rackRes = rackConnector.getRacks()
if rackRes: 
    allRacks = allRacks + rackRes["rack"]

print("getting distributors....")
allDistributors = [{"id": -1, "name": ""}]
distRes = distributorConnectors.getDistributors()
if distRes: 
    allDistributors = allDistributors + distRes["distributors"]

print("getting categories....")
allCategories = [{"id": -1, "name": "", "description":""}] 
catRes = categoryConnectors.getCategories()
if catRes: 
    allCategories = allCategories + catRes["category"]
# print("all cats", allCategories)

title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    with col1:
        st.image(path + '/../assets/bmore_food_logo.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Query imports</h1>", unsafe_allow_html=True)

# Opening JSON file
sortFile = open(path + '/../assets/sortBy.json')
  
# load sortBy map 
sortByMap = json.load(sortFile)["sortBy"]


categorySelect = st.selectbox("Show all food of type", allCategories, format_func=lambda cat: f'{cat["name"]}')
#categorySelect = st.selectbox("Show all food currently on rack", allRacks)
distributorSelect = st.selectbox("Show all food coming from", allDistributors, format_func=lambda dist: f'{dist["name"]}')
sortBySelect = st.selectbox("Sort food imports by", sortByMap)


allPallets = pallet.getFood()["Pallet"]
#print("allPallets: ", allPallets[:10])
df = pd.DataFrame.from_dict(allPallets)

# # Uncomment this when connected to backend 
# # # Filter by distributor 
if distributorSelect["name"] != "":
    indices = []
    for index, row in df.iterrows():
        if distributorSelect["name"] == row["company"]["name"]:
            indices.append(index)
    df = df.iloc[indices] #this maybe should sort by distributor ID 
# # # Filter by selected category
if categorySelect['id'] != -1:
    indices = []
    for index, row in df.iterrows():
        if categorySelect['id'] in row["categoryIds"]:
            indices.append(index)
    df = df.iloc[indices]

if sortByMap[sortBySelect] != 'none':
    df = df.sort_values([sortByMap[sortBySelect]])

st.table(df)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
