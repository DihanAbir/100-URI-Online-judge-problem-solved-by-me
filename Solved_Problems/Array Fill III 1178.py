#!/usr/bin/env python
# coding: utf-8

# In[3]:


X = float(input())
N = []
N.append(X)
for i in range(100):
    N.append(N[i]/2)
    print('N['+str(i)+'] = {:.4f}'.format(N[i]))


# In[ ]:




