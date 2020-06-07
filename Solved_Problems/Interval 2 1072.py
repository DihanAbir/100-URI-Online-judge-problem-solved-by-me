#!/usr/bin/env python
# coding: utf-8

# In[6]:


n = int(input())
lis=[]
for i in range(0,n):
    nums= int(input())
    lis.append(nums)
    
count=0
ncount=0
for i in lis:
    if i >= 10 and i <= 20:
        count+=1
    else:
        ncount+=1
print(count,'in')
print(ncount,'out')


# In[ ]:




