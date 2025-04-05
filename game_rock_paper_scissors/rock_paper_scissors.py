import random

while True:
    player_choice = input('your choice (rock, paper, scissors): ').lower()

    items = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(items)

    if player_choice == computer_choice:
        print(player_choice + ' vs ' + computer_choice)
        print('DRAW')
    elif player_choice == 'rock' and computer_choice == 'paper' or player_choice == 'paper' and computer_choice == 'scissors' or player_choice == 'scissors' and computer_choice == 'rock':
        print(player_choice + ' vs ' + computer_choice)
        print('computer WINS')
    else:
        print(player_choice + ' vs ' + computer_choice)
        print('player WINS')
