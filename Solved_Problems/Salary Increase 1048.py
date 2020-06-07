#!/usr/bin/env python
# coding: utf-8

# In[8]:


a = float(input())
perlist = [15,12,10,7,4]
    
if a > 2000.00:
    x = a*(perlist[4]/100)
    a += x
    print('Novo salario: {:.2f}'.format(a))
    print('Reajuste ganho: {:.2f}'.format(x))
    print('Em percentual:',perlist[4],'%')
    
if a > 1200 and a < 2000.01:
    x = a*(perlist[3]/100)
    a += x
    print('Novo salario: {:.2f}'.format(a))
    print('Reajuste ganho: {:.2f}'.format(x))
    print('Em percentual:',perlist[3],'%')
    
if a > 800 and a < 1200.01:
    x = a*(perlist[2]/100)
    a += x
    print('Novo salario: {:.2f}'.format(a))
    print('Reajuste ganho: {:.2f}'.format(x))
    print('Em percentual:',perlist[2],'%')
    
if a > 400 and a < 800.01:
    x = a*(perlist[1]/100)
    a += x
    print('Novo salario: {:.2f}'.format(a))
    print('Reajuste ganho: {:.2f}'.format(x))
    print('Em percentual:',perlist[1],'%')

if a > -1 and a < 400.01:
    x = a*(perlist[0]/100)
    a += x
    print('Novo salario: {:.2f}'.format(a))
    print('Reajuste ganho: {:.2f}'.format(x))
    print('Em percentual:',perlist[0],'%')


# In[ ]:




