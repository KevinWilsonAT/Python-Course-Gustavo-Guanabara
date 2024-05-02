from time import sleep

print("PROGRAM STARTED.")
print("=" * 50)

def greater(* num):
    count = great = 0
    
    print("\nAnalyzing registered values... ")
    for value in num:
        print(f'{value} ', end='', flush=True)
        sleep(0.3)

        if count == 0:
            great = value

        else:
            if value > great:
                great = value
        count += 1
    print()
    print('--' * 25)
    print(f'There are a total of {count} values')
    print(f'The greater value registered is: {great}')


greater(1,2,4,7,0,8)

print("=" * 50)
print("PROGRAM ENDED.")
