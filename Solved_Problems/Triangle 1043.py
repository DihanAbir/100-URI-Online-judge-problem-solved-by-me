#!/usr/bin/env python
# coding: utf-8

# In[6]:


A,B,C = [float(i) for i in input().split()]
if A+B>C and B+C>A and C+A>B:
    print('Perimetro = {:.1f}'.format(A+B+C))
else:
    print('Area = {:.1f}'.format((A+B)*C/2))


# In[ ]:




