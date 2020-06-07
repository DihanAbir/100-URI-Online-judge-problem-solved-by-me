#!/usr/bin/env python
# coding: utf-8

# In[2]:


notes = [100,50,20,10,5,2,1]
N = int(input())
print(N)
for i in notes:
    if N/i:
        y = int(N/i)
        print(y,'nota(s) de R$',str(i)+',00')
        N = N%i
    else:
        print('0 nota(s) de R$',str(notes[6])+',00')


# In[ ]:




