# <iteration_number> = initial value
# syntax: while <iteration_number> [relational_operator (< > <= >= == ===)] <final_value>:
# ...
# <iteration_number> += [1 or some variable])

# with limitations:
from builtins import input

c = 1
while c < 10:
    print(c, end=" ")
    c += 1
print("END")

# without limitations (using numbers, stops when is inserted 0):

n = 1
while n != 0:
    n = int(input("Insert a Value: "))
print("END")

# without limitations (using strings, stops when is inserted N or n):

r = 'S'
while r == "S":
    n = int(input("Insert a Value: "))
    r = str(input("Want to continue? [S/N] ")).upper()
print("END")