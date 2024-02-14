from time import sleep
from random import randint

chosen = randint(0, 10)
guesses = 0

user = int(input('Insert a number: '))

while user != chosen:
    guesses += 1
    if user < chosen:
        user = int(input('More, insert a number: '))
    if user > chosen:
        user = int(input('Less, insert a number: '))

print('Processing...')
sleep(0.5)
print('Congrats! You discovered the hidden number: {}'.format(chosen))
print('With {} guesses'.format(guesses))
