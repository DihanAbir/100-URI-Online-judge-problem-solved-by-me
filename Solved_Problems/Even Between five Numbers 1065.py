#!/usr/bin/env python
# coding: utf-8

# In[5]:


a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())

z = [a,b,c,d,e]
count = 0
for i in z:
    if i%2==0:
        count = count+1
print(count,'valores pares')


# In[ ]:




