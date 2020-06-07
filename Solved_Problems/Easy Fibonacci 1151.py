#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input())
a = 0
b = 1
lis=[]
if N==1:
    print(a)
else:
    lis.append(str(a))
    lis.append(str(b))
for i in range(2,N):
    c = a+b
    a = b
    b = c
    lis.append(str(c))
print(' '.join(lis))


# In[ ]:




