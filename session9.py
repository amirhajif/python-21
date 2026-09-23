class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
        
    def __str__(self):
        return f"{self.username} {self.password} {self.email}"

class Rectangle:
    def __init__(self,tol,arz):
        self.tol = tol
        self.arz = arz
        
    def area(self):
        return self.tol * self.arz
    def env(self):
        return (self.tol+self.arz)*2
  
class Customer:
    def __init__(self,name,age,nc,balance):
        self.name = name
        self.age = age
        self.nc = nc
        self.balance = balance
        self.has_loan = False
        self.loan_amount=0
        
    def __str__(self):
        if self.has_loan==False:
            return f"{self.name} {self.nc} {self.balance} dont have loan"
        else:
            return f"{self.name} {self.nc} {self.balance} has {self.loan_amount}"
    
    # Method for increase balance for customer
    def increase_balance(self,value):
        self.balance = self.balance + value
        
    # Method for decrease balance for customer
    def decrease_balance(self,value):
        self.balance = self.balance - value
    
    # Method for check customer can take loan or not 
    # Return : True | False
    def can_take_loan(self,loan_value):
        if self.has_loan==False and self.balance > loan_value:
            return True
        else:
            return False
    
    
    # pay loan value into customer
    # update balance,loanvalue,has_loan
    def take_loan(self,loan_value):
        if self.can_take_loan():
            self.balance = self.balance + loan_value
            # self.balance += loan_value
            self.has_loan = True
            self.loan_amount = loan_value
    
    # setter & getter for name
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    
    # setter & getter for age
    def set_age(self,age):
        self.age = age
    def get_age(self):
        return self.age
    
    # setter & getter for nc
    def set_nc(self,nc):
        self.nc = nc
    def get_nc(self):
        return self.nc
    
    # setter & getter for balance    
    def set_balance(self,balance):
        self.balance = balance
    def get_balance(self):
        return self.balance


c = Customer("amir",25,205,1000)
while True:
    option = int(input("""
1-show info
2-show balance
3-request loan
4-increase balance
5-update name
5-exit                  
please enter option:  """))
    if option==1:
        print(c)
    elif option==2:
        print(c.get_balance())
    elif option==3:
        value = int(input("please enter loan value: "))
        if c.can_take_loan(value)==True:
            c.take_loan(value)
        else:
            print("\n---------- you cant take loan -----------")
    elif option==4:
        value = int(input("how much do you want increase: "))
        c.increase_balance(value)
    elif option==5:
        name = input("plaese enter new name: ")
        c.set_name(name)
    elif option==6:
        break
        
        
