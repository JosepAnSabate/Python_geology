class Costumer:
    def __init__(self, name, membersip_type):
        self.name = name
        self.membership_type = membersip_type
        
        
c = Costumer("Caleb", "Gold")
print(c.name, c.membership_type)

c2 = Costumer("Brad", "Bronze")
print(c2.name, c2.membership_type)

costumers = [Costumer("Caleb", "Gold"),
             Costumer("Brad", "Bonze")]
        
print(costumers[1].name)