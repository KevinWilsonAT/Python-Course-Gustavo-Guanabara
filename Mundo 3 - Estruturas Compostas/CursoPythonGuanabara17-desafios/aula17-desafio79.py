list_numbers = list()

while True:
    numbers = int(input('Insert a value: '))
    if numbers not in list_numbers:
        list_numbers.append(numbers)
        print('Number Inserted Successfully')
    else:
        print('Duplicated Number. Insert denied.')
    option = str(input('Continue? [Y/N]')).upper().strip()[0]
    if option in 'N':
        break
print('='*40)
print(f'You inserted the following numbers:\n{list_numbers}')