# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import random as random
from matplotlib import pyplot as plt, dates as mdates
import calendar
import streamlit as st


import datetime

a = datetime.datetime.today()
numdays = 100
dateList = []
for x in range (0, numdays):
    dateList.append(a - datetime.timedelta(days = x))
#dateList

start = datetime.datetime.strptime("21-06-2014", "%d-%m-%Y")


#Define Dates
start = datetime.datetime.strptime("01-01-2023", "%d-%m-%Y")
#now = datetime.datetime.today() # current date and time
now = datetime.datetime.strptime("31-12-2023", "%d-%m-%Y")
now2 = datetime.datetime.strptime("30-06-2023", "%d-%m-%Y")
year = now.strftime("%Y")
year2 = now2.strftime("%Y")

month = now.strftime("%m")
month2 = now2.strftime("%m")

day = now.strftime("%d")
day2 = now2.strftime("%d")



date_time = now.strftime("%m-%d-%Y")
date_time2 = now2.strftime("%m-%d-%Y")



end = datetime.datetime.strptime(date_time, "%m-%d-%Y")
end2 = datetime.datetime.strptime(date_time2, "%m-%d-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
date_generated2 = [start + datetime.timedelta(days=x) for x in range(0, (end2-start).days)]

dates = []
dates2 = []
week_days = []
week_days2 = []


for date in date_generated:

    year = int(date.strftime("%Y"))
    year2 = int(date.strftime("%Y"))
    month = int(date.strftime("%m"))
    month2 = int(date.strftime("%m"))
    day = int(date.strftime("%d"))
    day2 = int(date.strftime("%d"))
    week_day = calendar.weekday(year, month, day)
    week_day2 = calendar.weekday(year2, month2, day2)
    week_days.append(week_day)
    week_days2.append(week_day2)
    
    dates.append(date.strftime("%d-%m-%Y"))
    dates2.append(date.strftime("%d-%m-%Y"))





#dates

volunteers_dates = []
for i in range(len(dates)):
    volunteers_dates.append([dates[i], week_days[i], random.randint(1, 20)])
    
df = pd.DataFrame(volunteers_dates, columns=['Date', 'DayOfWeek','Volunteers'])
print(df)


#Data for Last Week
x = list(df.Date[-1:-8:-1])
x.reverse()
y = list(df.Volunteers[-1:-8:-1])
y.reverse()

#Plot for Last Week
"""
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
ax = plt.gca()


fig, ax = plt.subplots()

st.title("Trend of Volunteers in the last Seven Days")
ax.plot(x, y)
ax.set_xlabel("Last Seven Days")
ax.set_ylabel("Total Volunteer Hours per Day")
st.pyplot(fig)
/"""




#Plot over Last 12 months
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

print(volunteer)     


"""
fig2, ax2 = plt.subplots()

#ax = plt.gca()
ax2.plot(months, volunteer)
ax2.set_xlabel("Months")
ax2.set_ylabel("Total Volunteer Hours")
st.title("Trend of Total Volunteers in the last 12 months")
st.write(fig2)
/"""
#Compare the volunteer show out on days of the week over time 

df_half = df.iloc[:183,:]
for day in df_half["DayOfWeek"]:
    if df_half["DayOfWeek"][day] == 0:
        df_mon = df_half[df_half["DayOfWeek"] == 0]
    elif df_half["DayOfWeek"][day] == 1:
        df_tues = df_half[df_half["DayOfWeek"] == 1]
    elif df_half["DayOfWeek"][day] == 2:
        df_wed = df_half[df_half["DayOfWeek"] == 2] 
    elif df_half["DayOfWeek"][day] == 3:
        df_thurs = df_half[df_half["DayOfWeek"] == 3]   
    elif df_half["DayOfWeek"][day] == 4:
        df_fri = df_half[df_half["DayOfWeek"] == 4]  
    elif df_half["DayOfWeek"][day] == 5:
        df_sat = df_half[df_half["DayOfWeek"] == 5]  
    elif df_half["DayOfWeek"][day] == 6:
        df_sun = df_half[df_half["DayOfWeek"] == 6] 



#Plot for six-month day to day
volunteer_days_of_week = [np.mean(df_mon["Volunteers"]),np.mean(df_tues["Volunteers"]),np.mean(df_wed["Volunteers"]),np.mean(df_thurs["Volunteers"]),np.mean(df_fri["Volunteers"]), np.mean(df_sat["Volunteers"]), np.mean(df_sun["Volunteers"])]
days_of_week = ["1_Mon","2_Tues","3_Wed","4_Thurs","5_Fri","6_Sat","7_Sun"]
y_pos = np.arange(len(days_of_week))
print(y_pos)

df_new = pd.DataFrame({'Days':days_of_week,'AverageVolunteersPerDay':volunteer_days_of_week})
st.write(df_new)
fig3,ax3 = plt.subplots()
st.bar_chart(df_new, y = "AverageVolunteersPerDay", x="Days")
st.title('Average Number of Volunteer Hours each day over last 6 months')



#last month
df_month = df.iloc[:32,:]
for day in df_month["DayOfWeek"]:
    if df_month["DayOfWeek"][day] == 0:
        df_mon2 = df_month[df_month["DayOfWeek"] == 0]
    elif df_month["DayOfWeek"][day] == 1:
        df_tues2 = df_month[df_month["DayOfWeek"] == 1]
    elif df_month["DayOfWeek"][day] == 2:
        df_wed2 = df_month[df_month["DayOfWeek"] == 2] 
    elif df_month["DayOfWeek"][day] == 3:
        df_thurs2 = df_month[df_month["DayOfWeek"] == 3]   
    elif df_month["DayOfWeek"][day] == 4:
        df_fri2 = df_month[df_month["DayOfWeek"] == 4]  
    elif df_month["DayOfWeek"][day] == 5:
        df_sat2 = df_month[df_month["DayOfWeek"] == 5]  
    elif df_month["DayOfWeek"][day] == 6:
        df_sun2 = df_month[df_month["DayOfWeek"] == 6]
        

volunteer_days_of_week2 = [np.mean(df_mon2["Volunteers"]),np.mean(df_tues2["Volunteers"]),np.mean(df_wed2["Volunteers"]),np.mean(df_thurs2["Volunteers"]),np.mean(df_fri2["Volunteers"]), np.mean(df_sat2["Volunteers"]), np.mean(df_sun2["Volunteers"])]


df_new2 = pd.DataFrame({'Days':days_of_week,'AverageVolunteersPerDay':volunteer_days_of_week2})
st.bar_chart(df_new2, y = "AverageVolunteersPerDay", x="Days")
st.title('Average Number of Volunteer Hours each day over last 1 month')


#Do code over the last month (temporary issues) and over the last 6 months









