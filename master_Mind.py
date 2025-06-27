import random
# !/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay

admin = "user"
AdminPassword = "password"
loggedIn = False

print("MasterMind")

# This function generates the code


def generate_Code():
    # This array contains all the options for the code
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pins = ["pos1", "pos2", "pos3", "pos4"]

    for i in range(len(pins)):
        pins[i] = colors[random.randint(0, len(colors) - 1)]
    return pins

# This function checks the secret code with the guess


def get_Feedback(secret, guess):
    blackPins = 0
    whitePins = 0
    userInput = guess.split()

    for i in range(len(userInput)):
        if userInput[i] == secret[i]:
            blackPins = blackPins + 1
        elif userInput[i] in secret:
            whitePins = whitePins + 1

    return blackPins, whitePins

# This function reveals the code


def show_Secret(mystery):
    print(mystery)

# This function allows the user to log in


def log_In_As_Admin():
    global loggedIn
    print("Before you cheat pls log in as a admin")
    user = input("User: ")
    if user == admin:
        userPassword = input("Enter the password: ")

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

# This function checks if the input (user input) is allowed


def check_Code(input):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    userInput = input.split()
    checkInput = ["pos1", "pos2", "pos3", "pos4"]
    validInput = True

    if(len(userInput) == 4):
        for i in range(len(userInput)):
            checkInput[i] = userInput[i] in colors

        if False in checkInput:
            validInput = False

        if validInput is True and len(userInput) == 4:
            return True
        else:
            return False
    else:
        return False


# This functions starts the game


def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4 colors. The colors can be: Red Orange, yellow, green, blue, and purple.")
    print("You have 10 attempts.")
    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_Guess = False
        while not valid_Guess:
            guess = input(f"Attempt {attempt}: ").lower()

            if guess == "cheat" or guess == "login":
                if loggedIn is True and guess == "cheat":
                    show_Secret(secret_Code)
                elif loggedIn is True and guess == "login":
                    print(f"You are already logged in as {admin}")
                else:
                    log_In_As_Admin()
            else:
                valid_Guess = check_Code(guess)

            if valid_Guess is False:
                print("Invalid input. Enter 4 colors or use the useable colors")

        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {secret_Code}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {secret_Code}")


if __name__ == "__main__":
    again = 'Y'
    while again == 'Y':
        play_Mastermind()
        again = input("Play again (Y/N) ?").upper()
