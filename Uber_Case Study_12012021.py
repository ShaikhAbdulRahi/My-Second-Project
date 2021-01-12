#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("E:/Decode_Lectures/Case Study/Case Study_02/Uber Request Data.csv")
df


# In[3]:


len(df["Request id"].unique())


# In[4]:


df.shape


# In[5]:


df.isnull().sum()# check the null values


# In[6]:


df.isnull().sum()/6745*100# check null percentage


# In[7]:


df.info()# check Date Time


# In[8]:


df["Request id"].value_counts()


# In[9]:


df["Request timestamp"].value_counts()


# In[10]:


df["Request timestamp"]=df["Request timestamp"].astype(str)


# In[11]:


df["Request timestamp"]=df["Request timestamp"].replace("/","-")


# In[ ]:


df["Request timestamp"]=pd.to_datetime(df["Request timestamp"],dayfirst=True)


# In[12]:


df["Request timestamp"]=pd.to_datetime(df["Request timestamp"],dayfirst=True)
df


# In[15]:


df["Drop timestamp"]=pd.to_datetime(df["Drop timestamp"],dayfirst=True)


# In[16]:


df.info()


# In[17]:


df["Request timestamp"]


# In[11]:


df.info()


# In[14]:


df["Drop timestamp"]


# In[18]:


import datetime as dt


# In[19]:


dt


# In[39]:


df["Request timestamp"].value_counts()


# In[21]:


req_hour=df["Request timestamp"].dt.hour


# In[ ]:


req_hour=df["Request timestamp"].dt.hour


# In[22]:


len(req_hour)


# In[24]:


df["req_hour"]=req_hour
df


# In[25]:


req_hour.head()


# In[26]:


req_day=df["Request timestamp"].dt.day#converting date column into Days


# In[27]:


df["req_day"]=req_day
df


# In[28]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[29]:


sns.countplot(x="req_hour",data=df,hue="Status")
plt.show()


# In[30]:


sns.factorplot(x="req_hour",data=df,row="req_day",kind="count",hue="Status")
plt.show()


# In[31]:


sns.factorplot(x="req_hour",data=df,row="req_day",kind="count",hue="Pickup point")
plt.show()#40 Min


# In[ ]:


<5           "Pre_morning"
5<=x<10   == "Morning Rush"
10<=x<17     'Day_time'
17<=x<22     "Evening rush"
else         "Late night"


# In[32]:


df


# In[33]:


df["Time_Slot"]=0


# In[34]:


df


# In[35]:


j=0
for i in df["req_hour"]:
    if df.iloc[j,6]<5:
        df.iloc[j,8]="Pre_Morning"
    elif 5<=df.iloc[j,6]<10:
        df.iloc[j,8]="Morning_Rush"
        
    elif 10<=df.iloc[j,6]<17:
        df.iloc[j,8]="Day_Time"
        
    elif 17<=df.iloc[j,6]<22:
        df.iloc[j,8]="Evening_Rush"
    else:
        df.iloc[j,8]="Late_Night"
    j=j+1


# In[36]:


df


# In[37]:


df["Time_Slot"].value_counts()


# In[40]:


plt.figure(figsize=(10,6))
sns.countplot(x="Time_Slot",hue="Status",data=df)
plt.show()


# In[43]:


df_morning_rush=df[df["Time_Slot"]=="Morning_Rush"]
df_morning_rush


# In[44]:


plt.figure(figsize=(10,6))
sns.countplot(x="Pickup point",hue="Status",data=df_morning_rush)
plt.show()


# # Severity of problem by location and their count (cancellation of cab as per the pickup location at morning rush hours)

# In[50]:


df_airport_cancelled=df_morning_rush.loc[(df_morning_rush["Pickup point"]=="Airport") & (df_morning_rush["Status"]=="Cancelled")]


# In[52]:


df_airport_cancelled.shape[0]


# In[53]:


df_city_cancelled=df_morning_rush.loc[(df_morning_rush["Pickup point"]=="City") & (df_morning_rush["Status"]=="Cancelled")]


# In[54]:


df_city_cancelled.shape[0]


# # Supply and demand for Morning

