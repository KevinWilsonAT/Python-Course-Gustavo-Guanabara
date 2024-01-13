from math import sin, cos, tan, radians
ang = float(input("Angle's value: "))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print('The angle of {}° has sine of: {:.2f}'.format(ang, s))
print('The angle of {}° has cosine of: {:.2f}'.format(ang, c))
print('The angle of {}° has tangent of: {:.2f}'.format(ang, t))