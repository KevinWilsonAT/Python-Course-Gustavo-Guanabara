above18 = man = under20f = 0
p = 1
option = 'Y'

while True:
    print(f'Person {p}:')
    age = int(input('Insert age: '))
    gender = str(input('Insert gender [M/F]: ')).strip()
    print('-' * 15)
    if age >= 18:
        above18 += 1
    if gender in 'Mm':
        man += 1
    if gender in 'Ff' and age < 20:
        under20f += 1
    option = str(input('Do you want to continue [Y/N]? '))
    if option not in 'Yy':
        break
    p+= 1

print(f'The group has a total of {p} people, which:')
print(f'{above18} people is above 18 years,')
print(f'{man} is a male')
print(f'and {under20f} are female below 20 years.')
