colors = {
    'clean': '\033[m',
    'red text': '\033[1;31m',
    'yellow text': '\033[1;33m',
    'blue text': '\033[1;34m'}

n1 = int(input('Insert a number: '))
n2 = int(input('Insert another number: '))
s = n1 + n2

print('The sum between {}{}{} and {}{}{} is {}{}{}'
      .format(colors['red text'], n1, colors['clean'], colors['yellow text'], n2, colors['clean'], colors['blue text'],
              s, colors['clean']))
