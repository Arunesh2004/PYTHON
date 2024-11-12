age = 1

if age >= 18:
    print("You are an adult")
    print("You can Vote")  #in python we dont need curly brackets to define a block of code, we use indentation instead
    
#we can put multiple if statements   for that we use elif and else
elif age < 18 and age > 3:
    print("You are in school")
    
else:
    print("You are a kid")  #this will run if the above conditions are not met