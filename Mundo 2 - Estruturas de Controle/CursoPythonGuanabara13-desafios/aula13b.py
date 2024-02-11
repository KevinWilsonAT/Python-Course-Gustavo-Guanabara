# this makes a looping based on what number the user inserts

n = int(input('Type a number: '))

for c in range(0, n+1):
    print(c)
print("END")

# this makes a customizable looping, specifying the start number,
# the end number and the iteration number

s = int(input('Insert initial number: '))
f = int(input('Insert final number: '))
i = int(input('Insert iteration number: '))

for c in range(s, f+1, i):
    print(c)
print("END")

# this makes the user insert values multiple times

for c in range(0, 3):
    n = int(input('Insert a value: '))
print("END")

# Summation example

s = 0
for c in range(0, 4):
    n = int(input('Insert a value: '))
    s += n
print("The summation of all values is {}".format(s))
