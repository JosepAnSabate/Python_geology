#OOP

x=1
print(type(x))
print(type("hy"))

#function 
def hello():
    print("hola")
    
print(type(hello))

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age= age
        print(name)
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
    #def add_one (self, x): #metode
        #return x + 1
    
    #def bark(self):
        #print("bark")
        
d = Dog("Tim", 34)
d2 = Dog("Bill",21)
d.set_age(23)
#print(d.name)
print(d2.get_age(), d2.get_name())
print(d.get_age())

#print(d.add_one(5))
#print(type(d))

