# Whenever we create an object :
#  sbi = Atm()  --> In this "Atm" is object and we are storing it in a refrence variable "sbi".  
#  and sbi is pointing towards the the actual address of the object ....

# Pass By Reference :

class Customer:
    
    def __init__(self, name):
        
        self.name = name 
        
def greet(customer):
    print(id(customer))
        
    
cust = Customer("Arunesh") 
print(id(cust))  # Both the id will be same ---> Just like Aliasing 

# Ex:-

# a = 4;
# b = a;
# id(a) = id(b);   Similarly cust is a reference variable   and   cust and customer are pointing towards the same object.

greet(cust) # Here "cust" is passed by reference to the function greet() which means it will change the original object.  

  
# if a object is passed to a function then it will change the original object.



# Ex:-

# class Customer:
    
#     def __init__(self, name):
        
#         self.name = name
        
# def greet(customer):
#     customer.name = "Arunesh Sharma"
#     print(customer.name)
    
# cust = Customer("Arunesh")

# greet(cust)



# print(cust.name)  # The name will be changed to "Arunesh Sharma" as we passed the reference of cust object to the function greet() which changed the original object.  
# --> class k objects are also mutable like, list, dict and sets  ---> because their addresses are also same as before...


# Conclusion :
    
#  -->   If you will send a mutable (Ex- List, objects) object to a function then it will change the original object. If you will send an immutable (Ex- Tuple) object to function then it will not affect the original object.