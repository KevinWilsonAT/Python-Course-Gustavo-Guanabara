number = sum = count = 0
number = int(input("Insert a value: "))
while number != 999:
    sum += number
    count += 1
    number = int(input("Insert a value: "))
print("You inserted {} number(s) and the addition of them is {}".format(count, sum))
