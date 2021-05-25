#diccionaris dict, permeten assignacio objecte valor
alumnes = {"Joan":24,"Maria":32,"Marta":26,"Marcel":28}

print(alumnes)
print(type(alumnes))
print(dir(dict))

claus = alumnes.keys()#command per impr nomez les claus
print(claus)
print(type(alumnes))
valors=alumnes.values()
print(type(valors))

#modificar els valors
alumnes["Joan"]+=1
print(alumnes)

#ex diccionari
diccionari_classes_roca = {"ignea":["basalt","granit","gabre"],
                           "metamorfica":["pissarra","esquist","gneis","marbre"],
                           "sedimentaria":["argila","gres","bretxes","carbo"]}

llista = ["basalt","pissarra","gres"]

#doble loop
for key, valor in diccionari_classes_roca.items():
    for roca in llista:
        if roca in valor:
            print("la roca: {0} es {1}".format(roca,key))
            