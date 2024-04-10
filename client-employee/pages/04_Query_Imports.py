
import streamlit as st
import numpy as np
import pandas as pd
import json
import os
from routeConnectors import pallet
from routeConnectors import distributorConnectors
from routeConnectors import rackConnector
from routeConnectors import categoryConnectors
from routeConnectors import userConnector
from routeConnectors import locationConnectors
from PIL import Image
from nav import nav_page
from datetime import datetime

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Query Imports")
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


def getCompanyNames(company):
    return company["name"]

# Get rack, distributor and category info 
allRacks = ["", 1, 2, 3, 4, 5, 6]
rackRes = rackConnector.getRacks()
if rackRes: 
    allRacks = allRacks + rackRes["rack"]


distributors = [{"id": -1, "name": "", "description": ""}]  + distributorConnectors.getDistributors()['distributors']
allDistributors = sorted(distributors, key=lambda cat: cat["name"])

categories = [{"id": -1, "name": "", "description": ""}]  + categoryConnectors.getCategories()['category']
sortedCategories = sorted(categories, key=lambda cat: cat["name"])


user_data = userConnector.getUsers()
user_data_str = user_data.decode('utf-8')
user_dict = json.loads(user_data_str)

users = [{"id": -1, "name": "", "email": "", "isActive": True}] + user_dict['users']
allUsers = sorted(users, key=lambda u: u["name"])

categoryDF = pd.DataFrame(categories)

title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    with col2:
        st.markdown("<h1 style='text-align: center; '>Query Imports</h1>", unsafe_allow_html=True)

# Opening JSON file
sortFile = open(path + '/../assets/sortByImport.json')
  
# load sortBy map 
sortByMap = json.load(sortFile)["sortBy"]

userSelect = st.selectbox("Show all import from user", allUsers, format_func=lambda u: f'{u["name"]}')
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

def getCompanyNameById(id):
    distributor = next((d for d in allDistributors if d['id'] == id), None)
    return distributor['name'] if distributor else ""

def getRackById(id):
    rack = next((r for r in allRacks if r['id'] == id), None)
    return rack['name'] if rack else ""

def getUserById(id):
    user = next((u for u in allUsers if u['id'] == id), None)
    return user['name'] if user else ""


df["Categories"] = df.categoryIds.apply(getCategories)

if userSelect['id'] != -1:
    userIndices = []
    for index, row in df.iterrows():
        if userSelect["id"] == row["entryUserId"]:
            userIndices.append(index)
    df = df.iloc[userIndices] #this maybe should sort by distributor ID 
    df = df.reset_index()


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

df['Distributor'] = df['companyId'].apply(getCompanyNameById)
df.drop(columns=['companyId'], inplace=True)

df['Entry User'] = df['entryUserId'].apply(getUserById)
df.drop(columns=['entryUserId'], inplace=True)

# df['Rack'] = df['rackId'].apply(getRackById)
# df.drop(columns=['rackId'], inplace=True)

df['inputDate'] = pd.to_datetime(df['inputDate'])
df['inputDate'] = df['inputDate'].dt.strftime('%Y-%m-%d %H:%M:%S')


df.rename(columns={'inputDate': 'Input Date', 'expirationDate': 'Expiration Date', 'weight': 'Weight', 'description': 'Description', 'categoryIds': 'Category IDs', 'barcodes': 'Barcodes', 'Categories': 'Categories'}, inplace=True)
columns_to_display = ['Entry User', 'Input Date', 'Expiration Date', 'Weight', 'Distributor', 'rackId', 'Description', 'Categories']
newDF = df[columns_to_display]

st.dataframe(newDF, use_container_width=True)

sum = newDF["Weight"].sum()

s = pd.Series([sum], name='Total Import Weight')

st.dataframe(s, use_container_width=True)

st.markdown("# Modify Imports: ")
if 'token' in st.session_state:
    columns_to_display = ['id', 'Entry User', 'Input Date', 'Distributor', 'Weight', 'Categories', "Description", "rackId"]
    df = df[columns_to_display]
    editType = st.selectbox("Modification Type (Edit) (Select Below)", ["", "Update Import"])
    if editType == "Update Import":

        import_id_to_update = st.selectbox("Select Import ID to Update:", df['id'].values, index=0)
        find_import = st.button("Find Import")
        
        if find_import:
            if import_id_to_update in df['id'].values:
                selected_import = df.loc[df['id'] == import_id_to_update]

                # racks = [{"id": -1, "name": "", "description": ""}]  + categoryConnectors.getCategories()['category']
                # formRacks = sorted(categories, key=lambda cat: cat["name"])

                # distributor = [{"id": -1, "name": "", "description": ""}]  + categoryConnectors.getCategories()['category']
                # formDistributors = sorted(categories, key=lambda cat: cat["name"])

                categories = [{"id": -1, "name": "", "description": ""}]  + categoryConnectors.getCategories()['category']
                formCategories = sorted(categories, key=lambda cat: cat["name"])

                users = [{"id": -1, "name": "", "email": "", "isActive": True}] + user_dict['users']
                formUsers = sorted(users, key=lambda u: u["name"])

                with st.form("template_form"):
                    left, right = st.columns(2)
                    # ADD DEFAULT VALUES index = selected_import['Import Type'].values[0]
                    entry_user = left.selectbox("Entry User", options = formUsers, format_func=lambda use: f'{use["name"]}')
                    import_date = right.date_input("Input Date", value = datetime.strptime(selected_import['Input Date'].values[0], '%Y-%m-%d %H:%M:%S'))
                    location = left.selectbox("Distributor", options = formDistributors, format_func=lambda loc: f'{loc["name"]}')
                    weight = right.text_input("Weight", selected_import['Weight'].values[0])
                    category = left.selectbox("Categories", options = formCategories, format_func=lambda cat: f'{cat["name"]}')
                    import_type = right.text_input(label = "Description", value = selected_import['Description'].values[0])
                    update_submit = st.form_submit_button("Update Import")

                    if update_submit:
                        print("yay")
                        # jsonObj = json.loads(userConnector.postUser(email, name, None if phoneNumber == "" else phoneNumber, None if address == "" else address, isActive))
                        # newCat = pd.DataFrame(jsonObj["user"], index=[0])
                        # st.experimental_rerun()
            else:
                st.warning("Import ID not found. Please enter a valid Import ID.")
        df

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")


if log_button :
    if "token" in st.session_state :
        if "role" in st.session_state :
            del st.session_state.role
        del st.session_state.token
        st.experimental_rerun()
    else:
        nav_page("")