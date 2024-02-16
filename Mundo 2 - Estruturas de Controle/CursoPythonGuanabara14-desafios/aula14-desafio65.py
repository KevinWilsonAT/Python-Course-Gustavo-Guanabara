response = 'Y'
sum = qty = avg = greater = lesser = 0
while response in 'Yy':
    number = int(input('Insert a number: '))
    sum += number
    qty += 1
    if qty == 1:
        greater = lesser = number
    else:
        if number > greater:
            greater = number
        if number < lesser:
            lesser = number
    response = str(input('Do you want to continue? [Y/N] ')).upper().strip()[0]
avg = sum / qty
print('You inserted {} numbers and the average is {}'.format(qty, avg))
print('The greater number is {} and the lesser number is {}'.format(greater, lesser))
print('END')
