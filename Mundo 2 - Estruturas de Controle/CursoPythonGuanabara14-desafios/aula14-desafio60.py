from time import sleep

vl = int(input("Value to calculate: "))
count = vl
fact = 1

print("Calculating {}!".format(vl))
sleep(1)
while count > 0:
    fact = fact * count
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    count -= 1

print("{}".format(fact))
