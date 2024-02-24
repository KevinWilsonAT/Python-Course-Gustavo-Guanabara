words = ('learn', 'program', 'language', 'Python', 'Course', 'free',
         'study', 'practice', 'work', 'market', 'programmer', 'future')
for number in words:
    n_letter = 0
    print(f'\nWord: {number.upper(): <15} Vowels within: ', end='')
    for letter in number:
        if letter.lower() in 'aeiou':
            print(f'{letter}', end=' ')
