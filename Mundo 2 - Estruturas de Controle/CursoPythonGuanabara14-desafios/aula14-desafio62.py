ft = int(input('Insert the 1st term of an A.P.: '))
r = int(input('Insert the ratio of the A.P.: '))
tt = ft + (10 - 1) * r
c = 1
op = 1


while c < (tt + r):
    print('{}'.format(c), end=", ")
    c += r



print("END")
