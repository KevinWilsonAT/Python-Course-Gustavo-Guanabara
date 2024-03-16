opt = 'Y'
listStudents = list()

print("PROGRAM STARTED.")
print("="*50)

while True:
    nameStudent = str(input('Student Name: '))
    r1 = float(input('1st Rank: '))
    r2 = float(input('2nd Rank: '))
    avg = (r1 + r2) / 2
    listStudents.append([nameStudent, [r1, r2], avg])


    # cadastrar tudo em uma lista composta
    # mostrar o boletim com a media de cada um dos alunos
    # permitir que o usuário possa mostrar as notas inidividuais de cada aluno, usando o numero 999

    opt = str(input('Do you want to continue [Y/N]: ')).upper().strip()[0]
    if opt not in 'Yy':
        break
    print(':' * 50)

print('-' * 50)

print(f'{"#":<4}{"Name":<10}{"Average Rank":>8}')
print('-' * 50)
for studentNumber, studentData in enumerate(listStudents):
    print(f'{studentNumber:<4}{studentData[0]:<10}{studentData[2]:>8.1f}')

while True:
    print('-' * 50)
    opt = int(input('Show rank of which student? [999 to exit]: '))
    if opt == 999:
        print('Closing...')
        break
    if opt <= len(listStudents) - 1:
        print(f'Ranks of the Student {listStudents[opt][0]} are: {listStudents[opt][1]}')

print("="*50)
print("PROGRAM ENDED.")
