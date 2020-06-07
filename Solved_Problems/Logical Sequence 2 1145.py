#!/usr/bin/env python
# coding: utf-8

# In[1]:


X,Y = [int (i) for i in input().split()]
lis=[]
for i in range(1,Y+1):
    lis.append(str(i))
    if len(lis) == X:
        print(' '.join(lis))
        lis = []


# In[ ]:




