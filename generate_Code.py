secret_Code = ["blue", "red", "red", "red"]


playerInput = "red BLUE yellow yellow"


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


        
print(get_Feedback(secret_Code, playerInput.lower()))

