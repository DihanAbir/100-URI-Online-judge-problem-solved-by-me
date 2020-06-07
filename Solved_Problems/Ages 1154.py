#!/usr/bin/env python
# coding: utf-8

# In[2]:


c = 0
v = 0
lis = []
while True:
    n = int(input())
    if n < 0:
        break
    else:
        v += 1
        lis.append(n)
for i in lis:
    c += i
print('{:.2f}'.format(c/v))

