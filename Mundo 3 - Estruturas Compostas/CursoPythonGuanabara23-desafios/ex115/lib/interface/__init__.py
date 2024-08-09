def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mError! Insert a valid INTEGER number.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mData entry aborted by user.\033[m')
            return 0
        else:
            return n


def line(sz = 42):
    return '-' * sz


def header(text):
    print(line())
    print(text.center(42))
    print(line())


def menu(list):
    header('MAIN MENU')
    c=1
    for item in list:
        print(f'\033[0;33m{c}\033[m - \033[0;34m{item}\033[m')
        c+=1
    print(line())
    opt = readInt('Your Option: ')


def ending(text):
    print(line())
    print(text.center(42))
    print(line())