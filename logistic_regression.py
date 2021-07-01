#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[11]:


data=pd.read_csv('placement_data_full_class.csv')
data


# In[66]:


data["gender"] = data["gender"].astype('category')
data["status"] = data["status"].astype('category')
data.dtypes


# In[22]:


data["gender"] = data["gender"].cat.codes
data["status"] = data["status"].cat.codes


# In[72]:


import seaborn as sns
sns.countplot(data['status'])
plt.show()


# In[73]:


sns.countplot(data['gender'])


# In[61]:


data


# In[63]:


X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values
  
Y


# In[64]:


from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, 
                                                    test_size=0.2)
  
data.head()


# In[65]:


from sklearn.linear_model import LogisticRegression
  
classifier = LogisticRegression(random_state=0, solver='lbfgs',max_iter=1000).fit(Xtrain,Ytrain)

classifier.score(Xtest, Ytest)


# In[ ]:




