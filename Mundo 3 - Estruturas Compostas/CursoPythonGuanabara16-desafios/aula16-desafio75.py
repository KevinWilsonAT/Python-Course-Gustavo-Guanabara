numbers = ( int(input('Insert the first number: ')),
            int(input('Insert the second number: ')),
            int(input('Insert the third number: ')),
            int(input('Insert the fourth number: ')))

print(f'The number 9 appeared {numbers.count(9)} times inside the tuple')
print('='*70 + '\n')

if 3 in (numbers):
    print(f'The number 3 appeared at position {numbers.index(3)+1} inside the tuple')
else:
    print('There is no number 3 in the tuple')
print('='*70 + '\n')

for n in numbers:
    if n % 2 == 0:
        print(numbers, end='')
