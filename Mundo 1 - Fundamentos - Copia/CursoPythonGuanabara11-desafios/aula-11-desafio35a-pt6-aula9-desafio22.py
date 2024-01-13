colors = {
    'clean': '\033[m',
    'upc': '\033[0;31m',
    'lwc': '\033[0;32m',
    'fun': '\033[0;33m',
    'fn': '\033[0;34m',
    'fin': '\033[0;35m',
    'many_let': '\033[0;36m'
}

name = str(input("Insert your full name: ")).strip()
splitter = name.split()

print('Analyzing...')

print('Uppercase is: {}{}{}'.format(colors['upc'], name.upper(), colors['clean']))
print('Lowercase is: {}{}{}'.format(colors['lwc'], name.lower(), colors['clean']))
print('Your full name has {}{}{} letters'.format(colors['fun'], len(name) - name.count(' '), colors['clean']))
print('Your first name has {}{}{} letters' .format(colors['fn'], name.find(' '), colors['clean']))
print('Your first name is {}{}{} and it has {}{}{} letters'
       .format(colors['fin'], splitter[0], colors['clean'], colors['many_let'], len(splitter[0]), colors['clean']))