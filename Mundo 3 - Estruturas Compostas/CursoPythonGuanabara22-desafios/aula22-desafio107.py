# MAIN PROGRAM

import coin_desafio107_module as coin

p = float(input('Insert the price: R$'))
print(f'The half of the value {p} is: {coin.half(p)}')
print(f'The double of the value {p} is: {coin.double(p)}')
print(f'Augmenting 10% to the value {p}, we have: {coin.augm(p, 10)}')
print(f'Reducing 10% of the value {p}, we have: {coin.red(p, 10)}')