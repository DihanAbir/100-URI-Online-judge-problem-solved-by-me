#!/usr/bin/env python
# coding: utf-8

# In[2]:


N = int(input())
for i in range(N):
    X = int(input())
    lis=[]
    for i in range(1,X+1):
        if X%i==0:
            lis.append(i)
    if len(lis)>2:
        print(X,'nao eh primo')
    else:
        print(X,'eh primo')

