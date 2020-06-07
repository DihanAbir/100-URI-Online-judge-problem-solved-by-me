#!/usr/bin/env python
# coding: utf-8

# In[4]:


ifirst = input()
isecond = input()
ithird = input()

v = {'ave':{'carnivoro':'aguia','onivoro':'pomba'},
    'mamifero':{'onivoro':'homem','herbivoro':'vaca'}}

iv = {'inseto':{'hematofago':'pulga','herbivoro':'lagarta'},
     'anelideo':{'hematofago':'sanguessuga','onivoro':'minhoca'}}

if ifirst == 'vertebrado':
    print(v[isecond][ithird])
    
if ifirst == 'invertebrado':
    print(iv[isecond][ithird])


# In[ ]:




