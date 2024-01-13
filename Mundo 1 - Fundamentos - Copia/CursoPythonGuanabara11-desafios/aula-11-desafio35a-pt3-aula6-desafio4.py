colors = {
    'clean': '\033[m',
    '1': '\033[0;30m',
    '2': '\033[1;31m',
    '3': '\033[4;32m',
    '4': '\033[7;33m',
    '5': '\033[1;34m',
    '6': '\033[0;35m',
    '7': '\033[4;36m',
    '8': '\033[7;37m',
    '9': '\033[0;38m',
    '10': '\033[4;39m'
}

a = input('Insert something: ')

print('Primitve Type: {}{}{}'.format(colors['1'], type(a), colors['clean']))
print('Has only spaces? {}{}{}'.format(colors['2'], a.isspace(), colors['clean']))
print('Is it a number? {}{}{}'.format(colors['3'], a.isnumeric(), colors['clean']))
print('Is it alphabetical? {}{}{}'.format(colors['4'], a.isalpha(), colors['clean']))
print('Is it alphanumerical? {}{}{}'.format(colors['5'], a.isalnum(), colors['clean']))
print('Is it uppercase? {}{}{}'.format(colors['6'], a.isupper(), colors['clean']))
print('Is it lowercase? {}{}{}'.format(colors['7'], a.islower(), colors['clean']))
print('Is it capitalized? {}{}{}'.format(colors['8'], a.istitle(), colors['clean']))
print('Is it decimal? {}{}{}'.format(colors['9'], a.isdecimal(), colors['clean']))
print('Is it a digit? {}{}{}'.format(colors['10'], a.isdigit(), colors['clean']))
