list_numbers = []
while True:
    list_numbers.append(int(input('Insert a number')))
    option = str(input('Continue? [Y/N] ')).upper().strip()[0]
    if option in 'N':
        break
print('=' * 30)
print(f'You inserted {len(list_numbers)} numbers')
list_numbers.sort(reverse = True)
print(f'The inserted number in decreasing order are: {list_numbers}')
if 5 in list_numbers:
    print('The number 5 was inserted in the list.')
else:
    print('The number 5 has been not inserted in the list.')