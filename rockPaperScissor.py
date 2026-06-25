import random
UserScore = 0
ComputerScore = 0
while True:
    inp = input("Enter rock, paper, or scissors or q to exit: ").lower()
    if inp == 'q':
        print("Thanks for playing!")
        print(f"Final Score - You: {UserScore}, Computer: {ComputerScore}")
        quit()
    if inp not in ['rock', 'paper', 'scissors', 'q']:
        print("Invalid input. Please try again.")
        continue
    randChoice = random.choice(['rock', 'paper', 'scissors'])
    if inp == 'paper' and randChoice == 'rock':
        print(f"You chose {inp} and the computer chose {randChoice}. You win!")
        UserScore += 1
    elif inp == 'rock' and randChoice == 'scissors':
        print(f"You chose {inp} and the computer chose {randChoice}. You win!")
        UserScore += 1
    elif inp == 'scissors' and randChoice == 'paper':
        print(f"You chose {inp} and the computer chose {randChoice}. You win!")
        UserScore += 1
    elif inp == randChoice:
        print(f"You chose {inp} and the computer chose {randChoice}. It's a tie!")
    else:
        print(f"You chose {inp} and the computer chose {randChoice}. You lose!")
        ComputerScore += 1