# import pdfkit
import streamlit as st
import datetime
import numpy as np
from PIL import Image
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import pandas as pd
import random as random
from matplotlib import pyplot as plt, dates as mdates
import urllib3
http = urllib3.PoolManager() # define http 
BASEURL = "http://????/api"


path = os.path.dirname(__file__)
st.set_page_config(layout="centered", page_icon=path + "/assets/bmore_food_logo.png", page_title="Bmore Food")

image = Image.open(path + '/assets/bmore_food_logo.png')
col1, col2, col3 = st.columns(3)



### Header ###
with col1:
    st.write(' ')

with col2:
    st.image(image)

with col3:
    st.write(' ')





### plot definitions
def importLineGraph():
    last_rows = np.random.randn(1, 1)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        last_rows = new_rows

    return st.line_chart(last_rows)

def distributorsBarGraph(key):
    last_rows = np.random.randn(1, 1)
    # chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        last_rows = new_rows

    return st.bar_chart(last_rows)

def test(col):
    last_rows = np.random.randn(1, 1)
    # chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        last_rows = new_rows

    return col.bar_chart(last_rows)

def tempVolunteerVis(col):
    a = datetime.datetime.today()
    numdays = 100
    dateList = []
    for x in range (0, numdays):
        dateList.append(a - datetime.timedelta(days = x))
    start = datetime.datetime.strptime("01-01-2023", "%d-%m-%Y")
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
    fig, ax = plt.subplots()


    ax.set_title("Trend of Volunteers in the last Seven Days")
    ax.plot(x, y)
    ax.set_xlabel("Last Seven Days")
    ax.set_ylabel("Total Volunteer Hours per Day")
    col.pyplot(fig)

def tempImportVis(col):
    a = datetime.datetime.today()
    numdays = 100
    dateList = []
    for x in range (0, numdays):
        dateList.append(a - datetime.timedelta(days = x))
    start = datetime.datetime.strptime("01-01-2023", "%d-%m-%Y")
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

    volunteers_dates = []
    for i in range(len(dates)):
        volunteers_dates.append([dates[i], random.randint(1, 20)])
        
    df = pd.DataFrame(volunteers_dates, columns=['Date', 'Volunteers'])

    x = list(df.Date[-1:-8:-1])
    x.reverse()
    y = list(df.Volunteers[-1:-8:-1])
    y.reverse()
    y = np.cumsum(y)

    m = max(y) + 10
    mx = [m for i in range(len(y))]

    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    ax = plt.gca()
    fig, ax = plt.subplots()


    ax.set_title("Total imports over time")
    ax.plot(x, y, label="Cumulative Imports")
    ax.plot(x, mx, label="Goal")
    ax.legend()
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Cumulative Imports (lbs)")
    col.pyplot(fig)




### display dashboard visualizations
# top left = imports/exports ; top right = clients ; bottom left = distributors ; bottom right = volunteers


last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    last_rows = new_rows

col1, col2 = st.columns(2)

tempImportVis(col1)
tempVolunteerVis(col2)
#col1.line_chart(last_rows)
col2.line_chart(last_rows)
col1.line_chart(last_rows)
#col2.line_chart(last_rows)




# TODO: month by month progress / month this year vs same month last yr 

