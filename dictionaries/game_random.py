from random import randint
from time import sleep
from operator import itemgetter

players = {}
ranking = {}

players['player1'] = randint(1,6)
players['player2'] = randint(1,6)
players['player3'] = randint(1,6)
players['player4'] = randint(1,6)

for p, n in players.items():
    print(f'{p.title()} got the number {n}.')
    sleep(1)

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)

for p, n in enumerate(ranking):
    print(f'{p+1} place: {n[0]} with {n[1]}.')
    sleep(1)