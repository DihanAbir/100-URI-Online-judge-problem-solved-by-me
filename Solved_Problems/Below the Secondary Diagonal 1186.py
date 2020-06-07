#!/usr/bin/env python
# coding: utf-8

# In[ ]:


O = input()
M = []
summ = 0
c = 0

for i in range(12):
    lis = []
    for j in range(12):
        num = float(input())
        lis.append(num)
    M.append(lis)
    
for i in range(12):
    for j in range(12-i,12):
        summ += M[i][j]
        c += 1
        

if O == 'S':
    print('{:.1f}'.format(summ))
if O == 'M':
    print('{:.1f}'.format(summ/c))


# In[ ]:




