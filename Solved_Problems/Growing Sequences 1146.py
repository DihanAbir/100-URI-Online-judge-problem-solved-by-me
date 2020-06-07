#!/usr/bin/env python
# coding: utf-8

# In[1]:


while True:
    lis=[]
    X = int(input())
    if X==0:
        break
    else:
        for i in range(1,X+1):
            lis.append(str(i))
        print(' '.join(lis))

