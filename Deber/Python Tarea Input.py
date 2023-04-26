# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:31:05 2023

@author: Usuario
"""
x=input("Ingrese su Nombre: ")
y=input("Ingrese su Apellido: ")
z=input("Ingrese su Ubicación: ")
w=input("Edad: ")
print("")
print(f"Hola, el usuario se llama {x} y apellida {y}, con una edad de {w} años. \nLa persona se ubica en {z}")
print("")
print("Hola, el usuario se llama {} y apellida {}, con una edad de {} años. \nLa persona se ubica en {}".format(x,y,w,z))