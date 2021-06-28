#!/usr/bin/python 
# -*- coding: latin-1 -*-

import os 
import time

t1= time.time() 

path = r"C:\Users\silve\Documents\Curso_python\Segunda Edicion\Z_Nuevos_Ejercicios_Tema_6\01_Lectura_y escritura"


path = path.replace("\\","/") + "/"

print(path)

os.chdir(path)

f = open("ejemplo.log","w")

for i in range(0,20):
    t = "\t \t Hola %s \n \n "%(i)
    print(t)
    f.write(t)


t2= time.time()

tiempo_ejecucion= t2-t1 

f.write("Ejecutado en {0}".format(tiempo_ejecucion))

f.close()
    