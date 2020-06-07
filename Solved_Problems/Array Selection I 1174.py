#!/usr/bin/env python
# coding: utf-8

# In[1]:


A = []
for i in range(100):
    x = float(input())
    A.append(x)
for i in range(len(A)):
    if A[i] < 11:
        print('A[' + str(i) + '] =',A[i])


# In[ ]:




