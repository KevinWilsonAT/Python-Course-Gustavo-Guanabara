from random import randint
numbers = (randint(1,10), randint(1,10), randint(1,10),randint(1,10), randint(1,10))
greater = lesser = 0

print('The sorted values are: ', end='')
for n in numbers:
    print(f'{number} ', end='')

print(f'The Biggest value sorted is: {max(greater)}')
print(f'The Smallest value sorted is: {min(lesser)}')
