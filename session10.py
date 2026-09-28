class Person:
    def __init__(self,name,age,nc):
        self.name = name
        self.age = age
        self.nc = nc
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

class Employee(Person):
    def __init__(self,name,age,nc,salary):
        super().__init__(name,age,nc)
        self.salary = salary

    # setter & getter for salary
    def set_salary(self,salary):
        self.salary = salary
    def get_salary(self):
        return self.salary
    
    
import os

print(os.getcwd())

# os.makedirs("folder2")
# os.makedirs("folder3")

# os.chdir("folder2")
# print(os.getcwd())
# os.makedirs("folder2-1")
# os.makedirs("folder2-2")
# os.makedirs("folder2-3")

# os.chdir("folder2/folder2-3")
# print(os.getcwd())
# os.chdir("../../folder1")
# print(os.getcwd())

# os.rename("data.txt","mahsolat.txt")

# os.remove("mahsolat.txt")

# data = open("data.txt","r")
# data = open("data.txt")
# print(data.read())

# for product in data:
#     print(product.strip())

# list_of_products = data.readlines()
# print(list_of_products)

# list_of_products = list(map(lambda product:product.strip() ,list_of_products))
# print(list_of_products)

# file = open("pdf.txt","w")
# file.write("faghat e faghat 300 hezar toman")
# file.write("good bye")

# file = open("pdf.txt","a")
# file.write("\n good bye")


a=10
b=0

try:
    print(a/b)
except:
    print("an error in divide")
else:
    print("app finished")
finally:
    print("class finished")
