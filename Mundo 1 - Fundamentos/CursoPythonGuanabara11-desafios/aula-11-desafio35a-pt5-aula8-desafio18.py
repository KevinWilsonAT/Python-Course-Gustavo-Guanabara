colors = {
    'clean': '\033[m',
    'ang': '\033[0;31m',
    'sin': '\033[0;32m',
    'cos': '\033[0;33m',
    'tan': '\033[0;34m'
}

from math import sin, cos, tan, radians
ang = float(input("Angle's value: "))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print('The angle of {}{}{}° has sine of: {}{:.2f}{}'
      .format(colors['ang'], ang, colors['clean'], colors['sin'], s, colors['clean']))
print('The angle of {}{}{}° has cosine of: {}{:.2f}{}'
      .format(colors['ang'], ang, colors['clean'], colors['cos'], c, colors['clean']))
print('The angle of {}{}{}° has tangent of: {}{:.2f}{}'
      .format(colors['ang'], ang, colors['clean'], colors['tan'], t, colors['clean']))