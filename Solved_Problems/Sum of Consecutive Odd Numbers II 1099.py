#!/usr/bin/env python
# coding: utf-8

# In[2]:


N = int(input())
for i in range(N):
    X,Y = [int (i) for i in input().split()]
    summ = 0
    if X > Y:
        for i in range(Y+1,X):
            if i %2 !=0:
                summ+=i
        print(summ)
    else:
        for i in range(X+1,Y):
            if i %2 !=0:
                summ+=i
        print(summ)


# In[ ]:




