colors = {
    'clean': '\033[m',
    'sal': '\033[0;32m',
    'perc': '\033[0;31m',
    'sal_augm': '\033[0;36m'
}

sal = float(input("Employee's salary: R$"))
sal_augm = 0
perc = 0

if sal <= 1250:
    sal_augm = sal + (sal * 15/100)
else:
    sal_augm = sal + (sal * 10 / 100)

print("The employee's salary was {}R${:.2f}{}; with a {}{}{}% increase: {}R${:.2f}{}"
      .format(colors['sal'], sal, colors['clean'], colors['perc'], perc, colors['clean'],
              colors['sal_augm'], sal_augm, colors['clean']))