# In[57]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="City")].shape[0]


# In[74]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="City")& (df_morning_rush["Status"]=="No Cars Available")].shape[0]


# In[75]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="City")& (df_morning_rush["Status"]=="Trip Completed")].shape[0]


# In[76]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="City")& (df_morning_rush["Status"]=="Cancelled")].shape[0]


# In[61]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="Airport")].shape[0]


# In[73]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="Airport")& (df_morning_rush["Status"]=="No Cars Available")].shape[0]


# In[62]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="Airport")& (df_morning_rush["Status"]=="Trip Completed")].shape[0]


# In[77]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="Airport")& (df_morning_rush["Status"]=="Cancelled")].shape[0]


# # # Supply and demand for evening

# In[63]:


df_evening_rush=df[df["Time_Slot"]=="Evening_Rush"]
df_evening_rush


# In[64]:


df_city_cancelled=df_evening_rush.loc[(df_evening_rush["Pickup point"]=="City") & (df_evening_rush["Status"]=="Cancelled")]


# In[66]:


df_city_cancelled.shape[0]


# In[67]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="City")].shape[0]


# In[68]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="City")& (df_evening_rush["Status"]=="Trip Completed")].shape[0]


# In[78]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="City")& (df_evening_rush["Status"]=="No Cars Available")].shape[0]


# In[79]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="City")& (df_evening_rush["Status"]=="Cancelled")].shape[0]


# In[69]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="Airport")].shape[0]


# In[70]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="Airport")& (df_evening_rush["Status"]=="Trip Completed")].shape[0]


# In[ ]:


#Morning_Rush City Demand=1677
#Morning_Rush City Supply= 472
#Morning_Rush Airport Demand=426
#Morning_Rush Airport Supply=382
#Evening_Rush City Demand=542
#Evening_Rush City Supply=411
#Evening_Rush Airport Demand=1800
#Evening_Rush Airport Supply=373


# # Severity problem at each location by looking at cancellation of cabs in each of the pickup location

# In[71]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="Airport")& (df_evening_rush["Status"]=="Cancelled")].shape[0]


# In[72]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="City")& (df_evening_rush["Status"]=="Cancelled")].shape[0]


# # PI Chart Evening Rush

# In[81]:


df_evening_city=df.loc[(df["Pickup point"]=="City")&(df["Time_Slot"]=="Evening_Rush")]


# In[83]:


df_evening_city["Status"].value_counts()


# In[85]:


df_evening_city_count=pd.DataFrame(df_evening_city["Status"].value_counts())


# In[86]:


df_evening_city_count


# In[88]:


df["Status"].values


# In[89]:


df_evening_city_count["Status"].values


# In[91]:


df_evening_city_count["Status"].index


# In[98]:


fig,ax=plt.subplots()
ax.pie(df_evening_city_count["Status"].values,labels=df_evening_city_count["Status"].index,autopct="%.2f%%",
      startangle=90)
plt.show()


# # PI Chart for Morning Rush

# In[99]:


df_morning_city=df.loc[(df["Pickup point"]=="City")&(df["Time_Slot"]=="Morning_Rush")]


# In[100]:


df_morning_city["Status"].value_counts()


# In[101]:


df_morning_city_count=pd.DataFrame(df_morning_city["Status"].value_counts())


# In[102]:


df_morning_city_count


# In[103]:


df["Status"].values


# In[104]:


df_morning_city_count["Status"].values


# In[105]:


df_morning_city_count["Status"].index


# In[106]:


fig,ax=plt.subplots()
ax.pie(df_morning_city_count["Status"].values,labels=df_morning_city_count["Status"].index,autopct="%.2f%%",
      startangle=90)
plt.show()


# 1. They could be given a bonus for each trip they complete from the city to the airport in the morning rush time, This will ensure that less number of trips are cancelled 
# 2. Uber can pay for the gas mileags of drivers to come back to the city without a ride.
# 3. Pay drivers extra at night
# 4. Drivers canagain be gicen bonus to complete a trip from the airport in the evening. This will ensure that the supply increases at the airport.
# 5. Uber cal also pay drivers to come without a passanger to the airport.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




