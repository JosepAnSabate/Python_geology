#!/usr/bin/python
# -*- coding: utf-8 -*-

# Variable local/global
a = 500

def xy ():
    # global a per a  ferla global
    a = 200
    print(a)
    return(a)

xy()

print(a)

b = [1,2,3,4]

def xz ():
    #b = [5,6,7]
    b[0] = 10 #variable mutable
    print(b)
    return(b)

xz()

print(b)

#exemple funcio
c = 346
d = 34

def suma_diferencia(x,y):
    suma = x+y
    diferencia = abs(x-y)
    
    return (suma, diferencia)
    
e,f = suma_diferencia(c,d)

print(e)
print(f)

g = 500
h = 10

print(suma_diferencia(g, h))