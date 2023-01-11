#!/usr/bin/env python
# coding: utf-8

# # Task-3:Exploratory Data Analysis - Retail
#                (Level - Beginner)

# # **The Sparks Foundation:Graduate Rotational Internship Program**

# # **Data science and Bussiness Analytics Intern**

# Author:Nikita Kumbhar.

# By using Exploratory Data Analysis(EDA) to find hidden information in data.

# In[1]:


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import style
import plotly.express as px


# In[2]:


# Load the dataset
#url = "https://bit.ly/3i4rbWl"
df = pd.read_csv("SampleSuperstore.csv")
df.head(10) # See the first 5 rows


# In[3]:


df.shape


# In[4]:


df.info()


# **We see in this dataset 9994 rows and 13 columns and zero null values.**

# In[5]:


df.isna().sum()


# **In this dataset zero null value.**

# In[6]:


df.describe()


# In[7]:


df.columns


# In[8]:


df['Ship Mode'].unique()


# In[9]:


df['State'].unique()


# In[10]:


df['Region'].unique()


# In[11]:


df['Category'].unique()


# In[12]:


df['Sub-Category'].unique()


# In[13]:


df['Segment'].unique()


# In[14]:


df['City'].unique()


# # Data visualization

# In[15]:


corr=df.corr()
fig,ax=plt.subplots(figsize=(5,4))
sns.heatmap(corr,annot=True,ax=ax , cmap='coolwarm') 


# **In the correlation plot we seen that the there is no correlation .**

# # To find top 10 staest in maximum profit.

# In[51]:


states_profit = pd.DataFrame(df.groupby('State')['Profit'].sum())


# In[113]:


states_profit_df = states_profit.sort_values( by="Profit",ascending=False)
df3=states_profit_df.head(10)
df3


# In[114]:


df3.plot(kind="bar",color="blue",xlabel="state",ylabel="Profit" ,rot=40,figsize=(15,6))


# **This plot show top 10 states which is California,New York,Washington,Michigan,Virginia,Indiana,Georgia,Kentucky,Minnesota and Delaware.**

# # To find top 10 staest in minimum profit.

# In[111]:


states_profit_df = states_profit.sort_values( by="Profit",ascending=True)
df4=states_profit_df.head(10)
df4


# In[112]:



df4.plot(kind="bar",color="blue",xlabel="state",ylabel="Profit" ,rot=40,figsize=(15,6))


# **There is a negative profit in Tables.
# Texas,Ohio,Pennsylvania,IIlinois,North Carolina,Colorado,Tennessee,Arizona,Florida,Oregon these staes has minimum profit.**

# # To find which top 10 City gives maximum profit.

# In[43]:


cities_profit = pd.DataFrame(df.groupby('City')['Profit'].sum())


# In[44]:


cities_profit = cities_profit.sort_values( by="Profit",ascending=False)
df1=cities_profit.head(10)
df1


# In[45]:



df1.plot(kind="bar",color="blue",xlabel="City",ylabel="Profit" ,rot=40,figsize=(15,6))


# **These top 10 city gives maximum profit.**

# # To find which 10 City gives minimum profit.

# In[48]:


cities_profit = cities_profit.sort_values( by="Profit",ascending=True)
df2=cities_profit.head(10)
df2


# In[49]:


df2.plot(kind="bar",color="blue",xlabel="City",ylabel="Profit" ,rot=40,figsize=(15,6))


# **There is a negative profit in Tables.
# These 10 city gives minimum profit after sale.**

# # Region wise visualization.

# In[76]:


Region_info = df.groupby('Region').sum()
Region_info 


# In[93]:


plt.bar(Region_info.index , Region_info['Sales'],color=["red",'yellow','green','blue'])
plt.xticks(Region_info.index)
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()


# **Highest sales in West Region and East Region. Less sales in South Region. Focused on South and Central Region to increse sale.**

# In[94]:


plt.bar(Region_info.index , Region_info['Profit'],color=["red",'yellow','green','blue'])
plt.xticks(Region_info.index)
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()


# **In this plot we see West and East region has more profit as compair to South and Central region.**

# In[92]:


plt.bar(Region_info.index , Region_info['Quantity'],color=["red",'yellow','green','blue'])
plt.xticks(Region_info.index)
plt.xlabel("Region")
plt.ylabel("Quantity")
plt.show()


# **In four region, South region has less quantity sales as compair to other region.Highest quantity sales in West region.**

# In[91]:


plt.bar(Region_info.index , Region_info['Discount'],,color=["red",'yellow','green','blue'])
plt.xticks(Region_info.index,color="red")
plt.xlabel("Region")
plt.ylabel("Discount")
plt.show()


# **In this four region Central region get more discount on sales and less discount get in South region.**

# # Category wise visualization.

# In[23]:


category_info = df.groupby('Category').sum()
category_info 


# In[104]:


plt.bar(category_info.index , category_info['Sales'],color=["red",'yellow','green'])
plt.xticks(category_info.index)
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()


# **In this 3 category Technology has more sales as compair to other category.**

# In[105]:


plt.bar(category_info.index , category_info['Discount'],color=["red",'yellow','green'])
plt.xticks(category_info.index)
plt.xlabel("Category")
plt.ylabel("Discount")
plt.show()


# **In the category, Office Suppliers get more discount on sales as compair to Furniture and Technology.**

# In[106]:


plt.bar(category_info.index , category_info['Quantity'],color=["red",'yellow','green'])
plt.xticks(category_info.index)
plt.xlabel("Category")
plt.ylabel("Quantity")
plt.show()


