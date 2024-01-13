colors = {
    'clean':'\033[m',
    'yellow text':'\033[1;33m'}

nome = input("What is your name? ")
print("Hello {}{}{}! Nice to meet you!".format(colors['yellow text'], nome, colors['clean']))
