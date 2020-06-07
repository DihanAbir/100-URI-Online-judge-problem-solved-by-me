#!/usr/bin/env python
# coding: utf-8

# In[18]:


a = int(input())
b = int(input())
summ=0
if a < b:
    if a%2==0:
        for i in range(a+1,b,2):
            summ+=i
        print(summ)
    if a%2!=0:
        for i in range(a,b,2):
            if i==a:
                continue
            summ+=i
        print(summ)
        
elif b < a:
    if b%2==0:
        for i in range(b+1,a,2):
            summ+=i
        print(summ)
    if b%2!=0:
        for i in range(b,a,2):
            if i==b:
                continue
            summ+=i
        print(summ)
else:
    print(summ)


# In[ ]:




