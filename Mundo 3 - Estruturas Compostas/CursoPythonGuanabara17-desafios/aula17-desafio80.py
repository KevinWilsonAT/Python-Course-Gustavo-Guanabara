list_numbers = []
for count in range(0, 5):
    number = int(input('Insert a number: '))
    if count == 0 or number > list_numbers[-1]:
        list_numbers.append(number)
        print('Add to the end of the list')
    else:
        position = 0
        while position < len(list_numbers):
            if number <= list_numbers[position]:
                list_numbers.insert(position, number)
                print(f'Added in the position {position} of the list.')
                break
            position += 1
print('='*30)
print(f'The inserted numbers in order are: {list_numbers}')