# **In the category, Office Suppliers sales more quantity as compair to Furniture and Technology**

# In[107]:


plt.bar(category_info.index , category_info['Profit'],color=["red",'yellow','green'])
plt.xticks(category_info.index)
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()


# **In the category, Technology  get more profit on sales. Furniture has less profit on sales.**

# In[118]:


subcategory_info = df.groupby('Sub-Category').sum()
subcategory_info 


# In[120]:


plt.bar(subcategory_info.index , subcategory_info['Profit'])
plt.xticks(category_info.index)
plt.xlabel("Sub-Category")
plt.ylabel("Profit")
plt.show()


# In[121]:


plt.bar(subcategory_info.index , subcategory_info['Sales'])
plt.xticks(category_info.index)
plt.xlabel("Sub-Category")
plt.ylabel("Sales")
plt.show()


# In[122]:


plt.bar(subcategory_info.index , subcategory_info['Quantity'])
plt.xticks(category_info.index)
plt.xlabel("Sub-Category")
plt.ylabel("Quantity")
plt.show()


# In[123]:


plt.bar(subcategory_info.index , subcategory_info['Discount'])
plt.xticks(category_info.index)
plt.xlabel("Sub-Category")
plt.ylabel("Discount")
plt.show()


# # Ship Mode wise Visualization.

# In[57]:


ship_mode_info = df.groupby('Ship Mode').sum()
ship_mode_info 


# In[115]:


plt.bar(ship_mode_info.index , ship_mode_info['Sales'],color=["red",'yellow','green','blue'])
plt.xticks(ship_mode_info.index)
plt.xlabel("Ship Mode")
plt.ylabel("Sales")
plt.show()


# **In 4 Ship Mode, Standard Class has more sales, Same Day has less sales.Focus on Same Day , First Class and Second Class to improve sales.**

# In[95]:



plt.bar(ship_mode_info.index , ship_mode_info['Quantity'],color=["red",'yellow','green','blue'])
plt.xticks(ship_mode_info.index)
plt.xlabel("Ship Mode")
plt.ylabel("Quantity")
plt.show()


# ****In 4 Ship Mode, Standard Class has more quantity sales, Same Day has less quantity sales.Focus on other ship mode quantity to improve sales.****

# In[96]:


plt.bar(ship_mode_info.index , ship_mode_info['Profit'],color=["red",'yellow','green','blue'])
plt.xticks(ship_mode_info.index)
plt.xlabel("Ship Mode")
plt.ylabel("Profit")
plt.show()


# ****In 4 Ship Mode, Standard Class has more profit on sales, Same Day has less profit on sales.****

# # Segment wise visualization.

# In[68]:


segment_info = df.groupby('Segment').sum()
segment_info 


# In[97]:


plt.bar(segment_info.index , segment_info['Profit'],color=["red",'green','blue'])
plt.xticks(segment_info.index)
plt.xlabel("Segment")
plt.ylabel("Profit")
plt.show()


# **On the above plot we see Consumer segment has more profit as compair to Corporate and Home Office segment.**

# In[98]:


plt.bar(segment_info.index , segment_info['Sales'],color=["red",'green','blue'])
plt.xticks(segment_info.index)
plt.xlabel("Segment")
plt.ylabel("Sales")
plt.show()


# **On the above plot we see Consumer segment has more sales as compair to Corporate and Home Office segment.**

# In[99]:


plt.bar(segment_info.index , segment_info['Quantity'],color=["red",'yellow','blue'])
plt.xticks(segment_info.index)
plt.xlabel("Segment")
plt.ylabel("Quantity")
plt.show()


# **On the above plot we see Consumer segment has more Quantity sale as compair to Corporate and Home Office segment .**

# In[100]:


plt.bar(segment_info.index , segment_info['Discount'],color=["red",'yellow','green'])
plt.xticks(segment_info.index)
plt.xlabel("Segment")
plt.ylabel("Discount")
plt.show()


# **On the above plot we see Consumer segment has more Discount as compair to Corporate and Home Office segment.**

# In[21]:


def categorical_colum_investigaton(col_name):

    f,ax = plt.subplots(1,3, figsize=(18,6))
    df['Region'].value_counts().plot.pie(autopct='%1.1f%%',ax=ax[0],shadow=True, cmap='Set3')
    ax[0].set_title(f'Profit')
    
    df['Category'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True,cmap='Set3',ax=ax[1])
    ax[1].set_title(f'Profit')
    
    
    df['Sub-Category'].value_counts().plot.bar(cmap='Set3',ax=ax[2])
    ax[2].set_title(f'Profit')
    


# In[22]:


categorical_colum_investigaton('Profit')


# **In the above grapha we see that the west region is 32% profit which is highest as compair to other region and 16.2% profit in south region.
# In the category 60.3% profit gain in office supplies,21.2% profit gain in Furniture and 18.5% profit gain in Technology.
# In the sub-Category Binders,paper is present in highest profit category and supplies,Machines and Copiers is present in lowest profit Category.**
# 

# # Conclusion:
# 

# ### 1)Shipment method used in each region is mostly Standard class, so obviously there is maximum sale in this shipment method.
# ### 2)Maximum category is of office suppliers where as maximum sale and profit is in technology. 
# ### 3)Highest sale and profit is in Consumer segment as compared to corporate and home office. 
# ### 4)Highest sale in West region as compared to other region, Standard class is used in each region where as First class is same in West and East. There is a negative profit in Tables.

# In[ ]:




