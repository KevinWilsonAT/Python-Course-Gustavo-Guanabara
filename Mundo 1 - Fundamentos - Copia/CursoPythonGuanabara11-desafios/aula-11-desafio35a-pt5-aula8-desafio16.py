colors = {
    'clean': '\033[m',
    'int': '\033[0;32m',
    'intp': '\033[0;35m',
}

from math import trunc

num = float(input('Insert a number: '))
intp = trunc(num)

print('The number {}{}{} has the integer part {}{}{}'.format(
    colors['int'], num, colors['clean'], colors['intp'], intp, colors['clean']))
