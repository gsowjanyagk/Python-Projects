import random

print("-" * 75)
print("                         Welcome to Mastermind!")
print("The objective of the games is to guess the randomly generated 4 digit number.")
print("-" * 75)

#randno = random.randint(1000, 9999)
randno = f"{random.randint(0, 9999):04d}"
#print(randno)
attempts = 0

# select difficulty - easy
while True:
    difficulty = input("Select difficulty level (easy, hard): ").lower()
    print("-" * 75)
    if difficulty == "easy":
        print("You have choosen easy difficulty.")
        print("Hint will be provided if correct digit is in correct or incorrect position.")
        print("You have unlimited attempts to guess the number.")
        print("-" * 75)
        while True:
            try:
                guess = input("Enter a 4 digit number: ")
                attempts += 1
                if len(guess) != 4 or not guess.isdigit():
                    print("Invalid input. Please enter a 4 digit number.")
                    print("-" * 75)
                    continue
            except ValueError:
                print("Invalid input. Please enter a 4 digit number.")
                print("-" * 75)
                continue
            if guess == randno:
                print(f"Yay! You've guessed the number {randno} in {attempts} attempt(s)!")
                break
            correct = 0
            outputlist = ['x'] * 4
            # adding code for incorrect position
            list_guess = list(guess)
            randno_list = list(randno)
            incorrect_position = []
            incorrect = 0
            for i in range(4):
                if randno_list[i] in list_guess and guess[i] != randno[i]:
                    incorrect += 1
                    incorrect_position.append(randno_list[i])
            print(f"Digits placed in incorrect position: {" ".join(incorrect_position)}")    
            ###
            for i in range(4):
                if guess[i] == randno[i]:
                    correct += 1
                    outputlist[i] = guess[i]
            print(f"Not there yet! You have {correct} digit(s) in the correct position.")
            print(f"Here is your progress: {" ".join(outputlist)}")
            print("-" * 75)
    # hard difficulty
    elif difficulty == "hard":
        print("You have choosen hard difficulty.")
        print("Hint will be provided if correct digit is in correct position. only")
        print("You have 10 attempts to guess the number.")
        print("-" * 75)
        for i in range(10):
            try:
                guess = input("Enter a 4 digit number: ")
                attempts += 1
                if len(guess) != 4 or not guess.isdigit():
                    print("Invalid input. Please enter a 4 digit number.")
                    print("-" * 75)
                    continue
            except ValueError:
                print("Invalid input. Please enter a 4 digit number.")
                print("-" * 75)
                continue
            if guess == randno:
                print(f"Yay! You've guessed the number {randno} in {attempts} attempt(s)!")
                break
            correct = 0
            outputlist = ['x'] * 4
            for j in range(4):
                if guess[j] == randno[j]:
                    correct += 1
                    outputlist[j] = guess[j]
            print(f"Not there yet! You have {correct} digit(s) in the correct position.")
            print(f"Here is your progress: {" ".join(outputlist)}")
            print("-" * 75)
        print(f"Sorry! You've used all your attempts. The number was {randno}. Better luck next time!")
    else:
        print("Invalid difficulty level. Please choose either 'easy' or 'hard'.")
        continue