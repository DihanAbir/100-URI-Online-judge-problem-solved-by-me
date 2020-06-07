#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for i in range(1,11):
    x = float(input())
    y = float(input())
    if i != x and i != y:
        print('nota invalida')
    else:
        print('media =',(x+y)/2)
        


# In[ ]:


for i in range(0,11):
    x = float(input())
    if x==i:
        p = x
    else:
        print('nota invalida')
for i in range(0,11):
    y = float(input())
    if y == i:
        q = y
        print('media =',(p+q)/2)
    else:
        print('nota invalida')
                
    


# In[ ]:


x = [0,1,2,3,4,5,6,7,8,9,10]
p = float(input())
for i in x:
    if p != i:
print('nota invalida')
q = float(input())
for i in x:
    if q != i:
        print('nota invalida')
    else:
        print('media =',(p+q)/2)


# In[ ]:


x = [0,1,2,3,4,5,6,7,8,9,10]
p = float(input())
for i in x:
    if p != i:
        q = float(input())
        for i in x:
            if q == i:
                print('media =',(p+q)/2)
            else:
                print('nota invalida')       
    else:
        print('nota invalida')


# In[5]:


p = float(input())
while p > 10 or p < -1:
    print('nota invalida')
    break
if p > -1 and p < 11:
    print('b')
        
    
        
    


# In[ ]:




