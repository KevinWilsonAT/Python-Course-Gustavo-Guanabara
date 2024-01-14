prod_price = float(input('Product price: R$'))
pay_option = int(input('''Payment option
1 = money / check
2 = credit card
'''))

if pay_option == 1:
    print('You will pay the product with 10% discount. The price will be R${:.2f}.'.format((prod_price * 0.9)))
elif pay_option == 2:
    installments = float(input('In how many installments do you want to pay? '))

    if installments <= 2:
        print('The price of your product will be in {:.0f} installments of R${:.2f}.'
              .format(installments, (prod_price / installments)))
    elif installments >= 3:
        total = prod_price + (prod_price * 0.2)
        print('The product price will cost R${:.2f} and will be in {:.0f} installments of R${:.2f}, with a fee of 20%.'
              .format(total, installments, ((prod_price / installments) * 1.2)))
else:
    print('Invalid Command!')