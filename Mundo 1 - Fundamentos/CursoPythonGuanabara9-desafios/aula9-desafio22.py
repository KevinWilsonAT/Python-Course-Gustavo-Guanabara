name = str(input("Insert your full name: ")).strip()
splitter = name.split()

print('Analyzing...')

print('Uppercase is: {}'.format(name.upper()))
print('Lowercase is: {}'.format(name.lower()))
print('Your full name has {} letters'.format(len(name) - name.count(' ')))
print('Your first name has {} letters' .format(name.find(' ')))
print(('Your first name is {} and it has {} letters' .format(splitter[0], len(splitter[0]))))
