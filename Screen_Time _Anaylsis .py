#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[3]:


data = pd.read_csv("Screentime-App-Details.csv")
print(data.head())


# In[4]:


data.isnull().sum()


# In[5]:


print(data.describe())


# In[6]:



# Convert the "Date" column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Group data by week and aggregate usage, notifications, and times opened
grouped_by_week = data.groupby(data['Date'].dt.to_period('W')).agg({
    'Usage': 'sum',
    'Notifications': 'sum',
    'Times opened': 'sum'
}).reset_index()

print(grouped_by_week)


# In[7]:


# Group data by month and aggregate usage, notifications, and times opened
grouped_by_month = data.groupby(data['Date'].dt.to_period('M')).agg({
    'Usage': 'sum',
    'Notifications': 'sum',
    'Times opened': 'sum'
}).reset_index()

print(grouped_by_month)


# In[8]:


figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Usage", 
                color="App", 
                title="Usage")
figure.show()


# In[9]:


figure=px.bar(data_frame=data,x='Date',y="Notifications",color="App",title="Notifications")
figure.show()


# In[10]:


figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Times opened", 
                color="App",
                title="Times Opened")
figure.show()


# In[11]:


figure = px.scatter(data_frame = data, 
                    x="Notifications",
                    y="Usage", 
                    size="Notifications", 
                    trendline="ols", 
                    title = "Relationship Between Number of Notifications and Usage")
figure.show()


# # Usage by App
# 

# In[14]:



app_usage = data.groupby("App")["Usage"].sum().reset_index()
app_usage = app_usage.sort_values(by="Usage", ascending=False)
fig = px.bar(app_usage, x="App", y="Usage", title="Screen Time Distribution by App")
fig.show()


# # App Switching Patterns

# In[17]:


data['App Switches'] = data.groupby('Date')['Times opened'].diff().fillna(0)
fig = px.histogram(data, x="App Switches", title="App Switching Patterns")
fig.show()


# In[ ]:




