colors = {
    'clean': '\033[m',
    'n1': '\033[0;31m',
    'n2': '\033[0;33m',
    'm': '\033[0;34m'
}

n = int(input('digite um numero: '))

print('-'*12)
print('{}{}{} x {}{:2}{} = {}{}{}'
      .format(colors['n1'], n, colors['clean'], colors['n2'], 0, colors['clean'], colors['m'], n*0, colors['clean']))
print('{}{}{} x {}{:2}{} = {}{}{}'
      .format(colors['n1'], n, colors['clean'], colors['n2'], 1, colors['clean'], colors['m'], n*1, colors['clean']))
print('{}{}{} x {}{:2}{} = {}{}{}'
      .format(colors['n1'], n, colors['clean'], colors['n2'], 2, colors['clean'], colors['m'], n*2, colors['clean']))
print('{}{}{} x {}{:2}{} = {}{}{}'
      .format(colors['n1'], n, colors['clean'], colors['n2'], 3, colors['clean'], colors['m'], n*3, colors['clean']))
print('{}{}{} x {}{:2}{} = {}{}{}'
      .format(colors['n1'], n, colors['clean'], colors['n2'], 4, colors['clean'], colors['m'], n*4, colors['clean']))
print('{}{}{} x {}{:2}{} = {}{}{}'
      .format(colors['n1'], n, colors['clean'], colors['n2'], 5, colors['clean'], colors['m'], n*5, colors['clean']))
print('{}{}{} x {}{:2}{} = {}{}{}'
      .format(colors['n1'], n, colors['clean'], colors['n2'], 6, colors['clean'], colors['m'], n*6, colors['clean']))
print('{}{}{} x {}{:2}{} = {}{}{}'
      .format(colors['n1'], n, colors['clean'], colors['n2'], 7, colors['clean'], colors['m'], n*7, colors['clean']))
print('{}{}{} x {}{:2}{} = {}{}{}'
      .format(colors['n1'], n, colors['clean'], colors['n2'], 8, colors['clean'], colors['m'], n*8, colors['clean']))
print('{}{}{} x {}{:2}{} = {}{}{}'
      .format(colors['n1'], n, colors['clean'], colors['n2'], 9, colors['clean'], colors['m'], n*9, colors['clean']))
print('{}{}{} x {}{:2}{} = {}{}{}'
      .format(colors['n1'], n, colors['clean'], colors['n2'], 10, colors['clean'], colors['m'], n*10, colors['clean']))
print('-'*12)