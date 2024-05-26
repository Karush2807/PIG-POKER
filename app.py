import random

#main function for the game
def roll():
    min_value=1
    max_value=6
    roll= random.randint(min_value, max_value)
    return roll


# value=roll()
# print(value)

while True:
    players=input("enter the number of players(1-4): ")
    
    #loop initiated to take proper number of players playing input
    if players.isdigit():
        players=int(players)

        if 1<=players<4:
            break #ye first-wale if loop se break hoke, bahar aajayga
        else:
            print("Players input, must be between 1-4")
    else:
        print("invalid, input!!")
    
max_score=100 #the max score is decided, a player can achieve
player_scores=[0 for _ in range(players)] #generated an empty list

while max(player_scores)<max_score:

    for index_players in range(players):
        print(f"\nPlayer {index_players+1} is playing\n")
        print(f"you current score is: {player_scores[index_players]}")
        current_score=0

        while True:

            turn=input("Would u like to play further and roll the die again?(yes/no): ")
            if turn.lower()!='yes':
                break

            value=roll()
            if value==1:
                print("You rolled a 1, no score for this turn")
                current_score=0
                break
            
            else:
                current_score+=value
                print(f"you rolled a {value}")

            print(f"your current score is: {current_score}")
        
        player_scores[index_players]+=current_score
        print(f"your total score is: {player_scores[index_players]}")