#!/usr/bin/env python
# coding: utf-8

# In[1]:


X = int(input())
summ = 0
c = 0
lis = []
while True:
    Z = int(input())
    if Z > X:
        break
for i in  range(X,Z):
    lis.append(i)
for i in lis:
    summ += i
    c += 1
    if summ > Z:
        print(c)
        lis.clear()


# In[ ]:




