from datetime import date
year = date.today().year

born_year = int(input('In which year you were born? '))
age = year - born_year

if age <= 9:
    print('You have {} years old. You belong to the Beginner Swimming Class'.format(age))
elif age > 9 and age <= 14:
    print('You have {} years old. You belong to the Child Swimming Class'.format(age))
elif age > 14 and age <= 19:
    print('You have {} years old. You belong to the Junior Swimming Class'.format(age))
elif age == 20:
    print('You have {} years old. You belong to the Senior Swimming Class'.format(age))
elif age > 20:
    print('You have {} years old. You belong to the Master Swimming Class'.format(age))