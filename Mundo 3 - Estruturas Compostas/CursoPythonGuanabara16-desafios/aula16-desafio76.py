list_prod = ('Pencil', 2,
             'Rubber', 2,
             'Notebook', 16,
             'Pencil Pocket', 25,
             'Transfer', 5,
             'Compass', 10,
             'Bag', 121,
             'Pens', 23,
             'Book', 35)

for position in range(0, len(list_prod)):
    if position % 2 == 0:
        print(f'{list_prod[position]:.<30}', end='')
    else:
        print(f' R${list_prod[position]:>7.2f}')