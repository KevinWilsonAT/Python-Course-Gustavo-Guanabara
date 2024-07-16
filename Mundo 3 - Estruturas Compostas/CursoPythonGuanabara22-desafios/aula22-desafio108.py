# MAIN PROGRAM

import coin_desafio108_module as coin

p = float(input('Insert the price: R$'))
print(f'The half of the value {coin.coin(p)} is: {coin.coin(coin.half(p))}')
print(f'The double of the value {coin.coin(p)} is: {coin.coin(coin.double(p))}')
print(f'Augmenting 10% to the value {coin.coin(p)}, we have: {coin.coin(coin.augm(p, 10))}')
print(f'Reducing 10% of the value {coin.coin(p)}, we have: {coin.coin(coin.red(p, 10))}')