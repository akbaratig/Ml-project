import random

count_player = 0
count_system = 0
eqal_round = 0

actions = ['rock', 'paper', 'scissors']

for item in range(10):
    print(f"Round {item}")
    action_player = input('Chosse actions ["Rock" , "Scissors", "Paper"] : ')
    action_player = action_player.lower()
    while action_player not in actions:
        print('SomeThing Went Wrong')
        action_player = input('Chosse actions ["Rock" , "Scissors", "Paper"] : ')

    action_system = random.choice(actions)
    print(f"action System : {action_system}")
    

    if action_system == 'paper' and action_player == 'rock':
        count_system += 1
        print(f"System win is Round >> {item}")
    elif action_system == 'paper' and action_player == 'scissors':
        count_player += 1
        print(f"Player win is Round >> {item}")
    elif action_system == 'paper' and action_player == 'paper':
        eqal_round += 0
        print(f"Tie!!!!!")
    elif action_system == 'rock' and action_player == 'rock':
        eqal_round += 0
        print(f"Tie!!!!!")
    elif action_system == 'rock' and action_player == 'paper':
        count_player += 1
        print(f"Player win is Round >> {item}")
    elif action_system == 'rock' and action_player == 'scissors':
        count_system += 1
        print(f"System win is Round >> {item}")
    elif action_system == 'scissors' and action_player == 'rock':
        count_player += 1
        print(f"Player win is Round >> {item}")
    elif action_system == 'scissors' and action_player == 'scissors':
        eqal_round += 1
        print(f"Tie!!!!!")
    elif action_system == 'scissors' and action_player == 'paper':
        count_system += 1
        print(f"System win is Round >> {item}")
    print('--------------------------------------')

print(f"Score for System : {count_system}")
print(f"Score for Player : {count_player}")
print(f"Score for eqal : {eqal_round}")


if count_player == count_system:
    print('The Game is Eqal!!!')
elif count_player > count_system:
    print('Player is Win!!!')
elif count_player < count_system:
    print('system is Win!!!') 