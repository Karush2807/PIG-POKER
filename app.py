import random
def roll():
    min_value=1
    max_value=6
    roll= random.randint(min_value, max_value)

    return roll


value=roll()
print(value)
while True:
    players=input("enter the number of players(1-4): ")
    if players.isdigit():
        
        players=int(players)

        if 1<=players<4:
            break
        else:
            print("Players input, must be between 1-4")
    else:
        print("invalid, input!!")
    
max_score=100
player_scores=[0 for i in range(len(players))]
n_turns=int(input("number of turns u want: "))