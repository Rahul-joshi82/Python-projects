import random

choice = ['rock', 'paper', 'scissors']

# Initialize scores
computerScore = 0
userScore = 0

while True:
    # check winning condition
    if computerScore == 3 or userScore == 3:
        print(f"User Score - {userScore}")
        print(f"Computer Score - {computerScore}")
        if computerScore > userScore:
            print("Computer wins the game!")
        else:
            print("You win the game!")
        break

    # new choices every round
    computerChoice = random.choice(choice)
    userChoice = input("Enter rock, paper or scissors: ").lower()

    # if invalid input
    if userChoice not in choice:
        print("Invalid choice! Try again.\n")
        continue

    print(f"Computer chose: {computerChoice}")
    print(f"You chose: {userChoice}")

    # compare results
    if computerChoice == userChoice:
        print("It's a tie!\n")

    elif (userChoice == 'rock' and computerChoice == 'scissors') or \
         (userChoice == 'paper' and computerChoice == 'rock') or \
         (userChoice == 'scissors' and computerChoice == 'paper'):
        print("You win this round!\n")
        userScore += 1
    else:
        print("Computer wins this round!\n")
        computerScore += 1
