import random
min = 1
max = 6
again = "y"
while again == "y":
    rolled = random.randint(min, max)
    print("Rolling the dice....")
    print("Rolled number is " + str(rolled))
    again = input("Roll the dices again? (y or n) : ")
print("exited")