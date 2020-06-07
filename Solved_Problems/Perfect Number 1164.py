#!/usr/bin/env python
# coding: utf-8

# In[2]:


N = int(input())
for i in range(N):
    lis = []
    c = 0
    X = int(input())
    for i in range(1,X):
        if X%i==0:
            lis.append(i)
    for i in lis:
        c += i
    if c == X:
        print(X,'eh perfeito')
    else:
        print(X,'nao eh perfeito')


# In[ ]:




