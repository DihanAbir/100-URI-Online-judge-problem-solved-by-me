#!/usr/bin/env python
# coding: utf-8

# In[3]:


def validity():
    while True:
        a =float(input())
        if a >= 0 and a <= 10:
            break
        else:
            print('nota invalida')
    while True:
        b = float(input())
        if b >= 0 and b <= 10:
            break
        else:
            print('nota invalida')
    avg = (a+b)/2
    print('media = {:.2f}'.format(avg))
def novo():
    print('novo calculo (1-sim 2-nao)')
    user_input = float(input())
    if user_input == 1:
        validity()
        novo()
    elif user_input == 2:
        return
    else:
        novo()
validity()
novo()


# In[ ]:




