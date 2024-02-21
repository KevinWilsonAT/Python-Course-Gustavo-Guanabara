prod_name = cheapest_name = ''
option = 'Y'
prod_number = 1
prod_price = prod_total = morethousand = cheapest_price = 0

while True:
    print(f'Product {prod_number}:')
    prod_name = str(input('Insert product name: ')).strip()
    prod_price = float(input('Insert price: '))
    prod_total += prod_price
    print('-' * 15)

    if prod_number == 1:
        cheapest_name = prod_name
        cheapest_price = prod_price
    if prod_price < cheapest_price:
        cheapest_name = prod_name
        cheapest_price = prod_price
    if prod_price > 1000:
        morethousand += 1

    option = str(input('Do you want to continue [Y/N]? '))
    if option not in 'Yy':
        break
    prod_number += 1

print(f'The total is R${prod_total}.')
print(f'There is {morethousand} products above R$1000,00.')
print(f'The cheapest product name is {cheapest_name} and costs R$ {cheapest_price}')
