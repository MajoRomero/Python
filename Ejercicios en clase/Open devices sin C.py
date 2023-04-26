# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:58:21 2023

@author: Usuario
"""

lista=[]
file = open("devices.txt","r")
for item in file:
    item=item.strip("C")#"" coloca espacios
    lista.append(item)
    print (item)
file.close()