elements = [
    'Aigua',
    'Bicicleta',
    'Te',
    'Sol',
    'Automobilistic',
    'Ordinador']

element_actual = 0

def element_mes_llarg(elements):
    element_actual= '' 
    for x in elements:
        if len(x) > len(element_actual):
            element_actual= x
    return element_actual
print(element_mes_llarg(elements))