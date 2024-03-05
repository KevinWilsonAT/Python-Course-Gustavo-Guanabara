test = list()
test.append('Name1')
test.append(44)
test2 = list()
# use [:] to copy the contents of the list
test2.append(test[:])
test[0] = 'Name2'
test[1] = 26
test2.append(test[:])
print(test2)
