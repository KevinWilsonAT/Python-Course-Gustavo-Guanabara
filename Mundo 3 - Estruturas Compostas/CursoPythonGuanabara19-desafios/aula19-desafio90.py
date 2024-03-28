student = dict()

print("PROGRAM STARTED.")
print("=" * 50)

student["Name"] = str(input('Student Name: '))
student["Average"] = int(input('Student Average Rank: '))

if student["Average"] >= 7:
    student["Situation"] = "Approved"
elif 5 <= student["Average"] < 7:
    student["Situation"] = "Exam"
else:
    student["Situation"] = "Reproved"

print("-" * 50)

for keys, values in student.items():
    print(f'Student {keys}: {values}')

print("=" * 50)
print("PROGRAM ENDED.")
