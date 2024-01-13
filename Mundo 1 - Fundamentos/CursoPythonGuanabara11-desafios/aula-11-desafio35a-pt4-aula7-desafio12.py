colors = {
    'clean': '\033[m',
    'pr': '\033[0;33m',
    'pr_desc': '\033[0;34m'
}

pr = float(input('preço do produto: R$'))
pr_desc = pr - (pr * 5/100)

print('O valor do produto de {}R${:.2f}{} com 5% de desconto: {}R${:.2f}{}'
      .format(colors['pr'], pr, colors['clean'], colors['pr_desc'], pr_desc, colors['clean']))
