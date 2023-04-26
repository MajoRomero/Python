# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:10:46 2023

@author: Usuario
"""

#Taller 25 min 18-04-2023

def readint(prompt, min, max):
    try:
        prompt=int(input("Ingrese un valor: "))
        if prompt<min or prompt >max:
            print("El valor no está dentro del rango permitido"+str(min)+"hasta"+str(max))
            return readint(print("Ingrese un valor nuevamente: en el rango permitido -10 a 10", end=""),-10,10)
    except ValueError:
        print("Error en el ingreso")
        return readint(print("Ingrese un valor nuevamente: en el rango permitido -10 a 10", end=""),-10,10)
    except IndexError:#fuera del rango
        print("El valor no está en el rango permitido -10 a 10")
        return readint(print("Ingrese un valor nuevamente: en el rango permitido -10 a 10", end=""),-10,10)
    else:
        return prompt

v = readint("Ingrese un número de -10 to 10: ", -10, 10)
print("El número es:", v)