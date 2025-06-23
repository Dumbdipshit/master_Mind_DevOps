import random

def generate_Code():
    # This array contains all the options for the code
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pins = ["pos1", "pos2", "pos3", "pos4"]

    for i in range(len(pins)):
        pins[i] = colors[random.randint(0, len(colors) - 1)]
    return pins

secret_Code = generate_Code()

secret_Code = generate_Code()
print(secret_Code)