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