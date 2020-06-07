#!/usr/bin/env python
# coding: utf-8

# In[6]:


value = input().split()
A,B,C = value
pi = 3.14159

TRIANGULO = (float(A)*float(C))/2
CIRCULO = pi*(float(C)*float(C))
TRAPEZIO = (float(A)+float(B))*float(C)/2
QUADRADO = float(B)*float(B)
RETANGULO = float(A)*float(B)

print('TRIANGULO: {:.3f}'.format(TRIANGULO))
print('CIRCULO: {:.3f}'.format(CIRCULO))
print('TRAPEZIO: {:.3f}'.format(TRAPEZIO))
print('QUADRADO: {:.3f}'.format(QUADRADO))
print('RETANGULO: {:.3f}'.format(RETANGULO))

