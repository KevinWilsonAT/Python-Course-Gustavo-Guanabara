def augm(price, tax, frmt=False):
    res = price + (price * tax/100)
    return res if frmt is False else coin(res)

def red(price, tax, frmt=False):
    res = price - (price * tax/100)
    return res if frmt is False else coin(res)

def double(price, frmt=False):
    res = price * 2
    return res if frmt is False else coin(res)

def half(price, frmt=False):
    res = price / 2
    return res if frmt is False else coin(res)

def coin(price=0, coin='R$'):
    return f'{coin}{price:.2f}'.replace('.',',')

def stats(price=0, taxaugm=10, taxred=10):
    print('-' * 30)
    print('VALUE STATS'.center(30))
    print('-' * 30)

    print('Analyzed price: \t{price}')
    print(f'The double of the price: \t{double(price, True)}')
    print(f'The half of the price: \t{half(price, True)}')
    print(f'Augmenting {taxaugm}% to the price: \t{augm(price, taxaugm, True)}')
    print(f'Reducing {taxred}% of the price: \t{red(price, taxred, True)}')
