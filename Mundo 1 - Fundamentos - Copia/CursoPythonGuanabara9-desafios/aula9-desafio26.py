text = str(input("Insert a text: ")).upper().strip()

print('The letter "A" appears {} times'.format(text.count('A')))
print('The first letter "A" appears in the position {}'.format(text.find("A")+1))
print('The last letter "A" appears in the position {}'.format(text.rfind("A")+1))
