import random

# Main function to simulate the roll of a die
def roll():
    min_value = 1  # Minimum value of the die
    max_value = 6  # Maximum value of the die
    roll = random.randint(min_value, max_value)  # Generate a random number between min_value and max_value
    return roll

# Uncomment below lines to test the roll function
# value = roll()
# print(value)

# Loop to get the number of players
while True:
    players = input("Enter the number of players (1-4): ")
    
    # Check if the input is a digit
    if players.isdigit():
        players = int(players)

        # Check if the number of players is between 1 and 4
        if 1 <= players <= 4:
            break  # Exit the loop if valid input
        else:
            print("Players input must be between 1-4")
    else:
        print("Invalid input!!")
    
max_score = 100  # The max score a player can achieve
player_scores = [0 for _ in range(players)]  # Initialize scores for all players to 0

# Loop until any player reaches the max score
while max(player_scores) < max_score:
    for index_players in range(players):
        print(f"\nPlayer {index_players + 1} is playing\n")
        print(f"Your current score is: {player_scores[index_players]}")
        current_score = 0  # Reset current score for the player's turn

        while True:
            turn = input("Would you like to play further and roll the die again? (yes/no): ")
            if turn.lower() != 'yes':
                break  # Exit the loop if the player chooses not to roll again

            value = roll()  # Roll the die
            if value == 1:
                print("You rolled a 1, no score for this turn")
                current_score = 0  # Reset current score if a 1 is rolled
                break
            else:
                current_score += value  # Add the rolled value to the current score
                print(f"You rolled a {value}")

            print(f"Your current score is: {current_score}")
        
        player_scores[index_players] += current_score  # Add the current score to the player's total score
        print(f"Your total score is: {player_scores[index_players]}")  # Print the total score for the player

max_score=max(player_scores)
winningscore=player_scores.index(max_score)
print(f"\nPlayer {winningscore + 1} wins with a score of {max_score}")  # Print the winner of the game