n = s = 0
while True:
    n = int(input('Insert a number: '))
    if n == 999:
        break
    s += n
# print('The total is {}'.format(s))
print(f'The total is {s}')