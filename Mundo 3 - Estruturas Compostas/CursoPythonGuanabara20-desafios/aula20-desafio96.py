def area(width, length):
    area = width * length
    print(f'Dimensions: {width}m x {length}m, Area: {area}m\u00b2 ')


print("PROGRAM STARTED.")
print("=" * 50)

print('Land Area Control')
print('-' * 30)
w = float(input('Width (m):'))
l = float(input('Length (m):'))

area(w, l)

print("=" * 50)
print("PROGRAM ENDED.")
