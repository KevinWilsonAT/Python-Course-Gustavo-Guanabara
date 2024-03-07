numbers = [[], []]
value = 0

print("PROGRAM STARTED.")
print("=" * 50)

for count in range(1, 8):
    value = int(input(f'Insert the value #{count}: '))
    if value % 2 == 0:
        numbers[0].append(value)
    else:
        numbers[1].append(value)

print("=" * 50)
numbers[1].sort()
numbers[0].sort()
print(f'All even inserted numbers: {numbers[0]}')
print(f'All odd inserted numbers: {numbers[1]}')

print("=" * 50)
print("PROGRAM ENDED.")
