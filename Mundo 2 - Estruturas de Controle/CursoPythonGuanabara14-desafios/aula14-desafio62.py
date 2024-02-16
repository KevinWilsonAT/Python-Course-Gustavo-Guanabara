first = int(input('Insert the 1st term of an A.P.: '))
ratio = int(input('Insert the ratio of the A.P.: '))
term = first
count = 1
total = 0
m_terms = 10
while m_terms != 0:
    total += m_terms
    while count <= total:
        print('{}'.format(term), end=", ")
        term += ratio
        count += 1
    print("PAUSE")
    m_terms = int(input('How many more terms do you want to show? '))
print("A.P. ended showing {} terms.".format(total))
print("END")
