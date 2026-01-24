# Week 02 Lab - Rock, Paper, Scissors Game
# COMP2152

# Step 1: Define the choices array
choices = ["Rock", "Paper", "Scissors"]

# Step 2: Get player input
playerChoice = input("Enter your choice (1 = Rock, 2 = Paper, 3 = Scissors): ")

# Step 3: Convert to integer
playerChoice = int(playerChoice)

# Step 4: Error handling for player input
if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
else:
    # Step 5: Get computer choice (simulated input)
    computerChoice = input("Enter computer choice (1 = Rock, 2 = Paper, 3 = Scissors): ")
    computerChoice = int(computerChoice)

    # Validate computer choice
    if computerChoice < 1 or computerChoice > 3:
        print("Error: Computer choice must be between 1 and 3.")
    else:
        # Step 6: Array indexing (subtract 1 because lists start at 0)
        playerMove = choices[playerChoice - 1]
        computerMove = choices[computerChoice - 1]

        print("Player chose:", playerMove)
        print("Computer chose:", computerMove)

        # Step 7: Determine the winner
        if playerChoice == computerChoice:
            print("It's a tie!")
        elif playerChoice == 1 and computerChoice == 3:
            print("Rock beats Scissors - You win!")
        elif playerChoice == 2 and computerChoice == 1:
            print("Paper beats Rock - You win!")
        elif playerChoice == 3 and computerChoice == 2:
            print("Scissors beats Paper - You win!")
        else:
            print("You lose!")
