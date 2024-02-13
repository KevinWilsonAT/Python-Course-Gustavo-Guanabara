n = sum = c = 0

n = int(input("Insert a value: "))

while n != 999:
    n = int(input("Insert a value: "))
    if n != 999:
        sum += n
        c += 1

print("You inserted {} number(s) and the addition of them is {}".format(c, sum))