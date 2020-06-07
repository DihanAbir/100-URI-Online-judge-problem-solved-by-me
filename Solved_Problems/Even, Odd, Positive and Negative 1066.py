#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lis = [a,b,c,d,e]
evecount=0
oddcount=0
poscount=0
negcount=0
for i in lis:
    if i%2==0:
        evecount+=1
    if i%2!=0:
        oddcount+=1
    if i>0:
        poscount+=1
    if i<0:
        negcount+=1
print(evecount,'valor(es) par(es)')
print(oddcount,'valor(es) impar(es)')
print(poscount,'valor(es) positivo(s)')
print(negcount,'valor(es) negativo(s)')   


# In[ ]:




