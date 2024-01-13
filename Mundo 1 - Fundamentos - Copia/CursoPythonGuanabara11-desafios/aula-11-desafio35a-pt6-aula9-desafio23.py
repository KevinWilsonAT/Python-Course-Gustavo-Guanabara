colors = {
    'clean': '\033[m',
    'n': '\033[0;31m',
    'u': '\033[0;32m',
    'd': '\033[0;33m',
    'c': '\033[0;34m',
    'm': '\033[0;35m'
}

n = int(input("Insert a number between 0 and 9999: "))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analyzing the number {}{}{}'.format(colors['n'], n, colors['clean']))

print('Units: {}{}{}'.format(colors['u'], u, colors['clean']))
print('Dozens: {}{}{}'.format(colors['d'], d, colors['clean']))
print('Hundreds: {}{}{}'.format(colors['c'], c, colors['clean']))
print('Thousands: {}{}{}'.format(colors['m'], m, colors['clean']))