numbers = list()
greater = lesser = 0

for count in range(0, 5):
    numbers.append(int(input(f'Insert a number in the position {count}: ')))

for index, value in enumerate(numbers):
    print(f'You inserted the values: {numbers}')

print(f'The Biggest value sorted is: {max(greater)}')
print(f'The Smallest value sorted is: {min(lesser)}')
