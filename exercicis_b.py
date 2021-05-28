# -*- coding: utf-8 -*-
#explicació primera línia https://stackoverflow.com/questions/14041020/my-first-step-in-python
#ex1
from astroid.bases import manager
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

#ex 2
from ex_b_2 import element_mes_llarg

#ex3
class Empleado():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print('Hola hem dic', self.nombre)

    def buscar_subordinado(self):
        if self.id:
            print(self.nombre, "es", self.id)
        else:
            print('id no disponible')
class Manager(Empleado):
    def __init__(self, nombre, edad, subordinados=[]):
        super().__init__(nombre, edad)

        self.subordinados = subordinados

    def contratar(self, subordinado):
        self.subordinados.append(subordinado)


class Tecnico(Empleado):
    def __init__(self, nombre, edad, id, salario):
        super().__init__(nombre, edad)

        self.id = id
        self.salario = salario

tecnico1 = Tecnico('Alba', 28, '001', 11.5)
tecnico2 = Tecnico('Marta', 31, '002', 12.3)
tecnico3 = Tecnico('Laura', 25, '003', 10.6)

subordinados = [tecnico1,tecnico2,tecnico3]

manager1 = Manager('Julia', 45, subordinados)

tecnico4 = Tecnico('Rocio', 34, '004', 12.4)
manager1.contratar(tecnico4)
#bucle
for subordinado in manager1.subordinados:
    subordinado.buscar_subordinado()

