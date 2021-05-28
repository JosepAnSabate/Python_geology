#ex4

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

class Administrativo(Empleado):
    def __init__(self, nombre, edad, subordinados=[]):
        super().__init__(nombre, edad)
        
    def calc_coste_persona(self, manager):
            coste_total = 0
                for subordinado in subordinados:
                    coste_total += subordinado.salario
                return coste_total 
                    

tecnico1 = Tecnico('Alba', 28, '001', 11.5)
tecnico2 = Tecnico('Marta', 31, '002', 12.3)
tecnico3 = Tecnico('Laura', 25, '003', 10.6)
tecnico4 = Tecnico('LLuis', 30, '004', 9.3)
tecnico5 = Tecnico('Mar', 29, '005', 8.6)

subordinados = [tecnico1,tecnico2,tecnico3]


manager1 = Manager('Julia', 45, subordinados)
manager2 = Manager('Marc', 55, subordinados)

manager2.contratar(tecnico4)
manager2.contratar(tecnico5)

for subordinado in manager1.subordinados:
    subordinado.calc_coste_persona()


