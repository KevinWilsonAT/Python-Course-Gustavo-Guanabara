from random import randint
from time import sleep

listNumbers = list()
games = list()

print("PROGRAM STARTED.")
print("="*50)

qty = int(input('How many games do you want me to sort? '))
total = 1

while total <= qty:
    count = 0

    while True:
        numbers = randint(1, 60)

        if numbers not in listNumbers:
            listNumbers.append(numbers)
            count += 1

        if count >= 6:
            break

    listNumbers.sort()
    games.append(listNumbers[:])
    listNumbers.clear()
    total += 1

print('#=#=' * 3, f' Sorting {qty} games', '=#=#' * 3)
for gameNumber, gameList in enumerate(games):
    print(f'Game #{gameNumber+1}: {gameList}')
    sleep(2)

print("="*50)
print("PROGRAM ENDED.")
