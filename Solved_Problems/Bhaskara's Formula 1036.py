#!/usr/bin/env python
# coding: utf-8

# In[4]:


A,B,C = [float(i) for i in input().split()]
import math

z = B**2-4*A*C
if A!=0 and z>-1:
    R1 = (-B+(math.sqrt(z)))/(2*A)
    R2 = (-B-(math.sqrt(z)))/(2*A)
    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))
else:
    print('Impossivel calcular')

