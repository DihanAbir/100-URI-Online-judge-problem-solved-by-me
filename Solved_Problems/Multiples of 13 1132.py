#!/usr/bin/env python
# coding: utf-8

# In[1]:


X =int(input())
Y = int(input())
summ = 0
if X<Y:
    for i in range(X,Y+1):
        if i%13!=0:
            summ +=i
    print(summ)
else:
    for i in range(Y,X+1):
        if i%13!=0:
            summ +=i
    print(summ)


# In[ ]:




