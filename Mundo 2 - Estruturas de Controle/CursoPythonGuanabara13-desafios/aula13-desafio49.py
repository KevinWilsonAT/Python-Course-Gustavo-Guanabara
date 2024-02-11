n = int(input('Insert a number: '))
print('-'*20)

for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
print('-'*20)
