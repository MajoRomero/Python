# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 08:43:21 2023

@author: Usuario
"""
#12-04-2023



print("Para mayor información porfavor completar:")
Nombre=input("Ingrese su Nombre:")
Apellido=input("Ingrese su Apellido:")
Edad=int(input("Ingrese su Edad:"))
cliente1 = [ 
            Nombre, 
            Apellido, 
            Edad]
print("\n")
print("Para mayor información porfavor completar:")
Nombre2=input("Ingrese su Nombre:")
Apellido2=input("Ingrese su Apellido:")
Edad2=int(input("Ingrese su Edad:"))
cliente2 = [ 
            Nombre2, 
            Apellido2, 
            Edad2]
print(cliente2)

clientes = {
    "clientes": [cliente1,
                        cliente2]}
print(clientes)