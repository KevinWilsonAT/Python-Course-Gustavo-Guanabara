colors = {
    'clean': '\033[m',
    'green text': '\033[1;32m',
    'yellow text': '\033[1;33m',
    'red text': '\033[1;31m'}

day = input("Day = ")
month = input("Month = ")
year = input("Year = ")

print('You born in the day {}{}{}, month {}{}{} and year {}{}{}. Is it correct?'
      .format(colors['green text'], day, colors['clean'],
              colors['yellow text'], month, colors['clean'],
              colors['red text'], year, colors['clean']))
