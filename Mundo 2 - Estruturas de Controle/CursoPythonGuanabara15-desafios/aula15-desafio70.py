prod_number = 1
prod_price = prod_total = more_thousand = cheapest_price = 0
prod_name = cheapest_name = ''

while True:
    print(f'Product {prod_number}: ')
    prod_name = str(input('Insert product name: ')).strip()
    prod_price = float(input('Insert price: '))
    prod_total += prod_price
    print('-' * 15)

    if prod_price > 1000:
        more_thousand += 1
    if prod_number == 1 or prod_price < cheapest_price:
        cheapest_name = prod_name
        cheapest_price = prod_price

    option = ' '
    while option not in 'YN':
        option = str(input('Do you want to continue [Y/N]? ')).strip().upper()[0]
    if option == 'N':
        break

    prod_number += 1
print(f'The total is R${prod_total:.2f}.')
print(f'There is {more_thousand} products above R$1000.00.')
print(f'The cheapest product name is {cheapest_name} and costs R${cheapest_price:.2f}')
