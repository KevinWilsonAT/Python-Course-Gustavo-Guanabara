from ex115.lib.interface import *
from ex115.lib.file import *
from time import sleep
import sys as s


file = 'file.txt'

if fileExists(file):
    system('cls')
    print('Reading File...')
    sleep(3)
    print(f'\033[0;33mWarning: File found\033[m')
    print('Reading Data...')
    sleep(3)
    system('cls')
else:
    print('Reading File...')
    sleep(3)
    print('\033[0;31mERROR! File not found.\033[m')
    sleep(1)
    createFile(file)
    sleep(3)
    system('cls')

while True:
    header('PROGRAM STARTED')
    response = menu(['Display Users','Register Users','End Program'])
    match response:
        case 1:
            displayFile(file)
        case 2:
            system('cls')
            header('NEW USER REGISTER')
            name = str(input('Name: '))
            age = readInt('Age: ')
            registerUser(file, name, age)
        case 3:
            print('Quitting system...')
            break
        case _:
            print('\033[0;31mERROR! Insert a valid option.\033[m')
            sleep(3)
            system('cls')
            

ending('PROGRAM ENDED')
sleep(2)
s.exit(0)