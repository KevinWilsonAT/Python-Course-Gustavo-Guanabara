number = int(input('Type an integer number: '))
base = int(input('In which base do you want to convert? (1 = binary / 2 = octal / 3 for hex) '))
binary = bin(number)
octal = oct(number)
hex = hex(number)

if base == 1:
    print('Number {} in binary base is: {}'.format(number, binary[2:]))
elif base == 2:
    print('Number {} in octal base is: {}'.format(number, octal[2:]))
elif base == 3:
    print('Number {} in hexadecimal base is: {}'.format(number, hex[2:]))
else:
    print('Invalid Command!')
