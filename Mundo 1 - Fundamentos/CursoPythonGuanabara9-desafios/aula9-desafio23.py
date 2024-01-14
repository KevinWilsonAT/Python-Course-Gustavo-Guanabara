n = int(input("Insert a number between 0 and 9999: "))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analyzing the number {}'.format(n))

print('Units: {}'.format(u))
print('Dozens: {}'.format(d))
print('Hundreds: {}'.format(c))
print('Thousands: {}'.format(m))
