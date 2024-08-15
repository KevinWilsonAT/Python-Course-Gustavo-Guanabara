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
        print(f'\033[0;33mThe file {name} was created successfully\033[m')
        sleep(3)

def displayFile(name):
    try:
        a = open(name, 'rt')
    except:
        print('\033[0;31mERROR! There\'s an error in file reading.\033[m')
        sleep(3)
    else:
        system('cls')
        print(f'Loading data...')
        sleep(3)
        system('cls')
        header('REGISTERED USERS')
        for line in a:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} years old')

        sleep(3)
        system('cls')
    finally:
        a.close()


def registerUser(file, name='unknown', age=0):
    try:
        a = open(file, 'at')
    except:
        print('\033[0;31mERROR! There\'s an error in file opening.\033[m')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('\033[0;31mERROR! There\'s an error in data registration.\033[m')
            sleep(3)
        else:
            system('cls')
            print(f'Writing data...')
            sleep(3)
            print(f'\033[0;33mThe user {name} data was added successfully\033[m')
            sleep(3)
            system('cls')
            a.close()