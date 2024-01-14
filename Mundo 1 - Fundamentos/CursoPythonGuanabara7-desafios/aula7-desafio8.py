m = float(input('digite o valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = int(m*10)
cm = int(m*100)
mm = int(m*1000)

print('o valor {}m equivale a {}km, {}hm, {}dam,'.format(m, km, hm, dam))
print('{}dm, {}cm e {}mm'.format(dm, cm, mm))