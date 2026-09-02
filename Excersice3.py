# E1
sentence = input("yek jpmle benevis: ").lower()
counter = 0
for letter in sentence :
    if letter in "aieou":
        counter = counter + 1
print(counter)


# E2
fruits=["apple","banana","apple","cherry","banana","apple"]
count=0

for fruit in fruits:
    if fruit=="apple":
        count+=1
print(count)


# E3
numbers = [24, 11, 3, 99, 2, 7]
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print("smallest num:" , smallest)

# E4
numbers = [0,-1,-2,8,7,0,4,6,-8]
mosbat = []
manfi = []
s = 0


for number in numbers:
    if number == 0:
        s = s + 1
    elif number < 0:
        manfi.append(number) 
    else:
        mosbat.append(number)       

print(f"tedad sefr:{s}\nmosbat:{sum(mosbat)/len(mosbat)}\nmanfi:{sum(manfi)/len(manfi)}")


# E5
passwords = ["abc123", "hello@123", "pass", "admin@admin", "user123@"]
password = []

for pass_d in passwords:
    if len(pass_d) > 8 and '@' in pass_d:
        password.append(pass_d)
print(password)        
