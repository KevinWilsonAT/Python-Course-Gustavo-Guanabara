from time import sleep

c= ('\033[m',             # 0 - no colors
    '\033[0;30;41m',      # 1 - red color
    '\033[0;30;42m',      # 2 - green color
    '\033[0;30;43m',      # 3 - yellow color
    '\033[0;30;44m',      # 4 - blue color
    '\033[0;30;45m',      # 5 - purple color
    '\033[7;30m',         # 6 - white color
    );

 
def custom_help(cmd):
    title(f'Accessing \'{cmd}\' command manual', 4)
    print(c[6], end='')
    help(cmd)
    print(c[0], end='')
    sleep(2)
    print('\n')


def title(msg, color = 0):
    sz = len(msg) + 4
    print(c[color], end='')
    print('-' * sz)
    print(f'  {msg}  ')
    print('-' * sz)
    print(c[0], end='')
    sleep(1)
    print('\n')


# main program
command =''

while True:
    
    title('PyHELP Help System', 2)
    command = str(input("Function or Library > "))
    if command.upper() == 'END':
        break

    else:
        custom_help(command)

    title('PROGRAM ENDED', 1)