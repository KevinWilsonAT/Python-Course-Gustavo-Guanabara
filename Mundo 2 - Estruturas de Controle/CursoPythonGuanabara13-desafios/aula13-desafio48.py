sum = 0
count = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        sum += c
        count += 1

print('The addition of all the {} requested values is {}'.format(count, sum))
