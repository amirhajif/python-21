# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum(n-1)
    
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
    
    
# def fibo(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
    
    
# def add_function(x,y):
#     return x+y

# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False

# def is_even_one(n):
#     return n%2==0

is_even_lambda = lambda n:n%2==0
# print(is_even_lambda(10))

# add = lambda x,y:x+y
# print(add(10,5))

# print(fibo(6))
    
# print(sum(6))

# print(fact(5))


# numbers = [1,2,3,4,5]
# pow_2_numbers = []
# for number in numbers:
#     pow_2_numbers.append(number**2)

# print(pow_2_numbers)
# pow_2_numbers = list(map(lambda n:n**2,numbers))
# print(pow_2_numbers)
# even_numbers = list(filter(lambda n:n%2==0,numbers))
# print(even_numbers)


# import functions as f
# print(functions.fact(5))
# print(functions.is_even(10))

# print(f.fact(5))


# from functions import fact as fa,fibo as fi

# print(fact(5))

# print(fibo(6))

import time
from shamsi import JulianDay,julian_day

print("hello.... please wait .....")
time.sleep(3)
print("welcome to our store ...")

