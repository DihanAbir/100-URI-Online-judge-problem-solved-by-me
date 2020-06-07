#!/usr/bin/env python
# coding: utf-8

# In[1]:


S = 1
c = 2
for i in range(2,40,2):
    S += (i+1)/c
    c *= 2
print('{:.2f}'.format(S))

