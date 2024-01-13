rs = float(input('How much do you have (in Reals)? R$'))
dol = rs / 4.88
eu = rs / 5.24
ien = rs /0.039

print('You have R${:.2f}, that is equivalent to US$ {:.2f}'.format(rs, dol))
print('You have R${:.2f}, that is equivalent to {:.2f} €'.format(rs, eu))
print('You have R${:.2f}, that is equivalent to ¥ {:.2f}'.format(rs, ien))