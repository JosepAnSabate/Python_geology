
a = "Curs geologia py"

if a ==2:
    print("es compleix a=2")
elif a.__contains__("py"):
    print(" Existeix la paraula py dins de la variable")
else:
    print("No es compleix cap de les condicions")
    


llista = [1,2,3,4,5,"Hola","Adeu"]

for i in llista:
    
    if type(i) ==int:
        llista = i**2
        print("{0} al quadrat es: {1}".format(i,llista))
        
    else:
        print("%s es un text"%(i))
      
  
if False:
    print("Falso")
elif True:
    print("Verdadero")
else:
    print("Finalmente Verdadero!") 
    
n=36
if n%2 ==0:
    print("par")
else:
    print("impar")