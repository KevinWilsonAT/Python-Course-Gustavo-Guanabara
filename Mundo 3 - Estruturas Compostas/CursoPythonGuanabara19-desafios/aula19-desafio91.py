from random import randint
from time import sleep
from operator import itemgetter

print("PROGRAM STARTED.")
print("=" * 50)

game = {str(input('Player 1 Name: ')): randint(1, 6),
        str(input('Player 2 Name: ')): randint(1, 6),
        str(input('Player 3 Name: ')): randint(1, 6),
        str(input('Player 4 Name: ')): randint(1, 6),
        }

ranking = dict()

sleep(1)
print('==' * 15)
sleep(1)

for keys, values in game.items():
    print(f'{keys} draws {values} from the dice')
    sleep(1)

ranking = sorted(game.items(), key=itemgetter(1), reverse=True)

print('==' * 15)
print('====== PLAYERS  RANKING ======')
print('==' * 15)
sleep(1)

for r_place, pl_data in enumerate (ranking):
    print(f'Rank #{r_place + 1}: {pl_data[0]} with number {pl_data[1]}')
    sleep(1)
print("=" * 50)
print("PROGRAM ENDED.")
