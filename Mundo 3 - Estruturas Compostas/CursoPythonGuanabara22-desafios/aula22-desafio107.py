# - criar modulo chamado coin.py
#       - coloque funcoes incorporadas augm(), red(), double(), half()
#       - fazer um programa que importe esse modulo e use algumas dessas funcoes

# MAIN PROGRAM

from desafio107_module import coin

p = float(input('Insert the price: R$'))

print(f'The half of the value {p} is: {coin.half(p)}')
print(f'The double of the value {p} is: {coin.double(p)}')
print(f'Augmenting 10% to the value {p}, we have: {coin.augm(p)}')
print(f'Reducing 13% of the value {p}, we have: {coin.red(p)}')