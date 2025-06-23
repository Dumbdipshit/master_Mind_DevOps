import random

def generate_Code():
    # This array contains all the options for the code
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pins = ["pos1", "pos2", "pos3", "pos4"]

    for i in range(len(pins)):
        pins[i] = colors[random.randint(0, len(colors) - 1)]
    return pins

secret_Code = generate_Code()


playerInput = "red BLUE yellow red"


# This function checks if the input (user input) is allowed
def check_Code(input):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    userInput = input.split()
    checkInput = ["pos1", "pos2", "pos3", "pos4"]
    validInput = True
    
    for i in range(len(userInput)):
        checkInput[i] = userInput[i] in colors
    
    if False in checkInput:
        validInput = False
        
    if validInput is True and len(userInput) == 4:
        return True
    else:
        return False
    
print(check_Code(input()))
        


