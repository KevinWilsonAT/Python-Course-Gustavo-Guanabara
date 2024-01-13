colors = {
    'clean': '\033[m',
    'has': '\033[0;32m',
}

person = input("Person's name: ").strip()

print('Does your name has Silva? {}{}{}'.format(colors['has'],'SILVA' in person.upper(), colors['clean']))
