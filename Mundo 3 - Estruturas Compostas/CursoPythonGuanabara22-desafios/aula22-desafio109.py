# MAIN PROGRAM

import coin_desafio109_module as coin

p = float(input('Insert the price: R$'))
print(f'The half of the value {coin.coin(p)} is: {coin.half(p, True)}')
print(f'The double of the value {coin.coin(p)} is: {coin.double(p, True)}')
print(f'Augmenting 10% to the value {coin.coin(p)}, we have: {coin.augm(p, 10, True)}')
print(f'Reducing 10% of the value {coin.coin(p)}, we have: {coin.red(p, 10, True)}')