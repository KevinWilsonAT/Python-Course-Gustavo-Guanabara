colors = {
    'clean': '\033[m',
    'win': '\033[0;32m',
    'lose': '\033[0;34m'
}

from random import randint

chosen = randint(0, 5)

user = int(input('Insert a number: '))

if user == chosen:
    print('Processing...')
    print('Congrats! You discovered the hidden number: {}{}{}'.format(colors['win'], chosen, colors['clean']))
else:
    print('Too bad! The hidden number was {}{}{}' .format(colors['lose'], chosen, colors['clean']))
