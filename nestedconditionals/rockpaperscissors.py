from time import sleep
from random import choice
from emoji import emojize

print('\033[1;43mROCK PAPER SCISSORS\033[m')

player = input('Rock Paper or Scissors: ').lower()
list = ['Rock', 'Paper', 'Scissors']
computer = choice(list).lower()

print('\033[31mLoading...\033[m')
sleep(2)

if computer == player:
    print(emojize(f'We both played {player}. It is a tie! 🤨'))
elif computer == 'rock':
    if player == 'paper':
        print(emojize('Paper covers rock. You win!:thumbs_up:'))
    else:
        print(emojize('Rock smashes scissors. I win! 😂'))
elif computer == 'paper':
    if player == 'rock':
        print(emojize('Paper covers rock. I win! 😂'))
    else:
        print(emojize('Scissors cuts paper. You win!:thumbs_up:'))
elif computer == 'scissors':
    if player == 'paper':
        print(emojize('Scissors cuts paper. I win! 😂'))
    else:
        print(emojize('Rock smashes scissors. You win!:thumbs_up:'))
else:
    print('ERROR! Try again.')
