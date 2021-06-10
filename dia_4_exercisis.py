  #!/usr/bin/python
# -*- coding: utf-8 -*-

import math 
import random

cadena_texto ="Geologia"


def contar_vocales(texto):
    """ Esta funcion devuelve un diccionario cuyas claves son las vocales y sus valores 
    hacen referencia al numero de veces que aparece dicha vocal en el texto."""
    
    texto = texto.lower()
    diccionario_vocales = {"a":0,"e":0,"i":0,"o":0,"u":0}
    for i in cadena_texto:
        if i in diccionario_vocales:  #por cada el de la cad de texto si...
            count= texto.count(i)   
            diccionario_vocales[i] += 1 #+1 en value dictionary

    return diccionario_vocales


numero_vocales= contar_vocales(cadena_texto)

print(help(contar_vocales)) #?
print(numero_vocales)

#ej 2

def generar_clave(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyz" + "0123456789" #variable
    clave = random.choices(caracteres, k = longitud)
    
    return clave

print(generar_clave(6))
print(generar_clave(8))

#ej 3
def factorial(n):
    if n == 0:
        return 1
    else:
        N = 1
        for i in range(1, n+1):
            N = N * i
        return(N)

a = factorial(5)
b = math.factorial(5)

print ("a: %s"%(a))
print ("b: %s"%(b))

# Los resultados deben ser iguales
print ("Coincidencia de resultados: %s"%(a==b))




