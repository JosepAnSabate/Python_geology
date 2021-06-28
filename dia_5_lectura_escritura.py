  #!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

t1 = time.time()

#evitar problemes barra/contabarra posar r
path1 = r"C:\Users\34639\eclipse-workspace\curspythongeol"

#o per evitar problesmes en llibreries
path2 = path1.replace("\\", "/") + "/"

print(path2)

#anar a directori
os.chdir(path2)

#crear arxiu
file = open("crearfile.txt","a")#write, read n appeand, write elimina i reescriu

#mostrar txt consola
#contenido = file.readlines()
#print(contenido)
#o
#for i in contenido:
#    print(i)
    
#afegir text a larxiu (rangs)
for i in range(0,20):
    t = "\t Hola %s \n "%(i) #\n salta de linea \t tabula
    print(t)
    file.write(t)
    
t2 = time.time()
tiempo_ejecucion= t2-t1
file.write("Ejecutado en {0}".format(tiempo_ejecucion))
file.close()