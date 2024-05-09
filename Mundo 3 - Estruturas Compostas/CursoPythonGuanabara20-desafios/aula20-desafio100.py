from random import randint
from time import sleep

print("PROGRAM STARTED.")
print("=" * 50)

def sort(list):
    print('Sorting 5 number of the list: ', end='')
    for count in range(0, 5):
        n = randint(1,10)
        list.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)

def sumEven(list):
    add = 0
    for value in list:
        if value % 2 == 0:
            add += value
    print('Adding the even values of the list {list}, the result is {add}')

numbers = list()
sort(numbers)
sumEven(numbers)

print("=" * 50)
print("PROGRAM ENDED.")
