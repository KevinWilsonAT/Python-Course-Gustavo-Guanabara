colors = {
    'clean':'\033[m',
    'green text':'\033[1;32m'}

n1 = int(input('First number: '))
n2 = int(input('Second number: '))
s = n1 + n2

print('The sum is {}{}{}.'.format(colors['green text'], s, colors['clean']))