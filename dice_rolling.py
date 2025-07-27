import random

no_of_dices = int(input("How many dice's you want to roll: "))
lst = [1, 2, 3, 4, 5, 6]
rolling_counter = 0
while True:
    drop = input("Roll the Dice(y/n)? ").lower()
    if drop == "y":
        rolling_counter += 1
        print(random.sample(lst, no_of_dices))
        print(f"dice's rolled {rolling_counter} times")
    elif drop == "n":
        print("Game quit")
        break
    else:
        print(f"{drop} is not valid")
