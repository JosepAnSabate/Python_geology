import numpy as np

t =(2,)
print(type(t))
print(dir(t)) #atr disponibles de les tuples

u=(-1.33,34.22) + t
print(u)
u = u[:2]
print(u)
x,y=u
print(x)
print(y)

#funcions

def suma_media(valors):
    "funcio que realitza la suma dels valors i la media"
    suma = sum(valors)
    media = np.mean(valors)    
    t = (suma,media)
    return (t)

suma,media = suma_media([1,2,3,4])
print(suma)
print(media)
print(help(suma_media)