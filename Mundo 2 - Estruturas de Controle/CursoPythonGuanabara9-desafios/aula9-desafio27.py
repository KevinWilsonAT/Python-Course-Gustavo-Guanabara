name = str(input("Insert your full name: ")).strip()

name = name.split()

print('First name: {}' .format(name[0]))
print('Last name: {}' .format(name[len(name)-1]))
