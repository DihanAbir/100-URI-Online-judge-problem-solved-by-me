#!/usr/bin/env python
# coding: utf-8

# In[3]:


values1 = input().split()
x1,y1 = values1

values2 = input().split()
x2,y2 = values2

import math

Distance = math.sqrt( (float(x2)-float(x1) )**2 + (float(y2) - float(y1))**2 )

print('{:.4f}'.format(Distance))


# In[ ]:




