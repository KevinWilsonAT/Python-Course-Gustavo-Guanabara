height = float(input("Wall's height (in meters): "))
width = float(input("Wall's width (in meters): "))
area = height * width
ink = area/2

print('Your wall has {}x{} in dimension and its area is {}m²'.format(height, width, area))
print('To paint the wall you will need {}l of ink'.format(ink))
