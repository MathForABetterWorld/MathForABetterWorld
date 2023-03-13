
import streamlit as st
import numpy as np
import pandas as pd
import json
import os

path = os.path.dirname(__file__)
# This has to be the first streamlit command called
st.set_page_config(page_title="Filter By", page_icon="📈")

# Opening JSON file
catFile = open(path + '/../assets/fakeCategories.json')
sortFile = open(path + '/../assets/sortBy.json')
distFile = open(path + '/../assets/distributors.json')
  
# load categories and sortBy map 
categories = json.load(catFile)["categories"]
sortByMap = json.load(sortFile)["sortBy"]
distList = json.load(distFile)["distributors"]

st.markdown("# Query imports")

categorySelect = st.selectbox("Show all food of type", categories)
distributorSelect = st.selectbox("Show all food coming from", distList)
sortBySelect = st.selectbox("Sort food imports by", sortByMap)

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

# # Uncomment this when connected to backend 
# df = df.sort_values(by=[sortByMap[sortBySelect]])
# # Filter by distributor 
# df = df[df['distributor'] == distributorSelect] #this maybe should sort by distributor ID 
# # Filter by selected category
# df = df[df['category'] == categorySelect] 

st.table(df)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
