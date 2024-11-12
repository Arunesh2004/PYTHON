# Encapsulation -> Encapsulation means hiding the data-members.

# For this we use different access modifiers :-

# 1. Public -> def name(self)
# 2. Protected -> def _name(self)
# 3. Private -> def __name(self)

# Nothings in python is truly private -> you can access everything with this syntax "_Classname__DataMembername = "abcd" ".


class Atm:
    
    def __init__(self):
        
        self.__pin = ""
        self.__balance = 0
        
        self.menu()
        
    # Getters
    def get_pin(self):
        return self.__pin
    
    # Setters
    def set_pin(self, new_pin):
        self.__pin = new_pin
        print("Pin set to " + str(self.__pin))
        
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
        self.__pin = input("Enter your pin : ")
        print("Pin created successfully")
        
        
    def deposit(self):
        temp = input("Enter your pin : ")
        
        if temp == self.__pin:
            amount = int(input("Enter the amount : "))
            self.__balance = self.__balance + amount
            print("Deposit successful")
        else:
            print("Invalid pin")
            
            
    def withdraw(self):
        temp = input("Enter your pin : ")
        
        if temp == self.__pin:
            amount = int(input("Enter the amount : "))
            
            if(amount <= self.__balance):
                self.__balance = self.__balance - amount
                print("Withdraw successful")
            else:
                print("Insufficient balance")
                
                
    def check_balance(self):
        temp = input("Enter your pin : ")
        
        if temp == self.__pin:
            print("Balance : ", self.__balance)
        else:
            print("Invalid Pin")
            
            
sbi = Atm()
sbi.get_pin()
sbi.set_pin(9999)
sbi.deposit()
sbi.withdraw()
sbi.check_balance()
