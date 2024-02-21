number = sum = count = 0
while True:
    number = int(input('Insert a number (Insert 999 to stop): '))
    if number == 999:
        break
    sum += number
    count += 1
# print('The total of the {} number(s) is {}'.format(count, sum))
print(f'The total of the {count} number(s) is {sum}')
