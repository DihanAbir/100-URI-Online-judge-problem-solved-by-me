#!/usr/bin/env python
# coding: utf-8

# In[2]:


total = 0
c = 0
dic = {'---':0,
       '--*':1,
       '-*-':2,
       '*--':4,
       '***':7,
       '**-':6,
       '*-*':5,
       '-**':3}
while True:
    n = input()
    if n != 'caw caw':
        total += dic[n]
    if n == 'caw caw':
        print(total)
        total = 0
        c += 1
    if c == 3:
        break

