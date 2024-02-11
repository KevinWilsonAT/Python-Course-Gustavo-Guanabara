sumAge = 0
avgAge = 0
old_manAge = 0
old_manName = ""
under20f = 0

for p in range(1, 5):
    print('{} Person:'.format(p))
    name = str(input('Insert name: ')).strip()
    age = int(input('Insert age: '))
    gender = str(input('Insert gender [M/F]: ')).strip()
    print('-' * 15)

    sumAge += age

    if p == 1 and gender in 'Mm':
        old_manAge = age
        old_manName = name
    if gender in 'Mm' and age > old_manAge:
        old_manAge = age
        old_manName = name
    if gender in 'Ff' and age < 20:
        under20f += 1

avgAge = sumAge / 4

print('The average of the group ages is {}.'.format(avgAge))
print('The oldest man is {} and he has {} years old.'.format(old_manName, old_manAge))
print('In this group, there are {} women below the age of 20 years.'.format(under20f))
