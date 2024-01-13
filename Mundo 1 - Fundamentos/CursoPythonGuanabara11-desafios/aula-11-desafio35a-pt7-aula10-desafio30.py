colors = {
    'clean': '\033[m',
    'even': '\033[0;32m',
    'odd': '\033[0;31m'
}

n = int(input('Insert a number: '))

if n % 2 == 0:
    print('{}{}{} is a even number'.format(colors['even'], n, colors['clean']))
else:
    print('{}{}{} is a odd number'.format(colors['odd'], n, colors['clean']))