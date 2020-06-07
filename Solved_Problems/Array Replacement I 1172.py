#!/usr/bin/env python
# coding: utf-8

# In[2]:


X = []
while True:
    X.append(int(input()))
    if len(X)==10:
        break
for i in range(len(X)):
    if X[i]==0 or X[i]<0:
        X.remove(X[i])
        X.insert(i,1)
for i in range(len(X)):
    print('X['+str(i)+'] =',X[i])


# In[ ]:




