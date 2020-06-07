#!/usr/bin/env python
# coding: utf-8

# In[5]:


employees_number = int(input())
worked_hours_in_a_month = int(input())
amount_received_per_hour = float(input())

SALARY = worked_hours_in_a_month*amount_received_per_hour

print('NUMBER =',employees_number)
print('SALARY = U$ {:.2f}'.format(SALARY))


# In[ ]:




