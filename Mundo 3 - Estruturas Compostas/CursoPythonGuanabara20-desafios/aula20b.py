def counter(* num):

    for value in num:
        print(f'{value} ', end='')
    print('END')
    print()

    size = len(num)
    print(f'Input Values: {num} and Quantity: {size}')


counter(2, 1, 7)
counter(8, 0)
counter(4, 4, 7, 6, 2)