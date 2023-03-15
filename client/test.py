import time
from collections import defaultdict

import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import datetime
from data import imports, exports
import numpy as np
import seaborn as sb
import json

st.markdown("# Baltimore Community Foods")
st.sidebar.markdown("# Baltimore Community Foods")

Exports = pd.read_csv('Exports.csv')
Imports = pd.read_csv('Imports.csv')

pallet_weights = Exports["Weight of pallet"].dropna().values.tolist()
cum_weights = []
for num_str in pallet_weights:
    num_str = num_str.replace(",","")
    if num_str.isnumeric():
        num = abs(int(num_str))
        prev = 0 if len(cum_weights) == 0 else cum_weights[-1]
        cum_weights.append(num + prev)


#print(cum_weights)
#print(cum_weight)

#st.line_chart(cum_weights)

food_provider = Imports["Where is the food coming from? "].dropna().tolist()
food_provider = set(food_provider)

food_provider = defaultdict(float)
food_receiver = defaultdict(float)

for i in imports:
    food_provider[i['distributor']] += i['weight']

for i in exports:
    food_receiver[i['category']] += np.absolute(i['weight'])

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


for x,y in dict(sorted_food_provider[-5:]).items():
    sorted_provider_labels.append(x)
    sorted_provider_sizes.append(y)

for x,y in dict(sorted_food_receiver[-5:]).items():
    sorted_receiver_labels.append(x)
    sorted_receiver_sizes.append(y)


sorted_other_labels = []
sorted_other_providers = []

sorted_other_rec_labels = []
sorted_other_receivers = []

for x,y in dict(sorted_food_provider[:-5]).items():
    sorted_other_labels.append(x)
    sorted_other_providers.append(y)

other_total = sum(sorted_other_providers)

#print(other_total)
sorted_provider_sizes.append(other_total)
sorted_provider_labels.append("other")

for x,y in dict(sorted_food_receiver[:-5]).items():
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

print(percTot)
print(sorted_provider_sizes)
print(sorted_provider_labels)

for i in range(len(sorted_provider_labels)):
    sorted_provider_labels[i] = f'{sorted_provider_labels[i]}: {(float(percTot[i])):.1f}'

print(sorted_provider_labels)
#print(sorted_provider_sizes)

fig1, ax = plt.subplots()
ax.pie(sorted_provider_sizes, labels=sorted_provider_labels)
#plt.legend(provider_labels[-5:], bbox_to_anchor=(0,-2.7), loc="lower right")
Imports_df = pd.DataFrame(list(zip(sorted_provider_sizes, sorted_provider_labels)),
               columns =['Provider Imports', 'Provider'])


Exports_df = pd.DataFrame(list(zip(sorted_receiver_sizes, sorted_receiver_labels)),
               columns =['Receiver Amt', 'Receiver'])
print(Exports_df)


fig2, ax = plt.subplots()
ax.pie(receiver_sizes, labels=receiver_labels)
plt.legend(receiver_labels, bbox_to_anchor=(0,-2.7), loc="lower right")

tab1, tab2, tab3 = st.tabs(["Export totals", "Provider Imports", "Export Destinations"])
with tab1:
    st.line_chart(cum_weights)
with tab2:
    st.pyplot(fig1, theme="streamlit")
    #if st.button("See Full Distributor Import List")
    #    st.table(Imports_df)
    st.bar_chart(data=Imports_df, x="Provider", y="Provider Imports", use_container_width=True)

with tab3:
    st.pyplot(fig2)
    st.bar_chart(data=Exports_df, x="Receiver", y="Receiver Amt", use_container_width=True)


#numdays = 20
#base = datetime.datetime.today()
#date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]

