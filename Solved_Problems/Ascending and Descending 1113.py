#!/usr/bin/env python
# coding: utf-8

# In[2]:


while True:
    X,Y = [int(i) for i in input().split()]
    if X > Y:
        print('Decrescente')
    elif X < Y:
        print('Crescente')
    else:
        break


# In[ ]:




