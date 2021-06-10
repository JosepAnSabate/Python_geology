#!/usr/bin/python
# -*- coding: utf-8 -*-

# triangulo de floyd
n = input("Escriu un num: ")

def Triangulo_de_floyd(n):
    n = int(n)
    if n == 0:
        print("El numero de filas es igual o 0")
    else:
        numero = 1
        
        for i in range(n):
            for j in range(i+1):
                print(numero, end= ' ')
                numero += 1
                
            print()
    
            
Triangulo_de_floyd(n)

#podem posar el valor tantes vegades com bulguem
condicion = True

while condicion == True:
    n = input("Escribe un numero o False si quieres terminar: ")
    
    if str(n) == "False":
        print("Sortim del loop")
        condicion = False 
    else:
        Triangulo_de_floyd(n)
        