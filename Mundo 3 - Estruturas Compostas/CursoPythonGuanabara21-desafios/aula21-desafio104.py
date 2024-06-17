def readInt(msg):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True

        else:
            print('\033[0;31mError! Insert a valid INTEGER number.\033[m')
        
        if ok:
            break

    return value


n = readInt('Insert a number:')
print(f'You inserted the number {n}')