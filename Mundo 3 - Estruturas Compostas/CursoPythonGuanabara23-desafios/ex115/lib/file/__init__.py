from ex115.lib.interface import *
from time import sleep
from os import system

def fileExists(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(name):
    try:
        a = open(name, 'wt+')
        a.close()
        print('Creating File...')
        sleep(3)
    except:
        print('\033[0;31mERROR! There\'s an error in file creation.\033[m')
        sleep(3)
    else:
        print(f'\033The file {name} was created successfully\033[m')
        sleep(3)

def displayFile(name):
    try:
        a = open(name, 'rt')
        print('Reading File...')
        sleep(3)
    except:
        print('\033[0;31mERROR! There\'s an error in file reading.\033[m')
        sleep(3)
    else:
        print(f'Reading data...')
        sleep(3)
        system('cls')
        header('REGISTERED USERS')
        print(a.readlines())
        sleep(3)
        system('cls')
