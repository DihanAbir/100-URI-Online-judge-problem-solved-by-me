#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input())

for i in range(1,N+1):
    if i == 1:
        print(i,i,i)
        print(i,i**2+1,i**3+1)
    else:
        print(i,i**2,i**3)
        print(i,i**2+1,i**3+1)

