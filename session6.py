# SET {}
# cars = {"bmw","prado","benz","pride","bmw"}
# print(cars)
# print(cars[1])
# for car in cars:
#     print(car)

# cars.add("changan")
# print(cars)


# remove \ discard
# cars.discard("audi")

# my_cars = {"benz","prado","bmw"}
# show_room_cars = {"audi","prado","porsche"}

# my_cars.update(show_room_cars)
# print(my_cars)

# all_cars = my_cars.union(show_room_cars)
# print(all_cars)

# my_cars.intersection_update(show_room_cars)
# print(my_cars)

# same_cars = my_cars.intersection(show_room_cars)
# print(same_cars)


# my_cars.symmetric_difference_update(show_room_cars)
# print(my_cars)

# symmetric = my_cars.symmetric_difference(show_room_cars)
# print(symmetric)

# definition
def sayHello():
    return "hello"

def circle_env(r):
    return 2*3.14*r

def rectangle_area(tol,arz):
    return tol*arz




def factoriel(n):
    fact=1
    for i in range(1,n+1):
        fact = fact*i
    
    return fact

def is_even(n):
    if n%2==0:
        return True
    else:
        return False


def introduce(name,family="hajitabar",age=25):
    return f"hello my name is {name} {family} and {age} years old"

def show_foods(*foods):
    for food in foods:
        print(food)
        
def restaurant_foods(**foods):
    # print(foods)
    for key,value in foods.items():
        print(f"{key} ---> {value}")
    
restaurant_foods(burger=1000,sandwich=1500,pizza=2000)

# show_foods("burger","sandwich","pizza")

# print(introduce("amir","hajitabar"))
# print(introduce(age=25,name="amir",family="hajitabar"))
# n = int(input("please enter n: "))
# result = is_even(n)
# if result==True:
#     print("the number is even")
# else:
#     print("the number is odd")

# print(introduce("amir","hajitabar",25))

# print(rectangle_area(8,6))


# x = int(input("please enter r: "))
# # env = circle_env(5)
# env = circle_env(x)
# print(env)


# call
# print(sayHello())

# message = sayHello()
# print(message)
