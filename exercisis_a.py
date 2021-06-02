#ex1

b = ["h","o","l","a"]
c = []

for bs in b:
    c.append(bs.upper())

print(c)
    
#ex2
e=9
f = 1/2*(2/(e-3))+e**3
g = 1/2*(2/e-3)+e**3

print(f)
print(g)

#ex 3

diccionari={'Monday':2,'Tuessay':5,
            'Wednesday':8,'Thursday':0,
            'Friday': 4,'Saturday':0,
            'Sunday':0}

print(dir({})) #visualize the methods and attributes of any Python object

print(sum(diccionari.values()))

for x in diccionari.values():
    print(x)

sum = 0
for x in diccionari.values():
        sum = sum + x
    
print(sum)

#ex4
tupla=(7,1,2,5,8,6,100,25)

for p in tupla:
    if p%2 == 0:
        print(p,"es parell")
    else: 
        print(p,"es imparell")




...     