# Types of Inheritance :
    # 1. Single Inheritance : One child class inherits from one parent class.
    # 2. Multilevel Inheritance : One child class inherits from multiple parent classes, where each parent class inherits from another parent class.
    # 3. Hierarchical Inheritance : Multiple child classes inherit from one parent class.
    # 4. Multiple Inheritance : One child class inherits from multiple parent classes.
    # 5. Hybrid Inheritance : One child class inherits from multiple parent classes, and some of the parent classes are related to each other.
    


# Single Inheritance Example :

class Phone:
    
    def __init__(self, price, brand, camera):
        
        print("Inside the phone")
        
        self.price = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a phone...")
        
    def return_phone(self):
        print("Returning the phone...")
        
class SmartPhone(Phone):
    pass

S1 = SmartPhone(1000, "Apple", "13px")
S1.buy()



# Multilevel Inheritance Example :

class Product:
    
    def review(self):
        print("This product has good reviews")
        
class Phone(Product):
    
    def __init__(self, price, brand, camera):
        
        print("Inside the phone")
        
        self.price = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a phone...")
        
class SmartPhone(Phone):
    
    pass

S1 = SmartPhone(1000, "Apple", "13px")

S1.buy()
S1.review()


# Hierarchical Inheritance Example :

class Phone:
    
    def __init__(self, price, brand, camera):
        
        print("Inside the phone")
        
        self.price = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a phone...")
        
        
class SmartPhone(Phone):
    
    pass

class FeaturePhone(Phone):
    
    pass

S1 = SmartPhone(1000, "Apple", "13px")
S2 = FeaturePhone(2345, "Apple", "13px")


# Multiple Inheritance Example :

class Phone:
    
    def __init__(self, price, brand, camera):
        
        print("Inside the phone")
        
        self.price = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a phone...")
        
class Product:
    
    def review(self):
        print("Reviewing the product...")
        
class SmartPhone(Phone, Product):
    pass

S1 = SmartPhone(1000, "Apple", "13px")

S1.buy()
S1.review()