#!/usr/bin/env python
# coding: utf-8

# In[13]:


lis = []
c = 0
while True:
    n = int(input())
    c += 1
    lis.append(n)
    if c == 100:
        break
maxx= 0
for i in lis:
    if i > maxx:
        maxx=i
print(maxx)
print(lis.index(maxx)+1)

