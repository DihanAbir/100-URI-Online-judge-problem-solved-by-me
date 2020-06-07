#!/usr/bin/env python
# coding: utf-8

# In[1]:


count = 0
Inter = 0 
Gremio = 0
Empates = 0
def novo():
    c = input('Novo grenal (1-sim 2-nao)')
while True:
    a,b = [int(i) for i in input().split()]
    count+=1
    if a > b:
        Inter+=1
    elif b > a:
        Gremio+=1
    else:
        Empates+=1
    print('Novo grenal (1-sim 2-nao)')
    c = int(input())
    if c != 1 and c!=2:
        novo()
    if c == 2:
        break

print(count,'grenais')
print('Inter:'+str(Inter))
print('Gremio:'+str(Gremio))
print('Empates:'+str(Empates))
if Inter > Gremio:
    print('Inter venceu mais')
elif Inter < Gremio:
    print('Gremio venceu mais')
else:
    print('Não houve vencedor')  


# In[ ]:




