#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = []
for i in range(20):
    Y = int(input())
    N.append(Y)
N=N[::-1]
for i in range(len(N)):
    print('N[' + str(i) + '] =',N[i])

