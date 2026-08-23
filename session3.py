n=int(input("please enter n: "))
# if n==0:
#     print("zero")
# elif n==1:
#     print("one")
# elif n==2:
#     print("two")
# elif n==3:
#     print("three")
# elif n==4:
#     print("four")
# elif n==5:
#     print("five")
# elif n==6:
#     print("six")
# elif n==7:
#     print("seven")
# elif n==8:
#     print("eight")
# elif n==9:
#     print("nine")
# else:
#     print("out of range")

numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
if n>9 or n<0:
    print("out of range")
else:
    print(numbers[n])
