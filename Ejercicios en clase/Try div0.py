# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:17:38 2023

@author: Usuario
"""

#17-04-2023
# 1ro el que no sea general
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")
