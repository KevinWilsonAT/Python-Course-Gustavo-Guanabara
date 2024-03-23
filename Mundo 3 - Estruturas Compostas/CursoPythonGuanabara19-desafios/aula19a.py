catalog = []

movie1 = {'Title':'Star Wars', 'Year':1977, 'Director':'George Lucas'}
movie2 = {'Title':'Indiana Jones: Last Crusade', 'Year':1989, 'Director':'Steven Spielberg'}
movie3 = {'Title':'Batman', 'Year':1989, 'Director':'Tim Burton'}

catalog.append(movie1)
catalog.append(movie2)
catalog.append(movie3)

for keys, values in movie2.items():
    print(f'{keys}: {values}')