colors = {
    'clean': '\033[m',
    'km': '\033[0;31m',
    'hm': '\033[0;32m',
    'dam': '\033[0;33m',
    'm': '\033[0;34m',
    'dm': '\033[0;35m',
    'cm': '\033[0;36m',
    'mm': '\033[0;37m',
}

m = float(input('Digite o valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = int(m*10)
cm = int(m*100)
mm = int(m*1000)

print('o valor de {}{}m{} equivale a {}{}km{}, {}{}hm{}, {}{}dam{},'
      .format(colors['m'], m, colors['clean'], colors['km'], km, colors['clean'], colors['hm'], hm, colors['clean'],
              colors['dam'], dam, colors['clean']))
print('{}{}dm{}, {}{}cm{} e {}{}mm{}'
      .format(colors['dm'], dm, colors['clean'], colors['cm'], cm, colors['clean'], colors['mm'], mm, colors['clean']))