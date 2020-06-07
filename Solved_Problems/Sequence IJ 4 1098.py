#!/usr/bin/env python
# coding: utf-8

# In[3]:


I = 0
J = 1
while True:
    x = J+2.0
    while True:
        if I >0.99 and I < 1.01:
            I = round(I)
            J = round(J)
            print('I='+str(I),'J='+str(J))
            J = J+1
            if J>x:
                J = J-3.0
                J = J+0.2
                break
        elif I > 1.80 and I < 2.01:
            I = round(I)
            J = round(J)
            print('I='+str(I),'J='+str(J))
            J = J+1
            if J>x:
                J = J-3.0
                J = J+0.2
                break
        elif I==0:
            print('I='+str(I),'J='+str(J))
            J = J+1
            if J>x:
                J = J-3.0
                J = J+0.2
                break
        else:
            print('I={:.1f}'.format(I),'J={:.1f}'.format(J))
            J = J+1
            if J>x:
                J = J-3.0
                J = J+0.2
                break
    I+=0.2
    if I >2.1:
        break


# In[ ]:




