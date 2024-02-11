summation = 0
count = 0

for c in range(1, 7):
    n = int(input('Insert a value: '))

    if n % 2 == 0:
        count += 1
        summation += n

print('You informed {} even numbers and its summation are: {}'.format(count, summation))
