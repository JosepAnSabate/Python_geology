#!/usr/bin/python

rang_n = range(0,11)

quadrats=[]

for i in rang_n:
    quadrat = i**2
    quadrats.append(quadrat)
    
print(quadrats)

quadrats_2=sum([i**2 for i in rang_n])

print(quadrats_2)