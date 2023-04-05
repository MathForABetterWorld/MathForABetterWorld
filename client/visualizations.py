### include functions that plot a graph in the given streamlit column

import streamlit as st
import datetime
import numpy as np
from PIL import Image
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import pandas as pd
import random as random
from matplotlib import pyplot as plt, dates as mdates



# example:
def test(col):
    last_rows = np.random.randn(1, 1)
    # chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        last_rows = new_rows
    
    col.line_chart(last_rows)



def importGraph1(col):
    # TODO
    test(col)
    pass

def importGraph2(col):
    # TODO
    test(col)
    pass

def importGraph3(col):
    # TODO
    test(col)
    pass

def importGraph4(col):
    # TODO
    test(col)
    pass



def volunteerGraph1(col):
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

    # actual graph::
    ax = plt.gca()
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')
    fig.patch.set_alpha(0.7)
    ax.patch.set_facecolor('black')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(axis='y', colors='white')
    ax.tick_params(axis='x', colors='white')
    fig.suptitle("Trend of Volunteers in the last Seven Days", color="white")
    ax.plot(x, y)
    ax.set_xlabel("Last Seven Days")
    ax.set_ylabel("Total Volunteer Hours per Day")
    col.pyplot(fig)

def volunteerGraph2(col):
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


    volunteer_data = list(df.Volunteers)
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    sd = 0
    month_average = []
    volunteer = []
    for mindex, m in enumerate(months):
        #print(type(m))
        sum_data = 0
        for dindex, d in enumerate(dates):
            #print(dindex)
            if df.Date[dindex].find(m,3,5) != -1:
                sum_data = sum_data + df.Volunteers[dindex]
        volunteer.append(sum_data)
    
    # actual graph::
    fig2, ax2 = plt.subplots()
    fig2.patch.set_facecolor('black')
    fig2.patch.set_alpha(0.7)
    ax2.patch.set_facecolor('black')
    ax2.xaxis.label.set_color('white')
    ax2.yaxis.label.set_color('white')
    ax2.tick_params(axis='y', colors='white')
    ax2.tick_params(axis='x', colors='white')
    ax2.plot(months, volunteer)
    ax2.set_xlabel("Months")
    ax2.set_ylabel("Total Volunteer Hours")
    fig2.suptitle("Trend of Total Volunteers in the last 12 months", color="white")
    col.write(fig2)

def volunteerGraph3(col):
    # TODO
    test(col)
    pass

def volunteerGraph4(col):
    # TODO
    test(col)
    pass



def clientGraph1(col):
    # TODO
    test(col)
    pass

def clientGraph2(col):
    # TODO
    test(col)
    pass

def clientGraph3(col):
    # TODO
    test(col)
    pass

def clientGraph4(col):
    # TODO
    test(col)
    pass



def distributorGraph1(col):
    # TODO
    test(col)
    pass

def distributorGraph2(col):
    # TODO
    test(col)
    pass

def distributorGraph3(col):
    # TODO
    test(col)
    pass

def distributorGraph4(col):
    # TODO
    test(col)
    pass



def tempImportLineGraph():
    last_rows = np.random.randn(1, 1)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        last_rows = new_rows

    return st.line_chart(last_rows)

def tempDistributorsBarGraph(key):
    last_rows = np.random.randn(1, 1)
    # chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        last_rows = new_rows

    return st.bar_chart(last_rows)

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