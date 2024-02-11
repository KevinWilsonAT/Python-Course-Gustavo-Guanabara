m = float(input('Insert the value (in meters): '))
km = m/1000
hm = m/100
dam = m/10
dm = int(m*10)
cm = int(m*100)
mm = int(m*1000)

print('{}m is equivalent to {}km, {}hm, {}dam,'.format(m, km, hm, dam))
print('{}dm, {}cm and {}mm'.format(dm, cm, mm))
