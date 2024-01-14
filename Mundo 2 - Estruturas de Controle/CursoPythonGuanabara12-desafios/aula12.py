name = str(input('What is your name? '))
if name == 'Kevin':
    print('What a beautiful name!')
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('Your name is quite popular on Brazil.')
elif name in 'Ana Cláudia Jéssica Juliana':
    print('Such a beautiful feminine name!')
else:
    print('Your name is kinda common')
print('Have a good day, {}!'.format(name))
