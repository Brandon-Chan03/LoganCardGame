import random

from Cards import cards
from Player import Player
from UI import printUi

yes = ["yes", 'y']
no = ['no', 'n']

print("Hello Welcome to My Game\nDo you want to play?")
run = True
playGame = False

while run:

    startGame = input('Y/N: ')

    if (startGame.lower() in yes):
        playGame = True
        break
    elif (startGame.lower() in no):
        print("Goodbye")
        break
    else:
        continue

if (playGame):

    player_one_name = input("Enter Player One's Name: ")
    player_two_name = input("Enter Player Two's Name: ")

    deck1 = random.sample(cards, len(cards))
    player_one = Player(player_one_name, deck1)

    deck2 = random.sample(cards, len(cards))
    player_two = Player(player_two_name, deck2)

    print(f'Welcome {player_one.getName()} and {player_two.getName()}')

    while True:
        if (player_one.getHealth() <= 0 or player_two.getHealth() <= 0):
            print('Game Over')
            break

        printUi(player_one.getName(), player_two.getName(), player_one.getHealth(), player_two.getHealth())
        
        

    printUi(player_one.getName(), player_two.getName(), player_one.getHealth(), player_two.getHealth())
    

    

