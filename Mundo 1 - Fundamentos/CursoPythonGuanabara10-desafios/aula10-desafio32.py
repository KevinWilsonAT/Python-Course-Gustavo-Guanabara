from datetime import date

year = int(input('Which year do you want to analyze? '))

if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or ano % 400 == 0:
    print('The year {} is a Leap Year'.format(year))
else:
    print('The year {} is not a Leap Year'.format(year))