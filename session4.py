# for i in range(0,10):
#     print("hello")
    

# i=0
# while i<10:
#     print("hello")
#     i=i+1
    

# factoriel

# n=int(input("please enter number: "))

# i=1
# fact = 1
# while i<=n:
#     fact=fact*i
#     i=i+1
    
# print(fact)


# 5
# 1*2*3*4*5

#  adad kamel
# n=int(input("please enter number: "))

# i=1
# sum=0
# while i<n:
#     if n%i==0:
#         sum=sum+i
#     i=i+1

# if n==sum:
#     print("kamel")
# else:
#     print("kamel nist")   


# n= int(input("please enter n: "))
# sum=0
# while n>0:
#     sum = sum + (n%10)
#     n=n//10
    
# print(sum)

# n= int(input("please enter n: "))
# sum=0
# while n>0:
#     sum = sum + 1
#     n=n//10
    
# print(sum)

# sum = 0
# while True:
#     score = int(input("please enter score: "))
#     sum = sum + score
    
#     option = input("do you want continue?y/n ")
#     if option.lower()=="n":
#         break

# print(sum)

# while True:
#     option = int(input("""
# 1-say hello
# 2-say bye
# 3-say name
# 4-exit
# enter option:   """))
#     if option==1:
#         print("hello")
#     elif option==2:
#         print("bye")
#     elif option==3:
#         print("amir")
#     elif option==4:
#         break
#     else:
#         print("invalid input")

# TUPLE

# degrees = (180,360,540)
# print(degrees)

# print(degrees[1])

# # degrees[1]=540
# for degree in degrees:
#     print(degree)

# user = {
#     "name":"amir",
#     "pass":"amir123",
#     "age":25,
#     "is_programmer":True,
#     "programming_languages":["python","js"]
# }

# print(user)
# print(user["pass"])

# user["age"]=26
# print(user)

# user["job"]="programmer"
# print(user)

# del user["job"]
# print(user)

# # print(user["father_name"])

# print(user.get("father_name","key not exist"))

user = {
    "name":"amir",
    "pass":"amir123",
    "age":25,
}

# print(user.items())
# # [('name', 'amir'), ('pass', 'amir123'), ('age', 25)]


# for key,value in user.items():
#     print(f"{key} ---> {value}")
    
    
print(user.keys())
# ['name', 'pass', 'age']

print(user.values())
