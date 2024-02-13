vl = int(input("Value to calculate: "))
count = vl
fact = 1

print("Calculating factorial of {}".format(vl))

if (vl != 0) or (vl > 1):
    while count >= 1:
        fact = fact * count
        count -= 1

print("{}! = {}".format(vl, fact))
