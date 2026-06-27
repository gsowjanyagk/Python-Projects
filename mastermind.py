import random

print("-" * 75)
print("                         Welcome to Mastermind!")
print("The objective of the games is to guess the randomly generated 4 digit number.")
print("You will be told if you have placed the correct digit in the correct position.")
print("-" * 75)

randno = random.randint(1000, 9999)
#print(randno)
attempts = 0

while True:
    try:
        guess = input("Enter a 4 digit number: ")
        attempts += 1
        if int(guess) < 1000 or int(guess) > 9999:
            print("Invalid input. Please enter a 4 digit number.")
            continue
    except ValueError:
        print("Invalid input. Please enter a 4 digit number.")
        continue
    if int(guess) == randno:
        print(f"Yay! You've guessed the number {randno} in {attempts} attempt(s)!")
        break
    randnostr = str(randno)
    correct = 0
    outputlist = ['x'] * 4
    for i in range(4):
        if guess[i] == randnostr[i]:
            correct += 1
            outputlist[i] = guess[i]
    print(f"Not there yet! You have {correct} digit(s) in the correct position.")
    print(f"Here is your progress: {" ".join(outputlist)}")
    print("-" * 75)

