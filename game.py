import random

# handle level selection
while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level <= 0:
            pass
        else:
            break

# handle guesses
random_num = random.choice([1, level])
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess <= 0:
            pass
        elif guess < random_num:
            print("Too small!")
        elif guess > random_num:
            print("Too large!")
        elif guess == random_num:
            print("Just right!")
            break