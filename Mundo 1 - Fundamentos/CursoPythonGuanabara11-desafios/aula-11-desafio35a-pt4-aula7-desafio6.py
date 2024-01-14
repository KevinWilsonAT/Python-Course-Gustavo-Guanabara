colors = {
    'clean': '\033[m',
    'n': '\033[0;31m',
    '2x': '\033[0;32m',
    '3x': '\033[0;33m',
    'sqrt': '\033[0;34m'
}

n = int(input('Insert an integer number: '))
doub = n*2
tri = n*3
sroot = pow(n, (1/2))

print('The integer number is {}{}{}, its double is {}{}{}, its triple is {}{}{} and your square root is {}{:.2f}{}'
      .format(colors['n'], n, colors['clean'], colors['2x'], doub, colors['clean'], colors['3x'], tri, colors['clean'],
              colors['sqrt'], sroot, colors['clean']))