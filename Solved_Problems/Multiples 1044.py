#!/usr/bin/env python
# coding: utf-8

# In[10]:


A,B = [int(i) for i in input().split()]
if A%B==0 or B%A==0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')

