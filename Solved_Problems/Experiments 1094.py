#!/usr/bin/env python
# coding: utf-8

# In[1]:


lis = []
coelhos = 0
ratos = 0
sapos = 0
N = int(input())
for i in range(N):
    c = input()
    lis.append(c)
for i in lis:
    if i[-1] == 'C':
        q = int(i[:-2])
        coelhos += q
    elif i[-1] == 'R':
        r = int(i[:-2])
        ratos += r
    else:
        s = int(i[:-2])
        sapos += s
total = coelhos+ratos+sapos
print('Total: {} cobaias'.format(total))
print('Total de coelhos:',coelhos)
print('Total de ratos:',ratos)
print('Total de sapos:',sapos)
print('Percentual de coelhos: {:.2f} %'.format((coelhos/total)*100))
print('Percentual de ratos: {:.2f} %'.format((ratos/total)*100))
print('Percentual de sapos: {:.2f} %'.format((sapos/total)*100))


# In[ ]:




