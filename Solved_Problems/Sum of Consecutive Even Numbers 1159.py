#!/usr/bin/env python
# coding: utf-8

# In[4]:


lis = []
summ = 0
while True:
    lis = []
    summ = 0
    X = int(input())
    if X == 0:
        break
    else:
        for i in range(X,X+10):
            if i%2 == 0:
                lis.append(i)
    for i in lis:
        summ += i
    print(summ)

