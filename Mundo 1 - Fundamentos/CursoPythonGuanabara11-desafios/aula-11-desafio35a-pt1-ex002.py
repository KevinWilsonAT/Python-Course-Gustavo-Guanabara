colors = {
    'clean':'\033[m',
    'red text':'\033[1;31m',
    'highlight text':'\033[4;31m'}

name = input('Type your '+colors['highlight text']+'name'+colors['clean']+':')
print("It's nice to meet you,{}{}{}!".format(colors['red text'], name, colors['clean']))
