#!/usr/bin/env python
# coding: utf-8

# In[2]:


X,Y = [int(i) for i in input().split()]
z = {1 : 4.00, 2 : 4.50, 3 : 5.00, 4 : 2.00, 5 : 1.50}
v= z.get(X)
print('Total: R$ {:.2f}'.format(v*Y))


# In[ ]:




