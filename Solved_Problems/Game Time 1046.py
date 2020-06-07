#!/usr/bin/env python
# coding: utf-8

# In[3]:


x,y = [int(i) for i in input().split()]

z = y-x

if z < 0:
    z = 24+(y-x)
    print('O JOGO DUROU '+str(z)+' HORA(S)')
elif x==y:
    print('O JOGO DUROU 24 HORA(S)')
else:
    print('O JOGO DUROU '+str(z)+' HORA(S)')


# In[ ]:




