# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:23:56 2023

@author: Usuario
"""
file = open("devices.txt", "a")
while True:
    newItem = input("Necesitas un nuevo dispositivo:")
    if newItem() == "exit":
        print("Todo hecho")
        break
    file.write(newItem + "\n")  
file.close()

#19-04-2023

    