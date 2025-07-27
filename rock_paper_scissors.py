import random

lst = ["r", "p", "s"]
continue_running = "y"
while continue_running == "y":
    user_choice = input("Rock, Paper, Scissors (r/p/s)?: ")
    computer_choice = random.choice(lst)
    lst1 = [user_choice, computer_choice]
    count = 0
    for item in lst1:
        match item:
            case "r" if item == "r":
                if count == 0:
                    count += 1
                    print(f"you choose this 🪨")
                else:
                    print(f"computer choose this 🪨")
            case "p" if item == "p":
                if count == 0:
                    count += 1
                    print(f"you choose this 🧻")
                else:
                    print(f"computer choose this 🧻")
            case "s" if item == "s":
                if count == 0:
                    count += 1
                    print(f"you choose this ✂️")
                else:
                    print(f"computer choose this ✂️")

    if computer_choice == user_choice:
        print("Game Tie")
    elif computer_choice == "r" and user_choice == "p":
        print("You won")
    elif computer_choice == "p" and user_choice == "r":
        print("computer won")
    elif computer_choice == "r" and user_choice == "s":
        print("computer won")
    elif computer_choice == "s" and user_choice == "r":
        print("you won")
    elif computer_choice == "p" and user_choice == "s":
        print("you won")
    elif computer_choice == "s" and computer_choice == "p":
        print("computer won")
    else:
        print("Invalid input")
    continue_running = input("continue ? (y/n): ")
    if continue_running != "y":
        print("Game exit")
        break
