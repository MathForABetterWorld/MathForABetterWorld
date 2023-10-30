# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import random as random
from matplotlib import pyplot as plt, dates as mdates
import streamlit as st
import datetime
from PIL import Image
import os

path = os.path.dirname(__file__)

st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo_dark_theme.png", page_title="Volunteer Data Summary")
image = Image.open(path + '/../assets/bmore_food_logo_dark_theme.png')

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(image)
with col3:
    st.write(' ')

title_container = st.container()
col1, col2 = st.columns([1, 50])
with title_container:
    # with col1:
    #     st.image(path + '/../assets/bmore_food_logo_dark_theme.png', width=60)
    with col2:
        st.markdown("<h1 style='text-align: center; '>Volunteer Data Summary</h1>", unsafe_allow_html=True)

a = datetime.datetime.today()
numdays = 100
dateList = []
for x in range (0, numdays):
    dateList.append(a - datetime.timedelta(days = x))
#dateList

start = datetime.datetime.strptime("21-06-2014", "%d-%m-%Y")

start = datetime.datetime.strptime("01-01-2023", "%d-%m-%Y")
#now = datetime.datetime.today() # current date and time
now = datetime.datetime.strptime("31-12-2023", "%d-%m-%Y")
year = now.strftime("%Y")

month = now.strftime("%m")

day = now.strftime("%d")


date_time = now.strftime("%m-%d-%Y")


end = datetime.datetime.strptime(date_time, "%m-%d-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

dates = []
for date in date_generated:
    dates.append(date.strftime("%d-%m-%Y"))

#dates

volunteers_dates = []
for i in range(len(dates)):
    volunteers_dates.append([dates[i], random.randint(1, 20)])
    
df = pd.DataFrame(volunteers_dates, columns=['Date', 'Volunteers'])
x = list(df.Date[-1:-8:-1])
x.reverse()
y = list(df.Volunteers[-1:-8:-1])
y.reverse()

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
ax = plt.gca()
#ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d-%y"))
#ax.xaxis.set_major_locator(mdates.DayLocator())


# Select time frame
timeFrames = {
    "Last 12 months": {
        "x": ['01','02','03','04','05','06','07','08','09','10','11','12'], 
        "volunteerHours": [286, 294, 365, 257, 347, 285, 374, 327, 358, 314, 337, 317]
    },
    "Last 6 months": {
        "x": ['01','02','03','04','05','06'], 
        "volunteerHours": [286, 294, 365, 257, 347, 285]
    },
    "Last 7 days": {
        "x": x,
        "volunteerHours": y
    }
}
timeRangeSelect = st.selectbox("Select time frame", timeFrames.keys())

fig, ax = plt.subplots()

st.title("Trend of Volunteers in the " + timeRangeSelect)

ax.plot(timeFrames[timeRangeSelect]["x"], timeFrames[timeRangeSelect]["volunteerHours"])
ax.set_xlabel(timeRangeSelect)
ax.set_ylabel("Total Volunteer Hours per Day")
st.pyplot(fig)


st.title("Trend of Volunteers in the last Seven Days")
ax.plot(x, y)
ax.set_xlabel("Last Seven Days")
ax.set_ylabel("Total Volunteer Hours per Day")
st.pyplot(fig)




volunteer_data = list(df.Volunteers)
months = ['01','02','03','04','05','06','07','08','09','10','11','12']


sd = 0
month_average = []
volunteer = []
for mindex, m in enumerate(months):
    sum_data = 0
    for dindex, d in enumerate(dates):
        if df.Date[dindex].find(m,3,5) != -1:
            sum_data = sum_data + df.Volunteers[dindex]
    volunteer.append(sum_data)
            
#volunteer



fig2, ax2 = plt.subplots()

#ax = plt.gca()
ax2.plot(months, volunteer)
ax2.set_xlabel("Months")
ax2.set_ylabel("Total Volunteer Hours")
st.title("Trend of Total Volunteers in the last 12 months")
st.write(fig2)
