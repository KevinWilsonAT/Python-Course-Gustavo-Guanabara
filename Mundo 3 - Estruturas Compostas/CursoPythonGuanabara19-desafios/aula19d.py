state = dict()
brazil = list()

for count in range(0, 3):
    state['UF'] = str(input('Federative Unit: '))
    state['Symbol'] = str(input('State Symbol: '))
    brazil.append(state.copy()) # <---------------------------- you have to use the command copy() instead of the command [:]

for s in brazil:
    for values in s.values():
        print(values, end=' ')
    print()