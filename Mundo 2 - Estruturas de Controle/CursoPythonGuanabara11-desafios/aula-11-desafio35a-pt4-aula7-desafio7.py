colors = {
    'clean': '\033[m',
    'n1': '\033[0;31m',
    'n2': '\033[0;32m',
    'avg': '\033[0;33m'
}

n1 = float(input('Insert the first note: '))
n2 = float(input('Insert the second note: '))
avg = (n1 + n2) / 2

print('The average between the notes {}{:.1f}{} and {}{:.1f}{} is: {}{:.1f}{}'
      .format(colors['n1'], n1, colors['clean'], colors['n2'], n2, colors['clean'],
              colors['avg'], avg, colors['clean']))