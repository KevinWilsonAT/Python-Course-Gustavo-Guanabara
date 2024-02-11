colors = {
    'clean': '\033[m',
    'r1': '\033[0;31m',
    'r2': '\033[0;32m',
    'avg': '\033[0;33m'
}

r1 = float(input('Insert the first rank: '))
r2 = float(input('Insert the second rank: '))
avg = (r1 + r2) / 2

print('The average between the ranks {}{:.1f}{} and {}{:.1f}{} is: {}{:.1f}{}'
      .format(colors['n1'], n1, colors['clean'], colors['n2'], n2, colors['clean'],
              colors['avg'], avg, colors['clean']))