#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import csv
import pandas as pd


# In[28]:


placement=pd.read_csv(r'D:\Placement_Data_Full_Class.csv')


# In[5]:


placement.head()


# In[6]:


type(placement)


# In[7]:


placement.shape


# In[8]:


placement.describe()


# In[9]:


placement.head(10)


# In[11]:


placement.isnull()


# In[29]:


placement['salary']


# In[30]:


placement.loc[2]


# In[31]:


placement.head(5)


# In[19]:


placement.head(5)


# In[39]:


placement.loc[['science','commerce']]


# In[21]:


placement.iloc[2,1,0]


# In[32]:


placement[:3]


# In[33]:


placement.describe()


# In[34]:


placement[3:6]


# In[38]:


placement.iloc['Central']


# In[40]:


placement.iloc[2,1,0]


# In[41]:


placement['specialisation'].head(20)


# In[42]:


placement['mba_p']


# In[43]:


placement[['sl_no','salary']][:10]


# In[44]:


placement.gender.iloc[3]


# In[45]:


placement[placement.specialisation=='Mkt&HR']


# In[50]:


placement.iloc[2]


# In[56]:


placement.iloc[[2,1,0]]


# In[57]:


placement[placement.ssc_b.isin(['Central'])].head()


# In[58]:


placement[placement.ssc_b.isin(['Central'])].describe()


# In[59]:


placement.isnull().salary


# In[60]:


missing_value=placement.isnull().sum()


# In[61]:


missing_value[0:10]


# In[63]:


total_missing_cells=np.product(placement.shape)
total_missing=missing_value.sum()
(total_missing/total_missing_cells)*100


# In[64]:


placement.dropna()


# In[65]:


columns=placement.dropna(axis=1)
columns.head()


# In[66]:


print("columns originally in the file: %d\n" % placement.shape[1])
print("columns after dropping columns: %d\n" %columns.shape[1])


# In[ ]:




