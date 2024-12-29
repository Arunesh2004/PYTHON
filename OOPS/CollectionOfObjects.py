class Customer:
    
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
        
    def intro(self):
        print("I am", self.name, "and I am", self.age)
        
c1 = Customer("Arunesh", 20);
c2 = Customer("Nikhil", 20);
c3 = Customer("Abhishek", 20);

# List :-

L = [c1, c2, c3]

for i in L:
    i.intro()
