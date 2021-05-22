#ranges : sequencies de numeros enters immutables. molt util en els bucles
rang = range(0,10)#el 10 no linclou
print(rang)
print(list(rang))#conv rang en llista

#bucle amb ranges
for i in range(0,10):
    print(i)

#sets
c = set([1,2,3,4,5,6])
print(c)
print(type(c))
print(dir(c))

c.add(3)#no s'afegira
print(c)
text = "Bon dia"

s_text = set(text)
print(s_text)
print(len(text))

homes = set([1,2,3,4,5,6])
dones = set([7,8,9,9,11,12])

ambdos_sexes = homes | dones
print(ambdos_sexes)

valors_a = set(range(0,10))
valors_b = set([7,8,9,9,11,12,12,12])

interseccio = valors_a & valors_b #& han destar als dos sets
print(interseccio)