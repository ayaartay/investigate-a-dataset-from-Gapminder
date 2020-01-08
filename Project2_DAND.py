#!/usr/bin/env python
# coding: utf-8

# In[78]:


#importing Python packages 
import pandas as pd
import numpy as np
import matplotlib as mp
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')


# In[79]:


# Importing time series data from the local drive through creating dataframes 
# (the original source: https://www.gapminder.org/data/)
# The economic time series data is on GDP, Gini index and Billionaires per 1M population for countries across the world   
gdp_df = pd.read_csv(r'/Users/ainurartay/Desktop/DAND/project2/data (gapminder)/gdppercapita_us_inflation_adjusted.csv')
gini_df = pd.read_csv(r'/Users/ainurartay/Desktop/DAND/project2/data (gapminder)/gini.csv')
bln_df = pd.read_csv(r'/Users/ainurartay/Desktop/DAND/project2/data (gapminder)/dollar_billionaires_per_million_people.csv')


# In[81]:


# We start exploring the data by viewing the contents (structure, time range) of the dataframes using .head() function 
gdp_df.head()


# In[82]:


gini_df.head()


# In[83]:


bln_df.head()


# In[13]:


#Exploring the data for completeness (nulls) and data types 
gdp_df.info()


# In[16]:


#checking the completeness of the data
gdp_df.isnull().sum()


# In[19]:


# Creating a new (sub) data frame with selected 4 countries (China, South Korea, United States, Venezuela). 
# "_mod" in the name of the data frame stands for "modified"  
gdp_mod = gdp_df.loc[[35, 155, 181, 185], :]


# In[20]:


# Checking if the new data farme captures the right countires
gdp_mod


# In[21]:


# Doing the same for the 2 other data frames and limiting the time range for 1960-2017 as in the gdp_mod dataframe
gini_mod = gini_df.loc[[35, 158, 186, 190], '1960' :'2017']


# In[22]:


# Checking the new dataframe
gini_mod


# In[25]:


# For convenience, I am transposing the dataframe. This transposed frame will be used to plot a graph.
# "_t" in the name stands for "transposed"
gdp_mod_t=gdp_mod.transpose() 


# In[26]:


# Checking the transposed dataframe
gdp_mod_t


# In[84]:


# Moving the first row with names of the countries as column names (next 3 lines of code)
new_header = gdp_mod_t.iloc[0]


# In[85]:


gpd_mod_t=gdp_mod_t[1:]


# In[86]:


gdp_mod_t.columns=new_header


# In[28]:


# Deleting the first row with the country names and the last 3 rows with null values for Venezuela 
gdp_mod_t.drop(['country', '2015', '2016', '2017'], inplace=True)


# In[40]:


# Checking the result
gdp_mod_t


# In[38]:


# Similar manipulation for Gini index and Billionaires per 1M population
gini_mod_t=gini_mod.transpose()


# In[39]:


# Renameing the column names from indeces to country names 
gini_mod_t.rename(columns={35:'China', 158:'South Korea', 186:'United States', 190:'Venezuela'}, inplace=True)


# In[33]:


gini_mod_t


# In[34]:


# For comparability, dropping the last 3 years from the data frame 
gini_mod_t.drop(['2015','2016','2017'])


# In[41]:


# Checking info in the new data frame
gdp_mod_t.info()


# In[42]:


# Plotting line graphs for 4 countries to see the GDP trends.
# Upward movement for all except for Venezuela  
gdp_mod_t.plot()


# In[43]:


# Visualizing Gini index trends 
gini_mod_t.plot()


# In[69]:


# Manipulating the data on billionaires per 1M population -- selecting the 4 countires into a new dataframe 
# and transposing the dataframe
bln_mod_t=(bln_df.loc[[7, 43, 52, 53], :]).transpose()


# In[70]:


# Checking the dataframe
bln_mod_t


# In[71]:


# Renaming the column names from indeces to appropriate country names 
bln_mod_t.columns=['China', 'South Korea', 'United States', 'Venezuela']


# In[75]:


# Dropping the first row (non-numerical)
bln_mod_t=bln_mod_t.drop('country')


# In[76]:


# Checking the new dataframe
bln_mod_t.info()


# In[77]:


# Visualizing the data on billionaires per 1M population
bln_mod_t.plot()


# In[ ]:




