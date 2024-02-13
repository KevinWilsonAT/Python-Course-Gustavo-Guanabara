# without limitations (using numbers, stops when is inserted 0 and counts odd and even numbers):

n = 1
odd = even = 0

while n != 0:
    n = int(input("Insert a value: "))
    if n != 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

print("You inserted {} even number(s) and {} odd number(s)".format(even, odd))
