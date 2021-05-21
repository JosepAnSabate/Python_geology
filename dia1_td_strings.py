#Strings
a = "Py para geologos"# "" = ''
print(a)
#primer element d'una cadena de text
b = a[0]
print(b)
#ultim element d'una cadena de text
c = a[-1]
print(c)
#primeres lletres
d = a[0:3]
print(d)
#ultims 3
e = a[-3:]
print(e)
#sumas cadenes de text
a = a + " classe variables"
print(a)
#afegir un num
f = a + " 1" # nomes es pot concatencar variables del mateix tipus
g = f + str(2)
print(g)
#separar paraules
h = a.split(" ")
print(h)
#tipus de dades
print(type(a))
print(type(h))
#longitud variable
print(len(a))
print(len(h))
print(a[-1])
print(h[-1])
#funcions tipiques string
print(dir(str))
#o
print(dir(a))
i = a.upper() #.lower minuscula
print(i)
#cops q apareix una lletra
print(a.count("p"))

#immutabilitat = sempre k es modifica lobjecte  es trenca la relacio
j = "Python"
k = j
print(j==k)
k = k.upper()
print(j==k)


