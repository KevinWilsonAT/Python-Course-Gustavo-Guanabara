from datetime import date

today_year = date.today().year
adults = 0
n_adults = 0

for p in range(1, 8):
    born_year = int(input('Insert birth year of the person {}: '.format(p)))
    s = today_year - born_year

    if s >= 21:
        adults += 1
    else:
        n_adults += 1

print('Adults: {}'.format(adults))
print('Not adults: {}'.format(n_adults))
