#!/usr/bin/env python
# coding: utf-8

# In[3]:


while True:
    a =float(input())
    if a >= 0 and a <= 10:
        break
    else:
        print('nota invalida')
while True:
    b = float(input())
    if b >= 0 and b <= 10:
        break
    else:
        print('nota invalida')
avg = (a+b)/2
print('media = {:.2f}'.format(avg))


# In[ ]:




