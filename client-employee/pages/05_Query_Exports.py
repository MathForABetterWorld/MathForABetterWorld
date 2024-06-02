
import streamlit as st
import numpy as np
import pandas as pd
import json
import os 
from routeConnectors import categoryConnectors, exportConnectors, locationConnectors, userConnector
from PIL import Image
from nav import nav_page
from datetime import datetime


path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Query Exports")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(image)
with col3:
    st.write(' ')

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
        st.markdown("<h1 style='text-align: center; '>Query Exports</h1>", unsafe_allow_html=True)

# Opening JSON file
catFile = open(path + '/../assets/fakeCategories.json')
sortFile = open(path + '/../assets/sortByExport.json')
#recFile = open(path + '/../assets/recipients.json')
  

# load categories and sortBy map 
#categories = json.load(catFile)["categories"]
sortByMap = json.load(sortFile)["sortBy"]
#recList = json.load(recFile)["recipients"]

locations = [{"id": -1, "name": "", "longitude":"", "latitude": ""}]  + locationConnectors.getLocations()['location']
sortedLocations = sorted(locations, key=lambda location: location["name"])

categories = [{"id": -1, "name": "", "description": ""}]  + categoryConnectors.getCategories()['category']
sortedCategories = sorted(categories, key=lambda cat: cat["name"])

locations = [{"id": -1, "name": ""}]  + locationConnectors.getLocations()['location']
allLocations = sorted(locations, key=lambda cat: cat["name"])

user_data = userConnector.getUsers()
user_data_str = user_data.decode('utf-8')
user_dict = json.loads(user_data_str)

users = [{"id": -1, "name": "", "email": "", "isActive": True}] + user_dict['users']
allUsers = sorted(users, key=lambda u: u["name"])

userSelect = st.selectbox("Show all exports from user", allUsers, format_func=lambda u: f'{u["name"]}')
categorySelect = st.selectbox("Show all food of type", categories, format_func=lambda cat: f'{cat["name"]}')
recSelect = st.selectbox("Show all food going to", sortedLocations, format_func=lambda loc: f'{loc["name"]}')

sortBySelect = st.selectbox("Sort food exports by", sortByMap)

df = pd.DataFrame(json.loads(exportConnectors.getExports().decode('utf-8'))["exports"])
categoryDF = pd.DataFrame(categories)
def getCategories(category):
    return categoryDF.loc[categoryDF.id == category["id"], "name"].values[0]

locationDF = pd.DataFrame(locations)
def getLocation(location):
    return locationDF.loc[locationDF.id == location["id"], "name"].values[0]

def getUserById(id):
    user = next((u for u in allUsers if u['id'] == id), None)
    return user['name'] if user else ""


df["category"] = df.category.apply(getCategories)
df["location"] = df.location.apply(getLocation) 

if userSelect['id'] != -1:
    userIndices = []
    for index, row in df.iterrows():
        if userSelect["id"] == row["userId"]:
            userIndices.append(index)
    df = df.iloc[userIndices] #this maybe should sort by distributor ID 
    df = df.reset_index()

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

if sortByMap[sortBySelect] != 'none':
    df = df.sort_values([sortByMap[sortBySelect]])
    df = df.reset_index()

df['Entry User'] = df['userId'].apply(getUserById)
df.drop(columns=['userId'], inplace=True)

df['exportDate'] = pd.to_datetime(df['exportDate'])
df['exportDate'] = df['exportDate'].dt.strftime('%Y-%m-%d %H:%M:%S')

df.rename(columns={'exportDate': 'Export Date', 'location': 'Location', 'weight': 'Weight', "exportType": "Export Type", 'category': 'Categories'}, inplace=True)
columns_to_display = ['Entry User', 'Export Date', 'Location', 'Weight', 'Categories', "Export Type"]
display_df = df[columns_to_display]

st.dataframe(display_df, use_container_width=True)

sum = display_df["Weight"].sum()

s = pd.Series([sum], name='Total Export Weight')

st.dataframe(s, use_container_width=True)

st.markdown("# Modify Exports: ")
if 'token' in st.session_state:
    columns_to_display = ['id', 'Entry User', 'Export Date', 'Location', 'Weight', 'Categories', "Export Type"]
    df = df[columns_to_display]
    editType = st.selectbox("Modification Type (Edit) (Select Below)", ["", "Update Export"])
    if editType == "Update Export":

        export_id_to_update = st.selectbox("Select Export ID to Update:", df['id'].values, index=0)
        find_export = st.button("Find Export")
        
        if find_export:
            if export_id_to_update in df['id'].values:
                selected_export = df.loc[df['id'] == export_id_to_update]

                locations = [{"id": -1, "name": "", "longitude":"", "latitude": ""}]  + locationConnectors.getLocations()['location']
                formLocations = sorted(locations, key=lambda location: location["name"])

                categories = [{"id": -1, "name": "", "description": ""}]  + categoryConnectors.getCategories()['category']
                formCategories = sorted(categories, key=lambda cat: cat["name"])

                users = [{"id": -1, "name": "", "email": "", "isActive": True}] + user_dict['users']
                formUsers = sorted(users, key=lambda u: u["name"])

                with st.form("template_form"):
                    left, right = st.columns(2)
                    # ADD DEFAULT VALUES index = selected_export['Export Type'].values[0]
                    entry_user = left.selectbox("Entry User", options = formUsers, format_func=lambda use: f'{use["name"]}')
                    export_date = right.date_input("Export Date", value = datetime.strptime(selected_export['Export Date'].values[0], '%Y-%m-%d %H:%M:%S'))
                    location = left.selectbox("Location", options = formLocations, format_func=lambda loc: f'{loc["name"]}')
                    weight = right.text_input("Weight", selected_export['Weight'].values[0])
                    category = left.selectbox("Categories", options = formCategories, format_func=lambda cat: f'{cat["name"]}')
                    export_type = right.selectbox(label = "Export Type", options = (["Regular", "Damaged", "Recycle", "Compost", "Return"]))
                    update_submit = st.form_submit_button("Update Export")

                    if update_submit:
                        print("yay")
                        # jsonObj = json.loads(userConnector.postUser(email, name, None if phoneNumber == "" else phoneNumber, None if address == "" else address, isActive))
                        # newCat = pd.DataFrame(jsonObj["user"], index=[0])
                        # st.experimental_rerun()
            else:
                st.warning("Export ID not found. Please enter a valid Export ID.")
        df
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
        if "role" in st.session_state :
            del st.session_state.role
        del st.session_state.token
        st.experimental_rerun()
    else:
        nav_page("")