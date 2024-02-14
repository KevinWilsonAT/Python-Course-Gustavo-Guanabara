gender = str(input("Insert the Gender: ").strip().upper())[0 ]

while gender not in 'MmFf':
    print("Incorrect value inserted. Please insert the gender correctly.")
    gender = str(input("Insert the Gender: ").strip().upper()[0])

print('Gender {} registered successfully'.format(gender))
print('END')
