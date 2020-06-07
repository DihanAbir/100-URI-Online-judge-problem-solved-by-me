#!/usr/bin/env python
# coding: utf-8

# In[ ]:


M = []
summ = 0.0
L = int(input())
T = input()

for i in range(12):
    lis = []
    for j in range(12):
        num = float(input())
        lis.append(num)
    M.append(lis)

for a in range(12):
    for b in range(12):
        if a == L:
            summ+=M[a][b]

if T == "S":      
    print('{:.1f}'.format(summ))      
elif T == "M":
    print('{:.1f}'.format(summ/12))

