# There are two major types of relationships between classes :
    
#     1. Aggregation (also called HAS-A relationship) :
        
#         Ex:
#             Customer(Class2) --> HAS-A --> Address(Class1)


class Customer:
    
    def __init__(self, name, gender, address):
        
        self.name = name
        self.gender = gender
        self.address = address
        
    def edit_profile(self, new_name, new_city, new_pin, new_state):
        
        self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)
        
class Address:
    
    def __init__(self, city, pin, state):
        
        self.city = city
        self.pin = pin
        self.state = state
        
    def change_address(self, new_city, new_pin, new_state):
        
        self.city = new_city
        self.pin = new_pin
        self.state = new_state
        

add = Address("New Delhi", 1234, "Delhi")    
cust = Customer("Arunesh", "Male", add)

cust.edit_profile("Nikhil", "Mumbai", 5678, "Maharashtra")


print(cust.name)
print(cust.address.city)
print(cust.address.pin)
print(cust.address.state)
        
        
            
            
#     2. Inheritance (also called IS-A relationship) :
        
#         Ex:
#             SmartPhone(Class1) ---> IS-A --> Product(Class2)   ==> This means all the things of products are applicable on smartphone..
#             Car(Class1) ---> IS-A --> Vehicle(Class2) ==> This means all the things of vehicle is applicable on car..
            