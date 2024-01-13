alt = float(input('Altura da parede em metros: '))
larg = float(input('Largura da parede em metros: '))
area = alt * larg
tinta = area/2

print('Sua parede tem a dimensão de {}x{}, sua area é de {}m² '.format(alt, larg, area))
print('Para pintar a parede, você precisa de {}l de tinta'.format(tinta))
