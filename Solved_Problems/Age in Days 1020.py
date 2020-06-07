#!/usr/bin/env python
# coding: utf-8

# In[2]:


x = int(input())

if x >= 360:
    year = int(x/365)
    day = int(x%365)
    month = 0
    if day >= 30:
        month = int(day/30)
        day = int(day%30)
else:
    year = 0
    month = int(x/30)
    day = int(x%30)
    
print(year,'ano(s)'+'\n'+str(month)+' mes(es)'+'\n'+str(day)+' dia(s)')
        

