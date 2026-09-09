# n = int(input("please enter n: "))
# reverse = 0

# while n>0:
#     reverse = reverse*10 + (n%10)
#     n=n//10

# print(reverse)


# n = int(input("please enter n: "))
# reverse = 0
# data = n

# while n>0:
#     reverse = reverse*10 + (n%10)
#     n=n//10

# if reverse == data:
#     print("palinrome")
# else:
#     print("not-palindrome")


# phone_book={}
# while True:
#     name = input("please enter name: ")
#     number = input("please enter number: ")
#     phone_book[name]=number
    
#     option = input("do you want continue?y/n ")
#     if option=='n':
#         break

# print(phone_book)
    
    
    

phone_book={}
while True:
    name = input("please enter name: ")
    if name=='s':
        break
    number = input("please enter number: ")
    phone_book[name]=number


print(phone_book)

