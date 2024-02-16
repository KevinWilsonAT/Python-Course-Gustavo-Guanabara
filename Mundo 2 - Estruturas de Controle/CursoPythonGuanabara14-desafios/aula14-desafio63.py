terms = int(input('How many terms do you want to show? '))
term1 = 0
term2 = 1
print('{}, {}'.format(term1, term2), end='')
count = 3
while count <= terms:
    term3 = term1 + term2
    print(', {}'.format(term3), end='')
    term1 = term2
    term2 = term3
    count += 1
print(', END')