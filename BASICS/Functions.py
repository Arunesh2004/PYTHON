# There are 3 types of functions in python :
    
#     1. In-Built Functions :
        
#         ex :- int(), float(), bool()
          
#         We use them directly.

        
#     2. Module Functions :
        
#         ex :- math.sqrt(), random.randint(), time.time()
        
#         for this we write --> from "Module Name" import "Name of the function we want to import from that module"

from math import sqrt

print(sqrt(4))


#     3. User Defined Functions :

#         ex :- def function_name(parameters): 
#                    do something

def print_sum(first, second):
    print("Sum of ", first, " and ", second, " is : ", first + second)
    
print_sum(3, 5) # here we are calling function by passing parameters.