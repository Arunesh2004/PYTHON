# Method Overloading : One method is implemented in multiple ways ... i.e. we can induce multiple behaviors from a single method by providing different inputs ...

class Geometry:
    
    def area(self, a):
        return 3.14159*a*a
    
    def area(self, a, b):
        return a*b
    
G1 = Geometry(3,5)
print (G1.area())  # --> In python this will show error .. i.e. technically in python method overloading is not implemented ...

#If we still want to use it : (we can use default arguments)

class Geometry:
    
    def area(self, a, b = 0):
        
        if(b == 0):
            print ("Circle", 3.14159*a*a)
            
        else:
            print ("Rectangle", a*b)
            
G1 = Geometry()

G1.area(3)
G1.area(3,5)



# Operator Overloading : 

a = 3 + 4 # This will do addition

b = "Hello" + "World" # This will do concatination 
