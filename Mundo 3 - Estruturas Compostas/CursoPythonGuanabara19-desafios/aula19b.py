people = {'Name': 'Peter', 'Gender': 'male', 'Age': '22'}
print(f'{people["Name"]} is a {people["Gender"]} person and has {people["Age"]} years old\n')

for keys in people.keys():
    print(keys)
print()

for keys in people.values():
    print(keys)
print()

for keys, values in people.items():
    print(f'{keys}: {values}')