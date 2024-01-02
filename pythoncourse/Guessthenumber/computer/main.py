import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number beetween 1 and {x}: "))
        if guess > random_number:
            print("Too high")
        elif guess < random_number:
            print("Too low")


    
    print(f"You got it, the number is {random_number}")
guess(10)