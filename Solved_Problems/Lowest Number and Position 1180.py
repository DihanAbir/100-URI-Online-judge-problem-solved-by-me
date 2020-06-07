#!/usr/bin/env python
# coding: utf-8

# In[2]:


N = int(input())
X = []
a = list(map(int,input().split()))
for i in range(N):
    X.insert(i,a[i])
c = X[0]
for i in range(1,N):
    if X[i] < c:
        c = X[i]
print('Menor valor:',c)
print('Posicao:',X.index(c))

