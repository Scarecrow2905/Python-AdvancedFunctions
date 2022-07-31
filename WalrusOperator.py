# Walrus Operator :=

# New to Python 3.8
# Assignment expression aka walrus operator
# Assigns values to variables as part of a larger expression

# happy = False
# print(happy)

#print(happy := False)


# foods = list()
# while True:
#    food = input("What type of food do you like?: ")
#    if food == "quit":
#        break
#    foods.append(food)


foods = list()
while food := input("What food would you like?: ") != "quit":
    foods.append(food)

