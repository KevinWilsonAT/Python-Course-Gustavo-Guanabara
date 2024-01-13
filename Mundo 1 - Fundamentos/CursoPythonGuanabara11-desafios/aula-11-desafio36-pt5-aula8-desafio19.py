from random import choice

n1 = str(input('1st student: '))
n2 = str(input('2nd student: '))
n3 = str(input('3rd student: '))
n4 = str(input('4th student: '))
l = [n1, n2, n3, n4]
chosen = choice(l)
print('The chosen student is: {}'.format(chosen))