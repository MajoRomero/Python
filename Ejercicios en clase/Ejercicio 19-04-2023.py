# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:21:33 2023

@author: Usuario
"""
#Abrir documentos que no estan en la misma carpeta 

print ("ok")
file = open("C:/Users/Usuario/Descargas/devices.txt","r")
#ruta de acceso file = open("C:/Usuarios/Usuario/Descargas/devices.txt","r")

for item in file:
    print (item)
file.close()





