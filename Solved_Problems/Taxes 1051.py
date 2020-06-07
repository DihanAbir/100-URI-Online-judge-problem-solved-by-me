#!/usr/bin/env python
# coding: utf-8

# In[13]:


x = float(input())
tax = [8/100,18/100,28/100]

if x > 2000:
    y = x-2000
    ot = 1000
    tf = 1500
    
    if y-ot > 0:
        r1 = y-ot
        result1 = tax[0]*1000
        
        if r1-tf > 0:
            r2 = r1-tf
            result2 = tax[1]*1500
            
            if r2 > 0:
                result3 = tax[2]*r2
                total = result1+result2+result3
                print('R$ {:.2f}'.format(total))
        
        elif r1 <= 1500:
            y = y-ot
            print('R$ {:.2f}'.format(y*tax[1]+result1))
                
    elif y <= 1000:
        print('R$ {:.2f}'.format(y*tax[0]))
        
else:
    print('Isento')


# In[ ]:





# In[ ]:




