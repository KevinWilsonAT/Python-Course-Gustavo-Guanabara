matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sumColThree = grLineTwo = sumEven = 0

print("PROGRAM STARTED.")
print("=" * 50)

for lines in range (0,3):
    for columns in range(0, 3):
        matrix[lines][columns] = int(input(f'Insert a Value on matrix position [{lines}, {columns}]: '))

for lines in range (0,3):

    sumColThree += matrix[lines][2]

    for columns in range(0,3):
        if matrix[lines][columns] % 2 == 0:
            sumEven += matrix[lines][columns]

        if matrix[lines][columns] == 0:
            grLineTwo = matrix[1][columns]
        elif matrix[1][columns] >= grLineTwo:
            grLineTwo = matrix[1][columns]

        print(f'[{matrix[lines][columns]:^5}]', end=' ')
    print()
print("-" * 50)
print(f'The sum of all even values in the matrix is: {sumEven}')
print(f'The sum of all values at the 3rd column of the matrix is: {sumColThree}')
print(f'The greater value at the 2nd line of the matrix is: {grLineTwo}')

print("=" * 50)
print("PROGRAM ENDED.")
