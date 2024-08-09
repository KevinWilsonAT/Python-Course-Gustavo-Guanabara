from ex115.lib.interface import *
from time import sleep
from os import system

while True:
    header('PROGRAM STARTED')
    response = menu(['Display Users','Register Users','End Program'])
    if response == 1:
        print('option 1 selected')
    elif response == 2:
        print('option 2 selected')
    elif response == 3:
        print('Quitting system...')
        break
    else:
        print('\033[0;31mERROR! Insert a valid option.\033[m')
        sleep(3)
        system('cls')

ending('PROGRAM ENDED')