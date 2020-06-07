#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input())
lis = []
for i in range(0,N):
    num = int(input())
    lis.append(num)
    
for i in lis:
    if i%2==0 and i/2 < 0:
        print('EVEN NEGATIVE')
    if i%2==0 and i/2 > 0:
        print('EVEN POSITIVE')
    if i%2 != 0 and i/2 < 0:
        print('ODD NEGATIVE')
    if i%2 != 0 and i/2 > 0:
        print('ODD POSITIVE')
    if i==0:
        print('NULL')


# In[ ]:




