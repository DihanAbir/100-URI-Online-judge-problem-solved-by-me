#!/usr/bin/env python
# coding: utf-8

# In[1]:


c = 0
par = []
impar = []
while True:
    n = int(input())
    c += 1
    if n%2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if len(par) == 5:
        for i in range(len(par)):
            print('par[' + str(i) + '] =',par[i])
        par = []
    if len(impar) == 5:
        for i in range(len(impar)):
            print('impar[' + str(i) + '] =',impar[i])
        impar = []
    if c == 15:
        for i in range(len(impar)):
            print('impar[' + str(i) + '] =',impar[i])
        for i in range(len(par)):
            print('par[' + str(i) + '] =',par[i])
        break


# In[ ]:




