# scores = [20,12,14,5,9,17,16]
# print(scores)
# print(scores[4])

# names = ["ali","reza","ahmmad","jafar"]
# print(names)

# # update
# names[2]="ahmad"
# print(names)

# # append
# names.append("arsham")
# print(names)

# # insert
# names.insert(1,"mamad arsham")
# print(names)

# # delete
# del names[0]
# print(names)

# # pop
# popedName = names.pop(0)
# print(popedName)
# print(names)

# # remove
# names.remove("arsham")
# print(names)


# scores = [20,12,14,5,9,17,16]
# names = ["ali","reza","ahmmad","jafar"]

# scores.sort()
# print(scores)

# names.sort()
# print(names)

# scores.sort(reverse=True)
# print(scores)

# new_list = sorted(names)
# print(new_list)
# print(names)

# names.reverse()
# print(names)


# reversed_names = reversed(names)
# print(list(reversed_names))
# print(names)

# print(max(scores))
# print(min(scores))
# print(sum(scores))
# print(sum(scores)/len(scores))

# my_cars = ["pride","pego","saina"]
# carsale_cars = my_cars[:]

# my_cars.append("206")
# carsale_cars.append("lexus")
# print(my_cars)
# print(carsale_cars)


# a=10
# b=a

# a=20

# print(a)
# print(b)


# score = 18
# if score>=10:
#     print("student pass exam")
# else:
#     print("fail")

users = ["ali","reza","ahmad","jafar"]

username = input("pelase enter username: ")

if username in users:
    print("exist")
else:
    print("not-exist")
