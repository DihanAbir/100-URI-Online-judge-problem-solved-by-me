#!/usr/bin/env python
# coding: utf-8

# In[9]:


n = int(input())
if n%2==0:
    for i in range(n+1,n+12,2):
        print(i)
if n%2!=0 :
    for i in range(n,n+12,2):
        print(i)


# In[ ]:




