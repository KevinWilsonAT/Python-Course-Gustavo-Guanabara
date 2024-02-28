numbers = []
greater = lesser = 0

for count in range(0, 5):
    numbers.append(int(input(f'Insert a number in the position {count}: ')))
    if count == 0:
        greater = lesser = numbers[count]
    else:
        if numbers[count] > greater:
            greater = numbers[count]
        if numbers[count] < lesser:
            lesser = numbers[count]

print(f'You inserted the values: {numbers}')

print(f'The Biggest value sorted is: {greater} at positions: ', end='')
for index, value in enumerate(numbers):
    if value == greater:
        print(f'{index}, ', end ='')
print()
print(f'The Smallest value sorted is: {lesser} at positions: ', end='')
for index, value in enumerate(numbers):
    if value == lesser:
        print(f'{index}, ', end ='')