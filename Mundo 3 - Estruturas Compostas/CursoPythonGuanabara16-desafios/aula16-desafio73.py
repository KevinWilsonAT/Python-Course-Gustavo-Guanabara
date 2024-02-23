football_teams = ('Palmeiras', 'Gremio', 'Atletico from Minas', 'Flamengo', 'Botafogo', 'Red Bull Bragantino',
                  'Fluminense', 'Athletico from Parana', 'Internacional', 'Fortaleza', 'Sao Paulo', 'Cuiaba',
                  'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goias', 'Coritiba', 'America from Minas')

print('\nAll the teams of the Brazilian Cup are:')
print(football_teams)
print('='*70 + '\n')

print('The first five teams of the Brazilian Cup are:')
print(football_teams[0:5])
print('='*70 + '\n')

print('The last four teams are:')
print(football_teams[-4:])
print('='*70 + '\n')

print('Sorting all the teams alphabetically, we have:')
print(sorted(football_teams))
print('='*70 + '\n')

print('In which position Chapecoense is? ')
if 'Chapecoense' not in (football_teams[0:]):
    print('Chapecoense is not on the list')
else:
    print('Chapecoense is in the {} position on the list', football_teams.index('Chapecoense')+1)
print('='*70 + '\n')
