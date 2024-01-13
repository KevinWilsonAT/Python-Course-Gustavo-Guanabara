colors = {
    'clean': '\033[m',
    'pay': '\033[0;33m',
}

d = int(input('Rental days: '))
km = float(input('Km traveled: '))
pay = (d * 60) + (km * 0.15)
print('Total payable: {}R${:.2f}{}'.format(colors['pay'], pay, colors['clean']))