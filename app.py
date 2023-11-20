import random

# Initialize player's score
score = 0

# List of valid options
options = ['rock', 'paper', 'scissors']

while True:
    # Ask player for their choice
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Check if player's choice is valid
    if player_choice not in options:
        print("Invalid option. Please try again.")
        continue

    # Generate opponent's choice
    opponent_choice = random.choice(options)

    # Determine the winner
    if player_choice == opponent_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and opponent_choice == 'scissors') or \
         (player_choice == 'paper' and opponent_choice == 'rock') or \
         (player_choice == 'scissors' and opponent_choice == 'paper'):
        print("You won!")
        score += 1
    else:
        print("You lost!")

    # Ask player if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != 'yes':
        break

# Display player's score
print("Your score: ", score)