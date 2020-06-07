#!/usr/bin/env python
# coding: utf-8

# In[8]:


X = int(input())
Y = int(input())
tmp = 0
if X < Y:
    tmp = X
    X = Y
    Y = tmp
if X > Y or X == Y:
    for i in range(Y+1,X):
        if i%5 == 2 or i%5 == 3:
            print(i)

