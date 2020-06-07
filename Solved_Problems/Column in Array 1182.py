#!/usr/bin/env python
# coding: utf-8

# In[ ]:


M = []
C = int(input())
T = input()
summ = 0

for i in range(12):
    lis = []
    for j in range(12):
        val = float(input())
        lis.append(val)
    M.append(lis)
    
for i in range(12):
    for j in range(12):
        if j == C:
            summ += M[i][j]
if T == 'S':
    print('{:.1f}'.format(summ))
if T == 'M':
    print('{:.1f}'.format(summ/12))


# In[ ]:




