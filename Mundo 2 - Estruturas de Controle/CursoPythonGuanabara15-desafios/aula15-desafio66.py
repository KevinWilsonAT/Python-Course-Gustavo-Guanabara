total = count = 0
while True:
    number = int(input('Insert a number (Insert 999 to stop): '))
    if number == 999:
        break
    total += number
    count += 1
print(f'The total of the {count} number(s) is {total}')
