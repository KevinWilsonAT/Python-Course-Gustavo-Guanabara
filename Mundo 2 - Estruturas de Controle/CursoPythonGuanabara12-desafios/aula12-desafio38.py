n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))

if n1 > n2:
    print('The first number is greater than the second number. ({} > {})'.format(n1, n2))
elif n1 < n2:
    print('The second number is greater than the first number. ({} < {})'.format(n2, n1))
else:
    print('Does not exist a greater number. Both are equal ({} = {})'.format(n1, n2))