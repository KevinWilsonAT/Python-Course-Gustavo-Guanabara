while True:
    number = int(input('Insert a number to see its multiplication sheet\n(Insert negative value to stop): '))
    if number < 0:
        break
    print('-'*20)
    for count in range(1, 11):
        print(f'{number} x {count} = {number*count}')
    print('-'*20)
print('-'*20)
print('MULTIPLICATION SHEET PROGRAM ENDED.')
