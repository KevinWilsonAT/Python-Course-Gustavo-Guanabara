number = sum = count = 0
while True:
    number = int(input('Insert a number to see its multiplication sheet\n(Insert negative value to stop): '))
    if number < 0:
        break

    print('-'*20)
    for count in range(1, 11):
        print('{} x {:2} = {}'.format(number, count, number*count))
    print('-'*20)
print('-'*20)
print('MULTIPLICATION SHEET PROGRAM ENDED.')