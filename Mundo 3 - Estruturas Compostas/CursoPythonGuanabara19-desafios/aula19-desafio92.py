from datetime import datetime

print("PROGRAM STARTED.")
print("=" * 50)

person_data = dict()

person_data["Name"] = str(input("Name: "))
birth_year = int(input("Birth year: "))
person_data["Age"] = datetime.now().year - birth_year
person_data["CTPS"] = int(input("Work Wallet (If you don't have, press 0): "))

if person_data["CTPS"] != 0:
    person_data["Hire"] = int(input("Hire Year: "))
    person_data["Salary"] = float(input("Salary (R$): "))
    person_data["Retirement"] = person_data["Age"] + ((person_data["Hire"] + 35) - datetime.now().year)

print('==' * 30)

for keys, values in person_data.items():
    print(f'{keys}: {values}')

print("=" * 50)
print("PROGRAM ENDED.")
