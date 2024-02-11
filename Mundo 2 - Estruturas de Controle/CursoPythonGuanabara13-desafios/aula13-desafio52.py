num = int(input("Insert a number: "))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[38m', end='')
    print('{} '.format(c), end='')
print('\n\033[mThe number {} is divisible {} times'.format(num, tot))
if tot == 2:
    print('Then the number IS A PRIME NUMBER')
else:
    print('Then the number IS NOT A PRIME NUMBER')
