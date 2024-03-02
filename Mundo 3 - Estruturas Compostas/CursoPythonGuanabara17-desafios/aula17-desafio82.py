list_numbers = list()
list_odd = list()
list_even = list()

print("PROGRAM STARTED")
print("="*50)
while True:
    list_numbers.append(int(input('Insert a number: ')))
    option = str(input('Continue? [Y/N] ')).upper().strip()[0]
    if option in 'N':
        break

for count, value in enumerate(list_numbers):
    if value % 2 == 0:
        list_even.append(value)
    elif value % 2 != 0:
        list_odd.append(value)
print("="*50)
print(f"All numbers inserted: {sorted(list_numbers)}\n")
print(f"All even numbers: {sorted(list_even)}")
print(f"All odd numbers: {sorted(list_odd)}")
print("="*50)
print("PROGRAM ENDED.")
