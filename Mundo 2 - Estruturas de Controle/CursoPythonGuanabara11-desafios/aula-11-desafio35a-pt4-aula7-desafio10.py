colors = {
    'clean': '\033[m',
    'real': '\033[0;33m',
    'dollar': '\033[0;32m',
    'euro': '\033[0;34m',
    'yen': '\033[0;31m'
}

rs = float(input('How much do you have (in Reals)? R$'))
dol = rs / 4.88
eu = rs / 5.24
yen = rs /0.039

print('You have {}R${:.2f}{}, that is equivalent to {}US$ {:.2f}{}'
      .format(colors['real'], rs, colors['clean'], colors['dollar'], dol, colors['clean']))
print('You have {}R${:.2f}{}, that is equivalent to {}{:.2f} €{}'
      .format(colors['real'], rs, colors['clean'], colors['euro'], eu, colors['clean']))
print('You have {}R${:.2f}{}, that is equivalent to {}¥ {:.2f}{}'
      .format(colors['real'], rs, colors['clean'], colors['yen'], yen, colors['clean']))