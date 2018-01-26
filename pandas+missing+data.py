
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[8]:


d = {'A':[1,2, np.nan], 'B':[5, np.nan, np.nan],'C':[1,2,3]}


# In[9]:


d


# In[10]:


df= pd.DataFrame(d)


# In[11]:


df


# In[13]:


df.dropna(axis=1)


# In[14]:


df.dropna(thresh=2)


# In[15]:


df.fillna(value='FILL VALUE')


# In[16]:


df['A'].fillna(value=df['A'].mean())

