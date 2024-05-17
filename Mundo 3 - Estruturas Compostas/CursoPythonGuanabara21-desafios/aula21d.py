def even(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Insert a number: '))

if even(num):
    print("It's even")
else:
    print("It's odd")