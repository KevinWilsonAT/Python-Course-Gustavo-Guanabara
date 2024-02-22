from random import randint
streak = 0

while True:
    player = int(input('Insert a value: '))
    cpu = randint(0, 10)
    total = player + cpu
    oddEven = ' '
    while oddEven not in 'OE':
        oddEven = str(input('Odd or Even? [O/E]: ')).strip().upper()[0]
    print(f'You have chosen {player} and the computer have chosen {cpu}. Total of {total}. ', end='')
    print('It\'s a EVEN NUMBER' if total % 2 == 0 else 'It\'s an ODD NUMBER')
    if oddEven == 'E':
        if total % 2 == 0:
            print('You Win')
            streak += 1
        else:
            print('You Lose')
            break
    elif oddEven == 'O':
        if total % 2 == 1:
            print('You Win')
            streak += 1
        else:
            print('You Lose')
            break
    print('Let\'s play again')
print(f'GAME OVER!\nYour Streak is: {streak}')
