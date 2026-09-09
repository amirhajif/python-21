# Q1
# secret = 18
# count = 0

# while True:
#     guess = int(input("please enter number: "))
#     count = count + 1
#     if guess > secret:
#         print("you gussed bigger")
#     elif guess < secret:
#         print("you gussed smaller")
#     else:
#         print(f"you gussed correct number after {count} try")
#         break

# Q2
# hello
# {'h':1,'e':1,'l':2,'o':1}

# sentence = input("please enter sentence: ")
# letters = {}

# for letter in sentence:
#     if letter in letters.keys():
#         letters[letter] =letters[letter]+1 
#     else:
#         letters[letter]=1    

# print(letters)


# sentence = input("please enter sentence: ")
# letters = {}

# for letter in sentence:
#     if letter in letters:
#         letters[letter] =letters[letter]+1 
#     else:
#         letters[letter]=1    

# print(letters)

# sentence = input("please enter sentence: ")
# letters = {}

# for letter in sentence:
#     letters[letter] = letters.get(letter,0)+1   

# print(letters)


# Q3

users = {
    'ali': '1234',
    'sara': 'qwerty'
}

username = input("please enter username: ")
password = input("please enter password: ")

if username in users and users[username]==password:
    print("login")
else:
    print("cant login")
    
