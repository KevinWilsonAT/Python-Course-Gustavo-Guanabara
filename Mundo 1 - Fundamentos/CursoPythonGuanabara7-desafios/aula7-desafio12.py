pr = float(input('Product price: R$'))
pr_desc = pr - (pr * 5/100)

print('The value of the product is R${:.2f}, with 5% discount it will be: R${:.2f}'.format(pr, pr_desc))