colors = {
    'clean': '\033[m',
    'pr': '\033[0;33m',
    'pr_desc': '\033[0;34m'
}

pr = float(input('Product price: R$'))
pr_desc = pr - (pr * 5/100)

print('The product price is {}R${:.2f}{}, with 5% discount it will be: {}R${:.2f}{}'
      .format(colors['pr'], pr, colors['clean'], colors['pr_desc'], pr_desc, colors['clean']))
