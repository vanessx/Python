list = ('pencil', 1.75, 'eraser', 2.35, 'notebook', 3.50, 'book', 13.75,
        'backpack', 7.99, 'pen', 1.85)

for item in range(0, len(list)):
    if item % 2 == 0:
        print(f'{list[item]:.<40}', end = '')
    else:
        print(f'{list[item]:>6}€')