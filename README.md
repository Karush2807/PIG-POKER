# Dice Game

This is a simple dice game implemented in Python where players take turns rolling a die, accumulating points until one of the players reaches a maximum score of 100. The game supports 1 to 4 players.

## How to Play

1. **Start the Game**:
    - Run the script.
    - Enter the number of players (between 1 and 4).

2. **Player Turns**:
    - Each player takes turns rolling a die.
    - After each roll, the player can choose to roll again or hold.
    - If a player rolls a 1, their turn ends, and they score no points for that turn.
    - If the player rolls any other number, that number is added to their current turn's score.
    - The player can keep rolling to accumulate more points or hold to add the current turn's score to their total score.

3. **Winning the Game**:
    - The first player to reach a total score of 100 wins the game.

## Code Overview

### `roll` Function

```python
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
```
### Main Game Loop

```pyhton
while max(player_scores) < max_score:
    for index_players in range(players):
        print(f"\nPlayer {index_players + 1} is playing\n")
        print(f"Your current score is: {player_scores[index_players]}")
        current_score = 0

        while True:
            turn = input("Would you like to play further and roll the die again? (yes/no): ")
            if turn.lower() != 'yes':
                break

            value = roll()
            if value == 1:
                print("You rolled a 1, no score for this turn")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}")

            print(f"Your current score is: {current_score}")
        
        player_scores[index_players] += current_score
        print(f"Your total score is: {player_scores[index_players]}")
```

### EXAMPLE OUTPUT 

```bash
Enter the number of players (1-4): 2

Player 1 is playing

Your current score is: 0
Would you like to play further and roll the die again? (yes/no): yes
You rolled a 4
Your current score is: 4
Would you like to play further and roll the die again? (yes/no): yes
You rolled a 3
Your current score is: 7
Would you like to play further and roll the die again? (yes/no): no
Your total score is: 7

Player 2 is playing

Your current score is: 0
Would you like to play further and roll the die again? (yes/no): yes
You rolled a 1
You rolled a 1, no score for this turn
Your total score is: 0
...
```