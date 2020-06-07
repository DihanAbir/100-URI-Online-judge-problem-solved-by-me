#!/usr/bin/env python
# coding: utf-8

# In[3]:


X = []
V = int(input())
for i in range(10):
    X.append(V)
    print('N['+str(i)+'] =',V)
    V = V*2

