from time import sleep

n1 = int(input('1st value: '))
n2 = int(input('2nd value: '))
op = 0

while op != 5:

    print('''    [ 1 ] Addition
    [ 2 ] Multiplication')
    [ 3 ] Greater and Lesser')
    [ 4 ] Insert new Values')
    [ 5 ] Quit Program''')
    op = int(input('>>>>> Option: '))

    if op == 1:
        r = n1 + n2
        print('{} + {} = {}'.format(n1, n2, r))
    elif op == 2:
        r = n1 * n2
        print('{} x {} = {}'.format(n1, n2, r))
    elif op == 3:
        if n1 > n2:
            gr = n1
            print('Between {} and {} the greater value is {}'.format(n1, n2, gr))
        elif n1 < n2:
            gr = n2
            print('Between {} and {} the greater value is {}'.format(n1, n2, gr))
        else:
            print('Both values are equal')
    elif op == 4:
            print('Insert the values again.')
            n1 = int(input('1st value: '))
            n2 = int(input('2nd value: '))
    else:
        print('Invalid Command. Try Again.')
    print('=-=' * 10)

print('Quiting Program...')
sleep(1)
print('END')
