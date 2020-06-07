#!/usr/bin/env python
# coding: utf-8

# In[6]:


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

z = [a,b,c,d,e,f]
x=[]
count = 0

for i in z:
    if i > -1:
        count += 1
        x.append(i)
print(len(x),'valores positivos')

suM = 0
for i in x:
    suM += i
    
avg = suM/len(x)
print('{:.1f}'.format(avg))


# In[ ]:




