def stats(player='<unknown>', num_goals=0):
    print(f'The player {player} made {num_goals} goals in the championship.')

# Main Program
name = str(input("Player's name: "))
goals = str(input("Number of goals: "))

if goals.isnumeric():
    goals = int(goals)

else:
    goals = 0

if name.strip() == '':
    stats(num_goals=goals)

else:
    stats(name, goals)