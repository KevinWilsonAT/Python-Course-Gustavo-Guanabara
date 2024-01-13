colors = {
    'clean': '\033[m',
    'n': '\033[0;35m',
    'bef': '\033[0;32m',
    'aft': '\033[0;34m'
}

n = int(input('Insert and integer number: '))
print('The integer number is {}{}{}, its predecessor is {}{}{} and its sucessor is {}{}{}'
      .format(colors['n'], n, colors['clean'], colors['bef'], (n-1), colors['clean'], colors['aft'],
              n+1, colors['clean']))
