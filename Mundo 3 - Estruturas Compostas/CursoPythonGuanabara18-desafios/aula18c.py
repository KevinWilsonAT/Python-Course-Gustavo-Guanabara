people = list()
datas = list()
tot_over18 = tot_under18 = 0

for counter in range(0, 3):
    datas.append(str(input('Name: ')))
    datas.append(int(input('Age: ')))
    people.append(datas[:])
    datas.clear()
    print('='*30)

for p in people:
    if p[1] >= 18:
        print(f'{p[0]} is over 18 years old')
        tot_over18 += 1
    else:
        print(f'{p[0]} is under 18 years old')
        tot_under18 += 1

print(f'There are {tot_over18} people over 18 years old and {tot_under18} people under 18 years old')