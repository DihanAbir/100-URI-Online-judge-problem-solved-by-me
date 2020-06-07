#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input())
for i in range(N):
    X,Y = [int(i) for i in input().split()]
    c = 0
    for i in range(X,(Y*2)+X):
        if i % 2 != 0:
            c += i
    print(c)

