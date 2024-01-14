from math import trunc

num = float(input('Insert a number: '))
intp = trunc(num)

print('The number {} has the integer part {}'.format(num, intp))