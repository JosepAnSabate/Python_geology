#lists
llista = [1,2,3,4]
ll2 = llista
#els objectes tenen un dientificador
print(id(llista))
print(id(ll2))
print(id(llista)==id(ll2))

#info metodes lists
print(dir(list))
ll2.append(8)
print(ll2)
print(id(llista)==id(ll2)) #les llistes son mutables

#crear un nou objecte metode propi de les  llistes copy
ll2 =llista.copy()
print(id(llista))
print(id(ll2))

#accedir elements de la llista
print(llista[0])
print(llista[-1])
print(llista[:2])#imp 0 i 1
ll2=llista+[["a","b","c"]]#concat
print(ll2)
print(len(ll2))
print(ll2[-1])

#metode lliestes sort i reverse
a = [8,4,4,7,9,1]
a.reverse()
print(a)
a.sort()
print(a)
a.reverse()
print(a)

#sorted funcio no metode. Guarda el nou valor com a un nou objecte
b=sorted(a)
print(b)
print(id(a))
print(id(b))

#modificar elements de la llista
a[0]=20
a[1]=3
print(a)