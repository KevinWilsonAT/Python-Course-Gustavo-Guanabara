colors = {
    'clean': '\033[m',
    'year': '\033[0;36m'
}

from datetime import date

year = int(input('Which year do you want to analyze? '))

if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or ano % 400 == 0:
    print('The year {}{}{} is a Leap Year'.format(colors['year'], year, colors['clean']))
else:
    print('The year {}{}{} is not a Leap Year'.format(colors['year'], year, colors['clean']))