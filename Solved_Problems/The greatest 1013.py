#!/usr/bin/env python
# coding: utf-8

# In[15]:


values = input().split()
a,b,c = values

m = int((int(a) + int(b) + abs((int(a) - int(b)))) / 2)
n = int((m + int(c) + abs(m-int(c))) /2)

print(n,'eh o maior')


# In[ ]:




