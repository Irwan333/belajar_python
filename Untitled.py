#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


np.arange(10,50)


# In[5]:


np.arange(10,50,2)


# In[72]:


np.linspace(0,8,9).reshape(3,3)


# In[13]:


np.random.rand(25)


# In[33]:


arr = np.arange(1,26)
arr1 = arr.reshape(5,5)
arr1


# In[35]:


arr1[2:6,1:5]


# In[37]:


arr[19]


# In[39]:


arr.max()


# In[40]:


arr.min()


# In[41]:


arr.argmax()


# In[42]:


arr.argmin()


# In[63]:


arr2 = arr[arr>10]
arr2


# In[65]:


arr2[arr2<=20]


# In[66]:


arr[arr>10][arr[arr>10]<=20]


# In[69]:


arr3 = arr[arr>10]
arr4 = arr3[arr3<=20]
arr4


# In[ ]:




