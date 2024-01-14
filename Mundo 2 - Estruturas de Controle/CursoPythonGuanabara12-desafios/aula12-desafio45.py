from random import randint
from time import sleep

you = int(input('Rock (0), Paper (1) or Scissors (2)? '))
cpu_chosen = randint(0, 2)

print('-='*20)
print('Jo...')
sleep(1)
print('Ken...')
sleep(1)
print('Po...')
print('-='*20)

if cpu_chosen == 0:
    if you == 0:
        print('It is a draw!!!     YOU: ''\u270A''     CPU: ''\u270A')
    elif you == 1:
        print('You Win!!!     YOU: ''\u270B''     CPU: ''\u270A')
    elif you == 2:
        print('You Lose!!!     YOU: ''\u270C''     CPU: ''\u270A')
    else:
        print('Invalid Command!')

elif cpu_chosen == 1:
    if you == 0:
        print('You Lose!!!     YOU: ''\u270A''     CPU: ''\u270B')
    elif you == 1:
        print('It is a draw!!!     YOU: ''\u270B''     CPU: ''\u270B')
    elif you == 2:
        print('You Win!!!     YOU: ''\u270C''     CPU: ''\u270B')
    else:
        print('Invalid Command!')
elif cpu_chosen == 2:
    if you == 0:
        print('You Win!!!     YOU: ''\u270A''     CPU: ''\u270C')
    elif you == 1:
        print('You Lose!!!     YOU: ''\u270B''     CPU: ''\u270C')
    elif you == 2:
        print('It is a draw!!!     YOU: ''\u270C''     CPU: ''\u270C')
    else:
        print('Invalid Command!')