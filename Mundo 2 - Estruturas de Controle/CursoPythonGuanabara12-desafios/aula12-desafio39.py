from datetime import date
year = date.today().year

sex = str.lower(input('Are you Male or Female? '))

if sex == 'female':
    print("You doesn't need to enlist to the army")
elif sex == 'male':
    born_year = int(input('In which year you were born? '))
    age = year - born_year

    if age < 18:
        y = 18 - age
        print('You are yet to enlist to the army. ({} years from now to enlist)'.format(y))
    elif age == 18:
        print('You are ready to enlist to the army')
    elif age > 18:
        y = age - 18
        print('You already past the age to enlist to the army. ({} years ago)'.format(y))
else:
    print('Invalid Command')
