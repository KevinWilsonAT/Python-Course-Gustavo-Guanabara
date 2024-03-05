temporary = []
main_list = []
greater = lesser = 0

print("PROGRAM STARTED.")
print("="*50)

while True:
    temporary.append(str(input("Name: ")))
    temporary.append(float(input("Weight: ")))

    if len(main_list) == 0:
        greater = lesser = temporary[1]
    else:
        if temporary[1] > greater:
            greater = temporary[1]
        if temporary[1] < lesser:
            lesser = temporary[1]
    main_list.append(temporary[:])
    temporary.clear()

    print("-" * 50)
    option = str(input("Continue? [Y/N] ")).upper().strip()[0]
    if option in 'N':
        break

print("="*50)
print(f'The inserted data was {main_list}')
print(f'You registered a total of {len(main_list)} people')
print(f'The heaviest person weighs {greater}Kg. The person is ', end='')
for p in main_list:
    if p[1] == greater:
        print(f'{p[0]}', end='')
print()
print(f'The lightest person weighs {lesser}Kg. The person is ', end='')
for p in main_list:
    if p[1] == lesser:
        print(f'{p[0]}', end='')
print()
print("PROGRAM ENDED.")
