import random

print("Welcome to number guessing game")
mini = input("Enter the starting and ending range  'Starting': ")
maxi = input("Enter the ending: ")
number = random.randint(int(mini), int(maxi))
limit = 0
while limit <= 5:
    print(f"Attempts left {5-limit}")
    guess = int(input(f"Guess the number between{mini} to {maxi}: "))
    if guess.isnumeric():
        if guess == number:
            print("Congratulation! you guessed the number")
            break
        if guess > number:
            limit += 1
            print("Too High")
        elif guess < number:
            limit += 1
            print("Too Low")
    else:
        print(f"{guess} is invalid")
