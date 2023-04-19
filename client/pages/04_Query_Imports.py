
import streamlit as st
import numpy as np
import pandas as pd
import json
import os
from routeConnectors import pallet
from routeConnectors import distributorConnectors
from routeConnectors import rackConnector
from routeConnectors import categoryConnectors
from PIL import Image

path = os.path.dirname(__file__)
# This has to be the first streamlit command called
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo_dark_theme.png", page_title="Query imports")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')
st.image(image)
def getCompanyNames(company):
    return company["name"]

# Get rack, distributor and category info 
print("getting racks....")
allRacks = ["", 1, 2, 3, 4, 5, 6]
rackRes = rackConnector.getRacks()
if rackRes: 
    allRacks = allRacks + rackRes["rack"]


distributors = [{"id": -1, "name": "", "description": ""}]  + distributorConnectors.getDistributors()['distributors']
allDistributors = sorted(distributors, key=lambda cat: cat["name"])

categories = [{"id": -1, "name": "", "description": ""}]  + categoryConnectors.getCategories()['category']
sortedCategories = sorted(categories, key=lambda cat: cat["name"])



categoryDF = pd.DataFrame(categories)

title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    # with col1:
    #     st.image(path + '/../assets/bmore_food_logo_dark_theme.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Query imports</h1>", unsafe_allow_html=True)

# Opening JSON file
sortFile = open(path + '/../assets/sortBy.json')
  
# load sortBy map 
sortByMap = json.load(sortFile)["sortBy"]


categorySelect = st.selectbox("Show all food of type", sortedCategories, format_func=lambda cat: f'{cat["name"]}')
#categorySelect = st.selectbox("Show all food currently on rack", allRacks)
distributorSelect = st.selectbox("Show all food coming from", allDistributors, format_func=lambda cat: f'{cat["name"]}')
sortBySelect = st.selectbox("Sort food imports by", sortByMap)

allPallets = json.loads(pallet.getFood())["Pallet"]
#print("allPallets: ", allPallets[:10])
df = pd.DataFrame.from_dict(allPallets)
df.company = df.company.apply(getCompanyNames)

def getCategories(category):
    catNames = []
    for cat in category:
        catNames.append(categoryDF.loc[categoryDF.id == cat, "name"].values[0])

    return pd.Series(catNames)

df["Categories"] = df.categoryIds.apply(getCategories)

# # Uncomment this when connected to backend 
# # # Filter by distributor 
# # # Filter by selected category


if categorySelect['id'] != -1:
    categoryIndices = []
    
    for index, row in df.iterrows():
        if categorySelect['id'] in row["categoryIds"]:
            categoryIndices.append(index)
    df = df.iloc[categoryIndices]
    df = df.reset_index()


if distributorSelect["name"] != "":
    distributorIndices = []
    for index, row in df.iterrows():
        if distributorSelect["name"] == row["company"]:
            distributorIndices.append(index)
    df = df.iloc[distributorIndices] #this maybe should sort by distributor ID 
    df = df.reset_index()

if sortByMap[sortBySelect] != 'none':
    df = df.sort_values([sortByMap[sortBySelect]])
    df = df.reset_index()

#st.dataframe(df)
st.dataframe(df)
# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
