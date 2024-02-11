# Traditional Method
time = int(input('How old is your car? '))

if time <= 3:
    print('New Car')
else:
    print('Old Car')
print('--END--')

# Simplified Method

time = int(input('How old is your car? '))

print('New Car' if time <= 3 else 'Old Car')
print('--END--')
