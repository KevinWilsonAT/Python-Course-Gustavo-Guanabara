pr = float(input('preço do produto: R$'))
pr_desc = pr - (pr * 5/100)

print('O valor do produto de R${:.2f} com 5% de desconto: R${:.2f}'.format(pr, pr_desc))