import os
import sys
import math
import numpy as np
import pandas


# funcions predefinides
#localitzar script en un directori
#rutes ente cometes, barra normal no invertida!
os.chdir("C:/Users/34639/eclipse-workspace/")

#metodes associats a les llibreries
print(dir(os))

#instalar llibreria
#cmd->cd ruta py39/scripts->pip install nomllibreria instalar com admin si hi ha problema

#tius dobjectes mutables/inmutables
#objecte inmutable
a = "hola"

print(a)

a.upper()

print(a)
#no funciona, per a poderho fer declarar nova variable per a crear un nou objecte
b = a.upper()

print(b)
#identificar identificador ram,
print(id(a))
print(id(b))

c = a
print(id(c))

#objectes mutables, per ex llistes
#llista
d = ["1","a","3",4]#num ente cometes semmagatzema com a text

print(d)

e=d
print(d)
e.append("afegit1")

print(d)
print(e) #igual resultat preque d ha mutat
print(id(d))
print(id(e))  #son el mateix objecte ram

#comparacio llibreries numpy i math
#funcio per calc arrel quadr sense llibreria
def sqrt_s(x):
    f = x**(1.0/2)
    return f

g = sqrt_s(2)
print(g)

h = math.sqrt(2)
print("l'arrel quadrada de la llibr. math es: %s"%(h))#evitar accents a qualsevol lloc

i = np.sqrt(2)
print("l'arrel quadrada de la llibr numpy es: %s"%(i))

#numpy pot calc per exemple larrel2 de tots els valors el duna martiu o llista
print(np.sqrt([1,3,6,7]))
#print(math.sqrt([1,3,6,7])) error

#info llibreries
#print(dir(np))
#print(dir(math))

#ajuda llibreia
#print(help(np.sqrt))
#print(help(math.sqrt))

#object.shape
j = np.array(["a",1,["b","c"]])

print(j.shape)#3 elements la 2a llista la compta com un element


print(type(j))



