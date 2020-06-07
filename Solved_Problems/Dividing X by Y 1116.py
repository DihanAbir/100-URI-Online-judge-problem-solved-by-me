#!/usr/bin/env python
# coding: utf-8

# In[2]:


N=int(input())
for i in range(N):
    X,Y = [int(i) for i in input().split()]
    if Y == 0:
        print('divisao impossivel')
    else:
        print('{:.1f}'.format(X/Y))


# In[ ]:




