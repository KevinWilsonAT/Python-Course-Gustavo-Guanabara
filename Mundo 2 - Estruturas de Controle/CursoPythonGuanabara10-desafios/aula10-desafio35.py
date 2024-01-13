line1 = float(input('1st line: '))
line2 = float(input('2nd line: '))
line3 = float(input('3rd line: '))

if line1 < line2 + line3 and line2 < line1 + line3 and line3 < line1 + line2:
    print('The Above lines CAN make a triangle')
else:
    print('The Above lines CANNOT make a triangle')