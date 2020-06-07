#!/usr/bin/env python
# coding: utf-8

# In[4]:


I = 1
J = 7
while True:
    x=J-2
    while True:
        print('I='+str(I),'J='+str(J))
        J = J - 1
        if J<x:
            J=J+3
            break
    I=I+2
    J = J+2
    if I>9:
        break


# In[ ]:




