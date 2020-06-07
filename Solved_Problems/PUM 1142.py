#!/usr/bin/env python
# coding: utf-8

# In[3]:


N = int(input())
lis=[]
for i in range(1,(N*4)+1):
    lis.append(str(i))
    if len(lis) == 4:
        lis[3] = 'PUM'
        print(' '.join(lis))
        lis=[]


# In[ ]:




