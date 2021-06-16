#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import csv
import pandas as pd


# In[3]:


placement=pd.read_csv('D:\Placement_Data_Full_Class.csv')


# In[4]:


placement.head()


# In[5]:


type(placement)


# In[6]:


placement.shape


# In[7]:


placement.describe()


# In[8]:


placement.head(10)


# In[9]:


placement.isnull()


# In[11]:


placement=placement[placement.salary<600000]


# In[ ]:




