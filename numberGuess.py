import random
randNumber = random.randint(1, 100)
noTry = 0
while True:
    userGuess = int(input("Guess a number between 1 and 100: "))
    if userGuess < randNumber:
        print("Too low! Try again.")
        noTry += 1
    elif userGuess > randNumber:
        print("Too high! Try again.")
        noTry += 1
    else:
        print("Congratulations! You've guessed the correct number.")
        print(f"It took you {noTry} tries.")
        quit()