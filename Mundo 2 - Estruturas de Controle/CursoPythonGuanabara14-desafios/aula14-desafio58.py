from time import sleep
from random import randint

chosen = randint(0, 10)
guesses = 0

user = int(input('Insert a number: '))

while user != chosen:
    print('Too bad! Try Again')
    guesses += 1
    user = int(input('Insert a number: '))


print('Processing...')
sleep(0.5)
print('Congrats! You discovered the hidden number: {}'.format(chosen))
print('With {} guesses'.format(guesses))