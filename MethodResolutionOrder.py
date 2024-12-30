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
        
class SmartPhone(Phone, Product): # Since Phone was written before, therefore the "buy" method of Phone class will be called... --> This concept is called MRO (Method Resolution Order Order)
    pass

S1 = SmartPhone(1000, "Apple", "13px")

S1.buy()