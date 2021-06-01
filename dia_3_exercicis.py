#!/usr/bin/python
# -*- coding: utf-8 -*-
import time 
#Autor: Josep Andreu Sabate

#ej1 script que sume 100 primeros numeros

num = 0

for i in range(0,101):
    num =+ num + i
    
print(num)

#ej 2 Lea dos numeros por teclado, y muestre el mayor de ambos. Hagalo con y sin la
#funcion max()

a = 7 #int(input("Ingrese el numero a: "))
b = 8 #int(input("Ingrese el numero b: "))

if a > b:
    print("a ",(a),"es mayor q b",(b))
else: 
    print("b ",(b)," es mayor que a",(a))

num_mayor = max(a, b)
print("numero mayor es:", num_mayor)

#3 
#Comprueba si en la lista existe la roca “gabro”, en caso contrario anyadalo a la lista. 

igneas= ["pumita","obsidiana","basalto","granito"]

c= "gabro"

if (c in igneas):
    print ("El elemento existe")
else:
    igneas.append(c)

print(igneas)

#ex4

ossos = {"Grizzly": "enfadado", "Pardo":"amistoso", "polar":"amistoso"}

print(ossos)

for oso in ossos.values():
    if oso == "amistoso":
        print("Hola, "+oso + "!")
    else:
        print("corre, corre, corre es un %s!"%(oso))


#ex 5
 
tcero = time.time()
              

# check for factors
for i in range(0, 21):
    if (i) == 0:
        print(i, "is not a prime number")  
    else:
        print(i, "is a prime number")
