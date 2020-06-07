#!/usr/bin/env python
# coding: utf-8

# In[11]:


x = int(input('Dia '))
a,b,c = map(int,input().split(' : '))

y = int(input('Dia '))
d,e,f = map(int,input().split(' : '))

day = y-x
hour = d-a

if hour < 0:
    hour = 24 + hour
    day = day - 1

mint = e-b
if mint < 0:
    mint = 60+mint
    hour = hour - 1
sec = f-c
if sec<0:
    sec = 60+sec
    mint = mint - 1
    
if(day <= 0):
    day = 0

print(day,'dia(s)')
print(hour,'hora(s)')
print(mint,'minuto(s)')
print(sec,'segundo(s)')


# In[ ]:


valor = input().split()
d1 = int(valor[1])

valores = input().split(" : ")
h1,m1,s1 = list(map(int,valores))


valor = input().split()
d2 = int(valor[1])

valores = input().split(" : ")
h2,m2,s2 = list(map(int,valores))

day = y-x
hour = d-a

if hour < 0:
    hour = 24 + hour
    day = day - 1

mint = e-b
if mint < 0:
    mint = 60+mint
    hour = hour - 1
sec = f-c
if sec<0:
    sec = 60+sec
    mint = mint - 1
    
if(day <= 0):
    day = 0

print(day,'dia(s)')
print(hour,'hora(s)')
print(mint,'minuto(s)')
print(sec,'segundo(s)')


# In[16]:


valor = input('Dia ').split()
d1 = int(valor[0])

valores = input().split(" : ")
h1,m1,s1 = list(map(int,valores))


valor = input('Dia ').split()
d2 = int(valor[0])

valores = input().split(" : ")
h2,m2,s2 = list(map(int,valores))

d = d2 - d1

h = h2 - h1
if(h < 0):
    h = 24 + h
    d = d - 1

m = m2 - m1 
if(m < 0):
    m = 60 + m
    h = h - 1

s = s2 - s1
if(s < 0):
    s = 60 + s
    m = m - 1

if(d <= 0):
    d = 0

print(d,"dia(s)")
print(h,"hora(s)")
print(m,"minuto(s)")
print(s,"segundo(s)")


# In[ ]:





# In[ ]:




