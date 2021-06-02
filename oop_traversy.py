class Customer:
    def __init__(self, name, membersip_type):
        self.name = name
        self.membership_type = membersip_type
        
    def update_membership(self, new_membership):
        #invoke an api
        #update a db
        #calc costs
         self.membership_type = new_membership 
        
    def print_all_customers(customers):
        for customer in customers:
            print(customer)
           
#c = Costumer("Caleb", "Gold")
#print(c.name, c.membership_type)

#c2 = Costumer("Brad", "Bronze")
#print(c2.name, c2.membership_type)
# 0 en una llista

customers = [Customer("Caleb", "Gold"),
             Customer("Brad", "Bonze")]
        
print(customers[0].name)
print(customers[1].name)

customers[1].update_membership("Gold")

print(customers[1].membership_type)

Customer.print_all_customers(customers)
