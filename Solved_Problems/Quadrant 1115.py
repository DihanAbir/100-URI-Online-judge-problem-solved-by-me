#!/usr/bin/env python
# coding: utf-8

# In[1]:


while True:
    X,Y = [float(i) for i in input().split()]
    if X==0 or Y==0:
        break
    while X!=0 or Y!=0:
        if X > 0 and Y > 0:
            print('primeiro')
            break
        elif X < 0 and Y > 0:
            print('segundo')
            break
        elif X < 0 and Y < 0:
            print('terceiro')
            break
        elif X > 0 and Y < 0:
            print('quarto')
            break


# In[ ]:




