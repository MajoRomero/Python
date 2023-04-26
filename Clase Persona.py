# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:09:04 2023

@author: Usuario
"""

#18-04-2023
class Persona:
    
    def  __init__(self, nombre, edad):##no olvidarse para construccion doble_ _)
        self.nombre=nombre
        self.edad=edad
        
    def presentarse(self):
        print(f"¡Hi,mi nombre es {self.nombre} y tengo {self.edad}  años!")
    
    def cumplir_anios(self):
        self.edad +=1
        print("!Feliz Cumpleaños! Ahora tengo {} años.".format(self.edad))   
        #f colocar {} para que se muestre a la pantalla .format(vel)
        #print(f"!Feliz Cumpleaños! Ahora tengo {self.edad} años.")
        #\n para espacio
        #ajusta a="" print(a.ljust(15))
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        print(f"Mi nombre ha sido cambiado a {self.nombre}.")
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
persona1=Persona("Juan", 16)
persona2=Persona("Ana", 36)
persona1.presentarse()
persona2.presentarse()
persona1.cumplir_anios()
persona1.cambiar_nombre("Juan Carlos")
persona1.es_mayor_de_edad()
persona2.cumplir_anios()
persona2.cambiar_nombre("Ana Maria")
persona2.es_mayor_de_edad()







