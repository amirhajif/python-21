#E1
list1=["ali","reza","sara"]
list2=["sara","amin","ali"]
for name in list1:
    if name in list2:
        print(name)
        
# E2
number = int(input("please enter number: ")) #12
for i in range(1,number+1): #1,2,3,4,5,6,7,8,9,10,11,12
    if number %i ==0:
        print(i)

# E3

number = int(input("pleas enter a number: "))
sum=0
for i in range(1,number):
    if number%i==0:
        sum = sum + i

if sum==number:
    print("adad kamel ast")
else:
    print("adad kamel nist")
