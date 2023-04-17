## defs for different dashboard views
## function definitions for graphs/visualizations are in visualizations.py

import streamlit as st
import datetime
import numpy as np
from PIL import Image
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import json
import pandas as pd
import random as random

from visualizations import *

from collections import defaultdict

from data import imports, exports
import seaborn as sb
from routeConnectors import pallet, exportConnectors


def changeState(num):
    st.session_state.pageID = num

def mainDashboardVis():
    col1, col2 = st.columns(2)

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Imports/Exports")
    col2.write("Volunteers")
    importGraph1(col1)
    volunteerGraph1(col2)


    impButton = col1.button("See More", key="import", on_click=changeState, args=(1, ))
    volunteerButton = col2.button("See More", key="volunteer", on_click=changeState, args=(2, ))

    col1.markdown("##")
    col2.markdown("##")

    col1.write("Clients")
    col2.write("Distributors")
    clientGraph1(col1)
    distributorGraph1(col2)

    clientButton = col1.button("See More", key="client", on_click=changeState, args=(3, ))
    distButton = col2.button("See More", key="distributor", on_click=changeState, args=(4, ))


def importVis():
    pallets = json.loads(pallet.getFood())
    exportItems = json.loads(exportConnectors.getExports())
    Exports = pd.DataFrame(exportItems["exports"])
    #Imports = pd.read_json(pallets["Pallet"])#pd.read_csv('Imports.csv')
    Imports = pd.DataFrame(pallets["Pallet"])
    pallet_weights = Exports["weight"].dropna().values.tolist()
    cum_weights = []
    for num_str in pallet_weights:
        #num_str = num_str.replace(",","")
        #if num_str.isnumeric():
        num = abs(int(num_str))
        prev = 0 if len(cum_weights) == 0 else cum_weights[-1]
        cum_weights.append(num + prev)
    #print(cum_weights)
    #print(cum_weight)

    #st.line_chart(cum_weights)

    food_provider = Imports["companyId"].dropna().tolist()
    food_provider = set(food_provider)

    food_provider = defaultdict(float)
    food_receiver = defaultdict(float)

    for index, row in Imports.iterrows():
        food_provider[row['company']["name"]] += row['weight']

    for index, row in Exports.iterrows():
        food_receiver[row['category']["name"]] += np.absolute(row['weight'])

    #print(food_provider)

    provider_labels = []
    provider_sizes = []

    sorted_provider_labels = []
    sorted_provider_sizes = []

    receiver_labels = []
    receiver_sizes = []

    sorted_receiver_labels = []
    sorted_receiver_sizes = []

    for x,y in food_provider.items():
        provider_labels.append(x)
        provider_sizes.append(y)

    for x,y in food_receiver.items():
        receiver_labels.append(x)
        receiver_sizes.append(y)


    sorted_food_provider = sorted(food_provider.items(), key=lambda x:x[1])
    sorted_food_receiver = sorted(food_receiver.items(), key=lambda x:x[1])


    for x,y in dict(sorted_food_provider[-10:]).items():
        sorted_provider_labels.append(x)
        sorted_provider_sizes.append(y)

    for x,y in dict(sorted_food_receiver[-10:]).items():
        sorted_receiver_labels.append(x)
        sorted_receiver_sizes.append(y)


    sorted_other_labels = []
    sorted_other_providers = []

    sorted_other_rec_labels = []
    sorted_other_receivers = []

    for x,y in dict(sorted_food_provider[:-10]).items():
        sorted_other_labels.append(x)
        sorted_other_providers.append(y)

    other_total = sum(sorted_other_providers)

    #print(other_total)
    sorted_provider_sizes.append(other_total)
    sorted_provider_labels.append("other")

    for x,y in dict(sorted_food_receiver[:-10]).items():
        sorted_other_rec_labels.append(x)
        sorted_other_receivers.append(y)

    other_rec_total = sum(sorted_other_receivers)

    sorted_receiver_sizes.append(other_rec_total)
    sorted_receiver_labels.append("other")

    ImpTot= sum(sorted_provider_sizes)
    percTot = []
    for size in sorted_provider_sizes:
        perc = size/ImpTot*100
        percTot.append(perc)

    ItemExpTot= sum(sorted_receiver_sizes)
    receiverPercTot = []
    for size in sorted_receiver_sizes:
        receiverPerc = size/ItemExpTot*100
        receiverPercTot.append(receiverPerc)


    print(percTot)
    print(sorted_provider_sizes)
    print(sorted_provider_labels)

    for i in range(len(sorted_provider_labels)):
        sorted_provider_labels[i] = f'{sorted_provider_labels[i]}: {(float(percTot[i])):.1f}%'

    for i in range(len(sorted_receiver_labels)):
        sorted_receiver_labels[i] = f'{sorted_receiver_labels[i]}: {(float(receiverPercTot[i])):.1f}%'

    print(sorted_provider_labels)
    #print(sorted_provider_sizes)

    fig1, ax = plt.subplots()
    ax.pie(sorted_provider_sizes, labels=sorted_provider_labels)
    #plt.legend(provider_labels[-5:], bbox_to_anchor=(0,-2.7), loc="lower right")
    Imports_df = pd.DataFrame(list(zip(sorted_provider_sizes, sorted_provider_labels)),
                columns =['Provider Imports', 'Provider'])


    Exports_df = pd.DataFrame(list(zip(sorted_receiver_sizes, sorted_receiver_labels)),
                columns =['Quantity (lbs)', 'Item'])
    print(Exports_df)


    fig2, ax = plt.subplots()
    ax.pie(receiver_sizes, labels=receiver_labels)
    plt.legend(receiver_labels, bbox_to_anchor=(0,-2.7), loc="lower right")

    tab1, tab2, tab3 = st.tabs(["Export totals", "Provider Imports", "Export Destinations"])
    with tab1:
        st.line_chart(cum_weights)
    with tab2:
        #st.pyplot(fig1)
        #if st.button("See Full Distributor Import List")
        #    st.table(Imports_df)
        st.bar_chart(data=Imports_df, x="Provider", y="Provider Imports", use_container_width=True)

    with tab3:
        #st.pyplot(fig2)
        st.bar_chart(data=Exports_df, x="Item", y="Quantity (lbs)", use_container_width=True)


    #numdays = 20
    #base = datetime.datetime.today()
    #date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]

    # col1.button("Back", key="bck", on_click=changeState, args=(0, ))

def volunteerVis():
    tab1, tab2, tab3 = st.tabs(["Last 7 Days", "Last 12 Months", "G3"])
    with tab1:
        volunteerGraph1(tab1)
    with tab2:
        volunteerGraph2(tab2)
    with tab3:
        volunteerGraph3(tab3)

    col1, col2 = st.columns(2)

    back = col1.button("Back", key="bck", on_click=changeState, args=(0, ))

def clientVis():
    tab1, tab2, tab3 = st.tabs(["G1", "G2", "G3"])
    with tab1:
        clientGraph1(tab1)
    with tab2:
        clientGraph2(tab2)
    with tab3:
        clientGraph3(tab3)

    col1, col2 = st.columns(2)

    back = col1.button("Back", key="bck", on_click=changeState, args=(0, ))

def distributorVis():
    tab1, tab2, tab3 = st.tabs(["G1", "G2", "G3"])
    with tab1:
        distributorGraph1(tab1)
    with tab2:
        distributorGraph2(tab2)
    with tab3:
        distributorGraph3(tab3)

    col1, col2 = st.columns(2)

    back = col1.button("Back", key="bck", on_click=changeState, args=(0, ))