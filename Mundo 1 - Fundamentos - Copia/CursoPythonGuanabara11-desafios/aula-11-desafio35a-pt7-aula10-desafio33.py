n1 = int(input('Insert the 1st number: '))
n2 = int(input('Insert the 2nd number: '))
n3 = int(input('Insert the 3rd number: '))

gr = 0
ls = 0

if n1 < n2:
    if n1 < n3:
        ls = n1
else:
    if n1 > n2:
        if n1 > n3:
            gr = n1

if n2 < n1:
    if n2 < n3:
        ls = n2
else:
    if n2 > n1:
        if n2 > n3:
            gr = n2