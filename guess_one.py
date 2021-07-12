import random


def guessing_game():
    a = random.randint(1, 9)
    user_guess = int(input("Enter You Guess between 1 to 9 : "))
    if a == user_guess:
        print("You Guessed Right...!!")
    else:
        print("Better Luck Next Time...!! guessed Number : " + str(a))
