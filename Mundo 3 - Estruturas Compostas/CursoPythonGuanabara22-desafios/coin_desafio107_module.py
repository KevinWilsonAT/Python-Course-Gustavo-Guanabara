def augm(price, tax):
    res = price + (price * tax/100)
    return res

def red(price, tax):
    res = price - (price * tax/100)
    return res

def double(price):
    res = price * 2
    return res

def half(price):
    res = price / 2
    return res