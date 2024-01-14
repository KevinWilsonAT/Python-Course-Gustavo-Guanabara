from random import randint
chosen = randint(0, 5)

user = int(input('Insert a number: '))

if user == chosen:
    print('Processing...')
    print('Congrats! You discovered the hidden number: {}'.format(chosen))
else:
    print('Too bad! The hidden number was {}' .format(chosen))
