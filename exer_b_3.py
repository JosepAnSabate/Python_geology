#ex4
class Empleado():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    
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
        
        self.subordinados = subordinados
        
    def calc_coste_personal(self):
        salario_total = 0
        for subordinado in self.subordinados:
            for x in self.salario:
                salario_total += x.salario
            
        return salario_total
    

tecnico1 = Tecnico('Alba', 28, '001', 11.5)
tecnico2 = Tecnico('Marta', 31, '002', 12.3)
tecnico3 = Tecnico('Laura', 25, '003', 10.6)

subordinados = [tecnico1,tecnico2,tecnico3]

manager1 = Manager('Julia', 45, subordinados)
manager2 = Manager('LLuisa', 45, subordinados)
tecnico4 = Tecnico('Rocio', 34, '004', 15.4)
tecnico5 = Tecnico('Marc', 54, '004', 17.4)
tecnico6 = Tecnico('LLuc', 24, '004', 19.4)
manager2.contratar(tecnico4)
manager2.contratar(tecnico5)
manager2.contratar(tecnico6)

admin = Administrativo('Pol', 31)

print(admin.calc_coste_personal())