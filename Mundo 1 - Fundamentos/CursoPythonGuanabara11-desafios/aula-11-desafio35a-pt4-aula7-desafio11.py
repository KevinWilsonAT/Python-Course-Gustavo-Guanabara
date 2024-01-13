colors = {
    'clean': '\033[m',
    'alt': '\033[0;31m',
    'larg': '\033[0;32m',
    'area': '\033[0;33m',
    'tinta': '\033[0;34m'
}

alt = float(input('Altura da parede em metros: '))
larg = float(input('Largura da parede em metros: '))
area = alt * larg
tinta = area/2

print('Sua parede tem a dimensão de {}{}{} x {}{}{}, sua area é de {}{}{}m² '
      .format(colors['alt'], alt, colors['clean'], colors['larg'], larg, colors['clean'],
              colors['area'], area, colors['clean']))

print('Para pintar a parede, você precisa de {}{}{}l de tinta'.format(colors['tinta'], tinta, colors['clean']))
