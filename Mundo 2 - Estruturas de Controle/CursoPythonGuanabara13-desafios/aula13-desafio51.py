ft = int(input('Insert the 1st term of an A.P.: '))
r = int(input('Insert the ratio of the A.P.: '))
tt = ft + (10 - 1) * r

for c in range(ft, tt + r, r):
    print('{}'.format(c), end=", ")
print("END")
