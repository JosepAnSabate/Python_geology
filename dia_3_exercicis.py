#!/usr/bin/python
#Autor: Josep Andreu Sabate

#ej1 script que sume 100 primeros numeros

num = 0

for i in range(0,101):
    num =+ num + i
    
print(num)

#ej 2 Lea dos numeros por teclado, y muestre el mayor de ambos. Hagalo con y sin la
#funcion max()

a = int(input("Ingrese el numero a: "))
b = int(input("Ingrese el numero b: "))

if a > b:
    print("a ",(a),"es mayor q b",(b))
else: 
    print("b ",(b)," es mayor que a",(a))

