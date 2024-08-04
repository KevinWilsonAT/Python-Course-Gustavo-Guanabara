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
        
def readFloat(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print('\033[0;31mError! Insert a valid FLOAT number.\033[m')
            continue

        except (KeyboardInterrupt):
            print('\033[0;31mData entry aborted by user.\033[m')
            return 0
        
        else:
            return n


n1 = readInt('Insert a integer number:')
n2 = readFloat('Insert a float number:')
print(f'You inserted the integer number {n1} and the float number {n2}')