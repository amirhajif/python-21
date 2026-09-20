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
    
    def increase_balance(self,value):
        self.balance = self.balance + value
    def decrease_balance(self,value):
        self.balance = self.balance - value
    
    def can_take_loan(self,loan_value):
        if self.has_loan==False and self.balance > loan_value:
            return True
        else:
            return False
    
    def take_loan(self,loan_value):
        if self.can_take_loan():
            self.balance = self.balance + loan_value
            # self.balance += loan_value
            self.has_loan = True
            self.loan_amount = loan_value
    
        
      

# rect = Rectangle(10,8)
# print(rect.area())
# print(rect.env())

        
# u1 = User("amirhossein","amir123","amir@gmail.com")
# print(u1)
# print(u1.password)
# print(u1.username)

# u2 = User("reza","r123","rez@gmail.com")
# print(u2.email)
