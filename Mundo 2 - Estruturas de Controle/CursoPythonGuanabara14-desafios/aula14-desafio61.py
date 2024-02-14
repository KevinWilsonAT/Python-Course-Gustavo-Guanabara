ft = int(input('Insert the 1st term of an A.P.: '))
r = int(input('Insert the ratio of the A.P.: '))
tr = ft
c = 1
while c <= 10 :
    print('{}'.format(tr), end=", ")
    tr += r
    c += 1
print("END")
