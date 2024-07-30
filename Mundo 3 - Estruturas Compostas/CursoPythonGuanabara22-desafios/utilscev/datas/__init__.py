def readMoney(msg):
    valid = False
    while not valid:
        enter = str(input(msg)).replace(',','.').strip()
        if enter.isalpha() or enter.strip() == '':
            print(f'\033[0;31mERROR: \"{enter}\" is an invalid price.\033[m')
        else:
            valid = True
            return float(enter)