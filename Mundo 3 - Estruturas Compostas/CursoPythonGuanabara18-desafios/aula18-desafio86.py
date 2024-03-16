matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print("PROGRAM STARTED.")
print("=" * 50)

for lines in range (0, 3):
    for columns in range (0, 3):
        matrix[lines][columns] = int(input(f'Insert a value for matrix position [{lines},{columns}]: '))

for lines in range (0, 3):
    for columns in range (0, 3):
        print(f'[{matrix[lines][columns]:^5}]', end=' ')
    print()
print("=" * 50)
print("PROGRAM ENDED.")
