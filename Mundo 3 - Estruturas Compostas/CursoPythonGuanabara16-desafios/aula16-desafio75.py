n1 = int(input('Insert the first number: '))
n2 = int(input('Insert the second number: '))
n3 = int(input('Insert the third number: '))
n4 = int(input('Insert the fourth number: '))

numbers = (n1, n2, n3, n4)

print(f'The number 9 appeared {numbers.count(9)} times inside the tuple')
print('='*20 + '\n')

if 3 not in (numbers[0:]):
    print('There is no number 3 in the tuple')
else:
    print(f'The number 3 appeared at position {numbers.index(3)} inside the tuple')
print('='*70 + '\n')