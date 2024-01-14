from math import hypot
ops = float(input('Opposite side value: '))
ads = float(input('Adjacent side value: '))
h = hypot(ops, ads)
print('The hypotenuse length is: {:.2f}'.format(h) )
