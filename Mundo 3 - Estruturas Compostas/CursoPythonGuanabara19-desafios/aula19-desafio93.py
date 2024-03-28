player = dict()
matches = list()

print("PROGRAM STARTED.")
print("=" * 50)

player["Name"] = str(input("Player Name: "))
t_matches = int(input(f'How many matches did {player["Name"]} play?'))

for count in range(1, t_matches+1):
    matches.append(int(input(f'How many goals in the match #{count}? ')))

player["Goals"] = matches[:]
player["Total"] = sum(matches)

print('=' * 30)
print(f'The Player {player["Name"]} played {len(player["Goals"])} matches')
print('=' * 30)
for m_number, values in enumerate (player["Goals"]):
    print(f'Match #{m_number+1}: {values} goals')

print(f'\nIn total, {player["Name"]} made {player["Total"]} goals')

print("=" * 50)
print("PROGRAM ENDED.")
