team = list()
player = dict()
matches = list()

print("PROGRAM STARTED.")
print("=" * 50)

while True:
    player["Name"] = str(input("Player Name: "))
    t_matches = int(input(f'How many matches did {player["Name"]} play?'))

    for count in range(1, t_matches+1):
        matches.append(int(input(f'How many goals in the match #{count}? ')))

    player["Goals"] = matches[:]
    player["Total"] = sum(matches)
    team.append(player.copy())

    while True:
        option = str(input('Do you want to continue [Y/N]? ')).upper()[0]
        if option in 'YN':
            break
        print('ERROR! Please Specify Y or N.')
    if option == 'N':
        break
print('=' * 30)

print('cod ', end='')
for index in player.keys():
    print(f'{index:<15}', end='')
print()
print('-' * 40)

for keys, values in enumerate(team):
    print(f'{keys:>3} ', end='')
    for d in values.values():
        print(f'{str(d):<15}', end='')
        print()
print('-' * 40)

while True:
    search = int(input('Show data statistics of which player? (999 to stop the program)'))
    if search == 999:
        break
    if search >= len(team):
        print(f'ERROR! The player with the code {search} does not exist in the system.')
    else:
        print(f' -- STATISTICS OF THE PLAYER {team[search]['Name']}:')

        for i, g in enumerate(team[search]["Goals"]):
            print(f'   In match #{i+1} made {g} goals.')
    print("=" * 50)
print("PROGRAM ENDED.")
