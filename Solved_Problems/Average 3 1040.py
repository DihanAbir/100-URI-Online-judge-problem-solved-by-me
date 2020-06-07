#!/usr/bin/env python
# coding: utf-8

# In[8]:


N1,N2,N3,N4 = [float(i) for i in input().split()]

Media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/(2+3+4+1)
print('Media: {:.1f}'.format(Media))

if Media >= 7.0:
    print('Aluno aprovado.')
if Media < 5.0:
    print('Aluno reprovado.')
if Media >= 5.0 and  Media < 7.0:
    print('Aluno em exame.')
    s = float(input())
    print('Nota do exame: {:.1f}'.format(s))
    reavg = (Media+s)/2
    if reavg >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(reavg))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(reavg))
    


# In[ ]:




