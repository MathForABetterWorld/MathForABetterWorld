
import streamlit as st
import numpy as np
import pandas as pd
import json
import os 

path = os.path.dirname(__file__)


# This has to be the first streamlit command called
st.set_page_config(layout="centered", page_icon=path + "/../assets/bmore_food_logo.png", page_title="Query exports")

title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    with col1:
        st.image(path + '/../assets/bmore_food_logo.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Query exports</h1>", unsafe_allow_html=True)

# Opening JSON file
catFile = open(path + '/../assets/fakeCategories.json')
sortFile = open(path + '/../assets/sortBy.json')
recFile = open(path + '/../assets/recipients.json')
  
# load categories and sortBy map 
categories = json.load(catFile)["categories"]
sortByMap = json.load(sortFile)["sortBy"]
recList = json.load(recFile)["recipients"]

categorySelect = st.selectbox("Show all food of type", categories)
recSelect = st.selectbox("Show all food going to", recList)
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

### TODO: Add totals / summary to bottom of table to see how much 
# food one person / place has taken
# Filter by time -- how much we've exported in the past month vs year
# 
###