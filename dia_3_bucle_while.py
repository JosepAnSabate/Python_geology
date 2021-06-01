#!/usr/bin/python
import time
#combienacio entre bucle i condicional, no molt utilitzats
#quants cops 500 es divisible per 2
n = 500

num_de_cops=0

while n>=1:
    n//=2
    print(n)
    num_de_cops +=1

print(num_de_cops)

x = True 
m=0
while x ==True:
        m+=1
        time.sleep(2)
        print(m)