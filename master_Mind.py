#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay

admin = "user"
AdminPassword = "password"
loggedIn = False

print("MasterMind")

import random

def generate_Code(length=4, digits=6):
    return [str(random.randint(1, digits)) for _ in range(length)]

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
    # Count whites by subtracting black and calculating min digit frequency match
    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    
    return black_Pegs, white_Pegs

def show_Secret(mystery):
    print(mystery)


# This function allows the user to log in
def log_In_As_Admin():
    global loggedIn
    print("Before you cheat pls log in as a admin")
    user = input("User: ")
        
    if user == admin:
        userPassword = input("Enter the password: " )

        if userPassword == AdminPassword:
            print(f"Welcome {admin}")
            print("Feel free to use the 'cheat' command to see the awnser")
            loggedIn = True
        else:
            print("Wrong password")
            print("You can still play or retry the log in")

    else:
        print("This user doesnt exist")
        print("You can still play or retry the log in")


# This functions starts the game

def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code. Each digit is from 1 to 6. You have 10 attempts.")
    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_Guess = False
        while not valid_Guess:
            guess = input(f"Attempt {attempt}: ").strip()
            valid_Guess = len(guess) == 4 and all(c in "123456" for c in guess)
            if not valid_Guess:
                print("Invalid input. Enter 4 digits, each from 1 to 6.")

            if guess == "cheat":
                if loggedIn == True:
                    show_Secret(secret_Code)
                else:
                    log_In_As_Admin()

            else:
                False

        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_Code)}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y' :
        play_Mastermind()
        again  = input (f"Play again (Y/N) ?").upper()

