try:
    print('PROGRAM START')
    a = int(input('Insert the First Number: '))
    b = int(input('Insert the Second Number: '))
    r = a / b

except Exception as errors:
    print(f'This operation cannot go further. There\'s an error. Error: {errors}')

else:
    print(f' The number {a} divided by the number {b} equals to {r}')

finally:
    print('PROGRAM ENDED')
