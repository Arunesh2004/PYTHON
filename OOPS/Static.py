class Atm:
    
    #Static/Class variables:-  (to access static variables we use class names)
    __counter = 1 # --> We dont need to create objects to access static variables...
    
    def __init__(self):
        
        
        #Instance variables :- (to access instance variables we use self.instance variables)
        
        self.pin = ""
        self.balance = 0
        
        self.sno = Atm.__Counter()
        Atm.__counter += 1
        
        
        self.menu()
        
    #BUT still if we want other programmers to access static variables : --> we use getters and setters
    
    def get_counter():
        return Atm.__counter
    def set_counter(value):
        if type(value) == int:
            Atm.__counter = value  # --> we don't need to pass self while using static methods...
            
            
        
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
