# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:21:35 2023

@author: Usuario
"""

"""
def sum_digits (n):
    if n<10:
        return n
    else:
        return n % 10 + sum_digits(n//10)
print(sum_digits(12345))#suma ver despues
"""
#modulo
"""
opcion 1
import math #siempre llamar sino no funcionara 
print(math.sin(math.pi/2))
"""
"""
opcion 2
from math import pi, sin #importa varias
print (sin(pi/2))
"""
"""
#opcion 2

from math import * #importa varias
print (sin(pi/2))
"""
"""
import math as m #lo llame o le importe como m
print(m.sin(m.pi/2))
"""
"""
print("majo")
from math import pi as p, sin as s #renombra las variables
resultado=s(p/2)
print(resultado)
"""

#puedo traer tambien carpetas-modulos con 
#import funargs

#cpython crea este archivo cuando corro
"""
ejercicio hizo majo
numero=int(input("Ingrese el número que desea ver la serie:"))
if numero>=0 :
    def parámetro(n):
        lista=[]
        for item in range (n+1):
            lista.append(item)
            return lista
    print(parámetro(8))
print("Ingrese número válido")
"""
def fibonacci(n):
    a, b = 0,1
    while a <= n:
        print(a, end=' ')
        """c=a+b
        a=b
        b=c"""
        a, b = b, a+b
    print()
fibonacci(8)

    


