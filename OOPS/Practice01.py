class Atm:
    
    # Constructor -> It is a special method, i.e. the code written inside it runs automatically when we make object of this class.
    # Here, init is a constructor. In other languages, name of a constructor is same as name of a class.
    
    # self --> Whatever object you are currently working with IS SELF.
    # __init__ --> This is a constructor method in Python. It's automatically called when an object is created.
    # self.pin and self.balance --> These are instance variables. They belong to each object of this class.
    
    # Instance variables --> Value of the instance variable is different for every object.
    
    def __init__(self):
        
        self.pin = ""
        self.balance = 0
        
        self.menu()
        
    def menu(self):
        
        user_input = input("""
                           Hello, how would you like to proceed ?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
        """)
        
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Bye")
    
    
    def create_pin(self):
        self.pin = input("Enter your pin : ")
        print("Pin created successfully")
        
        
    def deposit(self):
        temp = input("Enter your pin : ")
        
        if temp == self.pin:
            amount = int(input("Enter the amount : "))
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("Invalid pin")
            
            
    def withdraw(self):
        temp = input("Enter your pin : ")
        
        if temp == self.pin:
            amount = int(input("Enter the amount : "))
            
            if(amount <= self.balance):
                self.balance = self.balance - amount
                print("Withdraw successful")
            else:
                print("Insufficient balance")
                
                
    def check_balance(self):
        temp = input("Enter your pin : ")
        
        if temp == self.pin:
            print("Balance : ", self.balance)
        else:
            print("Invalid Pin")
            
            
sbi = Atm()
sbi.deposit()
sbi.withdraw()
sbi.check_balance()
