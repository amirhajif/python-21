# E1
# students = [
#     {'name': 'Ali', 'math': 17, 'english': 18},
#     {'name': 'Sara', 'math': 14, 'english': 15},
#     {'name': 'Reza', 'math': 19, 'english': 17}
# ]

# for student in students:
#     meyangin = (student['math'] + student['english']) / 2
#     print(f"{student['name']}:  {meyangin}")
#     if meyangin < 17:
#         print("Accepted")
#     else:
#         print("Great Accepted")    


# E2
# students = {}

# while True:
#     name = input("please enter name: ")
#     scores = []
#     # amir
#     # 12,14,15,9 ---> split ---> list
#     while True:
#         score = int(input("please enter score: "))
#         scores.append(score)
#         option1 = input("do you want to enter score?y/n ")
#         if option1=="n":
#             break 
#     students[name] = scores
#     option = input("do you want add student?y/n ")
#     if option=='n':
#         break

# print(students)

# E3
# while True:
#     users = {}
#     option = input("do u want login or singup?")
    
#     if option == "signup":
#         username = input("please enter UR username: ")
#         password = input("please enter UR pass: ")
        
#         users[username] = password
#         print("signup is successful U can enter")
        
#     elif option == "login":
#         username = input("please enter UR username: ")
#         password = input("please enter UR pass: ")
        
#         if username in users:
#             if users[username] == password:
#                 print("seccessful")
#             else:
#                 print("password is false")
#         else:
#             print("we cant find ur accont")
                        
#     else:
#         print("wrong option")

# E4
# while True:
#     option=int(input("""
#     1-jame
#     2-tafrigh
#     3-exit
#     pleas chose option: """))
#     if option==1:
#         number1=int(input("enter a number: "))
#         number2=int(input("enter a number: "))
#         print(number1+number2)
#     elif option==2:
#         number1=int(input("enter a number: "))
#         number2=int(input("enter a number: "))
#         print(number1-number2)
#     elif option==3:
#         break
#     else:
#         print("select 1-2-3")
