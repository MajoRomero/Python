# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:22:36 2023

@author: Usuario
"""
"""
contador=1
texto="hola"
a=5.8
estado=True
print(type(a))
resultado=contador/3
print(resultado)
print(texto*10)
print("/n"*3)
print(texto*10)
pi=22/7
print(pi)
print("{:.60f}".format(pi))

lista2=[1,2,3,4,5,6,7,8,9]
lista=[1,5.3,"Hola",True]
print(len(lista)) #extension
print("ok")
print(lista[0])
print(lista[1])
#posicion cero en print
print(lista[-1])
#posicion -1 true en print, no existe el 4, ni -5 ojo es 0,1,2,3
tupla=(1,5.3,"Hola",True)
print(tupla[1])
print(tupla[-1])
lista[3]="R1" #reempazar
del lista [3] #eliminar esa columna (abajo)
print(lista)
#tupla[3]="R1"
#del tupla [3] no puede agraegar ni quitar
print(type(lista))
lista2.append(7)
#añade 
print(lista2)

dict1={"R1":"10.10.10.2",
       5001:"Cod_emp",
       True:"estado", 
       5.5:"saldo",
       "s1":1,
       "R1":"Otro",
       "curso":["Alumno1","Alumno2", "Alumno3"]}#no soporta valores suplicados, no es ordenado..no devuelve por la posicion
#r1 esta repetido se sobreescribe al ultimo
print(dict1)
print(dict1[5.5])
print(dict1["s1"])
"""
"""
print("ok")
print("ok")
dato=int(input("Ingrese un dato:"))
print(dato)
print(type(dato))
Nombre=input("Ingrese el Nombre:")
Apellido=input("Ingrese el Apellido:")
"""

"""
datos=10
nativa=100
print("estoy antes del if")
if datos==nativa:
    print("LAS VLAN son iguales")
    print("estoy dentro del if")
else:
    print("Las VLAN son diferentes")
print("Fuera del if")

acl=int(input("Ingrese el # de ACL:"))
if acl>=1 and acl<=99:
    print("La ACL es estandar")
elif acl>=100 and acl <=199:
    print("La ACL es extendida")
else:
    print("No no es un # de ACL")
    """
"""
print("ok")
print("ok")
o=[]
lista=["a","b","c","d"]
texto="CEC EPN curso de Python ESS"
for item in range(10,0,-1):
     print (item)
print("\n"*2)
for i in texto:
    if "o" in i:
        o.append(i)
        print(i, end="")
print("\n"*2)
for elemento in lista:
    print(elemento, end="*")
"""
"""
contar=int(input("ingrese el que se debe contar:"))
contador=1
while contador<=contar:
     print (contador)
     contador+=5
""" 
"""     
contar=int(input("ingrese el que se debe contar:"))
contador=1
while True:
     print (contador)
     contador += 1 #aumentar el contador +=
     if contador> contar:
         break
""" 
""" 
while True: 

    x=input("Enter a number to coun to:")
    
    if x== "q" or x== "quit":
        break

    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1 
        if y>x:
            break
""" 
"""
opcion 1
print("Ingrese un dato")
a=input()
print("Ingrese un dato")
b=input()
print("Ingrese un dato")
c=input()
"""
"""
opcion 2
def mensaje():
    print("Ingrese un dato")
mensaje()
a=input()
mensaje()
b=input()
mensaje()
c=input()
"""
"""
def saludo(nombre):
    print("Hola!,", nombre,"\n")
saludo("Ana")
saludo("Juan")
"""
"""
def saludo02(nombre1,nombre2):
    print("Hola!,", nombre1,"\n")
    print("Hola!,", nombre2,"\n")
    print("")
saludo02("Juan","Pedro")
#debe ser 2 porque asi es el modulo saludo02("Majo")
saludo02("Ana","Sandra")
"""
"""
#para pasar parametros
def direccion(ciudad,calle, num_casa):
    print("Su ciudad es:", ciudad)
    print("La calle de entrega es:", calle)
    print("La entrega se realizará en la casa # ", num_casa)
ci=input("Ingrese la ciudad de domicilio")
#bloque indentado es mover a otro nivel ojo!!! colocar fuera de def
nc=input("Ingrese numero de la casa:")
ca=input("Ingrese el sitio de referencia:")
direccion(ci, ca,nc)#escribo el orden que yo requiera
"""
"""opcion 1
def resta (num1,num2):
    print("La resta de:", num1, "-", num2, "es:", num1-num2)
resta (2,3) 
"""
"""
opcion2
def resta (num1,num2):
    print("La resta de:", num1, "-", num2, "es:", num1-num2)
resta (2,3)
resta (num1=10,num2=5)
resta(num1=5,num2=10)
resta(num2=100,num1=45)
resta(100,num2=90)
"""
"""
#pasar parámetros
def multiplicar(numero1,numero2):
    print(numero1*numero2)
    return(numero1*numero2)
multiplicar(5,8)
resultado=multiplicar(5,2)
print(type(resultado))
opt=resultado+1
print(opt)
"""
"""
def saludo03(lista):
    for item in lista:
        print("Hola!,", item)
    print("")
saludo03(["Ana"])
saludo03(["Juan", "Carlos"])
saludo03(["Juan", "Carlos", "Julio"])
"""
"""
def crealista(n):
    lista=[]
    for item in range (n+1):
        lista.append(item)
    return lista
print(crealista(10))
"""
