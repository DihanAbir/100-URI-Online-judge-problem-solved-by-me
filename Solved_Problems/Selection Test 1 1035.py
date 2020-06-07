#!/usr/bin/env python
# coding: utf-8

# In[6]:


values = input().split()
A,B,C,D = values

if int(B)>int(C) and int(D)>int(C):
    if (int(C)+int(D))>(int(A)+int(B)):
        if int(C)>=0 and int(D)>=0:
            if (int(A)%2==0):
                
                print("Valores aceitos")
else:
    print("Valores nao aceitos")


# In[7]:


values = input().split()
A,B,C,D = values

if int(B)>int(C) and int(D)>int(C) and (int(C)+int(D))>(int(A)+int(B)) and int(C)>=0 and int(D)>=0 and(int(A)%2==0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")


# In[ ]:




