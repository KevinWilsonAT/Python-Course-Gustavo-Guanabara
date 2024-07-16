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

