#class atributs= atributs que son especifics a la classe
# no a la instancia o a  objectes de la classe

class Person:
    number_of_people=0
    
    def __init__(self, name):
        self.name = name
        Person.add_person()
        #Person.number_of_people += 1
        
    # Class methods
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
    
p1 = Person("Tim")
p2 = Person("Jill")
print(Person.number_of_people_())

Person.number_of_people=8
print(Person.number_of_people) # Person es pespecific de la classe no de la instancia
print(p1.number_of_people)

