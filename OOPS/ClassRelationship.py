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
            
        #         Inheritance is used to create a new class from an existing class.  
        #         It provides reusability and reduces code duplication.
        #         Inheritance can be used in multiple levels.
        #         Inheritance can be used to add new properties or methods to a class.
        #         Inheritance can be used to override existing properties or methods in a class.
        #         Inheritance can be used to hide existing properties or methods in a class.
        #         Inheritance can be used to restrict the access of properties or methods in a class.
        
        
        # Data members (Variables), Member Functions (Methods), Constructor, Destructor --> these are the things which are inherited from parent class to child class.
        # Private members are not Inherited...
        
        # Types of Inheritance :
            # 1. Single Inheritance : One child class inherits from one parent class.
            # 2. Multiple Inheritance : One child class inherits from multiple parent classes.
            # 3. Multilevel Inheritance : One child class inherits from multiple parent classes, where each parent class inherits from another parent class.
            # 4. Hierarchical Inheritance : One child class inherits from multiple parent classes, but all parent classes are related to each other.
            # 5. Hybrid Inheritance : One child class inherits from multiple parent classes, and some of the parent classes are related to each other.
        
        # Inheritance and Polymorphism :
            # Inheritance allows us to reuse code and reduce code duplication.
            # Polymorphism allows us to perform different actions based on the object type.
            # Polymorphism is achieved using method overriding and method overloading.
            # Method overriding is used to override a method in a child class with the same name and parameters as in the parent class.
            
class User:
    
    def login(self):
        print("User logged in")
        
    def register(self):
        print("User registered")
        
class Student(User):  # --> This tell that Student class is a subclass of User class...
    
    def enroll(self):
        print("Student enrolled")
        
    def review(self):
        print("Student reviewed")
        
s1 = Student()

s1.enroll()
s1.review()
s1.login()  # --> This will call the login() method from User class...
s1.register()  # --> This will call the register() method from User class...    --> But Reverse is not Possible...



# Ex1 (Inheriting Constructors):

class Phone:
    
    def __init__(self, price, brand, camera):
        
        print("Inside Phone class constructor")
        
        self.price = price
        self.brand = brand
        self.camera = camera
         
        
class SmartPhone(Phone):
    pass

Ph = SmartPhone(20000, "Apple", 13)
print(Ph.brand)  # --> This shows that if the child class do not have a constructor the the constructor of parent class will be called...



# Ex2 (Inheriting Private Members):

class Phone:
    
    def __init__(self, price, brand, camera):
        
        print("Inside Phone class constructor")
        
        self.price = price
        self.__brand = brand # --> For now this attribute is private...
        self.camera = camera
        
        
class SmartPhone(Phone):
    pass


Ph = SmartPhone(20000, "Apple", 13)
print(Ph.__brand) # --> This shows that Private Members can't be inherited...



# Ex3 (PolyMorphism):

class Phone:
    
    def __init__(self, price, brand, camera):
        
        print("Inside Phone class constructor")
        
        self.price = price
        self.__brand = brand # --> For now this attribute is private...
        self.camera = camera
        
    def buy(self):
        print("Phone bought")
        
        
class SmartPhone(Phone):
    def buy(self):
        print("Buying a smart phone")
        
Ph = SmartPhone(20000, "Apple", 13)
Ph.buy() # Since both classes have same function name, here SmartPhone will call its own function --> This is also called "Method Overriding".



# Ex4 (Class Parent):
 
class Parent:
    
    def __init__(self, num):
        self.__num = num
        
    def get_num(self):
        return self.__num
    
class Child:
    
    def show(self):
        print("Child Class")
        
son = Child(100)  # Since Child have no constructor, The value 100 will be passed to Parent
print(son.Child.get_num())
son.show()



# Ex5 (Class Parent):
 
class Parent:
    
    def __init__(self, num):
        self.__num = num
        
    def get_num(self):
        return self.__num
    
class Child:
    
    def __init__(self, value, num):
        self.__value = value
        
    def get_num(self):
        return self.__value
        
son = Child(100, 10)
print(son.Child.get_num())  # Since Child have both the Constructors, The values will pe passed accordingly, BUT the constructor num wasn't initialized in Child (and constructor num of Parent wasn't called since child have its own) --> The code will show error...



# Ex6 (Class Parent):

class Parent:
    
    def __init__(self):
        self.var = 100
        
    def display1(self, var):
        print("Parent Class : ", self.var)
        
class Child(Parent):
    
    def display2(self, var):
        print("Child Class : ", self.var)
        
obj = Child()
obj.display1(200) # This wills how 100 as output, even though we are passing 200 but in display1 we are using self.var  that is 100 ...



# Ex7 (Super):

class Phone:
    
    def __init__(self, price, brand, camera):
        
        print("Inside phone constructor")
        
        self.__price = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        
        print("Phone bought")
        
class SmartPhone(Phone):
    
    def buy(self):
        
        print("Buying a smart phone")
        
        super().buy()  # --> This is calling the buy() method from Parent class...
        
s = SmartPhone(2000, "Apple", 13)

s.buy() # super keyword is used to call the method of parent class from child class... and we can't use it from outside of the class...



# Ex7 (Super):

class Phone:
    
    def __init__ (self, price, brand, camera):
        
        print("Inside phone constructor")
        
        self.__price = price
        self.brand = brand
        self.camera = camera
        
class SmartPhone(Phone):
    
    def __init__(self, price, brand, camera, os, ram):
        
        super().__init__(price, brand, camera)  # Here we can see that the common attributes that are passed into the constructor of parent class from child class...
        
        self.os = os
        self.ram = ram
        print("Inside smart phone constructor")
        
s = SmartPhone(2000, "Apple", 13, "Android", 4)

print(s.os)
print(s.brand)
