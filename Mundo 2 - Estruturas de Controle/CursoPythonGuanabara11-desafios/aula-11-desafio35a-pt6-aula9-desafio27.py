colors = {
    'clean': '\033[m',
    'fin': '\033[0;32m',
    'lan': '\033[0;34m'
}

name = str(input("Insert your full name: ")).strip()
name = name.split()

print('First name: {}{}{}' .format(colors['fin'], name[0], colors['clean']))
print('Last name: {}{}{}' .format(colors['lan'], name[len(name)-1], colors['clean']))
