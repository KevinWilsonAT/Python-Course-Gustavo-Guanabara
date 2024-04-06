
print("PROGRAM STARTED.")
print("=" * 50)

people = list()
person = dict()
sum_values = avg = 0


while True:
    person.clear()
    person['name'] = str(input('Name: '))
    while True:
        person['gender'] = str(input('Gender [M/F]:')).upper()[0]
        if person['gender'] in 'MF':
            break
        print('ERROR! Please Specify M or F on Gender.')
    person['age'] = int(input('Age: '))
    sum_values += person['age']
    people.append(person.copy())

    while True:
        option = str(input('Do you want to continue [Y/N]? ')).upper()[0]
        if option in 'YN':
            break
        print('ERROR! Please Specify Y or N.')
    if option =='N':
        break

print('--' * 30)
print('Statistics:')
print('--' * 30)
print(f'A) In total, there are {len(people)} people registered')
avg = sum_values / len(people)
print(f'B) The Average age is {avg:5.2f} years.')
print(f'C) The female registered people are ', end='')
for p in people:
    if p['gender'] in 'Ff':
        print(f'{p["name"]} ', end='')
    elif p['gender'] in 'Mm':
        print('none', end='')
print()

print(f'D) List of people above the average: ', end='')
for p in people:
    if p['age'] >= avg:
        print('   ')
        for keys, values in p.items():
            print(f'{keys} = {values}; ', end='')
        print()

print("=" * 50)
print("PROGRAM ENDED.")